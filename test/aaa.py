import threading
import time

import urllib.request
def aaa():
    while True:
        response = urllib.request.urlopen('https://www.python.org')
        print(response.read().decode('utf-8'))
        time.sleep(0.5)
t1=threading.Thread(target=aaa)
t1.start()