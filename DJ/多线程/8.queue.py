import threading
import queue,time

q=queue.Queue(maxsize=10)
def Producer(name):
    #1.naem=Producer
    count=1
    while True:
        #2.加入队列  骨头  1
        q.put("骨头 %s"%count)
        #3.生产了骨头1
        print("生产了骨头",count)
        #4.count=2
        count+=1
        time.sleep(1)      
def Consumer(name):
    #5.name=dog
    
    while True:
        #6.[dog]取到  [骨头 1]并且吃了它...
        
        print("[%s] 取到  [%s] 并且吃了它。。。"%(name,q.get()))
        time.sleep(1)
p=threading.Thread(target=Producer,args=('cq',))
c=threading.Thread(target=Consumer,args=("dog",))
c1=threading.Thread(target=Consumer,args=("cc",))

p.start()
c.start()
c1.start()
