'''
调用函数
'''
print(abs(100))
print(abs(-20))
print(abs(12.34))

#而max函数max()可以接收任意多个参数，并返回最大的那个
print(max(2, 3, 1, -5))

'''
数据类型转换
'''
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))
#函数名其实就是指向一个函数对象的引用，
# 完全可以把函数名赋给一个变量
# ，相当于给这个函数起了一个“别名”：
a=abs
print(a(-1))

b=hex
print(b(10))