'''
使用 Timer 定时器有一个弊端，即只能控制线程在指定时间内执行一次任务，如果想实现每隔一段时间就执行一次，需要借助循环结构。

实际上，Python 还提供有一个更强大的、可用来定义执行任务调度的 sched 模块，该模块中含有一个 scheduler 类，可用来执行更复杂的任务调度。

scheduler 类常用的构造方法如下：
scheduler(timefunc=time.monotonic, delayfunc=time.sleep)

可以向该构造方法中传入 2 个参数（当然也可以不提供，因为都有默认值），分别表示的含义如下：
timefunc：指定生成时间戳的函数，默认使用 time.monotonic 来生成时间戳；
delayfunc：在未到达指定时间前，通过该参数可以指定阻塞任务执行的函数，默认采用 time.sleep() 函数来阻塞程序。

另外，scheduler 类中还提供有一些方法，表 1 罗列了常用的一些。

表 1 scheduler 类常用方法
方法格式	功能
scheduler.enter(delay, priority, action, argument=(), kwargs={})	在 time 规定的时间后，执行 action 参数指定的函数，其中 argument 和 kwargs 负责为 action 指定的函数传参，priority 参数执行要执行任务的等级，当同一时间点有多个任务需要执行时，等级越高（ priority 值越小）的任务会优先执行。该函数会返回一个 event，可用来取消该任务。
scheduler.cancel(event)	取消 event 任务。注意，如果 event 参数执行的任务不存在，则会引发 ValueError 错误。
scheduler.run(blocking=True)	运行所有需要调度的任务。如果调用该方法的 blocking 参数为 True，该方法将会阻塞线程，直到所有被调度的任务都执行完成。
下面程序示范了 scheduler 类的用法。
'''
import threading
from sched import scheduler
def action(arg):
    print(arg)
#定义线程要调用的方法，*add可接收多个以非关键字方式传入的参数
def thread_action(*add):
    #创建任务调度对象
    sche = scheduler()
    #定义优先级
    i = 3
    for arc in add:
        # 指定1秒后执行action函数
        sche.enter(1, i, action,argument=(arc,))
        i = i - 1
    #执行所有调度的任务
    sche.run()
#定义为线程方法传入的参数
my_tuple = ("http://c.biancheng.net/python/",\
            "http://c.biancheng.net/shell/",\
            "http://c.biancheng.net/java/")
#创建线程
thread = threading.Thread(target = thread_action,args =my_tuple)
#启动线程
thread.start()