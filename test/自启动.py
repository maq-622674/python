# filename =r'C:/Users/debug/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'
# #filename = r'G:\CSDN_L\python\test'
# name='2.txt'
# cmd='sadsa'
# def reg_startup(name,cmd):
#     with open(filename+'/'+name, 'w') as file_object:
#         file_object.write(cmd)
# reg_startup(name,cmd)
# 环境：python 3.5,无需管理员权限
import winreg
import winreg as wr


def getAutoRun():
    root1 = wr.ConnectRegistry(
        None, wr.HKEY_LOCAL_MACHINE)  # 获取LocalMachine Key
    root2 = wr.ConnectRegistry(None, wr.HKEY_CURRENT_USER)
    result = {}
    try:
        targ = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
        print("****reading from ", targ, "****")

        key1 = wr.OpenKey(root1, targ)  # 打开localmachine的autorun列表
        key2 = wr.OpenKey(root2, targ)  # 打开currentuser的autorun列表
        cnt = 0
        try:
            for i in range(1024):
                try:
                    n, v, t = wr.EnumValue(key1, i)  # 迭代localmachine
                    result[n] = v
                    cnt += 1
                except EnvironmentError:
                    break
            for i in range(1024):
                try:
                    n, v, t = wr.EnumValue(key2, i)  # 迭代currentuser
                    result[n] = v
                    cnt += 1
                except EnvironmentError:
                    break
        finally:
            wr.CloseKey(key1)
            wr.CloseKey(key2)
    finally:
        wr.CloseKey(root1)
        wr.CloseKey(root2)
    return result


    



    
    #main()
# -*- coding: gbk -*-
import os

f = os.popen(r"echo %HOMEPATH%", "r")
d = f.read()  # 读文件  
f.close()
if '\\' in d:
    d=d.replace('\\','/').strip()
    #print(d)
    # if '用户名'in aaa:
    #     aaa=aaa.split('用户名')[1].strip().split('工作站')[0]
    filename =d+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'
    print(filename)
# #filename = r'G:\CSDN_L\python\test'

# def reg_startup(name,cmd):
#     with open(filename+'/'+name, 'w') as file_object:
#         file_object.write(cmd) 
# def del_startup(name):
#     os.remove(filename+'/'+name)
# def reg_getlist():    
#     list1=os.listdir(filename)
#     print(list1)
#     return list1

# reg_getlist()

