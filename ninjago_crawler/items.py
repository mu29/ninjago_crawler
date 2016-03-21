# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VideoItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    video_id = scrapy.Field()
    minute = scrapy.Field()
    thumbnail_url = scrapy.Field()
