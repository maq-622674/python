'''
Python函数（函数定义、函数调用）用法详解
'''
n=0
for c in "http://c.biancheng.net/python/":
   n = n + 1
print(n)

#自定义 len() 函数
def my_len(str):
    length = 0
    for c in str:
       length = length + 1
    return length
#调用自定义的 my_len() 函数
length = my_len("http://c.biancheng.net/python/")
print(length)
#再次调用 my_len() 函数
length = my_len("http://c.biancheng.net/shell/")
print(length)

'''
Python函数的定义
'''
#定义个空函数，没有实际意义
def pass_dis():
    pass
#定义一个比较字符串大小的函数
# def str_max(str1,str2):
#     str = str1 if str1 > str2 else str2
#     return str
#更简洁   
def str_max(str1,str2):
    return str1 if str1 > str2 else str2

'''
py函数的调用
'''
pass_dis()
strmax = str_max("http://c.biancheng.net/python","http://c.biancheng.net/shell");
print(strmax)

'''
为函数提供说明文档
'''
#定义一个比较字符串大小的函数
def str_max(str1,str2):
    '''
    比较 2 个字符串的大小
    '''
    str = str1 if str1 > str2 else str2
    return str
help(str_max)
#print(str_max.__doc__)