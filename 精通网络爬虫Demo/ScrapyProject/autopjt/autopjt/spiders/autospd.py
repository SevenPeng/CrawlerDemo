# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

from 精通网络爬虫Demo.ScrapyProject.autopjt.autopjt import AutopjtItem


class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4002203-srsort_sale_amt_desc.html']

    def parse(self, response):
        item = AutopjtItem()
        # 通过Xpath表达式分别提取商品的名称,价格,链接,评论数等信息
        item["name"] = response.xpath("//a[@class='pic']/@title").extract()
        print(item["name"])
        item["price"] = response.xpath("//span[@class='price_n']/text()").extract()
        item["link"] = response.xpath("//a[@class='pic']/@href").extract()
        item["comnum"] = response.xpath("//a[@name='itemlist-review']/text()").extract()

        # 提取完后返回item
        yield item

        # 通过循环自动爬取75页的数据
        for i in range(1, 10):
            # 构造要爬取的网址
            url = "http://category.dangdang.com/pg" + str(i) + "-cid4002203-srsort_sale_amt_desc.html"
            # 通过yield返回的request,并指定要爬取的网址和回调函数
            # 实现自动爬取
            yield Request(url, callback=self.parse)
