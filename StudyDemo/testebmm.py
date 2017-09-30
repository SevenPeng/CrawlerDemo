# -*- coding: utf-8 -*-
import scrapy


class TestebmmSpider(scrapy.Spider):
    name = 'testebmm'
    allowed_domains = ['tbmm.com']
    start_urls = ['http://tbmm.com/']

    def parse(self, response):
        pass
