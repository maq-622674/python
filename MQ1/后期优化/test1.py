
import threading
import time
 
# 定义一个全局变量
#number = 0
list1=[
    {
        "code":"false",
        "id":"123",
        "name":"黄同学"
    },{
        "code":"false",
        "id":"456",
        "name":"张大"
    },{
        "code":"false",
        "id":"789",
        "name":"李工"
    },{
        "code":"false",
        "id":"1011",
        "name":"李工"
    },{
        "code":"false",
        "id":"1112",
        "name":"李工"
    },{
        "code":"false",
        "id":"1213",
        "name":"李工"
    },{
        "code":"false",
        "id":"1314",
        "name":"李工"
    }
]
mutex = threading.Lock()
DATA=[]
'''创建一个互斥锁，默认是没有上锁的'''
def test1():
    global DATA
    '''上锁'''
    
    while True:
        for i in list1:  
            #mutex.acquire()      
            DATA.append(i)
            # if i==50:
            #     print("第50位学生被卡在这里3秒")
            #     time.sleep(30)
               
            #print("number",DATA)       
            #     DATA.append(i)
            # DATA.append(i)
            #mutex.release()
        #print("number",DATA)       
        time.sleep(10)
        
    # for i in range(temp):
    #     number += 1
    '''解锁'''
            
    #print("-----in test1 number=%s-----" % number)
 
def test2():
    global DATA
    '''上锁'''
    
    while True:          
        if DATA:
            for i in DATA:
                mutex.acquire()
                #print("data[0]",DATA[0])
                if DATA[0]["code"]=="true":
                    print("该学生请假了",DATA[0])
                if DATA[0]["code"]=="false":
                    print("该学生没请假",DATA[0])
                DATA.remove(DATA[0])
                mutex.release()
                print("number1",DATA)
                
        # for i in number:
        #     number.remove(i)  
        #time.sleep(5)
    # for i in range(temp):
    #     number += 1
    '''解锁'''
   
    #print("-----in test2 number=%s-----" % number)
def test3():
    global list1
    time.sleep(15)
    print("开始运行")
    list1[1]["code"]="true"
def main():
 
    t1 = threading.Thread(target=test1)  # 加上要传递的参数，元组类型
    t2 = threading.Thread(target=test2)
    t3 = threading.Thread(target=test1)
    t1.start()
    t2.start()
    #t3.start()
    
    #time.sleep(2)
 
    #print("-----in main number=%s-----"% number)
 
if __name__ == '__main__':
    main()
'''
旧的方案DATA数据堆积没有删除

实现思路
一个线程:学校每60s检测一次append到DATA中
一个线程:一直循环DATA数据,删掉第一个
问题:有可能DATA数据太多导致另一个线程还没有删完
来了很多数据,造成不是实时或者延迟
数据量小的时候不易察觉

一个线程访问5000个同学假如某个学生卡在那里了
假如这个线程append加了锁,比如第2000名学生卡在那里，append到DATA里,
他会一直等到那个学生请求成功才会执行别的线程,所以append时候不加锁,
别的线程要想一直删除DATA里的数据,会因为这第2000名学生,删除不掉前1999名学生

好的解决方案
#三个线程
向学校的接口请求,学校有多少个学生,然后每个学生判断是否请假,然后再推送机器里比如耗时90s,可以缩短为30s
1.请求学校有多少个学生
2.那个学生是否请假
3.那个学生是要添加的还是删除的
'''

