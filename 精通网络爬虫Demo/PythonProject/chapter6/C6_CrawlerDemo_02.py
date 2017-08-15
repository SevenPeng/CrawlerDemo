import re
import urllib.request


def getlink(url):
    # 模拟成浏览器
    headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # 将opener安装为全局
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    # 根据需求构建连接表达式
    # 需要后期改进,只能获取部分网页
    pat = '(http?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    # 去除重复元素
    link = list(set(link))
    return link


# 要爬取的网页链接
url = "http://blog.csdn.net/"
# 获取对应网页中包含的链接地址
linklist = getlink(url)
# 通过for循环分别遍历输出到链接地址到屏幕上
for link in linklist:
    print(link[0])
