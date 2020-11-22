
import os
import subprocess
szpath="C:\\Users\plug\\7z.exe"  #7z.exe的；路径
zippath="C:\\python\\MQ1.zip"#压缩文件
outputpath="C:\\python\\MQ1\\"#解压位置
# my_cmd = '{} x "{}" -o{} -aoa'.format(szpath,zippath,outputpath)
# #os.cmd(my_cmd) #会显示黑屏
# subprocess.call(my_cmd) #不显示黑屏

import os
import threading
import time
from multiprocessing import Process
from threading import Thread



def Extract_File(filePath,target):
    """
    """
    zip_command = szpath+ " "+"x %s -y -o%s"%(filePath,target)
    aaa=os.system(zip_command)
    return aaa
 
def process():
    aaa=Extract_File(zippath,outputpath)
    if aaa==0:
        os._exit(0)
    

def func():

    p1 = Process(target=process)
    p1.start()

func()
# import py7zr
# a = py7zr.SevenZipFile(r'G:\CSDN_L\python\s\MQ1.zip','r')
# a.extractall(path=r'G:\CSDN_L\python\s')
# a.close()