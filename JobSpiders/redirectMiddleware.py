import time
from io import BytesIO

from PIL import Image
from scrapy.downloadermiddlewares.redirect import BaseRedirectMiddleware
from selenium import webdriver
from six.moves.urllib.parse import urljoin
from w3lib.url import safe_url_string

from JobSpiders.utils.ruokuai_code import *


class RedirectMiddleware(BaseRedirectMiddleware):
    """
    Handle redirection of requests based on response status
    and meta-refresh html tag.
    """

    def process_response(self, request, response, spider):
        if response.status == 302 and 'lagou' not in response.url:
            print('302.....')
            time.sleep(100)
            flag = True
            while flag:
                src = response.xpath("//img[@id='captcha']/@src").extract_first("")
                img_src = "https://www.lagou.com" + src
                print('img_src', img_src)
                image = Image.open(BytesIO((requests.get(img_src)).content))
                image.save('verify2.gif')
                rcf = RClientFour('你的若快账号', '你的若快密码')
                image = open('verify2.gif', 'rb').read()
                result = rcf.rk_create_code(image, 3040).get('Result')
                print('result', result)
                browser = webdriver.Chrome(executable_path="/home/wqh/下载/chromedriver")
                browser.get(response.url)
                browser.find_element_by_xpath("//*[@id='code']").send_keys(result)
                browser.find_element_by_xpath("//a[@id='submit']").click()
                time.sleep(10)
                if response.status != 302:
                    flag = False
            return

        if (request.meta.get('dont_redirect', False) or
                response.status in getattr(spider, 'handle_httpstatus_list', []) or
                response.status in request.meta.get('handle_httpstatus_list', []) or
                request.meta.get('handle_httpstatus_all', False)):
            return response

        allowed_status = (301, 302, 303, 307, 308)
        if 'Location' not in response.headers or response.status not in allowed_status:
            return response

        location = safe_url_string(response.headers['location'])

        redirected_url = urljoin(request.url, location)

        if response.status in (301, 307, 308) or request.method == 'HEAD':
            redirected = request.replace(url=redirected_url)
            return self._redirect(redirected, request, spider, response.status)

        redirected = self._redirect_request_using_get(request, redirected_url)
        return self._redirect(redirected, request, spider, response.status)
