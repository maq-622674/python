import threading

'''
py创建线程(2种方式)详解
Python 中，有关线程开发的部分被单独封装到了模块中，和线程相关的模块有以下 2 个：
    _thread：是 Python 3 以前版本中 thread 模块的重命名，此模块仅提供了低级别的、原始的线程支持，以及一个简单的锁。功能比较有限。正如它的名字所暗示的（以 _ 开头），一般不建议使用 thread 模块；
    threading：Python 3 之后的线程模块，提供了功能丰富的多线程支持，推荐使用。

本节就以 threading 模块为例进行讲解。Python 主要通过两种方式来创建线程：
    使用 threading 模块中 Thread 类的构造器创建线程。即直接对类 threading.Thread 进行实例化创建线程，并调用实例化对象的 start() 方法启动线程。
    继承 threading 模块中的 Thread 类创建线程类。即用 threading.Thread 派生出一个新的子类，将新建类实例化创建线程，并调用其 start() 方法启动线程。
'''
'''
1.调用Thread类的构造器创建线程
Thread 类提供了如下的 __init__() 构造器，可以用来创建线程：

__init__(self, group=None, target=None, name=None, args=(), kwargs=None, *,daemon=None)
此构造方法中，以上所有参数都是可选参数，即可以使用，也可以忽略。其中各个参数的含义如下：
    group：指定所创建的线程隶属于哪个线程组（此参数尚未实现，无需调用）；
    target：指定所创建的线程要调度的目标方法（最常用）；
    args：以元组的方式，为 target 指定的方法传递参数；
    kwargs：以字典的方式，为 target 指定的方法传递参数；
    daemon：指定所创建的线程是否为后代线程。
    这些参数，初学者只需记住 target、args、kwargs 这 3 个参数的功能即可。
下面程序演示了如何使用 Thread 类的构造方法创建一个线程： 




'''
#定义线程要调用的方法，*add可接收多个以非关键字方式传入的参数
def action(*add):
    for arc in add:
        #调用 getName() 方法获取当前执行该程序的线程名
        '''
        如果这里是
        Thread-7 http://c.biancheng.net/python/
        Thread-7 http://c.biancheng.net/shell/
        Thread-7 http://c.biancheng.net/java/
        说明有其他线程
        正常应该是
        Thread-1 http://c.biancheng.net/python/
        Thread-1 http://c.biancheng.net/shell/
        Thread-1 http://c.biancheng.net/java/
        '''
        print(threading.current_thread().getName() +" "+ arc)
#创建子线程类，继承自 Thread 类
class my_Thread(threading.Thread):
    def __init__(self,add):
        threading.Thread.__init__(self)
        self.add=add
    def run(self):
        # 重写run()方法
        for arc in self.add:
             #调用 getName() 方法获取当前执行该程序的线程名
            print(threading.current_thread().getName()+" "+arc)
def main():
    #定义为线程方法传入的参数
    #1.定义参数
    my_tuple = ("http://c.biancheng.net/python/",\
            "http://c.biancheng.net/shell/",\
            "http://c.biancheng.net/java/")
    #2.创建线程
    thread = threading.Thread(target = action,args =my_tuple)
    thread.start()
    '''
    默认情况下，主线程的名字为 MainThread，用户启动的多个线程的名字依次为 Thread-1、Thread-2、Thread-3、...、Thread-n 等。
    为了使 thread 线程的作用更加明显，可以继续在上面程序的基础上添加如下代码，让主线程和新创建线程同时工作： 
    可以看到，当前程序中有 2 个线程，分别为主线程 MainThread 和子线程 Thread-1，它们以并发方式执行，即 Thread-1 执行一段时间，然后 MainThread 执行一段时间。通过轮流获得 CPU 执行一段时间的方式，程序的执行在多个线程之间切换，从而给用户一种错觉，即多个线程似乎同时在执行。
    如果程序中不显式创建任何线程，则所有程序的执行，都将由主线程 MainThread 完成，程序就只能按照顺序依次执行。

    '''
    for i in range(5):
        print(threading.current_thread().getName())
    print('*'*10)
    '''
    2.继承Thread类创建线程类
    '''    
    #定义为 run() 方法传入的参数
    my_tuple = ("http://c.biancheng.net/python/",\
                "http://c.biancheng.net/shell/",\
                "http://c.biancheng.net/java/")
    #创建子线程
    mythread = my_Thread(my_tuple)
    #启动子线程
    mythread.start()
    #主线程执行此循环
    for i in range(5):
        print(threading.current_thread().getName())

if __name__ == "__main__":
    main()