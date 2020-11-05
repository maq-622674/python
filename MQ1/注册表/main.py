import winreg
import os

'''
自己添加的标识
'''
def reg_startup(name,cmd):
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
            winreg.SetValueEx(key,name+'_jmt',0,winreg.REG_SZ, cmd)
            winreg.CloseKey(key)
            return "ok"


def del_startup(name):
    '''
    删除指定启动项
    '''
    if os.name=='nt':
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_SET_VALUE)
        if key:   
            winreg.DeleteValue(key,name+'_jmt') 
            winreg.CloseKey(key)
            return "ok"


def get_list():
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
            if '_jmt' in i:
                data=i.replace('_jmt','')
                data1.append(data)
        return data1




 
