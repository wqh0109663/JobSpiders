# -*- coding: utf-8 -*-
from urllib import parse  # 如果url不是完整的就加上这个

import scrapy
from scrapy.http import Request

from JobSpiders.utils.parse_detail import parse_detail_utils


class Job51Spider(scrapy.Spider):
    name = 'job51'
    allowed_domains = ['jobs.51job.com', 'search.51job.com']
    start_urls = ['https://search.51job.com/list/180000,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def parse(self, response):
        # 1获取到每一条招聘的url并将url给具体的解析函数进行解析字段
        all_url = response.xpath('//*[@id="resultList"]//div/p/span/a/@href').extract()
        for one_url in all_url:
            yield Request(url=parse.urljoin(response.url, one_url), callback=self.parse_detail, )

        # 2获取下一页的url并交给scrapy下载
        next_url = response.xpath('//*[@id="resultList"]/div[55]/div/div/div/ul/li[8]/a/@href').extract_first("")
        if next_url:
            # yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse)
            yield Request(url=next_url, callback=self.parse)

    def parse_detail(self, response):
        yield parse_detail_utils(self, response, '软件工程师')
