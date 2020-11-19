import multiprocessing
import time

def colck(interval):
    for i in range(3):
        print("当前时间",time.ctime())
        time.sleep(interval)

if __name__ == "__main__":
    #创建子进程
    p=multiprocessing.Process(target=colck(1,))
    #调用子进程
    p.start()
    p.join()
    print("p.pid",p.pid)
    print("p.name",p.name)
    #子进程是否存活
    print("p.is_alive:",p.is_alive())