# -*- coding: utf-8 -*-
import re
from datetime import datetime
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time
from selenium import webdriver
import pickle
import logging

from JobSpiders.items import LagouJobItem, LagouJobItemLoader
from JobSpiders.utils.common import get_md5
from JobSpiders.utils.getLaGouCookie import *


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com']
    login_url = "https://passport.lagou.com/login/login.html"

    rules = (
        Rule(LinkExtractor(allow=("zhaopin/.*",)), follow=True),
        Rule(LinkExtractor(allow=("gongsi/j\d+.html",)), follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_job', follow=True),
    )
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-Requested-With': 'XMLHttpRequest'
    }
    # cookie='ga=GA1.2.430541542.1531227260; user_trace_token=20180710205419-5c6c1887-8440-11e8-993d-5254005c3644; LGUID=20180710205419-5c6c1cf6-8440-11e8-993d-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAGFABEFC268BFA79F037F3E81290C6985343757; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1531877495,1531982693,1532526791,1532937871; _gid=GA1.2.1809205573.1532937871; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=256bfa9cb92ef88a7f7ee1f7bc905564; SEARCH_ID=9ad79bdbdd374fe2afcc9e4b06b54b58; ab_test_random_num=0; hasDeliver=0; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; _gat=1; LGSID=20180730180847-8c66cefa-93e0-11e8-abc3-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LG_LOGIN_USER_ID=d972850df5693982a5f2563e25543780d46de1e07ef92a97ca47f15c949e2c50; _putrc=4FD3D6BE655DEA0F123F89F2B170EADC; login=true; unick=%E5%90%B4%E5%90%AF%E6%AC%A2; gate_login_token=3bac4153fd3381c0933726c618b0bc9039dac868f848721a67b3379dee220f4c; LGRID=20180730180923-a1f5d23c-93e0-11e8-a082-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532945363'
    # cookie = getLaGouCookie()
    cookie = {'JSESSIONID': 'ABAAABAAAHAAAFD8DAE0CD2E746F43F737F035650B6E7EF',
              'ticketGrantingTicketId': '_CAS_TGT_TGT-cfa8b888370445b5b755364bfbb804cf-20180730225005-_CAS_TGT_',
              'user_trace_token': '20180730225004-a4d90eec-e01f-4a00-9f5c-2645eda28272',
              'LG_LOGIN_USER_ID': '2da6d20b2b5356d5198633f97505a8223f09a663fe92f78f64936c31a3bfd73c'}

    def start_requests(self):
        browser = webdriver.Chrome(executable_path="/home/wqh/下载/chromedriver")
        # browser = webdriver.Firefox(executable_path="/home/wqh/下载/geckodriver")
        browser.get(self.login_url)
        browser.find_element_by_css_selector("div:nth-child(2) > form > div:nth-child(1) > input").send_keys(
            "13677134970")
        browser.find_element_by_css_selector("div:nth-child(2) > form > div:nth-child(2) > input").send_keys(
            "wqh999999999")
        browser.find_element_by_css_selector(
            "div:nth-child(2) > form > div.input_item.btn_group.clearfix > input").click()
        time.sleep(100)
        cookies = browser.get_cookies()
        cookie_dict = {}
        for cookie in cookies:
            cookie_dict[cookie['name']] = cookie['value']
        with open('cookies_dict.lagou', 'wb') as wf:
            pickle.dump(cookie_dict, wf)
        logging.info('--------lagou cookies---------')
        print(cookie_dict)
        return [scrapy.Request(self.start_urls[0], cookies=cookie_dict)]
        # yield scrapy.Request(url='https://www.lagou.com', headers=self.headers, cookies=self.cookie, dont_filter=True)

    def parse_job(self, response):
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
