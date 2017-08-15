import re

string = "apythonhellomypythonhispythonourpythonend"
pattern = ".python."
result1 = re.match(pattern, string)
result2 = re.match(pattern, string).span()
print(result1)
print(result2)

string = "hellomypythonhispythonourpythonend"
pattern = ".python."
print(re.match(pattern, string))
print(re.search(pattern, string))

string = "hellomypythonhispythonourpythonend"
pattern = re.compile(".python.")  # 预编译
print(pattern.findall(string))
print(re.compile(pattern).findall(string))

string = "hellomypythonhispythonourpythonend"
pattern = "python."
print(re.sub(pattern, "php", string))
print(re.sub(pattern, "php", string, 2))
