import time
import threading
def run():
    lock.acquire()    #修改数据前加锁
    global num
    num +=1
    lock.release()    #修改完后释放
lock=threading.Lock()
num=0
t_objs = []
for i in range(1000):
    t=threading.Thread(target=run)
    t.start()
    t_objs.append(t)
for t in t_objs:  #循环线程实例列表，等待子线程执行完毕
    t.join()
print(num)         