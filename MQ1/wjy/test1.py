
import os,stat
import urllib.request
import time
 
#下载照片路径
img_url="" 
file_path=r'C:\新建文件夹'
file_name ="aaa.jpg"
def url_img(url,path,name):
    try:
        urllib.request.urlretrieve(img_url,filename=file_path+"/"+file_name)    
    except:
        print("error")
time1=str(time.time())
print(time1.replace('.','_'))
print(type(time1))
