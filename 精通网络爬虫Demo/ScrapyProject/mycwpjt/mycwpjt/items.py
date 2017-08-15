# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MycwpjtItem(scrapy.Item):
    # 存储对应新闻的标题
    name = scrapy.Field()
    # 存储对应新闻的链接
    link = scrapy.Field()
