import urllib.request
import urllib.parse
import http.cookiejar

url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes"
postdata = urllib.parse.urlencode({
    "username": "seventest",
    "password": "seven456"
}).encode('utf-8')  # 使用urlcode编码处理后,再设置为utf-8编码
req = urllib.request.Request(url, postdata)  # 构造Request对象
# Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0
req.add_header('User-Agent',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0')  # 模拟浏览器
# 使用http.cookiejar.CookJar()创建Cookie对象
cjar = http.cookiejar.CookieJar()
# 使用HTTPCookieProcessor创建cookie处理器,并以其为参数构建opener对象
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
# 将opener安装为全局
urllib.request.install_opener(opener)
file = opener.open(req)
data = file.read()
file = open("F:/CrawlerData/c5_3.html", "wb")
file.write(data)
file.close()

url2 = "http://bbs.chinaunix.net/"  # 设置要爬取得该网站下的其他网站
data2 = urllib.request.urlopen(url2).read()
fhandle = open("F:/CrawlerData/c5_4.html", "wb")
fhandle.write(data2)
fhandle.close()

