import re
import urllib.request


def getcontent(url, page):
    # 模拟成浏览器
    headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)  # 将opener安装为全局
    data = urllib.request.urlopen(url).read().decode("utf-8")
    # 构造对应用户的正则表达式
    userpat = 'target="_blank" title="(.*?)">'
    # 构造对应内容的正则表达式
    contentpat = '<div class="content">(.*?)</div>'
    # 寻找出所有的用户
    userlist = re.compile(userpat, re.S).findall(data)  # re.S	(DOTALL): 点任意匹配模式，改变’.’的行为
    # 寻找出所有的内容
    contentlist = re.compile(contentpat, re.S).findall(data)
    x = 1
    # 通过for循环遍历段子内容并将内容分别赋给对应的变量
    for content in contentlist:
        # 替换无关字符
        content = content.replace("<span>", "")
        content = content.replace("</span>", "")
        content = content.replace("<br/>", "")
        content = content.replace("\n", "")
        # 用字符串作为变量名, 先将对应字符串赋给一个变量
        name = "content" + str(x)
        # 通过 exec()函数实现用字符串作为变量名并赋值
        exec(name + '=content')
        x += 1
    y = 1
    # 通过 for 循环遍历用户, 并输出该用户对应的内容
    for user in userlist:
        name = "content" + str(y)
        print("用户" + str(page) + '-' + str(y) + "是:" + user)
        print("内容是:")
        exec("print(" + name + ")")
        print("\n")
        y += 1


# 分别获取各页的段子, 通过 for 循环可以获取多页
for i in range(1, 3):
    url = "http://www.qiushibaike.com/8hr/page/" + str(i)
    getcontent(url, i)
