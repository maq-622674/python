'''
Python字符串大小写转换（3种）函数及用法
'''
#1.py title()方法
#两个单词之间无论用什么分开他都会把首字母变为大写
#比如apple——orange apple?orange apple_orange  apple*orange 
str="c_biancheng.net"
print(str.title())

#2.py lower()方法
#全部变小写
str="I LIKE C"
print(str.lower())

#3.py upper()方法
str="i like c"
print(str.upper())
#需要注意的是，以上 3 个方法都仅限于将转换后的新字符串返回，而不会修改原字符串。
print(str)