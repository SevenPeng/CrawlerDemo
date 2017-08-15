import re

pattern = "yue"  # 普通字符作为原子
String = "http://yum.iqianyue.com"
reasult1 = re.search(pattern, String)
print(reasult1)

pattern2 = "\n"
String2 = '''http://asdf.com
http://baidu.com'''
reasult2 = re.search(pattern2, String2)
print(reasult2)

pattern3 = "\w\dpython\w"
string = "abcdefphp345pythony_py"
reasult3 = re.search(pattern3, string)
print(reasult3)

pattern4 = "\w\dpython[xyz]\w"
pattern5 = "\w\dpython[^xyz]\w"
pattern6 = "\w\dpython[xyz]\W"
reasult4 = re.search(pattern4, string)
reasult5 = re.search(pattern5, string)
reasult6 = re.search(pattern6, string)
print(reasult4)
print(reasult5)
print(reasult6)

pattern = ".python..."
print(re.search(pattern, string))

pattern1 = "^abd"
pattern2 = "^abc"
pattern3 = "py$"
pattern4 = "ay$"
string = "abcdfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
result3 = re.search(pattern3, string)
result4 = re.search(pattern4, string)
print(result1)
print(result2)
print(result3)
print(result4)

pattern1 = "py.*n"
pattern2 = "cd{2}"
pattern3 = "cd{3}"
pattern4 = "cd{2,}"
string = "abcdddfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
result3 = re.search(pattern3, string)
result4 = re.search(pattern4, string)
print(result1)
print(result2)
print(result3)
print(result4)

pattern = "python|php"
string = "abcdfphp345pythony_py"
reasult = re.search(pattern, string)
print(reasult)

pattern1 = "(cd){1,}"
pattern2 = "cd{1,}"
string = "abcdddddcdcdcddddfphp345pythony_py"
print(re.search(pattern1, string))
print(re.search(pattern2, string))

pattern1 = "python"
pattern2 = "python"
string = "abcdfphp345Pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string, re.I)
print(result1)
print(result2)

pattern1 = "p.*y"
pattern2 = "p.*?y"
string="abcdfphp345pythony_py"
print(re.search(pattern1,string))
print(re.search(pattern2,string))


