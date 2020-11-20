<<<<<<< HEAD
list1=[{
    "id":"123",
    "code":"true"
},{
    "id":"456",
    "code":"false"
}]
import time
a=0
while True:
    a=a+1
    for item in list1:   
        if a==10:
            item["code"]="@@@@@@@@@@@@@@@@@@@@@@@@"
        print(item["id"])
        print(item["code"])
    time.sleep(1)
=======
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
>>>>>>> 717a2bd7f5645517b58231aa6f157c15332b1068
