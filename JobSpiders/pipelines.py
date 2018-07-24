# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


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

        if spider.name == 'job51':
            query = self.dbpool.runInteraction(self.do_insert_job51, item)
            query.addErrback(self.handle_error, item, spider)  # 处理异常

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        print(failure)

    def do_insert_job51(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        # insert_sql, params = item.get_insert_sql()
        # print(insert_sql, params)
        # cursor.execute(insert_sql, params)
        insert_table_name = ""
        if re.search('java', item['title'], re.IGNORECASE):
            insert_table_name = "java"
        elif re.search('人工智能', item['title'], re.IGNORECASE):
            insert_table_name = "ai"
        elif re.search('算法', item['title'], re.IGNORECASE):
            insert_table_name = "arithmetic"
        elif re.search("大数据", item['title'], re.IGNORECASE):
            insert_table_name = "bigdata"
        elif re.search("C\+\+", item['title'], re.IGNORECASE):
            insert_table_name = "cplus"
        elif re.search('go', item['title'], re.IGNORECASE):
            insert_table_name = "go"
        elif re.search('python', item['title'], re.IGNORECASE):
            insert_table_name = "python"
        insert_sql = "insert into  `job_"+insert_table_name+"` (url,url_obj_id,title,salary_min,salary_max,job_city,experience_year,education_need,publish_date,job_advantage_tags,position_info,job_classification,crawl_time)   VALUES (%s , %s ,%s ,%s ,%s,%s,%s , %s ,%s ,%s ,%s,%s,%s)    "
        cursor.execute(insert_sql,
                       (item["url"], item["url_obj_id"], item["title"], item["salary_min"], item["salary_max"],
                        item["job_city"], item["experience_year"], item["education_need"], item["publish_date"],
                        item["job_advantage_tags"], item["position_info"], item["job_classification"],
                        item["crawl_time"]))

