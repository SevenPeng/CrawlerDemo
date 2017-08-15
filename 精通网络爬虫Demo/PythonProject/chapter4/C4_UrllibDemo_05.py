import urllib.request
import urllib.parse

url = "http:// www.iqianyue.com/mypost/"
postdata = urllib.parse.urlencode({
    "name": "ceo@iqianyue.com",
    "pass": "aA123456"
}).encode('utf-8')  # 将数据使用urlencode编码处理后, 使用encode()设置为utf-8编码
req = urllib.request.Request(url, postdata)
req.add_header('User-Agent',
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
data = urllib.request.urlopen(req).read()
fhandle = open("F:/CrawlerData/5.html", "wb")
fhandle.write(data)
fhandle.close()
