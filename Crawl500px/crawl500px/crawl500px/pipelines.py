# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib


class Crawl500PxPipeline(object):

    def process_item(self, item, spider):
        # # 图片网址
        # url = item['url']
        # # 构造出图片在本地存储的地址
        # localpath = "F:/CrawlerData/500px/Image/" + item["picid"] + "-" + item['name'] + ".jpg"
        # # 通过urllib.request.urlretrieve()将原图片下载到本地
        # urllib.request.urlretrieve(url, filename=localpath)
        return item
