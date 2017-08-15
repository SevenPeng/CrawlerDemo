# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HexunpjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 建立 name 存储文章名
    name = scrapy.Field()
    # 建立 url 存储文章网址
    url = scrapy.Field()
    # 建立 hits 存储文章阅读数
    hits = scrapy.Field()
    # 建立 comment 存储文章评论数
    comment = scrapy.Field()
