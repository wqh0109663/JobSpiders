# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from email import charset

import MySQLdb
from twisted.enterprise import adbapi
import MySQLdb.cursors


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
        #or spider.name == 'zhaopin_java'
        if spider.name == 'job51' or spider.name == 'zhaopin_java' :
            query = self.dbpool.runInteraction(self.do_insert_java, item)
        elif spider.name == 'job_python' or spider.name == 'zhaopin_python':
            query = self.dbpool.runInteraction(self.do_insert_python, item)
        elif spider.name == 'job_go' or spider.name == 'zhaopin_go':
            query = self.dbpool.runInteraction(self.do_insert_go, item)
        elif spider.name == 'job_cplus' or spider.name == 'zhaopin_cplus':
            query = self.dbpool.runInteraction(self.do_insert_cplus, item)
        elif spider.name == 'job_bigdata' or spider.name == 'zhaopin_bigdata':
            query = self.dbpool.runInteraction(self.do_insert_bigdata, item)
        elif spider.name == 'job_arithmetic' or spider.name == 'zhaopin_arithmetic':
            query = self.dbpool.runInteraction(self.do_insert_arithmetic, item)
        elif spider.name == 'job_ai' or spider.name == 'zhaopin_ai':
            query = self.dbpool.runInteraction(self.do_insert_ai, item)
        # elif spider.name == 'zhaopin_cplus':
        #     query = self.dbpool.runInteraction(self.do_insert_test, item)
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