# 整合后代码
import urllib.request
import urllib.error
try:
    urllib.request.urlopen("http://blog.baudisss.net")
except urllib.error.HTTPError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)
