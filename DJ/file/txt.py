class Text:
    def __init__(self):
        '''    
        '''
        #r,w,a,r+,w+,a+,rb,wb
        pass

    def rtxt(self):
        '''     
        读 
        r : 读取文件，若文件不存在则会报错
        '''
        with open('G:/CSDN_L/python/DJ/file/1.txt','r') as file:
            content=file.read()
        return content
            
    def wtxt(self):
        '''
        写 覆盖
        w : 写入文件，若文件不存在则会先创建再写入，会覆盖原文件
        '''
        with open('G:/CSDN_L/python/DJ/file/2.txt', 'w') as file:   # .txt可以不自己新建,代码会自动新建
            file.write('\n')     # 写入
    def atxt(self):
        '''
        追加
        a : 写入文件，若文件不存在则会先创建再写入，但不会覆盖原文件，而是追加在文件末尾
        '''
        with open("G:/CSDN_L/python/DJ/file/b.txt","a") as file:
                # //0，写入前指针为0
            file.write("123")      # //写入123
              
    def aatxt(self):
        '''
        rb,wb：分别于r,w类似，但是用于读写二进制文件
        r+ : 可读、可写，文件不存在也会报错，写操作时会覆盖

        w+ : 可读，可写，文件不存在先创建，会覆盖

        a+ ：可读、可写，文件不存在先创建，不会覆盖，追加在末尾

        注意：这里的覆盖是指每次重新打开文件进行操作时覆盖原来的，如果是在打开文件中则不会覆盖
        '''
        pass

import shutil
class File_shuitl:
    def __init__(self):
        pass
    def file(self):
        shutil.copyfileobj(open('old.xml','r'), open('new.xml', 'w'))


#当前在线人数和在线设备

NUM=0
DATA=[]
G_CONN_POOL=[]
import threading
import time
class User:
    def __init__(self,name):
        pass
    def new(self):
        print("新用户第一次上线")
    def old(self):
        print("老用户上线")
    def over(self):
        print("哪个用户掉线了")
    def old_over(self):
        print('老用户掉线重新连上了','掉线了几次')

def zhaopian():
    data='123'
    return data
def msg():
    data=zhaopian()
    #client.sendall(data.encode(encoding='utf8')) 
def xun():
    global NUM
    while True:
        pass
        #client, _ = G_SOCKET_SERVER.accept()  # 阻塞，等待客户端连接
        # 加入连接池
        #G_CONN_POOL.append(client)
        #t2=threading.Thread(target=msg,args=(client,))
        #t2.setDaemon(True)
       # t2.start()
t1=threading.Thread(target=xun)
#设置成守护线程
t1.setDaemon(True)
t1.start()





















import os
class Nt:
    def __init__(self):
        pass
    def aa(self):
        if os.name=='nt':
            pass 
class Cmd:
    def __init__(self):
        pass
import xlwt
# 安装
import os
res = os.popen('cd G:/CSDN_L/python/DJ/file/')
#res1 = os.popen('pip install pipreqs')
 #在当前目录生成
res2 = os.popen('pipreqs . --encoding=utf8 --force')
res3 = os.popen('pip install -r requirements.txt')

output_str = res.read()   # 获得输出字符串
