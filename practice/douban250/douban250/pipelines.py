# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl
import pymysql

class DBPipeline:

    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    passwd='hyyldlbhs.1314',
                                    db='spiders',
                                    port=3306,
                                    charset='utf8mb4'
                                    )
        self.cursor = self.conn.cursor()
        self.data = []

    def close_spider(self,spider):
        if len(self.data) >0:
            self.write_to_db()
        self.conn.close()
        
    def process_item(self,item,spider):
        title = item.get('title','')#如果拿不到就给空字符串
        rank = item.get('rank',0)
        subject = item.get('subject','')
        duration = item.get('duration','')
        intro = item.get('intro','')
        self.data.append((title,rank,subject,duration,intro))
        if len(self.data) >= 100:
            self.write_to_db()
            self.data.clear()
        return item

    def write_to_db(self):
        self.cursor.executemany('insert into tb_top_movie (title, rating, subject, duration, intro) values (%s, %s, %s, %s, %s)',
                                self.data)
        self.conn.commit()
    
class Douban250Pipeline:

    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title= 'TOP250'
        self.ws.append(('标题','评分','主题','时长','简介'))#表头
        print('open done')

    def close_spider(self,spider):
        self.wb.save('电影数据.xlsx')
        print('save done')

    def process_item(self, item, spider):
        title = item.get('title','')#如果拿不到就给空字符串
        rank = item.get('rank','')
        subject = item.get('subject','')
        duration = item.get('duration','')
        intro = item.get('intro','')
        self.ws.append((title,rank,subject,duration,intro))
        return item
