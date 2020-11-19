import time
import threahing
def ccc():
    a=0
    while True:
        a+=1
        print(a)
        time.sleep(1)
t1=threahing.Thread(target=ccc)
t1.start()