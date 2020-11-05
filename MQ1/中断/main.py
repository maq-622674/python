import threading
import os
import time
def aaa():
    while True:
        print("123")
        time.sleep(1)

def bbb():
    t1=threading.Thread(target=aaa)
    t1.start()
    os._exit(1)

bbb()