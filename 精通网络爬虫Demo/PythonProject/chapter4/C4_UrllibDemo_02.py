import urllib.request

# 方法1：使用build_opener（）修改报头
url = "http://blog.csdn.net/jiangwei0910410003/article/details/73385819"
# 1.定义一个变量headers存储对应的User-Agent信息，定义的格式为（“User-Agent”，具体信息）
headers = ("User-Agent",
           "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36")
# 2.自定义的opener对象并赋给变量opener
opener = urllib.request.build_opener()
# 3.设置对应的头信息，设置格式为：“opener对象名.addheaders=［头信息］”
opener.addheaders = [headers]
# 4.打开对应的网址
data = opener.open(url).read()
fhandle = open("F:\CrawlerData/3.html", "wb")
fhandle.write(data)
fhandle.close()

# 方法2：使用add_header（）添加报头
url = "http:// blog.csdn.net/weiwei_pig/article/details/51178226"
# 1.创建一个Request对象并赋给变量req
req = urllib.request.Request(url)
# 2.使用add_header（）方法添加对应的报头信息，格式为：Request对象名.add_header（字段名，字段值）
req.add_header('User-Agent',
               "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36")
# 3.打开对应网址并读取网页内容，并赋给了data变量
data = urllib.request.urlopen(req).read()





