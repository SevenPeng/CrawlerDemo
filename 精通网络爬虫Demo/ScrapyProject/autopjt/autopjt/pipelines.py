# -*- coding: utf-8 -*-
import codecs
import json


class AutopjtPipeline(object):
    def __init__(self):
        # 打开mydata.json文件
        # self.file = codecs.open("F:\CrawlerData\part15\mydata.json", "wb", encoding="utf-8")
        self.file = codecs.open("F:\CrawlerData\part15\mydata3.json", "wb", encoding="utf-8")

    def process_item(self, item, spider):
        # i = json.dumps(dict(item), ensure_ascii=False)
        # # 每条数据后加上换行
        # line = i + '\n'
        # # 数据写入到mydata.json文件中
        # self.file.write(line)
        # return item
        for j in range(0, len(item["name"])):
            # 将当前页的第j个商品的名称赋值给变量name
            name = item["name"][j]
            price = item["price"][j]
            comnum = item["comnum"][j]
            link = item["link"][j]

            # 将当前页下第j个商品的name,price,commun,link信息处理一下,重新组合成一个字典
            goods = {"name": name, "price": price, "comnum": comnum, "link": link}
            # 写入json文件
            i = json.dumps(dict(goods), ensure_ascii=False)
            line = i + '\n'
            self.file.write(line)
        return item

    def close_spider(self, spider):
        # 关闭mydata.json文件
        self.file.close()
