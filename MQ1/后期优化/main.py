import threading
import queue
import time
import random

'''
需求：主线程开启了多个线程去干活，每个线程需要完成的时间
不同，但是在干完活以后都要通知给主线程
多线程和queue配合使用，实现子线程和主线程相互通信的例子
'''
q = queue.Queue()
threads=[]
class MyThread(threading.Thread):
    def __init__(self,q,t,j):
        super(MyThread,self).__init__()
        self.q=q
        self.t=t
        self.j=j

    def run(self):
        time.sleep(self.j)
        # 通过q.put()方法，将每个子线程要返回给主线程的消息，存到队列中
        self.q.put("我是第%d个线程，我睡眠了%d秒,当前时间是%s" % (self.t, self.j,time.ctime()))



'''
# 生成15个子线程，加入到线程组里，
# 每个线程随机睡眠1-8秒（模拟每个线程干活时间的长短不同）
'''

for i in range(15):
   j=random.randint(1,8)
   threads.append(MyThread(q,i,j))

#    循环开启所有子线程
for mt in threads:
    mt.start()
print('进程开启时间：%s'%(time.ctime()))
'''
通过一个while循环，当q队列中不为空时，通过q.get()方法，
循环读取队列q中的消息，每次计数器加一，当计数器到15时，
证明所有子线程的消息都已经拿到了，此时循环停止
'''
count = 0
while True:
    if not q.empty():
        print(q.get())
        count+=1
    if count==15:
        break
print("threads")