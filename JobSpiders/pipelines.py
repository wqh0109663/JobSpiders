# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import random

import MySQLdb
from twisted.enterprise import adbapi
import MySQLdb.cursors
import re


class JobspidersPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlTwistedPipline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行
        # or spider.name == 'zhaopin_java'
        if spider.name == 'job51' or spider.name == 'zhaopin_java':
            query = self.dbpool.runInteraction(self.do_insert_java, item)
            query.addErrback(self.handle_error, item, spider)  # 处理异常
        elif spider.name == 'job_python' or spider.name == 'zhaopin_python':
            query = self.dbpool.runInteraction(self.do_insert_python, item)
            query.addErrback(self.handle_error, item, spider)  # 处理异常
        elif spider.name == 'job_go' or spider.name == 'zhaopin_go':
            query = self.dbpool.runInteraction(self.do_insert_go, item)
            query.addErrback(self.handle_error, item, spider)  # 处理异常
        elif spider.name == 'job_cplus' or spider.name == 'zhaopin_cplus':
            query = self.dbpool.runInteraction(self.do_insert_cplus, item)
            query.addErrback(self.handle_error, item, spider)  # 处理异常
        elif spider.name == 'job_bigdata' or spider.name == 'zhaopin_bigdata':
            query = self.dbpool.runInteraction(self.do_insert_bigdata, item)
            query.addErrback(self.handle_error, item, spider)  # 处理异常
        elif spider.name == 'job_arithmetic' or spider.name == 'zhaopin_arithmetic':
            query = self.dbpool.runInteraction(self.do_insert_arithmetic, item)
            query.addErrback(self.handle_error, item, spider)  # 处理异常
        elif spider.name == 'job_ai' or spider.name == 'zhaopin_ai':
            query = self.dbpool.runInteraction(self.do_insert_ai, item)
        elif spider.name == 'lagou':
            print(type(item['type']))
            for it in range(len(item['type'])):
                if "java" in item['type']:
                    # item['url_obj_id'] = item['url_obj_id']+ "{0}".format(random.randint(61, 70))
                    query = self.dbpool.runInteraction(self.do_insert_java, item)
                    query.addErrback(self.handle_error, item, spider)  # 处理异常
                if "python" in item['type'] :
                    # item['url_obj_id'] = item['url_obj_id'] + "{0}".format(random.randint(51, 60))
                    query = self.dbpool.runInteraction(self.do_insert_python, item)
                    query.addErrback(self.handle_error, item, spider)  # 处理异常
                if "人工智能" in item['type'] :
                    # item['url_obj_id'] = item['url_obj_id'] + "{0}".format(random.randint(41, 50))
                    query = self.dbpool.runInteraction(self.do_insert_ai, item)
                    query.addErrback(self.handle_error, item, spider)  # 处理异常
                if "算法" in item['type'][it] :
                    # item['url_obj_id'] = item['url_obj_id'] + "{0}".format(random.randint(31, 40))
                    query = self.dbpool.runInteraction(self.do_insert_arithmetic, item)
                    query.addErrback(self.handle_error, item, spider)  # 处理异常
                if"大数据" in item['type']:
                    # item['url_obj_id'] = item['url_obj_id'] + "{0}".format(random.randint(21, 30))
                    query = self.dbpool.runInteraction(self.do_insert_bigdata, item)
                    query.addErrback(self.handle_error, item, spider)  # 处理异常
                if "C++" in item['type']:
                    # item['url_obj_id'] = item['url_obj_id'] + "{0}".format(random.randint(1, 10))
                    query = self.dbpool.runInteraction(self.do_insert_cplus, item)
                    query.addErrback(self.handle_error, item, spider)  # 处理异常
                if "go" in item['type']:
                    # item['url_obj_id'] = item['url_obj_id'] + "{0}".format(random.randint(11, 20))
                    query = self.dbpool.runInteraction(self.do_insert_go, item)
                    query.addErrback(self.handle_error, item, spider)  # 处理异常


    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        print(failure)

    def do_insert_java(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        # insert_sql, params = item.get_insert_sql()
        # print(insert_sql, params)
        # cursor.execute(insert_sql, params)
        insert_sql = "insert into  `job_java` (url,url_obj_id,title,salary_min,salary_max,job_city,experience_year,education_need,publish_date,job_advantage_tags,position_info,job_classification,crawl_time)   VALUES (%s , %s ,%s ,%s ,%s,%s,%s , %s ,%s ,%s ,%s,%s,%s)    "
        item['url_obj_id'] = item['url_obj_id'] + "{0}".format(random.randint(61, 70))
        cursor.execute(insert_sql,
                       (item["url"], item["url_obj_id"], item["title"], item["salary_min"], item["salary_max"],
                        item["job_city"], item["experience_year"], item["education_need"], item["publish_date"],
                        item["job_advantage_tags"], item["position_info"], item["job_classification"],
                        item["crawl_time"]))

    def do_insert_python(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        # insert_sql, params = item.get_insert_sql()
        # print(insert_sql, params)
        # cursor.execute(insert_sql, params)
        insert_sql = "insert into  `job_python` (url,url_obj_id,title,salary_min,salary_max,job_city,experience_year,education_need,publish_date,job_advantage_tags,position_info,job_classification,crawl_time)   VALUES (%s , %s ,%s ,%s ,%s,%s,%s , %s ,%s ,%s ,%s,%s,%s)    "
        item['url_obj_id'] = item['url_obj_id'] + "{0}".format(random.randint(51, 60))
        cursor.execute(insert_sql,
                       (item["url"], item["url_obj_id"], item["title"], item["salary_min"], item["salary_max"],
                        item["job_city"], item["experience_year"], item["education_need"], item["publish_date"],
                        item["job_advantage_tags"], item["position_info"], item["job_classification"],
                        item["crawl_time"]))

    def do_insert_ai(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        # insert_sql, params = item.get_insert_sql()
        # print(insert_sql, params)
        # cursor.execute(insert_sql, params)
        insert_sql = "insert into  `job_ai` (url,url_obj_id,title,salary_min,salary_max,job_city,experience_year,education_need,publish_date,job_advantage_tags,position_info,job_classification,crawl_time)   VALUES (%s , %s ,%s ,%s ,%s,%s,%s , %s ,%s ,%s ,%s,%s,%s)    "
        item['url_obj_id'] = item['url_obj_id'] + "{0}".format(random.randint(41, 50))
        cursor.execute(insert_sql,
                       (item["url"], item["url_obj_id"], item["title"], item["salary_min"], item["salary_max"],
                        item["job_city"], item["experience_year"], item["education_need"], item["publish_date"],
                        item["job_advantage_tags"], item["position_info"], item["job_classification"],
                        item["crawl_time"]))

    def do_insert_arithmetic(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        # insert_sql, params = item.get_insert_sql()
        # print(insert_sql, params)
        # cursor.execute(insert_sql, params)
        insert_sql = "insert into  `job_arithmetic` (url,url_obj_id,title,salary_min,salary_max,job_city,experience_year,education_need,publish_date,job_advantage_tags,position_info,job_classification,crawl_time)   VALUES (%s , %s ,%s ,%s ,%s,%s,%s , %s ,%s ,%s ,%s,%s,%s)    "
        item['url_obj_id'] = item['url_obj_id'] + "{0}".format(random.randint(31, 40))
        cursor.execute(insert_sql,
                       (item["url"], item["url_obj_id"], item["title"], item["salary_min"], item["salary_max"],
                        item["job_city"], item["experience_year"], item["education_need"], item["publish_date"],
                        item["job_advantage_tags"], item["position_info"], item["job_classification"],
                        item["crawl_time"]))

    def do_insert_bigdata(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        # insert_sql, params = item.get_insert_sql()
        # print(insert_sql, params)
        # cursor.execute(insert_sql, params)
        insert_sql = "insert into  `job_bigdata` (url,url_obj_id,title,salary_min,salary_max,job_city,experience_year,education_need,publish_date,job_advantage_tags,position_info,job_classification,crawl_time)   VALUES (%s , %s ,%s ,%s ,%s,%s,%s , %s ,%s ,%s ,%s,%s,%s)    "
        item['url_obj_id'] = item['url_obj_id'] + "{0}".format(random.randint(21, 30))
        cursor.execute(insert_sql,
                       (item["url"], item["url_obj_id"], item["title"], item["salary_min"], item["salary_max"],
                        item["job_city"], item["experience_year"], item["education_need"], item["publish_date"],
                        item["job_advantage_tags"], item["position_info"], item["job_classification"],
                        item["crawl_time"]))

    def do_insert_cplus(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        # insert_sql, params = item.get_insert_sql()
        # print(insert_sql, params)
        # cursor.execute(insert_sql, params)
        insert_sql = "insert into  `job_cplus` (url,url_obj_id,title,salary_min,salary_max,job_city,experience_year,education_need,publish_date,job_advantage_tags,position_info,job_classification,crawl_time)   VALUES (%s , %s ,%s ,%s ,%s,%s,%s , %s ,%s ,%s ,%s,%s,%s)    "
        item['url_obj_id'] = item['url_obj_id'] + "{0}".format(random.randint(1, 10))
        cursor.execute(insert_sql,
                       (item["url"], item["url_obj_id"], item["title"], item["salary_min"], item["salary_max"],
                        item["job_city"], item["experience_year"], item["education_need"], item["publish_date"],
                        item["job_advantage_tags"], item["position_info"], item["job_classification"],
                        item["crawl_time"]))

    def do_insert_go(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        # insert_sql, params = item.get_insert_sql()
        # print(insert_sql, params)
        # cursor.execute(insert_sql, params)
        insert_sql = "insert into  `job_go` (url,url_obj_id,title,salary_min,salary_max,job_city,experience_year,education_need,publish_date,job_advantage_tags,position_info,job_classification,crawl_time)   VALUES (%s , %s ,%s ,%s ,%s,%s,%s , %s ,%s ,%s ,%s,%s,%s)    "
        item['url_obj_id'] = item['url_obj_id'] + "{0}".format(random.randint(11, 20))
        cursor.execute(insert_sql,
                       (item["url"], item["url_obj_id"], item["title"], item["salary_min"], item["salary_max"],
                        item["job_city"], item["experience_year"], item["education_need"], item["publish_date"],
                        item["job_advantage_tags"], item["position_info"], item["job_classification"],
                        item["crawl_time"]))

    def do_insert_test(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        # insert_sql, params = item.get_insert_sql()
        # print(insert_sql, params)
        # cursor.execute(insert_sql, params)
        insert_sql = "insert into  `job_test` (url,url_obj_id,title,salary_min,salary_max,job_city,experience_year,education_need,publish_date,job_advantage_tags,position_info,job_classification,crawl_time)   VALUES (%s , %s ,%s ,%s ,%s,%s,%s , %s ,%s ,%s ,%s,%s,%s)    "

        cursor.execute(insert_sql,
                       (item["url"], item["url_obj_id"], item["title"], item["salary_min"], item["salary_max"],
                        item["job_city"], item["experience_year"], item["education_need"], item["publish_date"],
                        item["job_advantage_tags"], item["position_info"], item["job_classification"],
                        item["crawl_time"]))
        # 使用twisted将mysql插入变成异步执行
    #
    #     if spider.name == 'job51':
    #         query = self.dbpool.runInteraction(self.do_insert_job51, item)
    #         query.addErrback(self.handle_error, item, spider)  # 处理异常
    #
    # def handle_error(self, failure, item, spider):
    #     # 处理异步插入的异常
    #     print(failure)
    #
    # def do_insert_job51(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        # insert_sql, params = item.get_insert_sql()
        # print(insert_sql, params)
        # cursor.execute(insert_sql, params)
        # insert_table_name = ""
        # if re.search('java', item['title'], re.IGNORECASE):
        #     insert_table_name = "java"
        # elif re.search('人工智能', item['title'], re.IGNORECASE):
        #     insert_table_name = "ai"
        # elif re.search('算法', item['title'], re.IGNORECASE):
        #     insert_table_name = "arithmetic"
        # elif re.search("大数据", item['title'], re.IGNORECASE):
        #     insert_table_name = "bigdata"
        # elif re.search("C\+\+", item['title'], re.IGNORECASE):
        #     insert_table_name = "cplus"
        # elif re.search('go', item['title'], re.IGNORECASE):
        #     insert_table_name = "go"
        # elif re.search('python', item['title'], re.IGNORECASE):
        #     insert_table_name = "python"
        # insert_sql = "insert into  `job_"+insert_table_name+"` (url,url_obj_id,title,salary_min,salary_max,job_city,experience_year,education_need,publish_date,job_advantage_tags,position_info,job_classification,crawl_time)   VALUES (%s , %s ,%s ,%s ,%s,%s,%s , %s ,%s ,%s ,%s,%s,%s)    "
        # cursor.execute(insert_sql,
        #                (item["url"], item["url_obj_id"], item["title"], item["salary_min"], item["salary_max"],
        #                 item["job_city"], item["experience_year"], item["education_need"], item["publish_date"],
        #                 item["job_advantage_tags"], item["position_info"], item["job_classification"],
        #                 item["crawl_time"]))

