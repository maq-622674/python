
# -*- coding: utf-8 -*-
import psutil
import os
import logging
import threading
import time
#初始化路径



# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='C:/demo.log',
#                     filemode='a')
 
# PROCESS_RE = re.compile("pid=\d{1,4},\sname='\S{1,20}'") # 采用正则，获取数据 pid=x/xx/xxx/xxxx, name=[1~20个字符，
 
 
# 监控windows系统所有进程服务任务。定时任务执行，发现run.pid进程号系统中不存在，执行命令python Demo.py启动程序



class Monitor:
 
    pidNotHandle = []
    pidlogpath = "C:/CN_L/pyhon/Q1/pid.run"
 
    def __init__(self):
        self.pidNotHandle = list(psutil.process_iter())  # 获取当前计算机的pid
 
    def getpid(self):  # 获取进程号PID
        # fo = open(self.pidlogpath, "r")
        # result = fo.read()
        # fo.flush()
        # fo.close()
        result=PID
        return result
    def Extract_File(self,szpath,filePath,target):
        """
        用7z.exe 
        filePath:要解压的文件
        target:解压到哪个地方
        -aoa覆盖原来的文件
        """
        zip_command = szpath+ " "+"x %s -y -o%s -aoa"%(filePath,target)
        os.popen(zip_command)
    def execute(self):
        pid = []
        for each in self.pidNotHandle:
            a = str(each)  # each 是 class类型，可用type(each)查看类型
            # a 数据样式为：psutil.Process(pid=0, name='System Idle Process')
            pid.append(a[15:-1])  # 只取括号内部分；pid=0, name='System Idle Process'
 
        status = 0  # 被监控程序进程存在状态，0不存在，1存在
        for each in pid:
            nameposition = each.find("name")  # 获取name的位置；name='System Idle Process'
            namevalue = each[nameposition + 6:-1]  # 获取name值；System Idle Process
            pidposition = each.find("pid")
            pidvalue = each[pidposition + 4:nameposition-2]
            print("name="+namevalue + ", pid="+pidvalue+"\n")
 
            if pidvalue == self.getpid():
                status = 1
                print("发现进程==============name=" + namevalue + ", pid=" + pidvalue + "\n")
                break
 
        if status == 0:  # 进程不存在，重新启动程序     
            global PID      
            if os.path.exists('/tmp/MQ1.zip'):
            #if fso.exist(fso.appfold+'/tmp/MQ1.zip'):
                if os.name=='nt':
                    if os.path.exists('/plug/7z.exe'):
                        self.Extract_File('/plug/7z.exe','/tmp/MQ1.zip','')            
            time.sleep(1)
            #print("解压完成")
            #print("7z.exe路径:%s,从哪里解压:%s,解压到哪里:%s"%(+'/plug/7z.exe',+'/tmp/MQ1.zip',))
            #print("执行解压的命令是")
            cmd_base_py='python '+'/Base.py'
            #print("运行cmd")
            #os.popen(cmd_base_py)
            p1=subprocess.Popen(cmd_base_py)
            PID=str(p1.pid)
           
            
 
        print("ending.............")
        return 0
import subprocess
def aaa(): 
    while True:  
        Monitor().execute()
        time.sleep(30)
            
if __name__ == '__main__':
    cmd_base_py='python '+'/Base.py'
    p=subprocess.Popen(cmd_base_py)
    PID=str(p.pid)
    '''
    注意这里传参数的时候PID是str类型
    '''
    print("PID:",PID)
 
    t1=threading.Thread(target=aaa)
    t1.start()
   
    
  





