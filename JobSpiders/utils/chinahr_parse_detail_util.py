import re
from JobSpiders.items import Job51Item, Job51ItemLoader
from JobSpiders.utils.common import get_md5
from datetime import datetime
from selenium import webdriver
import time

def parse_detail_utils_zhaopin(self, response, value):

    contain_key_word = response.xpath("//div[@class='main1 cl main1-stat']//h1/text()").extract_first()
    m = re.search(value, contain_key_word, re.IGNORECASE)
    if m:
        itemloader = Job51ItemLoader(item=Job51Item(), response=response)
        itemloader.add_value("url", response.url)
        itemloader.add_value("url_obj_id", get_md5(response.url))
        itemloader.add_value("title", contain_key_word)
        str_salary = response.xpath("//div[@class='l info-money']/strong/text()").extract_first("")
        if '元/月' in str_salary:
            list_str = str_salary.split("-")
            salary_min = float(list_str[0])
            salary_max = float(list_str[1].strip().split("元")[0].strip())
            itemloader.add_value("salary_min", salary_min)
            itemloader.add_value("salary_max", salary_max)
        elif '面议' in str_salary:
            salary_min = 0.0
            salary_max = 0.0
            itemloader.add_value("salary_min", salary_min)
            itemloader.add_value("salary_max", salary_max)
        job_city = response.xpath("//div[@class='info-three l']/span/a/text()").extract_first("")
        itemloader.add_value("job_city", job_city)
        experience_year = response.xpath("//div[@class='info-three l']/span[2]/text()").extract_first("")
        itemloader.add_value("experience_year", experience_year)
        education_need = response.xpath("//div[@class='info-three l']/span[3]/text()").extract_first("")
        itemloader.add_value("education_need", education_need)
        itemloader.add_value("publish_date", datetime.now())
        job_advantage_tags_list = response.xpath("//div[@class='welfare']//ul//li/text()").extract()
        if len(job_advantage_tags_list) == 0:
            job_advantage_tags = " "
        else:
            job_advantage_tags = ','.join(job_advantage_tags_list)
        position_info_contains_job_request_list = response.xpath(
            "//div[@class='responsibility pos-common']//text()").extract()
        if len(position_info_contains_job_request_list) == 0:
            position_info_contains_job_request = " "
        else:
            position_info_contains_job_request = ','.join(position_info_contains_job_request_list)
        itemloader.add_value("job_advantage_tags", job_advantage_tags)
        itemloader.add_value("position_info", position_info_contains_job_request)
        itemloader.add_value("job_classification", "未分类")
        itemloader.add_value("crawl_time", datetime.now())
        item = itemloader.load_item()
        return item
