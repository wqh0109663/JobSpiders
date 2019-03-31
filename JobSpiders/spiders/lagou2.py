# -*- coding: utf-8 -*-
import time
from datetime import datetime

import scrapy

from JobSpiders.items import LagouJobItem, LagouJobItemLoader
from JobSpiders.utils.common import get_md5
from JobSpiders.utils.getLaGouCookie import *


class Lagou2Spider(scrapy.Spider):
    name = 'lagou2'
    allowed_domains = ['www.lagou.com/']
    start_urls = [
        'https://www.lagou.com/jobs/list_?city=%e5%85%a8%e5%9b%bd&cl=false&fromSearch=true&labelWords=&suginput=']

    headers = {'Connection': 'keep-alive',
               'Cache-Control': 'max-age=0',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
               }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        cookies = {
            'X_MIDDLE_TOKEN': '797bc148d133274a162ba797a6875817',
            'JSESSIONID': 'ABAAABAAAIAACBI03F33A375F98E05C5108D4D742A34114',
            '_ga': 'GA1.2.1912257997.1548059451',
            '_gat': '1',
            'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1548059451',
            'user_trace_token': '20190121163050-dbd72da2-1d56-11e9-8927-525400f775ce',
            'LGSID': '20190121163050-dbd72f67-1d56-11e9-8927-525400f775ce',
            'PRE_UTM': '',
            'PRE_HOST': '',
            'PRE_SITE': '',
            'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F%3F_from_mid%3D1',
            'LGUID': '20190121163050-dbd73128-1d56-11e9-8927-525400f775ce',
            '_gid': 'GA1.2.1194828713.1548059451',
            'index_location_city': '%E5%85%A8%E5%9B%BD',
            'TG-TRACK-CODE': 'index_hotjob',
            'LGRID': '20190121163142-fb0cc9c0-1d56-11e9-8928-525400f775ce',
            'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1548059503',
            'SEARCH_ID': '86ed37f5d8da417dafb53aa25cd6fbc0',
        }

        headers = {
            'Origin': 'https://www.lagou.com',
            'X-Anit-Forge-Code': '0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': 'https://www.lagou.com/jobs/list_java?px=new&city=%E4%B8%8A%E6%B5%B7',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'X-Anit-Forge-Token': 'None',
        }
        params = (
            ('px', 'new'),
            ('city', '\u5168\u56fd'),
            ('needAddtionalResult', 'false'),
        )
        data = {'first': True,
                'kd': 'java',
                'pn': 1}

        # cookiejar = CookieJar()
        type_list = ['java', 'python', '人工智能', '算法', '大数据', 'C++', 'go']
        flag_type = 0
        while flag_type < len(type_list):
            data['kd'] = type_list[flag_type]
            while True:
                # print('cookie:::::', response.request.headers.getlist('Cookie'))
                # print('set-cookie::::::', response.headers.getlist('Set-Cookie'))
                # print('cookie jar:', cookiejar.extract_cookies(response, response.request))

                # print('cookie jar type:', type(cookiejar.extract_cookies(response, response.request)))
                # print('set-cookie type:', type(response.headers.getlist('Set-Cookie')))
                if data['first'] != True:
                    response_my = requests.get(
                        'https://www.lagou.com/jobs/list_?city=%e5%85%a8%e5%9b%bd&cl='
                        'false&fromSearch=true&labelWords=&suginput=',
                        headers=headers)  # 请求原网页
                    r = requests.utils.dict_from_cookiejar(response_my.cookies)  # 获取cookies
                    # r['LGRID'] = r["LGRID"]
                else:
                    r = {}  # 获取cookies
                    r['LGRID'] = (response.headers.getlist('Set-Cookie'))[2].decode("utf-8").split(';')[0].split('=')[1]
                    print(r)
                r["user_trace_token"] = r["LGRID"]
                r["LGSID"] = r["LGRID"]
                r["LGUID"] = r["LGRID"]  # 构造cookies的参数113.92.199.204

                cookies.update(r)  # 更新接口的cookies

                response = requests.post('https://www.lagou.com/jobs/positionAjax.json', headers=headers, params=params,
                                         cookies=cookies, data=data)  # 请求接口

                print(response.json())
                data_json = response.json()
                content_list = data_json.get('content')
                positionResult = content_list.get('positionResult')
                totalCount = positionResult.get('totalCount')
                resultSize = positionResult.get('resultSize')
                result_list = positionResult.get('result')
                flag_type = flag_type + 1
                if len(result_list) != 0:
                    data['pn'] = data['pn'] + 1
                    data['first'] = False
                    print('data:', data)
                if len(result_list) == 0:
                    data['first'] = True
                    break
                for i in range(0, len(result_list)):
                    page_id = result_list[i].get('positionId')
                    url_i = "https://www.lagou.com/jobs/{0}.html".format(page_id)
                    print(url_i)
                    yield scrapy.Request(url=url_i, headers=self.headers, callback=self.parse_job)

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
            item_loader.add_value("url_obj_id",
                                  get_md5(response.url) + str(int(time.time())))
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
                item_loader.add_xpath("job_city",
                                      "//*[@class='job_request']/p/span[2]/text()")
                item_loader.add_xpath("experience_year",
                                      "//*[@class='job_request']/p/span[3]/text()")
                item_loader.add_xpath("education_need",
                                      "//*[@class='job_request']/p/span[4]/text()")
                item_loader.add_xpath("job_type",
                                      "//*[@class='job_request']/p/span[5]/text()")
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
