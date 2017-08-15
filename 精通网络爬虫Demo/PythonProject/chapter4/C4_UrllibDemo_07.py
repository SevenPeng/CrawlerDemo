import urllib.request

httphd = urllib.request.HTTPHandler(debuglevel=1)
httpshd = urllib.request.HTTPHandler(debuglevel=1)
opener = urllib.request.build_opener(httphd, httpshd)
urllib.request.install_opener(opener)
data = urllib.request.urlopen("http://edu.51cto.com")
