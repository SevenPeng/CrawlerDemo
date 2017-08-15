import urllib.request
import http.cookiejar
import json
import datetime
import time

# 设置头信息伪装成浏览器爬取
headers = {'Host': '500px.me',
           'Connection': 'keep-alive',
           'Cache-Control': 'max-age=0',
           'Accept': 'application/json, text/javascript, */*; q=0.01',
           'X-Requested-With': 'XMLHttpRequest',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
           'Referer': ' https://500px.me/community/discover',
           'Accept-Encoding': 'gzip, deflate',
           'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
           "Cookie": "UM_distinctid=15dcf940bafd0-0c828ace06578b-7f5935-1fa400-15dcf940bb0387; JSESSIONID=BCE2027EEE27A114BFAE2F44A3E0ABD5; CNZZDATA1256793290=352559349-1502424042-%7C1502517948; _ga=GA1.2.253009900.1497271844; _gid=GA1.2.1016557290.1502519195; Hm_lvt_78ea451fc4ef02358930eaa6448bfcaf=1502426173,1502432403,1502519195,1502519734; Hm_lpvt_78ea451fc4ef02358930eaa6448bfcaf=1502519748"
           }
# 设置cookie
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
headall = []
for key, value in headers.items():
    item = (key, value)
    headall.append(item)
opener.addheaders = headall
urllib.request.install_opener(opener)


def craw(page):
    url = "https://500px.me/community/discover/rating?resourceType=0,2&category=&page=" + str(
        page) + "&size=20&type=json"
    datas = json.loads(urllib.request.urlopen(url).read().decode("utf-8"))
    for data in datas:
        now_time = datetime.datetime.now().strftime('%Y%m%d')
        fileurl = "F:/CrawlerData/500px/Image/" + str(now_time) + "-" + str(data['rating']) + "-" + str(data['id']) + ".jpg"
        data = urllib.request.urlopen(data['url']['p4']).read()
        fhandle = open(fileurl, "wb")
        fhandle.write(data)
        fhandle.close()


for i in range(1, 200):
    print("------------------第" + str(i) + "次--------------")
    craw(i)
    # time.sleep(5)
