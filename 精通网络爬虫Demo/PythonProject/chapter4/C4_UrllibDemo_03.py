import urllib.request

for i in range(1, 10):
    try:
        # 格式为:urllib.request.urlopen（要打开的网址，timeout=时间值）。
        file = urllib.request.urlopen("https://500px.com", timeout=5)
        data = file.read()
        print(len(data))
    except Exception as e:
        print("出现异常-->" + str(e))
