# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from 精通网络爬虫Demo.ScrapyProject.mysqlpjt.mysqlpjt import MysqlpjtItem


class SevenSpider(CrawlSpider):
    name = 'seven'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=('.*?/[0-9]{4}.[0-9]{2}.[0-9]{2}.doc-.*?shtml'),
                           allow_domains=('sina.com.cn')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = MysqlpjtItem()
        # 通过XPath表达式提取网页标题
        i["name"] = response.xpath("/html/head/title/text()").extract()
        # 通过XPath表达式提取网页的关键词
        i["keywd"] = response.xpath("/html/head/meta[@name='keywords']/@content").extract()
        return i
