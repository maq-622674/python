import threading
import time
#全局变量
num = []

# 任务一：加1
def work1():
    #上锁
    global num
    while True:    
        for i in range(3000):
            num.append(i)
        #print("num",num)
        time.sleep(20)
        #     num += 1
        # print('此时num等于',num)
        #解锁
        
# 任务二：加1
def work2():
    global num
    while True:        
        #for i in num:
    #    num += 1
        print('此时num等于',num)
        time.sleep(10)
   



if __name__ == '__main__':
    t1=threading.Thread(target=work1)
    t2=threading.Thread(target=work2)
    t1.start()
    t2.start()
'''
单线程
假如学校每60s循环一次
机器每30s检测一次
总计90s
'''

'''
多线程
学校每60s循环一次,机器跟着也循环
总计60s
'''