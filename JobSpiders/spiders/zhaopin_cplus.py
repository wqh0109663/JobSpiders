# -*- coding: utf-8 -*-
import re
from datetime import datetime
import requests
import scrapy
from scrapy.http import Request
import json
from JobSpiders.items import Job51Item, Job51ItemLoader
from JobSpiders.utils.common import get_md5

class ZhaopinCplusSpider(scrapy.Spider):
    name = 'zhaopin_cplus'
    allowed_domains = ['fe-api.zhaopin.com', 'jobs.zhaopin.com']
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=489&workExperience=-1&education=-1'
                  '&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=c%2B%2B&kt=3&lastUrlQuery=%7B%22jl%22:%22489'
                  '%22,%22kw%22:%22c%2B%2B%22,%22kt%22:%223%22%7D']

    def parse(self, response):
        dict = json.loads(response.text)
        code = dict['code']
        numFound = dict['data']['numFound']
        meta_data = 0
        pageNum = 1
        if code == 200 and numFound > 0:
            yield Request(url=response.url, callback=self.parse_detail, meta={'meta_data': meta_data, 'page': pageNum})

    def parse_detail(self, response):
        if response.status == 200:
            value = 'c\+\+'
            dict_obj = json.loads(response.text)
            if dict_obj['data']:
                code = dict_obj['code']
                numFound = dict_obj['data']['numFound']
                # print(type((json.loads(response.text))['data']['numFound']))
                # print(type(response.meta['meta_data']))
                list_len = len(dict_obj['data']['results'])
                if code == 200 and numFound > 0:
                    for i in range(list_len):
                        contain_key_word = dict_obj['data']['results'][i]['jobName']
                        m = re.search(value, contain_key_word, re.IGNORECASE)
                        if m:
                            itemloader = Job51ItemLoader(item=Job51Item(), response=response)
                            itemloader.add_value("url", response.url)
                            itemloader.add_value("url_obj_id", get_md5(response.url) + "{0}".format(i))
                            itemloader.add_value("title", contain_key_word)
                            str_salary = dict_obj['data']['results'][i]['salary']
                            if 'K' in str_salary:
                                try:
                                    list_str = str_salary.split("-")
                                    salary_min = float(list_str[0].strip().split("K")[0].strip()) * 1000
                                    salary_max = float(list_str[1].strip().split("K")[0].strip()) * 1000
                                    itemloader.add_value("salary_min", salary_min)
                                    itemloader.add_value("salary_max", salary_max)
                                except Exception as e:
                                    print('error str_salary', str_salary)
                                    print(e)

                            else:
                                print('str_salary error', str_salary)
                                itemloader.add_value("salary_min", 0)
                                itemloader.add_value("salary_max", 0)

                            job_city = dict_obj['data']['results'][i]['city']['display']

                            itemloader.add_value("job_city", job_city)
                            experience_year = dict_obj['data']['results'][i]['workingExp']['name']
                            print('experience_year', experience_year)
                            itemloader.add_value("experience_year", experience_year)
                            education_need = dict_obj['data']['results'][i]['eduLevel']['name']
                            print('education_need', education_need)
                            itemloader.add_value("education_need", education_need)

                            job_advantage_tags_list = dict_obj['data']['results'][i]['welfare']
                            if len(job_advantage_tags_list) == 0:
                                job_advantage_tags = " "
                            else:
                                job_advantage_tags = ','.join(job_advantage_tags_list)
                            position_info_contains_job_request_list = self.get_position_info_contains_job_request_list(
                                dict_obj['data']['results'][i]['positionURL'])

                            if len(position_info_contains_job_request_list) == 0:
                                print('error response url', response.url)
                                print('error item 第几个', i)
                                position_info_contains_job_request = " "
                            else:
                                position_info_contains_job_request = ','.join(position_info_contains_job_request_list)
                            itemloader.add_value("job_advantage_tags", job_advantage_tags)
                            itemloader.add_value("position_info", position_info_contains_job_request)
                            itemloader.add_value("job_classification",
                                                 dict_obj['data']['results'][i]['jobType']['display'])
                            itemloader.add_value("crawl_time", datetime.now())
                            publish_date = dict_obj['data']['results'][i]['createDate'].strip().split(" ")[
                                               0].strip() + ""
                            itemloader.add_value("publish_date", publish_date)
                            item = itemloader.load_item()
                            yield item
        if response.status == 200 and response.meta.get('meta_data', '') < (json.loads(response.text))['data'][
            'numFound'] - 60:
            meta_data = 60 + response.meta.get('meta_data', '')
            print('start', meta_data)
            page = response.meta.get('page', '') + 1
            print('current_page', page)
            dic_page = {"p": 1, "jl": "489", "kw": "go", "kt": "3"}
            dic_page['p'] = page
            data = '{0}'.format(dic_page)
            print(data)
            from urllib import parse
            url_data = parse.quote(string=data, encoding="utf-8")
            url_next = 'https://fe-api.zhaopin.com/c/i/sou?start={start}&pageSize=60&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=c&kt=3&lastUrlQuery={lastUrlQuery}'.format(
                start=meta_data, lastUrlQuery=url_data)
            yield Request(url=url_next, callback=self.parse_detail, meta={'meta_data': meta_data, 'page': page})

    def get_position_info_contains_job_request_list(self, url):
        info = []
        print('url', url)
        try:
            response_t = requests.get(url=url)
            from lxml import html
            tree = html.fromstring(response_t.text)
            info = tree.xpath("//div[@class='tab-inner-cont']/p//text()")
        except Exception as e:
            print('error', e)
            print('error url', url)

        return info
