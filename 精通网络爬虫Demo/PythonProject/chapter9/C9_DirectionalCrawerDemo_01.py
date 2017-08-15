import urllib.request
import http.cookiejar
import re

# 设置视频编号
vid = "1472528692"
# 设置评论起始编号
comid = "6289453800084752070"
# 构造出真实评论请求网址
url = "http://coral.qq.com/article/" + vid + "/comment?commentid=" + comid + "&reqnum=20"
# 设置头信息伪装成浏览器爬取
headers = {"Accept": " text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Encoding": " gb2312,utf-8",
           "Accept-Language": " zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
           "Connection": "keep-alive",
           "referer": "qq.com"}
# 设置cookie
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
headall = []
for key, value in headers.items():
    item = (key, value)
    headall.append(item)
opener.addheaders = headall
urllib.request.install_opener(opener)
# 爬取该网页
data = urllib.request.urlopen(url).read().decode("utf-8")
print(data)
# 分别构建筛选id、用户名、评论内容等信息的正则表达式
idpat = '"id":"(.*?)"'
userpat = '"nick":"(.*?)",'
conpat = '"content":"(.*?)",'
# 分别根据正则表达式查找所有id、用户名、评论内容等信息
idlist = re.compile(idpat, re.S).findall(data)
userlist = re.compile(userpat, re.S).findall(data)
conlist = re.compile(conpat, re.S).findall(data)
# 通过循环将获取到的各信息遍历出来
for i in range(0, 20):
    # 输出对应信息, 并对字符串进行unicode编码, 从而正常显示
    print("用户名是 :" + eval('u"' + userlist[i] + '"'))
    print("评论内容是:" + eval('u"' + conlist[i] + '"'))
    print("\n")
