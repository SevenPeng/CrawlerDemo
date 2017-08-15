import urllib.request
import urllib.parse

url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes"
postdata = urllib.parse.urlencode({
    "username": "seventest",
    "password": "seven456"
}).encode('utf-8')  # 使用urlcode编码处理后,再设置为utf-8编码
req = urllib.request.Request(url, postdata)  # 构造Request对象
# Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0
req.add_header('User-Agent',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0')  # 模拟浏览器
data = urllib.request.urlopen(req).read()  # 登录并爬取对应网页
fhandle = open("F:/CrawlerData/c5_1.html", "wb")
fhandle.write(data)  # 将内容写入对应文件
fhandle.close()

url2 = "http://bbs.chinaunix.net/"  # 设置要爬取得该网站下的其他网站
req2 = urllib.request.Request(url2, postdata)
req.add_header('User-Agent',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0')  # 模拟浏览器
data2 = urllib.request.urlopen(req2).read()  # 爬去该网站下的其他网页
fhandle = open("F:/CrawlerData/c5_2.html", "wb")
fhandle.write(data2)
fhandle.close()
