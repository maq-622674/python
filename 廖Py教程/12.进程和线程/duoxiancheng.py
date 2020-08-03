#导入time和threading高级模块
import time, threading

# 新线程执行的代码:
def loop():
    #第三步输出thread is LoopThread running... 
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    #第四步     开始循环 循环5次0-4  判断是否n<5
    #第七步
    #第十一步
    #第十五步
    #第十九步
    #第二十三步 判断5<5为False不执行while往下执行
    while n < 5:  
        #第五步n=1 
        #第八步n=2
        #第十二步n=3
        #第十六步n=4
        #第二十步n=5    进来之后才加+1的  没进来之前还是4
        n = n + 1 
        #第六步输出thread LoopThread >>> 1
        #第九步输出thread LoopThread >>> 2
        #第十三步输出thread LoopThread >>> 3
        #第十七步输出thread LoopThread >>> 4
        #第二十一步输出thread LoopThread >>> 5
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        #第七步等1秒钟 
        #第十步等1秒钟
        #第十四步等1秒钟
        #第十八步等1秒钟
        #第二十二步等1秒钟
        time.sleep(1)
    #第二十四步输出thread LoopThread ended.
    print('thread %s ended.' % threading.current_thread().name)

'''
threading.current_thread（）
threading.currentThread（）
返回当前Thread对象，对应于调用者的控制线程。如果未通过threading模块创建调用者的控制 线程，则返回具有有限功能的虚拟线程对象。

在2.6版中更改：添加了current_thread()拼写。

由于任何进程默认就会启动一个线程，我们把该线程称为主线程，
主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，
它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定，
我们用LoopThread命名子线程。名字仅仅在打印时用来显示，
完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……


知识点三：
此时join的作用就凸显出来了，join所完成的工作就是线程同步，即主线程任务结束之后，进入阻塞状态，一直等待其他的子线程执行结束之后，主线程在终止

知识点四：
join有一个timeout参数：

当设置守护线程时，含义是主线程对于子线程等待timeout的时间将会杀死该子线程，最后退出程序。所以说，如果有10个子线程，全部的等待时间就是每个timeout的累加和。简单的来说，就是给每个子线程一个timeout的时间，让他去执行，时间一到，不管任务有没有完成，直接杀死。
没有设置守护线程时，主线程将会等待timeout的累加和这样的一段时间，时间一到，主线程结束，但是并没有杀死子线程，子线程依然可以继续执行，直到子线程全部结束，程序退出。
'''
#第一步输出主线程
#threading MainThread is running...
print('thread %s is running...' % threading.current_thread().name)
#第二步创建一个线程 线程名字为LoopThread   执行loop函数
t = threading.Thread(target=loop, name='LoopThread')
#启动刚刚创建的线程
t.start()

#等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
t.join()
#第二十五步输出thread MainThread ended.
print('thread %s ended.' % threading.current_thread().name)