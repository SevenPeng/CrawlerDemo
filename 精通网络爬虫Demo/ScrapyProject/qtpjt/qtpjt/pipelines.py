# -*- coding: utf-8 -*-
import urllib.request


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QtpjtPipeline(object):
    def process_item(self, item, spider):
        print("---------------进入pipelines----------------")
        # 一个图片列表页中有多张图片, 通过for循环依次将图片存储到本地
        print(len(item["picurl"]))
        for i in range(0, len(item["picurl"])):
            thispic = item["picurl"][i]
            print("thispic is " + thispic)
            # 根据上面总结的规律构造出原图片的URL地址
            trueurl = thispic + "_1024.jpg"
            print("truturl is " + trueurl)
            # 构造出图片在本地存储的地址
            localpath = "F:/CrawlerData/part19/" + item["picid"][i] + ".jpg"
            print("localpath is " + localpath)
            # 通过urllib.request.urlretrieve()将原图片下载到本地
            urllib.request.urlretrieve(trueurl, filename=localpath)
        return item
