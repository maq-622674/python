from multiprocessing import Process
from time import sleep
import time

class ClockProcess(Process):
    #重写初始化方法
    def __init__(self,inverval):
        Process.__init__(self)
        self.inverval=inverval
    #重写run()
    def run(self):
        print("子进程开始执行的时间",time.ctime())
        sleep(self.inverval)
        print("子进程结束的时间",time.ctime())
if __name__ == "__main__":
    #创建子进程
    p=ClockProcess(3)
    #调用子进程
    p.start()
    p.join()
    print("主进程执行完")