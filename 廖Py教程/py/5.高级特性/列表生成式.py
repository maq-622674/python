print(list(range(1, 11)))

#但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

#但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
print([x * x for x in range(1, 11)])

#写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print([x * x for x in range(1, 11) if x % 2 == 0])

#还可以使用两层循环，可以生成全排列：
print([m + n for m in 'ABC' for n in 'XYZ'])

#三层和三层以上的循环就很少用到了。
#运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os 
# 导入os模块，模块的概念后面讲到
# os.listdir可以列出文件和目录
print([d for d in os.listdir('.')])


#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

#因此，列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

#最后把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

'''
if ... else
使用列表生成式的时候，有些童鞋经常搞不清楚if...else的用法。

例如，以下代码正常输出偶数
'''
print([x for x in range(1, 11) if x % 2 == 0])

#但是，我们不能在最后的if加上else：
#print([x for x in range(1, 11) if x % 2 == 0 else 0])

#这是因为跟在for后面的if是一个筛选条件，不能带else，否则如何筛选？
#另一些童鞋发现把if写在for前面必须加else，否则报错：
#print([x if x % 2 == 0 for x in range(1, 11)])

#这是因为for前面的部分是一个表达式，它必须根据x计算出一个结果。因此，考察表达式：x if x % 2 == 0，它无法根据x计算出结果，因为缺少else，必须加上else：
print([x if x % 2 == 0 else -x for x in range(1, 11)])

#上述for前面的表达式x if x % 2 == 0 else -x才能根据x计算出确定的结果。

#可见，在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。

#练习
#第一种
L1=['Hello','World',1,'Apple',None]
# L2=[]
# for i in L1:
#     if(isinstance(i,str)):      
#         L2.append(i)     
#         L2=[j.lower() for j in L2]
          
# print(L2)

#第二种
L2=[x for x in L1 if(isinstance(x,str))]
L2=[x.lower() for x in L2]
print(L2)
if L2==['hello','world','apple']:
    print('测试通过!')
else:
    print('测试失败!')