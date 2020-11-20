import winreg
import os
import sys
'''
自己添加的标识
'''

#https://blog.csdn.net/jiahaoangle/article/details/102740223?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param
class WinLin:
    def __init__(self):
        pass
    def os_name(self):
        '''
        该变量返回当前操作系统的类型，当前只注册了3个值：分别是posix , nt , java， 对应linux/windows/java虚拟机
        '''
        if os.name=="nt":
            return "windows"
        elif os.name=="posix":
            return "liunx"
        elif os.name=="java":
            return "java虚拟机"
    def sys_platform(self):
        '''
        该变量返回当前系统的平台标识
        '''
        if sys.platform=="win32":
            return "windows"
        elif sys.platform=="linux":
            return "linux"
        elif sys.platform=="cygwin":
            return "windows/cygwin"
        elif sys.platform=="darwin":
            return "mac os x"
    def lujing(self,data):
        '''
        '''
        if self.os_name()=="windows":
            if '/' in data:
                data=data.replace('/','\\')
        elif self.os_name()=="liunx":
            if '\\' in data:
                data=data.replace('\\','/')
        return data
    def os_getcwd(self):
        '''
        获取当前工作的目录
        '''
        return os.getcwd()
    def list_file(self,data="."):
        '''
        列出path目录下所有的文件和目录名。Path参数可以省略
        '''
        return os.listdir(data)
    





class Regedit:
    """
    控制开机自启动注册表
    带自己的标识符比如:qq_lll wechat_lll,防止删除别人的自启动项
    默认开启
    """
    def __init__(self,data="_lll",cc=True):
        self.__data=data
        self.__cc=cc


    def reg_startup(self,name,cmd):
        '''
        增加注册表启动项
        name是名称
        cmd是数据
        '''
        if os.name=='nt':
            if '/' in cmd:
                cmd=cmd.replace('/','\\')
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_SET_VALUE)        
            if key:
                winreg.SetValueEx(key,name+self.__data,0,winreg.REG_SZ, cmd)
                winreg.CloseKey(key)
                return "ok"

    def del_startup(self,name):
        '''
        删除指定启动项
        '''
        if os.name=='nt':
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_SET_VALUE)
            if key:   
                winreg.DeleteValue(key,name+self.__data) 
                winreg.CloseKey(key)
                return "ok"


    def get_list(self):
        '''
        获取_jmt启动项
        '''
        if os.name=='nt':
            key_one = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_QUERY_VALUE)
            count_key = winreg.QueryInfoKey(key_one)[1]  # index 1获取个数
            key_list = []
            for i in range(count_key):
                name, key_value, value_type = winreg.EnumValue(key_one, i)
                key_list.append((name,key_value,value_type))  
            if key_one:
                winreg.CloseKey(key_one)
                #print('close key success.')
            res_list = [x[0] for x in key_list]
            data1=[]
            for i in res_list:
                if self.__data in i:
                    data=i.replace(self.__data,'')
                    data1.append(data)
            return data1



class Port:
    def __init__(self):
        pass
    def cat(self):
        '''
        查看所有端口号
        '''
        cmd="netstat -ano"
        data=os.popen(cmd).read()
        print("data",data)
    def cat_find(self):
        '''
        查看指定端口的使用情况
        '''
        pass
    def jincheng(self):
        '''
        查看所有进程
        '''
        cmd="tasklist"
        data=os.popen(cmd).read()
        
        # data=data.split("======")
        # print(data)
        # print(data.find("="))
        wei=data.rfind("=")
        data=data[wei:]
        print(data)
        # print(type(data))
p1=Port()
p1.cat()
 


