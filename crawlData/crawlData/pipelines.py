# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3


class CrawlDataPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("baoDienTu.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS doanh_nghiep_tb""")
        self.curr.execute("""create table doanh_nghiep_tb(
                            title text,
                            url text,
                            description text
                            )""")
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        for i in range(len(item['title'])):
            self.curr.execute("""insert into doanh_nghiep_tb values(?, ?, ?)""", (
                item['title'][i],
                item['url'][i],
                item['description'][i]
            ))
            self.conn.commit()
