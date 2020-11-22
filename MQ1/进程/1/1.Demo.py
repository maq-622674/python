# -*- coding: utf-8 -*-
import logging
import time
import os
 
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='G:/CSDN_L/python/MQ1/进程/1/demo.log',
#                     filemode='a')
 
 
# Demo.py 10秒关闭程序，模拟程序崩溃
# author 胖胖的alex 2017/09/10
class Demo:
 
    pidlogpath = "C:/新建文件夹/1/pid.run"
 
    def __init__(self):
        pass
 
    def setpid(self):  # 记录进程号PID
        fo = open(self.pidlogpath, "w")
        pid = str(os.getpid())
        fo.write(pid)
        fo.flush()
        fo.close()
        return pid
 
    def execute(self):
        pid = self.setpid()
        a=0
        while True:
            a=a+1
            if a==10:
                os._exit(1)
            else:
                print("a:",a)
            time.sleep(1)
        # print("启动程序,进程号:",pid)
        # logging.info("启动程序，进程号：" + str(pid))
        # i = 1
        # while True:
        #     logging.info("pid = " + pid + " ---------- run " + str(i) + " s ")
        #     print("pid:",pid)
        #     time.sleep(1)
        #     i += 1
        #     if i > 10:
        #         break
        # print("程序关闭")
        # logging.info("程序关闭...")
 
 
if __name__ == '__main__':
    Demo().execute()