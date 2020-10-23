import threading,time
class MyThread(threading.Thread):
    def __init__(self,n,sleep_time):
        super(MyThread, self).__init__()
        self.n=n
        self.sleeptime=sleep_time
    def run(self):
        print("run task",self.n)
        time.sleep(2)
        print("task done,",self.n)


t1=MyThread("t1",2)
t2=MyThread("t2",4)


t1.start()
t2.start()
t1.join()  #wait()  第一个线程执行完毕后再执行第二个线程
t2.join()
