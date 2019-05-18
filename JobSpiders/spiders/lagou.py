# -*- coding: utf-8 -*-
import re
from datetime import datetime
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time
from selenium import webdriver
import pickle
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import requests
from PIL import Image
from io import BytesIO
from JobSpiders.utils.ruokuai_code import *
from JobSpiders.utils.ruokuai import *

from JobSpiders.items import LagouJobItem, LagouJobItemLoader
from JobSpiders.utils.common import get_md5
from JobSpiders.utils.getLaGouCookie import *


class LagouSpider(CrawlSpider):
    ruokuai_username = 'w*****'
    ruokuai_passwd = '*****'
    lagou_username = '136**4970'
    lagou_passwd = '*****'
    handle_httpstatus_list = [302]
    custom_settings = {'COOKIES_ENABLED': False, 'CONCURRENT_REQUESTS': 2, 'DOWNLOAD_DELAY': 2}
    meta = {'dont_redirect': True, "handle_httpstatus_list": [302]}
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com']
    login_url = "https://passport.lagou.com/login/login.html"
    # custom_settings = {'REDIRECT_ENABLED': False}
    rules = (
        Rule(LinkExtractor(allow=("zhaopin/.*",)), follow=True),
        Rule(LinkExtractor(allow=("gongsi/j\d+.html",)), follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_job', follow=True),
    )
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    # cookie='ga=GA1.2.430541542.1531227260; user_trace_token=20180710205419-5c6c1887-8440-11e8-993d-5254005c3644; LGUID=20180710205419-5c6c1cf6-8440-11e8-993d-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAGFABEFC268BFA79F037F3E81290C6985343757; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1531877495,1531982693,1532526791,1532937871; _gid=GA1.2.1809205573.1532937871; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=256bfa9cb92ef88a7f7ee1f7bc905564; SEARCH_ID=9ad79bdbdd374fe2afcc9e4b06b54b58; ab_test_random_num=0; hasDeliver=0; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; _gat=1; LGSID=20180730180847-8c66cefa-93e0-11e8-abc3-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LG_LOGIN_USER_ID=d972850df5693982a5f2563e25543780d46de1e07ef92a97ca47f15c949e2c50; _putrc=4FD3D6BE655DEA0F123F89F2B170EADC; login=true; unick=%E5%90%B4%E5%90%AF%E6%AC%A2; gate_login_token=3bac4153fd3381c0933726c618b0bc9039dac868f848721a67b3379dee220f4c; LGRID=20180730180923-a1f5d23c-93e0-11e8-a082-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532945363'
    # cookie = getLaGouCookie()
    cookie = {'JSESSIONID': 'ABAAABAAAHAAAFD8DAE0CD2E746F43F737F035650B6E7EF',
              'ticketGrantingTicketId': '_CAS_TGT_TGT-cfa8b888370445b5b755364bfbb804cf-20180730225005-_CAS_TGT_',
              'user_trace_token': '20180730225004-a4d90eec-e01f-4a00-9f5c-2645eda28272',
              'LG_LOGIN_USER_ID': '2da6d20b2b5356d5198633f97505a8223f09a663fe92f78f64936c31a3bfd73c'}

    def start_requests(self):
        global rc, im
        browser = webdriver.Chrome(executable_path="/home/wqh/下载/chromedriver")
        # browser = webdriver.Firefox(executable_path="/home/wqh/下载/geckodriver")
        browser.get(self.login_url)
        browser.find_element_by_css_selector("div:nth-child(2) > form > div:nth-child(1) > input").send_keys(
            self.lagou_username)
        browser.find_element_by_css_selector("div:nth-child(2) > form > div:nth-child(2) > input").send_keys(
            self.lagou_passwd)
        browser.find_element_by_css_selector(
            "div:nth-child(2) > form > div.input_item.btn_group.clearfix > input").click()
        time.sleep(5)
        element = browser.find_element_by_xpath("//div[@class='geetest_table_box']")
        print('element::::', element)
        if element:
            print('i am in ....')
            flag = True
            while flag:
                try:
                    footer_element = browser.find_element_by_xpath(
                        "//div[@class='geetest_panel_footer' and @style='display: none;']")
                    print('footer::::', footer_element)
                except NoSuchElementException as e:
                    print('正在重试。。。。', e)
                    browser.find_element_by_xpath(
                        "//div[@class='geetest_panel_error_content']").click()
                    time.sleep(5)
                    pass
                imgs = browser.find_elements_by_xpath("//img[@class='geetest_item_img']")
                print('imgs::::::', imgs)
                try:
                    img = Image.open(BytesIO((requests.get(imgs[0].get_attribute('src'))).content))
                    img.save('test.jpg')
                    rc = RClient(self.ruokuai_username, self.ruokuai_passwd)
                    im = open('test.jpg', 'rb').read()
                except IOError:
                    print('*****检查自己的快豆是不是没了****')
                    return
                result_img_code = rc.rk_create(im, 6900)
                print(result_img_code)
                results_code = result_img_code.get('Result')
                print(results_code)
                list_code = results_code.split('.')
                print('list_code', list_code)
                list_arr = []
                for item in list_code:
                    print('item', item)
                    pixel_x_y = item.split(',')
                    print('pixel_x_y', pixel_x_y)
                    pixel_x = pixel_x_y[0]
                    pixel_y = pixel_x_y[1]
                    print('pixel_x', pixel_x)
                    print('pixel_y', pixel_y)
                    pixel_x = int(pixel_x)
                    pixel_y = int(pixel_y)
                    if pixel_x < 110:
                        if pixel_y < 110:
                            list_arr.append(1)
                        elif 110 < pixel_y < 220:
                            list_arr.append(4)
                        elif 220 < pixel_y < 330:
                            list_arr.append(7)
                    elif 110 < pixel_x < 220:
                        if pixel_y < 110:
                            list_arr.append(2)
                        elif 110 < pixel_y < 220:
                            list_arr.append(5)
                        elif 220 < pixel_y < 330:
                            list_arr.append(8)
                    elif 220 < pixel_x < 330:
                        if pixel_y < 110:
                            list_arr.append(3)
                        elif 110 < pixel_y < 220:
                            list_arr.append(6)
                        elif 220 < pixel_y < 330:
                            list_arr.append(9)
                print(list_arr)
                for i in list_arr:
                    xpath_str = "(//div[@class='geetest_item'][{0}]//div[@class='geetest_item_ghost'])".format(i)
                    print(xpath_str, i)
                    try:
                        browser.find_element_by_xpath(xpath_str).click()
                    except Exception as e:
                        print(e)
                        pass
                time.sleep(1)
                browser.find_element_by_xpath("//a[@class='geetest_commit']").click()
                time.sleep(5)  # 等一会看是不是会跳转到首页
                print(browser.current_url)
                if browser.current_url != 'https://passport.lagou.com/login/login.html':
                    flag = False

        time.sleep(5)
        cookies = browser.get_cookies()
        cookie_dict = {}
        for cookie in cookies:
            cookie_dict[cookie['name']] = cookie['value']
        with open('cookies_dict.lagou', 'wb') as wf:
            pickle.dump(cookie_dict, wf)
        logging.info('--------lagou cookies---------')
        print(cookie_dict)
        self.cookie = cookie_dict
        return [scrapy.Request(self.start_urls[0], cookies=cookie_dict, headers=self.headers, meta={
            'dont_redirect': True,
            'handle_httpstatus_list': [302]
        })]
        # yield scrapy.Request(url='https://www.lagou.com', headers=self.headers, cookies=self.cookie, dont_filter=True)

    # def _build_request(self, rule, link):
    #     # 没有改完 。。。。。
    #     print(link.url)
    #     response = requests.get(link.url, headers=self.headers)  # 请求原网页
    #     r = requests.utils.dict_from_cookiejar(response.cookies)  # 获取cookies
    #     print(r)
    #     if "LGRID" in r:
    #         r["user_trace_token"] = r["LGRID"]
    #         r["LGSID"] = r["LGRID"]
    #         r["LGUID"] = r["LGRID"]  # 构造cookies的参数
    #         self.cookie.update(r)
    #     my_request = Request(url=link.url, headers=self.headers, callback=self.parse_job, cookies=self.cookie)
    #     my_request.meta.update(rule=rule, link_text=link.text)
    #     # time.sleep(1)  ## 每一次请求停一秒
    #     return my_request

    def parse_job(self, response):
        global global_result
        if response.status == 302:
            print("302")
            print(response.url)
            try:
                time.sleep(1)
                src = response.xpath("//img[@id='captcha']/@src").extract_first("")
                if src:
                    print('src:', src)
                    img_src = "https://www.lagou.com" + src
                    try:
                        image = Image.open(BytesIO((requests.get(img_src)).content))
                        image.save('verify2.gif')
                        rcf = RClientFour(self.ruokuai_username, self.ruokuai_passwd)
                        image = open('verify2.gif', 'rb').read()
                        global_result = rcf.rk_create_code(image, 3040).get('Result')
                        print('result:', global_result)
                    except IOError:
                        print('*****检查自己的快豆是不是没了****')
                        pass
                    # time.sleep(100000)
                    browser = webdriver.Chrome(executable_path="/home/wqh/下载/chromedriver")
                    browser.find_element_by_xpath("//*[@id='code']").send_keys(global_result)
                    browser.find_element_by_xpath("//a[@id='submit']").click()
                    return
            except Exception as e:
                print(e)
                print('不是验证页面')
                pass

        title = response.xpath("/html/body/div[2]/div/div[1]/div/span").extract_first("")
        item_loader = LagouJobItemLoader(item=LagouJobItem(), response=response)
        list_type = []
        flag = False
        m = re.search("java", title, re.IGNORECASE)
        if m:
            flag = True
            list_type.append("java")

        if re.search("python", title, re.IGNORECASE):
            flag = True
            list_type.append("python")
        if re.search("人工智能", title, re.IGNORECASE):
            flag = True
            list_type.append("人工智能")
        if re.search("算法", title, re.IGNORECASE):
            flag = True
            list_type.append("算法")
        if re.search("大数据", title, re.IGNORECASE):
            flag = True
            list_type.append("大数据")
        if re.search("C\+\+", title, re.IGNORECASE):
            flag = True
            list_type.append("C++")
        if re.search("go", title, re.IGNORECASE):
            flag = True
            list_type.append("go")
        if flag:
            # 解析拉勾网的职位
            item_loader.add_value("type", list_type)
            item_loader.add_css("title", ".job-name::attr(title)")
            item_loader.add_value("url", response.url)
            item_loader.add_value("url_obj_id", get_md5(response.url) + str(int(time.time())))
            str_salary = response.xpath("//span[@class='salary']/text()").extract_first("")
            if 'k' in str_salary:
                try:
                    list_str = str_salary.split("-")
                    salary_min = float(list_str[0].strip().split("k")[0].strip()) * 1000
                    salary_max = float(list_str[1].strip().split("k")[0].strip()) * 1000
                    item_loader.add_value("salary_min", salary_min)
                    item_loader.add_value("salary_max", salary_max)
                except Exception as e:
                    print('error str_salary', str_salary)
                    print(e)

            else:
                print('str_salary error', str_salary)
                item_loader.add_value("salary_min", 0)
                item_loader.add_value("salary_max", 0)
            # item_loader.add_css("salary", ".job_request .salary::text")
            item_loader.add_xpath("job_city", "//*[@class='job_request']/p/span[2]/text()")
            item_loader.add_xpath("experience_year", "//*[@class='job_request']/p/span[3]/text()")
            item_loader.add_xpath("education_need", "//*[@class='job_request']/p/span[4]/text()")
            item_loader.add_xpath("job_type", "//*[@class='job_request']/p/span[5]/text()")
            item_loader.add_value("job_classification", title)

            item_loader.add_css("publish_date", ".publish_time::text")
            item_loader.add_css("job_advantage_tags", ".job-advantage p::text")
            item_loader.add_css("position_info", ".job_bt div")
            item_loader.add_css("job_addr", ".work_addr")
            item_loader.add_css("company_name", "#job_company dt a img::attr(alt)")
            item_loader.add_css("company_url", "#job_company dt a::attr(href)")
            item_loader.add_value("crawl_time", datetime.now())

            job_item = item_loader.load_item()

            return job_item
