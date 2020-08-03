'''
美国
127个字符 大小写英文字符和数字和一些符号
ASCII编码

A的编码是65
z的编码是122

中文制定GB2312
日文制定Shift_JIS
韩文制定Euc-kr

多个国家容易混乱
所以出现了Unicode

ASCOO编码是1个字节
Unicode编码是2个字节

A用ASCII编码是十进制的65,二进制的01000001
0用ASCII编码是十进制的48,二进制的00110000,注意字符'0'和整数0是不同的
汉字中已经超出了ASCII编码的范围,用Unicode编码是十进制的20013,二进制的01001110 00101101

大量英文用Unicode编码存储和传输不划算
节约精神，把Unicode编码转化为"可变长编码"的UTF-8编码
常用字母被编码成1个字节
汉字通常是3个字节
生僻字符会被编码成4-6个字节
大量英文很节省空间

在计算机内存中，统一使用Unicode编码，
当需要保存的时候再把Unicode转换为UTF-8保存到文件中

记事本 Unicode编码
保存:转换为UTF-8         读取:转换为Unicode
文件abc.txt  UTF-8编码

浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8
再传输到浏览器

服务器 Unicode编码
输出UTF-8网页
浏览器
所以你看到很多网页的源码都会有类似的<meta charset="UTF-8"/>
的信息，表示该网页正是用的UTF-8编码

python的字符串
再python3版本中，字符串是以Unicode编码，所以python的字符串支持多语言


'''
print("こんにちは")
print("Olá.")
print("здравствй")
print("안녕 하세요")


'''
对于单个字符的编码,python提供了ord()函数获取字符的整数表示
chr()函数把编码转换为对应的字符
'''
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6587')

'''
由于python的字符串类型是str，在内存中Unicode表示
一个字符对应若干个字节，
如果要在网络上传输，或者保存到磁盘上
就需要把str变为以字节为单位的bytes
python对bytes类型的数据用b前缀的单引号或双引号表示
'''
x=b'ABC'
#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
#不认识,因为中文不能用ASCII编码
#print('中文'.encode('ascii'))



#在bytes中，无法显示为ASCII字符的字节，用\x##显示
#反过来，如果我们从网络或磁盘上读取了字节流，那么
#读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

#如果bytes中包含无法解码的字节，decode()方法会报错
#print(b'\xe4\xb8\xad\xff'.decode('utf-8'))

#如果bytes红只有一小部分无效的字节，可以传入errors='ignore'
print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))

#要计算str包含多少个字符,可以用len()函数
print(len('ABC'))
print(len('中文'))

#如果换成bytes.len()函数就计算字节数
#1各种问经过utf-8编码后通常会占用3个字节，而一个英文字符只占用1个字节
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))
#在操作字符串时，我们经常遇到str和bytes的互相转换，
#为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换

#由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，
#在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，
#为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
#申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码：
#如果.py文件本身使用UTF-8编码，并且也申明了# -*- coding: utf-8 -*-，打开命令提示符测试就可以正常显示中文：

#格式化
print('Hello,%s'%'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
#占位符
'''
%d 整数
%f 浮点数
%s 字符串
%x 十六进制整数
'''
#如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
print('Age: %s. Gender: %s' % (25, True))

#有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
print('growth rate: %d %%' % 7)

#另一种格式化字符串是format()方法它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

'''
小结
Python 3的字符串使用Unicode，直接支持多语言。
当str和bytes互相转换时，需要指定编码。最常用的编码是UTF-8。
Python当然也支持其他编码方式，比如把Unicode编码成GB2312：
但这种方式纯属自找麻烦，如果没有特殊业务要求，请牢记仅使用UTF-8编码。
'''
print('中文'.encode('gb2312'))