import re

# 匹配.com或.cn后缀的URL网址
pattern = "[a-zA-Z]+:// [^\s]*[.com|.cn]"
string = "<a href='http:// www.baidu.com'>百度首页</a>"
print(re.search(pattern, string))

# 匹配电话号码
pattern = "\d{4}-\d{7}|\d{3}-\d{8}"
string = "021-6728263653682382265236"
print(re.search(pattern, string))

# 匹配电子邮件地址
pattern = "\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*"  # 匹配电子邮件的正则表达式
string="<a href='http:// www.baidu.com'>百度首页</a><br><a href='mailto:c-e+o@iqi-anyue.com.cn'>电子邮件地址</a>"
print(re.search(pattern,string))
























