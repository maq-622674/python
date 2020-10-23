'''
Python str 提供了 3 种可用来进行文本对齐的方法，分别是 ljust()、rjust() 和 center() 方法，本节就来一一介绍它们的用法。
'''

#1.py ljust()方法
'''
ljust() 方法的功能是向指定字符串的右侧填充指定字符，从而达到左对齐文本的目的。

ljust() 方法的基本格式如下：
S.ljust(width[, fillchar])

其中各个参数的含义如下：
S：表示要进行填充的字符串；
width：表示包括 S 本身长度在内，字符串要占的总长度；
fillchar：作为可选参数，用来指定填充字符串时所用的字符，默认情况使用空格。
'''
S="http://c.biancheng.net/python/"
addr='http://c.biancheng.net'
print(S.ljust(35))
print(addr.ljust(35))
a='http'
b=1
#中间有很多个空格不明显，自己操作一下
#这35个字符长度=字符串+空格
#左对齐
print("a=%s,b=%d"%(a.ljust(35),b))
print("a=%s,b=%d"%(a.ljust(35,'-'),b))

#2.py rjust()方法
#这个比较明显
#右对齐
print(S.rjust(35))
print(addr.rjust(35))

print(S.rjust(35,'-'))
print(addr.rjust(35,'-'))

#3.py center()方法
#居中
print(S.center(35,))
print(addr.center(35,))

#这个更加明显，默认是空格
print(S.center(35,'-'))
print(addr.center(35,'-'))