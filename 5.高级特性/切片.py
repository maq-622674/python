#第一种笨方法
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0])
print(L[1])
print(L[2])

#第二种笨方法
r=[]
n=3
for i in range(n):
    r.append(L[i])
print(r)

#第三种
print(L[0:3])

#也可以从索引1开始，取出2个元素出来：
print(L[1:3])

#类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：
print(L[-2:])
print(L[-2:-1])


#记住倒数第一个元素的索引是-1。
#切片操作十分有用。我们先创建一个0-99的数列：
L = list(range(100))
print(L)

#可以通过切片轻松取出某一段数列。比如前10个数：
print(L[:10])

#后10个数：
print(L[-10:])

#前11-20个数：
print(L[11:20])

#前10个数，每两个取一个：
print(L[:10:2])

#所有数，每5个取一个：
print(L[::5])

#甚至什么都不写，只写[:]就可以原样复制一个list：
print(L[:])

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print((0, 1, 2, 3, 4, 5)[:3])

#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])


'''
利用切片把字符串的空格切掉
'''
def trim(s):
    #第一种
    #如果s字符串前面一直有空格一直切，直到切到能看到不是空格
    while s[0:1]==' ':
        s=s[1:]
    #第二种
    
    #先判断最后一位是不是空格
    #然后判断
    #判断s[5:6]
    while s[(len(s)-1):len(s)]==' ':
        s=s[:-1]
    #第三种
    return s

s=input("请输入一个字符串:")
print('去除首尾空格后',trim(s))

#三种情况
'''
第一种 hello
开头有空格，末位没有空格
第二种 hello world
开头没有空格，中间和末位有空格
第三种
全部没空格直接返回了
'''
