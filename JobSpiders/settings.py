# -*- coding: utf-8 -*-

# Scrapy settings for JobSpiders project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'JobSpiders'

SPIDER_MODULES = ['JobSpiders.spiders']
NEWSPIDER_MODULE = 'JobSpiders.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'JobSpiders (+http://www.yourdomain.com)'
# USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 ' \
#              'Chrome/66.0.3359.181 Safari/537.36 '
# RANDOM_UA_TYPE = 'random'
# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False
from JobSpiders.utils.getLaGouCookie import *
# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'application/json, text/javascript, */*; q=0.01',
#   'Accept-Language': 'zh-CN,zh;q=0.9',
#   'Cookie': 'ga=GA1.2.430541542.1531227260; user_trace_token=20180710205419-5c6c1887-8440-11e8-993d-5254005c3644; LGUID=20180710205419-5c6c1cf6-8440-11e8-993d-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAGFABEFC268BFA79F037F3E81290C6985343757; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1531877495,1531982693,1532526791,1532937871; _gid=GA1.2.1809205573.1532937871; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=256bfa9cb92ef88a7f7ee1f7bc905564; SEARCH_ID=9ad79bdbdd374fe2afcc9e4b06b54b58; ab_test_random_num=0; hasDeliver=0; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; _gat=1; LGSID=20180730180847-8c66cefa-93e0-11e8-abc3-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LG_LOGIN_USER_ID=d972850df5693982a5f2563e25543780d46de1e07ef92a97ca47f15c949e2c50; _putrc=4FD3D6BE655DEA0F123F89F2B170EADC; login=true; unick=%E5%90%B4%E5%90%AF%E6%AC%A2; gate_login_token=3bac4153fd3381c0933726c618b0bc9039dac868f848721a67b3379dee220f4c; LGRID=20180730180923-a1f5d23c-93e0-11e8-a082-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532945363',
#   'Connection': 'keep-alive',
#   'Host': 'www.lagou.com',
#   'Referer': 'https://www.lagou.com/',
#   'X-Anit-Forge-Code': '0',
#   'X-Anit-Forge-Token': 'None',
#   'Accept-Encoding': 'gzip, deflate, br',
#   'X-Requested-With': 'XMLHttpRequest'
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'JobSpiders.middlewares.JobspidersSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'JobSpiders.middlewares.JobspidersDownloaderMiddleware': 543,
    'JobSpiders.middlewares.RandomUserAgentMiddleware': 1,
    # 'JobSpiders.middlewares.JSPageMiddleware' : 100,
    'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': 700,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,  # 这里要设置原来的scrapy的useragent为None，否者会被覆盖掉
}

RANDOM_UA_TYPE = 'random'
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'JobSpiders.pipelines.JobspidersPipeline': 3,
    'JobSpiders.pipelines.MysqlTwistedPipline': 1,
    # 'JobSpiders.pipelines.MysqlTwistedPythonPipline':2,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
MYSQL_HOST = "127.0.0.1"
MYSQL_DBNAME = "jobspider"
MYSQL_USER = "root"
MYSQL_PASSWORD = "Wuqihuan19950903"

SQL_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
SQL_DATE_FORMAT = "%Y-%m-%d"

ES_HOST = "127.0.0.1"
