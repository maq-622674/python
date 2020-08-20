'''
位于 time 模块中的 sleep(secs) 函数，可以实现令当前执行的线程暂停 secs 秒后再继续执行。所谓暂停，即令当前线程进入阻塞状态，当达到 sleep() 函数规定的时间后，再由阻塞状态转为就绪状态，等待 CPU 调度。

sleep() 函数位于 time 模块中，因此在使用前，需先引入 time 模块。

sleep() 函数的语法规则如下所示：

time.sleep(secs)
其中，secs 参数用于指定暂停的秒数，

仍以前面章节创建的 thread 线程为例，下面程序演示了 sleep() 函数的用法：
可以看到，和未使用 sleep() 函数的输出结果相比，显然主线程 MainThread 在前期获得 CPU 资源的次数更多，因为 Thread-1 线程中调用了 sleep() 函数，在一定程序上会阻碍该线程获得 CPU 调度。
'''
import threading
import time

def action(*add):
    for arc in add:
        #暂停 0.1 秒后，再执行
        time.sleep(0.1)
        #调用 getName() 方法获取当前执行该程序的线程名
        print(threading.current_thread().getName() +" "+ arc)
def main():
    #定义线程要调用的方法，*add可接收多个以非关键字方式传入的参数

    #定义为线程方法传入的参数
    my_tuple = ("http://c.biancheng.net/python/",\
                "http://c.biancheng.net/shell/",\
                "http://c.biancheng.net/java/")
    #创建线程
    thread = threading.Thread(target = action,args =my_tuple)
    #启动线程
    thread.start()
    #主线程执行如下语句
    for i in range(5):
        print(threading.current_thread().getName())
if __name__ == "__main__":
    main()