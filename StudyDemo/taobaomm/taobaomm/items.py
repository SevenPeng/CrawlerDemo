# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaommItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class tbModelItem(scrapy.Item):
    avatarUrl = scrapy.Field()
    cardUrl = scrapy.Field()
    city = scrapy.Field()
    height = scrapy.Field()
    identityUrl = scrapy.Field()
    modelUrl = scrapy.Field()
    realName = scrapy.Field()
    totalFanNum = scrapy.Field()
    totalFavorNum = scrapy.Field()
    userId = scrapy.Field()
    viewFlag = scrapy.Field()
    weight = scrapy.Field()
