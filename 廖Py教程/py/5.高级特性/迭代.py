d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for ch in 'ABC':
    print(ch)
#所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
#那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections import Iterable
#str是否可迭代
print(isinstance('abc',Iterable))

# list是否可迭代
print(isinstance([1,2,3], Iterable))

# 整数是否可迭代
print(isinstance(123, Iterable))

'''
最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
'''
for i, value in enumerate(['A', 'B', 'C']):
     print(i,value)

#上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y in [(1, 1), (2, 4), (3, 9)]:
     print(x, y)

#练习
def findMinAndMax(L):
    if(L):
        if(len(L)==1):   
            L.append(L[0])
            a=tuple(L) 
            return a
        a=max(L)
        b=min(L)
        r=[]
        for a,b in r:
            r.append(a,b)
        tuple(r)
        return (a,b)          
    else:  
        return (None,None)

b=[1,3,5,-1,7,10]
b1=[2]
print(len(b))
b2=[]
a=findMinAndMax(b)
print(a)
a=findMinAndMax(b1)
print(a)
a=findMinAndMax(b2)
print(a)