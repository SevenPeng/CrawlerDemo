# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutopjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义好name用来储存商品名
    name = scrapy.Field()
    # 定义好price用来储存商品价格
    price = scrapy.Field()
    # 定义好name用来储存商品链接
    link = scrapy.Field()
    # 定义好name用来储存商品评论数
    comnum = scrapy.Field()
