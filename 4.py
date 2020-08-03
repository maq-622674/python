class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        #3.self.name=骆昊 self.age=38
        #10.self.name=王大锤 self.age=15
        self.name = name
        self.age = age
        

    def study(self, course_name):
        #5.输出 骆昊正在学习Python程序设计.
        #12.输出 王大锤正在学习思想品德
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        #7.self.age=38 >18
        #14.self.age=15<18
        if self.age < 18:
            #15.所以输出 王大锤只能看《熊出没》.
            print('%s只能观看《熊出没》.' % self.name)
        else:
            #8.所以输出 骆昊正在观看岛国爱情大电影
            print('%s正在观看岛国爱情大电影.' % self.name)
    
    def __str__(self):
        print("2")
        return ("你实例化对象了:%s,%s"%(self.name,self.age))




### 创建和使用对象



def main():
    # 创建学生对象并指定姓名和年龄
    #2.实例化对象stu1
    
    stu1 = Student('骆昊', 38)
    stu2 = Student('王大锤', 15)
    print("1")
    print(stu1)
    print("3")
    print(stu2)


if __name__ == '__main__':
    #1.执行主函数main()
    main()