import threading
import time
def run(n):
    print("task",n)
    time.sleep(2)
    print("task has done!")     
start_time=time.time()
for i in range(50):
    t=threading.Thread(target=run,args=("t-%s"%i,))
    t.setDaemon(True)  #把当前线程设置为守护线程，一定在start前设置
    t.start()
print(threading.current_thread(),threading.active_count())
print(time.time()-start_time)  