import threading

'''
前面不只一次提到，当程序中拥有多个线程时，主线程执行结束并不会影响子线程继续执行。换句话说，只有程序中所有线程全部执行完毕后，程序才算真正结束。
下面程序演示了包含 2 个线程的程序执行流程： 
'''
def action(*add):
        for arc in add:
            #调用 getName() 方法获取当前执行该程序的线程名
            print(threading.current_thread().getName() +" "+ arc)
def main():
       
    #主线程执行如下语句
    for i in range(5):
        print(threading.current_thread().getName())
    #定义线程要调用的方法，*add可接收多个以非关键字方式传入的参数
    
    #定义为线程方法传入的参数
    my_tuple = ("http://c.biancheng.net/python/",\
                "http://c.biancheng.net/shell/",\
                "http://c.biancheng.net/java/")
    #创建线程
    thread = threading.Thread(target = action,args =my_tuple)
    #启动线程
    thread.start()
    print('*'*10)
    '''
    显然，只有等 MatinThread 和 Thread-1 全部执行完之后，程序才执行结束。

    除此之外，Python 还支持创建另一种线程，称为守护线程（或后台线程）。此类线程的特点是，当程序中主线程及所有非守护线程执行结束时，未执行完毕的守护线程也会随之消亡（进行死亡状态），程序将结束运行。

    Python 解释器的垃圾回收机制就是守护线程的典型代表，当程序中所有主线程及非守护线程执行完毕后，垃圾回收机制也就没有再继续执行的必要了。

    前面章节中，我们学习了 2 种创建线程的方式，守护线程本质也是线程，因此其创建方式和普通线程一样，唯一不同之处在于，将普通线程设为守护线程，需通过线程对象调用其 damon 属性，将该属性的值该为 True。

    并且需要注意的一点是，线程对象调用 daemon 属性必须在调用 start() 方法之前，否则 Python 解释器将报 RuntimeError 错误。

    举个例子，下面程序演示了如何创建一个守护线程： 在main1.py
    '''
if __name__ == "__main__":
    main()