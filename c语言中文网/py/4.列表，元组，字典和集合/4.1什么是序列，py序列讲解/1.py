#1.序列索引
str="c语言中文网"
print(str[0],"==",str[-6])
print(str[5],"==",str[-1])

#2.序列切片
str="c语言中文网"
print(str[:2])
print(str[::2])
print(str[:])

#3.序列相加
str="c.biancheng.net"
print("c语言"+"中文网:"+str)

#4.序列相乘
str="c语言中文网"
print(str*3)
list=[None]*5
print(list)

#5.检查元素是否包含在序列中
str="c.biancheng.net"
print('c' in str)
print('c' not in str)

#6.和序列相关的内置函数
print(max(str))
print(min(str))
print(sorted(str))
