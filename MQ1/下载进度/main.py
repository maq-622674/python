# encoding:utf-8
from urllib.request import urlretrieve
import os


def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
    '''
    
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print('%.2f%%'%per)
    


def dowlonad():
    url = 'http://ls.jimuti.com:808/File/uploads/jimuti/MQ1.zip'
    local = os.path.join('G:/CSDN_L/python/MQ1/下载进度/', 'MQ1.zip')
    urlretrieve(url, local, Schedule)
    
    #print("下载进度:",)
import urllib
import time
def aaa():
    while True:
        try:
            url="http://ls.jimuti.com:808/File/uploads/jimuti/MQ1.zip"
            response=urllib.request.urlopen(url)
        #调用status属性可以此次请求响应的状态码，200表示此次请求成功
            if response.status==200:
                pass
        #调用url属性，可以获取此次请求的地址
            
        except:
            print("网站上暂时没有")
        #res=urllib.request.get(url)
        time.sleep(30)
        #print(res)
            
if __name__ == '__main__':
    aaa()
    #dowlonad()