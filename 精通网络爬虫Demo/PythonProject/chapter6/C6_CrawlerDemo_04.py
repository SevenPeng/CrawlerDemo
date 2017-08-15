import re
import urllib.request
import time
import urllib.error

# 模拟成浏览器
headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0')
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)  # 将opener安装为全局
# 设置一个列表Listurl存储文章网址列表
listurl = []


# 自定义函数,功能为使用代理服务器
def use_proxy(proxy_addr, url):
    # 建立异常处理机制
    try:
        import urllib.request
        proxy = urllib.request.ProxyHandler({'http': proxy_addr})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        # 若为URLError异常,延时10秒执行
        time.sleep(10)
    except Exception as e:
        print("exception:" + str(e))
        # 若为Exception异常,延时1秒执行
        time.sleep(1)


def getlisturl(key, pagestart, pageend, proxy):
    try:
        page = pagestart
        # 编码关键词key
        keycode = urllib.request.quote(key)
        # 编码"&page"
        pagecode = urllib.request.quote("&page")
        # 循环构建各页的url链接
        for page in range(pagestart, pagestart + 1):
            # 分别各页带URL链接,每次循环构建一次
            url = "http://weixin.sogou.com/weixin?type=2&query=" + keycode + pagecode + str(page)
            # 用代理服务器爬取,解决IP被封杀问题
            data1 = use_proxy(proxy, url)
            # 获取文章链接的正则表达式
            listurlpat = '<div class="txt-box">.*?(http:// .*?)"'
            # 获取每页的所有文章链接并添加到列表listurl中
            listurl.append(re.compile(listurl, re.S).findall(data1))
        print("共获取到" + str(len(listurl)) + "页")  # 便于调试
        return listurl
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    except Exception as e:
        print("exception: " + str(e))
        # 若为Exception异常,延时1秒执行
        time.sleep(1)


# 通过文章链接获取对应内容
def getcontent(listurl, proxy):
    i = 0
    # 设置本地文件中的开始html编码
    html1 = '''<!DOCTYPE html PUBLIC "-// W3C// DTD XHTML 1.0 Transitional// EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http:// www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>微信文章页面</title>
</head>
<body>'''
    fh = open("F:/CrawlerData/wechat/1.html", "wb")
    fh.write(html1.encode("utf-8"))
    fh.close()
    # 再次以追加写入的方式打开文件,写入对应文章内容
    fh = open("F:/CrawlerData/wechat/1.html", "ab")
    # 此时listurl为二维列表,形入listurl[][],第一纬存储的信息跟第几页相关,第二纬存的跟该页带第几个文章链接相关


# for i in range(0, len(listurl)):
#     for j in range(0, len(listurl[i])):
