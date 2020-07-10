'''
类和实例
'''
# class Student(object):
#     pass
# bart = Student()
# print(bart)
# print(Student)

# bart.name='Bart Simpson'
# print(bart.name)

'''
例子二
'''
# class Student(object):

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
# bart = Student('Bart Simpson', 59)
# print(bart.name)
# print(bart.score)

'''
数据封装
'''
# def print_score(std):
#     print('%s: %s' % (std.name, std.score))
# print_score(bart)

# class Student(object):

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))
    
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
# bart = Student('Bart Simpson', 59)
# bart.print_score()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

print('bart.name =', bart.name)
print('bart.score =', bart.score)
bart.print_score()

print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())