# -*- coding: utf-8 -*-
import json
import urllib

import scrapy
from scrapy.http import Request

from Crawl500px import Crawl500PxItem


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['500px.com']
    # start_urls = ['https://500px.me/community/discover/rating?resourceType=0,2&category=&page=1&size=20&type=json']
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            'Host': '500px.me',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Referer': ' https://500px.me/community/discover',
            'Accept-Encoding': 'gzip, deflate',
            'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
            "Cookie": "UM_distinctid=15dcf940bafd0-0c828ace06578b-7f5935-1fa400-15dcf940bb0387; JSESSIONID=BCE2027EEE27A114BFAE2F44A3E0ABD5; CNZZDATA1256793290=352559349-1502424042-%7C1502517948; _ga=GA1.2.253009900.1497271844; _gid=GA1.2.1016557290.1502519195; Hm_lvt_78ea451fc4ef02358930eaa6448bfcaf=1502426173,1502432403,1502519195,1502519734; Hm_lpvt_78ea451fc4ef02358930eaa6448bfcaf=1502519748"
        },
    }

    # 通过start_request方法编写首次的爬取行为
    def start_requests(self):
        # 首次爬取模拟成浏览器进行
        yield Request("https://500px.me/community/discover/rating?resourceType=0,2&category=&page=1&size=20&type=json")

    def parse(self, response):
        item = Crawl500PxItem()
        sites = json.loads(response.body_as_unicode())
        i = 0
        for site in sites:
            item['title'] = site['title']
            item['ratingMax'] = site['ratingMax']
            item['url'] = site['url']['p4']
            item['name'] = site['uploaderInfo']['nickName']
            i=i+1
            localpath = "F:/CrawlerData/500px/Image/" + str(i)+".jpg"
            # localpath = "F:/CrawlerData/500px/Image/" +str(i)+ '-' + item['title'] + ".jpg"
            print(i)
            urllib.request.urlretrieve(item['url'], filename=localpath)
        yield item
        for i in range(1, 2000):
            # 构造要爬取的网址
            url = "https://500px.me/community/discover/rating?resourceType=0,2&category=&page="+str(i)+"&size=20&type=json"
            print(url)
            # 通过yield返回的request,并指定要爬取的网址和回调函数
            # 实现自动爬取
            yield Request(url, callback=self.parse)
