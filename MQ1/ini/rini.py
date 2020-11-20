
# -*- coding: utf-8 -*-
 

 
#读取配置文件

 
#写入宿舍配置文件
import os
import configparser
def rini():

    abspath="C:/新建文件夹/IpConfig.ini"
    if not os.path.exists(abspath):
        with open(abspath,"a") as file:
            pass
    else:
        pass

    config=configparser.ConfigParser()
    config.read(abspath)
    try:
        config.add_section("School")
        config.set("School","IP","10.15.40.123")
        config.set("School","Mask","255.255.255.0")
        config.set("School","Gateway","10.15.40.1")
        config.set("School","DNS","211.82.96.1")
    except configparser.DuplicateSectionError:
        print("Section 'School' already exists")
 
# #写入比赛配置文件
'''
后期优化
两个线程各自运行
一个线程请求
-每隔30s请求一次
一个线程发送
-
'''





