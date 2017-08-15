# -*- coding: utf-8 -*-
import scrapy
import re
import urllib.request
from scrapy.http import Request
from hexunpjt.items import HexunpjtItem


class MyhexunspdSpider(scrapy.Spider):
    name = "myhexunspd"
    allowed_domains = ["hexun.com"]
    # 设置要爬取的用户的 uid, 为后续构造爬取网址做准备
    uid = "19940007"

    # 通过 start_requests 方法编写首次的爬取行为
    def start_requests(self):
        # 首次爬取模拟成浏览器进行
        yield Request("http://" + str(self.uid) + ".blog.hexun.com/p1/default.html", headers={
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0"})

    def parse(self, response):
        item = HexunpjtItem()
        item['name'] = response.xpath("//span[@class='ArticleTitleText']/a/text()").extract()
        item["url"] = response.xpath("//span[@class='ArticleTitleText']/a/@href").extract()
        # 接下来需要使用 urllib 和 re 模块获取博文的评论数和阅读数
        # 首先提取存储评论数和点击数网址的正则表达式
        pat1 = '<script type="text/javascript" src="(http://click.tool.hexun.com/.*?)">'
        # hcurl 为存储评论数和点击数的网址
        hcurl = re.compile(pat1).findall(str(response.body))[0]
        # 模拟成浏览器
        headers2 = ("User-Agent",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0")
        opener = urllib.request.build_opener()
        opener.addheaders = [headers2]
        # 将 opener 安装为全局
        urllib.request.install_opener(opener)
        # data 为对应博客列表页的所有博文的点击数与评论数数据
        data = urllib.request.urlopen(hcurl).read()
        # pat2 为提取文章阅读数的正则表达式
        pat2 = "click\d*?','(\d*?)'"
        # pat3 为提取文章评论数的正则表达式
        pat3 = "comment\d*?','(\d*?)'"
        # 提取阅读数和评论数数据并分别赋值给 item 下的 hits 和 comment
        item["hits"] = re.compile(pat2).findall(str(data))
        item["comment"] = re.compile(pat3).findall(str(data))
        yield item
        # 提取博文列表页的总页数
        pat4 = "blog.hexun.com/p(.*?)/"
        # 通过正则表达式获取到的数据为一个列表, 倒数第二个元素为总页数
        data2 = re.compile(pat4).findall(str(response.body))
        if (len(data2) >= 2):
            totalurl = data2[-2]
        else:
            totalurl = 1
        # 在实际运行中, 下一行 print 的代码可以注释掉, 在调试过程中, 可以开启下一行 print 的代码
        # print("一共"+str(totalurl)+"页")
        # 进入 for 循环, 依次爬取各博文列表页的博文数据
        for i in range(2, int(totalurl) + 1):
            # 构造下一次要爬取的 url, 爬取一下页博文列表页中的数据
            nexturl = "http://" + str(self.uid) + ".blog.hexun.com/p" + str(i) + "/default.html"
            # 进行下一次爬取, 下一次爬取仍然模拟成浏览器进行
            yield Request(nexturl, callback=self.parse, headers={
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0"})
