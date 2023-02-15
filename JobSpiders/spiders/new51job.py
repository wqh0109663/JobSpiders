import scrapy
from scrapy.http import Request
from urllib import parse
import hmac
import hashlib
from jobSpiders.items import Job51ItemLoader, Job51Item
import time
import uuid
import json

def parse_detail_utils(self, response):
    print(response.text)
    dict_resp = json.loads(response.text)
    print()

    # itemloader = Job51ItemLoader(item=Job51Item(), response=response)


class A51jobSpider(scrapy.Spider):
    name = "51job"
    allowed_domains = ['jobs.51job.com', 'search.51job.com', 'we.51job.com', 'cupid.51job.com']
    start_urls = ["https://www.51job.com/"]

    def parse(self, response):
        secret_key = b"abfc8f9dcf8c3f3d8aa294ac5f2cf2cc7767e5592590f39c3f503271dd68562b"
        timestamp = str(int(time.time()))
        total_params = str.encode("/open/noauth/search-pc?api_key=51job&timestamp="+timestamp+"&keyword=%E9%94%80%E5%94%AE&searchType=2&function=&industry=&jobArea=180000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum=1&requestId=&pageSize=50&source=1&accountId=&pageCode=sou%7Csou%7Csoulb")
        signature = hmac.new(secret_key, total_params, hashlib.sha256).hexdigest()
        print("signature = {0}".format(signature))
        s_uuid = str(uuid.uuid4())
        l_uuid = s_uuid.split('-')
        s_uuid = ''.join(l_uuid)
        # property  search key 需要更改
        url = 'https://cupid.51job.com/open/noauth/search-pc?api_key=51job&timestamp='+timestamp+'&keyword=%E9%94%80%E5%94%AE&searchType=2&function=&industry=&jobArea=180000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum=1&requestId=&pageSize=50&source=1&accountId=&pageCode=sou%7Csou%7Csoulb'
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
            'Connection': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'From-Domain': '51job_web',
            'Host': ' cupid.51job.com',
            'Origin': 'https://we.51job.com',
            'property': '%7B%22partner%22%3A%22%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3FjobArea%3D180000%26keyword%3D%25E9%2594%2580%25E5%2594%25AE%26searchType%3D2%26sortType%3D0%26metro%3D%22%2C%22identityType%22%3A%22%22%2C%22userType%22%3A%22%22%2C%22isLogin%22%3A%22%E5%90%A6%22%2C%22accountid%22%3A%22%22%7D',
            'Referer': 'https://we.51job.com/',
            'sec-ch-ua': ' "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': ' ?0',
            'sec-ch-ua-platform': ' "Windows"',
            'Sec-Fetch-Dest': ' empty',
            'Sec-Fetch-Mode': ' cors',
            'Sec-Fetch-Site': ' same-site',
            'sign': signature,
            'user-token': '',
            'uuid': s_uuid
        }
        # parse.urljoin(response.url,
        yield Request(url=url, callback=self.parse_detail, headers=headers,
                      meta={'meta_data': '销售'})
        # pass

    def parse_detail(self, response):
        yield parse_detail_utils(self, response)