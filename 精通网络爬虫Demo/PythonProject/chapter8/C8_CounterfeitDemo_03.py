import urllib.request
import http.cookiejar

url = "https://www.baidu.com/"
# 以字典形式设置headers
headers = {"Accept": " text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Encoding": " gb2312,utf-8",
           "Accept-Language": " zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
           "Connection": "keep-alive",
           "referer": "baidu.com"}
# 设置cookie
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
# 建立空列表,为了以指定格式存储头信息
headall = []
# 通过for循环遍历字典,构造出格式的headers信息
for key, value in headers.items():
    item = (key, value)
    headall.append(item)
# 将指定格式的headers信息添加好
opener.addheaders = headall
# 将opener安装为全局
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read()
print(data)
fhandle = open("F:/CrawlerData/Counterfeit/3.html", "wb")
fhandle.write(data)
fhandle.close()
