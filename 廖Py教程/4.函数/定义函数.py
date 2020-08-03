from abstest import hello
from abstest import my_abs
import math

print(my_abs(-99))
print(hello())

#空函数
#如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass

#参数检查
#调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
#print(my_abs(1,2))

#但是如果参数类型不对，Python解释器就无法帮我们检查。试试my_abs和内置函数abs的差别
#my_abs('A')
#abs('A')

#当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善。

#让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
def my_abs_a(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
#print(my_abs_a('A'))

#返回多个值
#import math语句表示导入math包，
# 并允许后续代码引用math包里的sin、cos等函数。

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x,y)

#但其实这只是一种假象，Python函数返回的仍然是单一值：
r = move(100, 100, 60, math.pi / 6)
print(r)

#原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
'''
小结
定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。
练习
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0 的两个解。
'''
print('#'*10)
def quadratic(a, b, c):
    d=(-b+(int(math.sqrt(b*b-4*a*c))))/(2*a)
    d1=(-b-(int(math.sqrt(b*b-4*a*c))))/(2*a)
    return d,d1
   
print(quadratic(1,5,6))
