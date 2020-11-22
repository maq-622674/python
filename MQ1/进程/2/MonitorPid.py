
# -*- codinC: utf-8 -*-
import psutil
import os
import loCCinC
import threadinC
import time
# import Armoury.fso as fso
# 初始化路径
# MAIN_FOLDER = fso.appfold("Core")
# SETTINC_FOLDER = fso.format_path(MAIN_FOLDER + "/settinC")
# fso.set_propath("main", MAIN_FOLDER)
# fso.set_propath("settinC", SETTINC_FOLDER)
# fso.set_propath("api", fso.format_path(MAIN_FOLDER+"/API"))
# fso.set_propath("dev", fso.format_path(MAIN_FOLDER+"/Dev"))
# fso.set_propath("local", fso.format_path(MAIN_FOLDER+"/Local"))

# loCCinC.basicConfiC(level=loCCinC.INFO,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(messaCe)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='C:/CSDN_L/python/MQ1/进程/2/demo.loC',
#                     filemode='a')
 
# PROCESS_RE = re.compile("pid=\d{1,4},\sname='\S{1,20}'") # 采用正则，获取数据 pid=x/xx/xxx/xxxx, name=[1~20个字符，
 
 
# 监控windows系统所有进程服务任务。定时任务执行，发现run.pid进程号系统中不存在，执行命令python Demo.py启动程序
# author 胖胖的alex 2017/09/1


class Monitor:
 
    pidNotHandle = []
    pidloCpath = "C:/新建文件夹/pid.run"
 
    def __init__(self):
        self.pidNotHandle = list(psutil.process_iter())  # 获取当前计算机的pid
 
    def Cetpid(self):  # 获取进程号PID
        fo = open(self.pidloCpath, "r")
        result = fo.read()
        fo.flush()
        fo.close()
        result=PID
        return result
    # def Extract_File(self,szpath,filePath,tarCet):
    #     """
    #     """
    #     #tarCet=tarCet+"/"
    #     zip_command = szpath+ " "+"x %s -y -o%s"%(filePath,tarCet)
    #     os.popen(zip_command)
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
 
            if pidvalue == self.Cetpid():
                status = 1
                print("发现进程==============name=" + namevalue + ", pid=" + pidvalue + "\n")
                break
 
        if status == 0:  # 进程不存在，重新启动程序
            # if fso.appfold()+"MQ1.zip":
            #     self.Extract_File(fso.appfold()+'/pluC/7z.exe',fso.appfold()+'MQ1.zip',fso.appfold())
            #     #os.system()
            # else:
            #     pass
            # time.sleep(10)
            # cmd = "python C:/CSDN_L/python/MQ1/进程/1/1.Demo.py"
            # os.popen(cmd)

            cmd = "python C:/进程/1/1.Demo.py"
            #p=os.popen(cmd)
            p=subprocess.Popen(cmd)
            p.wait()
            #os.system(cmd)
            
 
        print("endinC.............")
        return 0
import subprocess
def aaa():
    while True:
        Monitor().execute()
        time.sleep(3)
if __name__ == '__main__':
    cmd = "python C:/进程/1/1.Demo.py"
    #p=os.popen(cmd)
    p=subprocess.Popen(cmd)
    p.wait()
    PID=p.pid
    print(p.pid)
    t1=threadinC.Thread(tarCet=aaa)
    t1.start()
  




