import threading

'''
可以看到，我们用 Thread 类创建了一个线程（线程名为 Thread-1），其任务是执行 action() 函数。同时，我们也给主线程 MainThread 安排了循环任务（第 16、17 行）。通过前面的学习我们知道，主线程 MainThread 和子线程 Thread-1 会轮流获得 CPU 资源，因此该程序的输出结果才会向上面显示的这样。
但是，如果我们想让 Thread-1 子线程先执行，然后再让 MainThread 执行第 16、17 行代码，该如何实现呢？很简单，通过调用线程对象的 join() 方法即可。
join() 方法的功能是在程序指定位置，优先让该方法的调用者使用 CPU 资源。该方法的语法格式如下：

thread.join( [timeout] )
其中，thread 为 Thread 类或其子类的实例化对象；timeout 参数作为可选参数，其功能是指定 thread 线程最多可以霸占 CPU 资源的时间（以秒为单位），如果省略，则默认直到 thread 执行结束（进入死亡状态）才释放 CPU 资源。
'''
   
    #定义线程要调用的方法，*add可接收多个以非关键字方式传入的参数
def action(*add):
        for arc in add:
            #调用 getName() 方法获取当前执行该程序的线程名
            print(threading.current_thread().getName() +" "+ arc)
  
def main():
    #定义为线程方法传入的参数
    my_tuple = ("http://c.biancheng.net/python/",\
                "http://c.biancheng.net/shell/",\
                "http://c.biancheng.net/java/")
    #创建线程
    thread = threading.Thread(target = action,args =my_tuple)
    #启动线程
    thread.start()
    #指定 thread 线程优先执行完毕
    thread.join()
    #主线程执行如下语句
    for i in range(5):
        print(threading.current_thread().getName())
    '''
     程序中第 16 行的位置，thread 线程调用了 join() 方法，并且没有指定具体的 timeout 参数值。这意味着如果程序想继续往下执行，必须先执行完 thread 线程。
    '''
if __name__ == "__main__":
    main()