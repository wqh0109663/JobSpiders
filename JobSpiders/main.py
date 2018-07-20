from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#execute(["scrapy", "crawl", "zhaopin_cplus"])
os.system("scrapy crawl zhaopin_java")
os.system("scrapy crawl zhaopin_python")
os.system("scrapy crawl zhaopin_bigdata")
os.system("scrapy crawl zhaopin_arithmetic")
os.system("scrapy crawl zhaopin_ai")
os.system("scrapy crawl zhaopin_go")
os.system("scrapy crawl zhaopin_cplus")
# execute(["scrapy", "crawl", "job_python"])