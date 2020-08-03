# print absolute value of an integer:
a=100
if a>=0:
    print(a)
else:
    print(-a)

#转义字符
print('I\'m ok.')
print("I\'m learing\nPython")
print("\\\n\\")
print('\\\t\\')
#python允许r''表示''内部的字符串默认不转义
print(r'\\\t\\')

#python允许'''...'''的格式表示多行内容
print('''
linel
line2
line3''')

print(r'''hello,\n
world''')


###################
'''布尔值'''
###################
print(3>2)
print(3>5)

#布尔可以用and，or和not运算
#and运算
print(True and True)
print(True and False)
print(False and True)
print(5>3 and 3>1)

#or运算
print(True or True)
print(True or False)
print(False or False)
print(5>3 or 1>3)

#not运算
print(not True)
print(not False)
print(not 1>2)

age=17
if age>=18:
    print("adult")
else:
    print("teenager")

#######################
'''
空值是python的一个特殊的值，用None表示
None不能理解为0，因为0是有意义的，而None是一个特殊的空值 
'''
#######################



#######################
'''
变量
python是动态语言
java是静态语言
int a=123; //a是证书类型变量
a="ABC"; //不能把字符串赋给整型变量

python的整数没有大小限制
java对32位整数的范围限制在-2147483648-2147483647
python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf(无限大)

'''
#######################
a=1
t_007='T007'
Answer=True
print(a)
a='ABC'
print(a)
print(a)

a='ABC'
b=a
a='XYZ'
print(b)

########
'''
常量
通常用大写的变量名表示常量
要改变常量的值，也拦不住你
'''
########
PI=3.14159265359
print(PI)
print(10/3)
#浮点数 整除也是浮点数
print(9/3)
#地板除 两个整数的除法仍是整数
print(10//3)
print(10//3.0)
print(10.0//3)
print(10.0//3.0)

print(10%3)