import urllib.request

file = urllib.request.urlopen("http://www.iplaypy.com/jichu/note.html")

print(file.info())  # 返回与当前环境有关的信息
print(file.getcode())  # 获取当前爬取网页的状态码
print(file.geturl())  # 获取当前所爬取的URL地址

string = urllib.request.quote("http:// www.sina.com.cn")  # URL编码
print(string)
print(urllib.request.unquote(string))  # URL解码

data = file.read()
dataline = file.readline()
"""
1）file.read（）读取文件的全部内容，与readlines不同的是，read会把读取到的内容赋给一个字符串变量。
2）file.readlines（）读取文件的全部内容，与read不同的是，readlines会把读取到的内容赋给一个列表变量，若要读取全部内容，推荐使用这种方式。
3）File.readline（）读取文件的一行内容
"""
print(data)

fhandle = open("F:/CrawlerData/1.html", "wb")  # wb以二进制写模式打开
fhandle.write(data)
fhandle.close()

filename = urllib.request.urlretrieve("http://daily.zhihu.com", filename="F:\CrawlerData/2.html")
urllib.request.urlcleanup()  # 清除Urlretrieve执行所造成的缓存
