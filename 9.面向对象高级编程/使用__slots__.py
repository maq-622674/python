'''
使用__slots__
可以写个方法然后绑定在类上
如果是这样添加进去的，子类是找不到的
除非在子类中也定义__slots__，这样，
子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
'''
class Student(object):
    pass

#然后，尝试给实例绑定一个属性：
s = Student()
# 动态给实例绑定一个属性
s.name = 'Michael'
print(s.name)

#还可以尝试给实例绑定一个方法：
def set_age(self, age): # 定义一个函数作为实例方法
   self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print(s.age)

#但是，给一个实例绑定的方法，对另一个实例是不起作用的：
# 创建新的实例
#s2 = Student()
# 尝试调用方法
#print(s2.set_age(25))


#为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score
Student.set_score = set_score
s.set_score(100)
print(s.score)

s.set_score(99)
print(s.score)

print('*'*10)
#使用__slots__
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

#s = Student() # 创建新的实例
#s.name = 'Michael' # 绑定属性'name'
#s.age = 25 # 绑定属性'age'
#s.score = 99 # 绑定属性'score'

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999