# -*- coding: utf-8 -*-
import scrapy


class Tbmm2Spider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['mm.taobao.com']
    # scrapy工程里有多个spider的时候这个custom_setting就显得很有用了
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            'authority': 'mm.taobao.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
            'origin': 'https://mm.taobao.com',
            'referer': 'https://mm.taobao.com/search_tstar_model.htm?spm=719.1001036.1998606017.2.KDdsmP',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'x-requested-with': 'XMLHttpRequest',
            'cookie': 'thw=cn; isg=AoqKYZ_s50Ww7mvpPjMafqhr2nMm501MlyFc-hTDxV1uxyqB_Ate5dA_oQnk; cna=; t=585d676f6e1e87ee12994d3a68f84e86; JSESSIONID=0314745906546971EB3D78C232582620; uc1=cookie14=UoTcDU9NdOLNgw%3D%3D; v=0; cookie2=13d4de71952d3a05208383c6b682f297'
        },
        # ITEM_PIPELINES，自定义管道模块，当item获取到数据后会调用你指定的管道处理命令
        "ITEM_PIPELINES": {
            'MySpider.pipelines.tbModelPipeline': 300
        }
    }

    def start_requests(self):
        url = "https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8"
        requests = []
        for i in range(1, 2):
            formdata = {
                "q": "",
                "sortType": "default",
                "searchStyle": "",
                "searchRegion": "city:",
                "searchFansNum": "",
                "currentPage": str(i),
                "pageSize": "100"
            }
            request = FormRequest(url, callback=self.parse_model, formdata=formdata)
            requests.append(request)
        return requests

        # parse函数里利用json库解析了返回来得数据，赋值给item的相应字段
        def parse_model(self, response):
            print(response)

    def parse(self, response):
        pass

