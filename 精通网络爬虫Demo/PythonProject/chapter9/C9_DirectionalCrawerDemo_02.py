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


# 建立一个自定义函数craw(vid,comid),实现自动爬取对应评论网页并返回爬取数据
def craw(vid, comid):
    url = "http://coral.qq.com/article/" + vid + "/comment?commentid=" + comid + "&reqnum=20"
    data = urllib.request.urlopen(url).read().decode("utf-8")
    return data


idpat = '"id":"(.*?)"'
userpat = '"nick":"(.*?)",'
conpat = '"content":"(.*?)",'
# 第一层循环, 代表爬取多少页, 每一次外层循环爬取一页
for i in range(1, 10):
    print("------------------------------------")
    print("第" + str(i) + "页评论内容")
    data = craw(vid, comid)
    # 第二层循环, 根据爬取的结果提取并处理每条评论的信息, 一页20条评论
    for j in range(0, 10):
        idlist = re.compile(idpat, re.S).findall(data)
        userlist = re.compile(userpat, re.S).findall(data)
        conlist = re.compile(conpat, re.S).findall(data)
        print("用户名是 :"+userlist[j])
        print("评论内容是:"+conlist[j])
        print("\n")
    # 将comid改变为该页的最后一条评论id, 实现不断自动加载
    comid = idlist[19]
