# -*- coding: utf-8 -*-
import re
from datetime import datetime
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from JobSpiders.items import LagouJobItem, LagouJobItemLoader
from JobSpiders.utils.common import get_md5


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com']

    rules = (
        Rule(LinkExtractor(allow=("zhaopin/.*",)), follow=True),
        Rule(LinkExtractor(allow=("gongsi/j\d+.html",)), follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_job', follow=True),
    )
    #
    # def parse_start_url(self, response):
    #     return []
    #
    # def process_results(self, response, results):
    #     return results

    def parse_job(self, response):
        title = response.xpath("/html/body/div[2]/div/div[1]/div/span").extract_first("")
        m = re.search("java", title, re.IGNORECASE)
        #解析拉勾网的职位
        item_loader = LagouJobItemLoader(item=LagouJobItem(), response=response)
        item_loader.add_css("title", ".job-name::attr(title)")
        item_loader.add_value("url", response.url)
        item_loader.add_value("url_object_id", get_md5(response.url))
        str_salary = response.xpath("//span[@class='salary']/text()").extract_first("")
        if 'K' in str_salary:
            try:
                list_str = str_salary.split("-")
                salary_min = float(list_str[0].strip().split("K")[0].strip()) * 1000 / 12.0
                salary_max = float(list_str[1].strip().split("K")[0].strip()) * 1000 / 12.0
                item_loader.add_value("salary_min", salary_min)
                item_loader.add_value("salary_max", salary_max)
            except Exception as e:
                print('error str_salary', str_salary)
                print(e)

        else:
            print('str_salary error', str_salary)
            item_loader.add_value("salary_min", 0)
            item_loader.add_value("salary_max", 0)
        item_loader.add_css("salary", ".job_request .salary::text")
        item_loader.add_xpath("job_city", "//*[@class='job_request']/p/span[2]/text()")
        item_loader.add_xpath("work_years", "//*[@class='job_request']/p/span[3]/text()")
        item_loader.add_xpath("degree_need", "//*[@class='job_request']/p/span[4]/text()")
        item_loader.add_xpath("job_type", "//*[@class='job_request']/p/span[5]/text()")

        item_loader.add_css("tags", '.position-label li::text')
        item_loader.add_css("publish_time", ".publish_time::text")
        item_loader.add_css("job_advantage", ".job-advantage p::text")
        item_loader.add_css("job_desc", ".job_bt div")
        item_loader.add_css("job_addr", ".work_addr")
        item_loader.add_css("company_name", "#job_company dt a img::attr(alt)")
        item_loader.add_css("company_url", "#job_company dt a::attr(href)")
        item_loader.add_value("crawl_time", datetime.now())

        job_item = item_loader.load_item()

        return job_item
