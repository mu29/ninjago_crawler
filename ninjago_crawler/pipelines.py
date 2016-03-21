# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import MySQLdb

class DataStorePipeline(object):

    def __init__(self):
        self.conn = MySQLdb.connect(user='root', passwd='projectDanbi', db='ninjago', host='localhost', charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("INSERT INTO videos (title, video_id, minute, thumbnail_url) VALUES (%s, %s, %s, %s)",
                                (item['title'].strip(), item['video_id'], item['minute'], item['thumbnail_url']))
            self.conn.commit()

        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])

        return item
