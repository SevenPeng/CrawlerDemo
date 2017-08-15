import urllib.request
import urllib.error

try:
    data = urllib.request.urlopen("https://blog.csdn.net")
    print(data)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)
