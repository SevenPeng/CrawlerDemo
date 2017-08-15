import urllib.request
keywd = "word"
key_code = urllib.request.quote(keywd)
url = "http://blog.csdn.net"
req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read()
fhand = open("F:/CrawlerData/4.html", "wb")
fhand.write(data)
fhand.close()
