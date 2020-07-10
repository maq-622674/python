'''
__str__
'''
'''
第一种
不雅观
'''
class Student(object):
     def __init__(self, name):
         self.name = name

print(Student('Michael'))

'''
第二种 还是不雅观
'''
class Student(object):
    def __init__(self, name):
         self.name = name
    def __str__(self):
         return 'Student object (name: %s)' % self.name

print(Student('Michael'))
s = Student('Michael')
print(s)

'''
第三种 偷懒的写法
'''
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__
s = Student('Michael')
print(s)

'''
__iter__
'''
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
for n in Fib():
     print(n)

'''
__getitem__
Fib实例虽然能作用于for循环，
看起来和list有点像，但是，
把它当成list来使用还是不行，
比如，取第5个元素：

要表现得像list那样按照下标取出元素，
需要实现__getitem__()方法：
'''
#print(Fib()[5])
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[10])
print(f[100])

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f = Fib()
#现在试试Fib的切片：
print(f[0:5])
#但是没有对step参数作处理：
print(f[:10:2])

'''
__getattr__
正常情况下，当我们调用类的方法或属性时，
如果不存在，就会报错。比如定义Student类：
'''
class Student(object):
    
    def __init__(self):
        self.name = 'Michael'

#调用name属性，没问题，但是，
#调用不存在的score属性，就有问题了：
s = Student()
print(s.name)
#print(s.score)

class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
s = Student()
print(s.name)
print(s.score)

class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
s = Student()           
print(s.age())
'''
举个例子：

现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：

http://api.server/user/friends
http://api.server/user/timeline/list
如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。

利用完全动态的__getattr__，我们可以写出一个链式调用：
'''

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
print(Chain().status.user.timeline.list)

'''
__call__
'''
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
s = Student('Michael')
# self参数不要传入
s()
#print(callable(s())
print(callable('str'))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))



