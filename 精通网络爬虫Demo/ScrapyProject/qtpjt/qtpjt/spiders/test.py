# -*- coding: utf-8 -*-
import scrapy


class QtspdSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['58pic.com']
    start_urls = ['http://www.58pic.com/piccate/3-0-0.html']

    def parse(self, response):
        print(str(response.body))
