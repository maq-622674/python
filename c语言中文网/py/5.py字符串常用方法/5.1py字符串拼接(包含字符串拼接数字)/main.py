str1 = "Python教程" "http://c.biancheng.net/python/"
print(str1)
str2 = "Java" "Python" "C++" "PHP"
print(str2)

name = "C++教程"
url = "http://c.biancheng.net/cplus/"
info = name + "的网址是：" + url
print(info)

name = "C语言中文网"
age = 8
course = 30
info = name + "已经" + str(age) + "岁了，共发布了" + repr(course) + "套教程。"
print(info)

'''
str() 和 repr() 的区别
str() 和 repr() 函数虽然都可以将数字转换成字符串，但它们之间是有区别的：
str() 用于将数据转换成适合人类阅读的字符串形式。
repr() 用于将数据转换成适合解释器阅读的字符串形式（Python 表达式的形式），适合在开发和调试阶段使用；如果没有等价的语法，则会发生 SyntaxError 异常。

'''
s = "http://c.biancheng.net/shell/"
s_str = str(s)
s_repr = repr(s)
print(type(s_str))
print(s_str)
print(type(s_repr))
print(s_repr)