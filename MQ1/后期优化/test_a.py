
import threading
import time
 
# 定义一个全局变量
#number = 0
# mutex = threading.Lock()
DATA=[]
'''创建一个互斥锁，默认是没有上锁的'''
def test1():
    global DATA
    '''1.判断有多少学生''' 
    while True:
        for i in range(100):  
            #mutex.acquire() 
            data={}     
            data[i]=i
            DATA.append(data)
            if i==50:
                print("第50位学生被卡在这里3秒")
                time.sleep(20)
               
            #print("DATA:",DATA)       
            #     DATA.append(i)
            # DATA.append(i)
            #mutex.release()
        #print("number",DATA)       
        time.sleep(30)
        
    # for i in range(temp):
    #     number += 1
   
            
    #print("-----in test1 number=%s-----" % number)
DATA1=[]
def test2():
    global DATA,DATA1
    '''2.判断'''
    while True:          
        if DATA:
            for i in DATA:          
                #mutex.acquire()             
                #print("data[0]",DATA[0])
                DATA[0]["code"]="true"
                DATA1.append(DATA[0])
                DATA.remove(DATA[0])
                #mutex.release()
                print("DATA:",DATA)
                print("\n")
                print("DATA1:",DATA1)
                
        # for i in number:
        #     number.remove(i)  
        #time.sleep(5)
    # for i in range(temp):
    #     number += 1
    '''解锁'''
   
    #print("-----in test2 number=%s-----" % number)
DATA2=[]
def test3():
    global DATA1,DATA2
    while True:
        if DATA1:
            for i in DATA1:
                #mutex.acquire()
                if DATA1[0]["code"]=="true":
                    '''
                    推送加记录
                    '''
                    DATA2.append(DATA1[0])
                if DATA1[0]["code"]=="false":
                    '''
                    删除加删除记录
                    '''
                    # if DATA1[0] in str(DATA2):
                    #     DATA2.remove(DATA1[0])
                    pass
                    
                
                DATA1.remove(DATA1[0])
                #print("DATA1:",DATA1)
                print("DATA2:",DATA2) 
                #mutex.release()
def main():
    t1 = threading.Thread(target=test1)  # 加上要传递的参数，元组类型
    t2 = threading.Thread(target=test2)
    t3 = threading.Thread(target=test1)
    t1.start()
    t2.start()
    t3.start()
    
    #time.sleep(2)
 
    #print("-----in main number=%s-----"% number)
 
if __name__ == '__main__':
    main()
'''
好的解决方案
#三个线程
向学校的接口请求,学校有多少个学生,然后每个学生判断是否请假,然后再推送机器里比如耗时90s,可以缩短为30s
1.请求学校有多少个学生
2.那个学生是否请假
3.那个学生是要添加的还是删除的

还有两个要判断
一个是重复的照片不再下载
一个是提交过的照片不再提交
'''



