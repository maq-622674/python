from multiprocessing import Process
import os
from time import sleep

def run_proc(name,**kwargs):
    for i in range(5):
        print("子进程运行中,参数name:%s,age:"%(name))
        print("字典参数kwargs:",kwargs)
        sleep(0.5)
if __name__ == "__main__":
    print("主进程开始运行")
    p=Process(target=run_proc('test'))
    print("子进程将要执行")
    p.start()