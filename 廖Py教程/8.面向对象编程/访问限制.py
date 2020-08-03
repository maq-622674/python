'''
在外部可以修改类方法的属性
例子一  不健壮 不好维护
'''
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
print(bart.score)

bart.score = 99
print(bart.score)


'''
例子二
在外部不可以修改类方法的属性
健壮性 可维护 加限制保护
'''
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
bart = Student('Bart Simpson', 59)
#这个已经无法访问
print(bart.__name)


'''
例子三
如果外部要获取name和score 可以这样写
'''
class Student(object):
  

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

'''
例子四
如果又允许外部代码修改score怎么办 增加个方法
'''
class Student(object):
    

    def set_score(self, score):
        self.__score = score


'''
例子五
你也许会问，原先那种直接通过bart.score = 99也可以修改啊，
为什么要定义一个方法大费周折？
因为在方法中，可以对参数做检查，避免传入无效的参数：
'''
class Student(object):

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')