import re
import urllib.request
import time
import urllib.error

# 模拟成浏览器
headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0')
opener = urllib.request.build_opener()
opener.addheaders = [headers]
# 将opener安装为全局
urllib.request.install_opener(opener)
# 设置一个列表listurl存储文章网址列表
listurl = []


# 自定义函数, 功能为使用代理服务器爬取指定网页,将数据返回
# 此方法不可久用,易出现"用户您好，您的访问过于频繁，为确认本次访问为正常用户行为，需要您协助验证。"
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
        # 若为URLError异常, 延时10秒执行
        time.sleep(5)
    except Exception as e:
        print("exception on proxy:" + str(e))
        # 若为Exception异常, 延时1秒执行
        time.sleep(1)


# 获取所有文章链接
def getlisturl(key, pagestart, pageend, proxy):
    try:
        page = pagestart
        keycode = urllib.request.quote(key)  # 编码关键词key
        # pagecode = urllib.request.quote("&page")  # 编码"&page" --不编码 2017-7-7
        pagecode = "&page="
        # 循环爬取各页的文章链接
        for page in range(pagestart, pageend + 1):
            # 分别构建各页的url链接, 每次循环构建一次
            url = "http://weixin.sogou.com/weixin?type=2&query=" + keycode + pagecode + str(page)
            # 用代理服务器爬取, 解决IP被封杀问题
            data1 = use_proxy(proxy, url)
            # 获取文章链接的正则表达式
            listurlpat = '<div class="txt-box">.*?(http://.*?)"'
            # 获取每页的所有文章链接并添加到列表listurl中
            listurl.append(re.compile(listurlpat, re.S).findall(data1))
            print(listurl)
        print("共获取到" + str(len(listurl)) + "页")  # 便于调试
        return listurl
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        # 若为URLError异常, 延时3秒执行
        time.sleep(3)
    except Exception as e:
        print("exception on get:" + str(e))
        # 若为Exception异常, 延时1秒执行
        time.sleep(1)


# 通过文章链接获取对应内容
def getcontent(listurl, proxy):
    i = 0
    # 设置本地文件中的开始html编码
    html1 = '''<!DOCTYPE html PUBLIC "-// W3C// DTD XHTML 1.0 Transitional// EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>微信文章页面</title>
</head>
<body>'''
    fh = open("F:/CrawlerData/wechat/1.html", "wb")
    fh.write(html1.encode("utf-8"))
    fh.close()
    # 再次以追加写入的方式打开文件, 以写入对应文章内容
    fh = open("F:/CrawlerData/wechat/1.html", "ab")
    # 此时listurl为二维列表, 形如listurl[][],第一维存储的信息跟第几页相关, 第二维存的跟该页第几个文章链接相关
    for i in range(0, len(listurl)):
        for j in range(0, len(listurl[i])):
            try:
                url = listurl[i][j]
                # 处理成真实url, 读者亦可以观察对应网址的关系自行分析, 采集网址比真实网址多一串amp
                url = url.replace("amp;", "")
                # 使用代理去爬取对应网址的内容
                data = use_proxy(proxy, url)
                # 文章标题正则表达式
                titlepat = "<title>(.*?)</title>"
                # 文章内容正则表达式
                contentpat = 'id="js_content">(.*?)id="js_sg_bar"'
                # 通过对应正则表达式找到标题并赋给列表title
                title = re.compile(titlepat).findall(data)
                # 通过对应正则表达式找到内容并赋给列表content
                content = re.compile(contentpat, re.S).findall(data)
                # 初始化标题与内容
                thistitle = "此次没有获取到"
                thiscontent = "此次没有获取到"
                # 如果标题列表不为空, 说明找到了标题, 取列表第零个元素, 即此次标题赋给变量thistitle
                if (title != []):
                    thistitle = title[0]
                if (content != []):
                    thiscontent = content[0]
                # 将标题与内容汇总赋给变量dataall
                dataall = "<p>标题为:" + thistitle + "</p><p>内容为:" + thiscontent + "</p><br>"
                # 将该篇文章的标题与内容的总信息写入对应文件
                fh.write(dataall.encode("utf-8"))
                print("第" + str(i) + "个网页第" + str(j) + "次处理")  # 便于调试
            except urllib.error.URLError as e:
                if hasattr(e, "code"):
                    print(e.code)
                if hasattr(e, "reason"):
                    print(e.reason)
                # 若为URLError异常, 延时10秒执行
                time.sleep(10)
            except Exception as e:
                print("exception:" + str(e))
                # 若为Exception异常, 延时1秒执行
                time.sleep(1)
    fh.close()
    # 设置并写入本地文件的html后面结束部分代码
    html2 = '''</body>
</html>
    '''
    fh = open("F:/CrawlerData/wechat/1.html", "ab")
    fh.write(html2.encode("utf-8"))
    fh.close()


key = "物联网"  # 设置关键词
proxy = "125.45.87.12:9999"  # 设置代理服务器, 该代理服务器有可能失效, 读者需要换成新的有效代理服务器
proxy2 = ""  # 可以为getlisturl()与getcontent()设置不同的代理服务器, 此处没有启用该项设置
pagestart = 1  # 起始页
pageend = 2  # 爬取到哪页

listurl = getlisturl(key, pagestart, pageend, proxy)
getcontent(listurl, proxy)
