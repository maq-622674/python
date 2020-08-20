#py创建元组
#1.使用()直接创建
num = (7, 14, 21, 28, 35)
course = ("Python教程", "http://c.biancheng.net/python/")
abc = ("Python", 19, [1,2], ('c',2.0))

course = "Python教程", "http://c.biancheng.net/python/"
print(course)
print(type(course))

#最后加上逗号
a =("http://c.biancheng.net/cplus/",)
print(type(a))
print(a)
#最后不加逗号
b = ("http://c.biancheng.net/socket/")
print(type(b))
print(b)

#2.使用tuple()函数创建元组
#将字符串转换成元组
tup1 = tuple("hello")
print(tup1)
#将列表转换成元组
list1 = ['Python', 'Java', 'C++', 'JavaScript']
tup2 = tuple(list1)
print(tup2)
#将字典转换成元组
dict1 = {'a':100, 'b':42, 'c':9}
tup3 = tuple(dict1)
print(tup3)
#将区间转换成元组
range1 = range(1, 6)
tup4 = tuple(range1)
print(tup4)
#创建空元组
print(tuple())

#二.py访问元组元素
url = tuple("http://c.biancheng.net/shell/")
#使用索引访问元组中的某个元素
print(url[3])  #使用正数索引
print(url[-4])  #使用负数索引
#使用切片访问元组中的一组元素
print(url[9: 18])  #使用正数切片
print(url[9: 18: 3])  #指定步长
print(url[-6: -1])  #使用负数切片

#三.py修改元组
tup = (100, 0.5, -36, 73)
print(tup)
#对元组进行重新赋值
tup = ('Shell脚本',"http://c.biancheng.net/shell/")
print(tup)

tup1 = (100, 0.5, -36, 73)
tup2 = (3+12j, -54.6, 99)
print(tup1+tup2)
print(tup1)
print(tup2)

#四.py删除元组
tup = ('Java教程',"http://c.biancheng.net/java/")
print(tup)
del tup

    