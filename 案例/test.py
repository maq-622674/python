import urllib.request
import random
#proxies = [{'http': 'http://124.231.50.56:8118'}]
#proxy = random.choice(proxies)
#设置代理操作器
# proxy = urllib.request.ProxyHandler({'http':'http://115.212.39.37:9000'})
# #构建新的请求器，覆盖默认opener
# opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
# urllib.request.install_opener(opener)
# reponse = urllib.request.urlopen('http://www.baidu.com/s?wd=ip')
# html_content = reponse.read().decode('utf-8')
# #返回结果中查找“主机ip”看是否变更为代理ip
# print(html_content)
import time
import ast

def str_json(data):
    user_dict = ast.literal_eval(data)
    #data=json.loads(data)
    return user_dict

            
    
# rtxt()

# import ast
# user = '{"name" : "john", "gender" : "male", "age": 28}'
# user_dict = ast.literal_eval(user)
# print(user_dict)

# user_info = "{'name' : 'john', 'gender' : 'male', 'age': 28}"
# user_dict = ast.literal_eval(user)
# print(user_dict)

# -*- coding:utf-8 -*-
'''
Create time:
author: 
Function:
    Check http proxy
'''
import time,urllib, urllib3,urllib.request,random, requests


class CheckProxy():

    def __init__(self):
        self.headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-language':'zh-CN,zh;q=0.9',
            'accept-encoding':'gzip, deflate',
            'Connection':'keep-alive',
            # 'Host:':'icanhazip.com',
        }
        self.urls_inland = ['https://www.baidu.com']
        self.urls_foreign = ["http://www.google.com"]
        self.proxy_info = {"user": "dm", "pass": "innodealing"}
        self.timeout = 5

    def get_data(self,url, headers={}):
        try:
            req = urllib.request.Request(url, headers=headers)
            ret = urllib.request.urlopen(req, timeout=self.timeout)
            return url, ret, 1
        # except urllib2.URLError, e:
        except Exception as e:
            # raise Exception(e)
            # print("Check Failed: %s" %e)
            return  url, e, 0

    def check_proxy_main1(self,proxy, foreign=0):
        if foreign:
            urls = self.urls_foreign
        else:
            urls = self.urls_inland
        print("Starting check proxy = %s..." % proxy)
        for url in urls:
            #设置代理
            proxy_support = urllib.request.ProxyHandler({"http" : "http://%(user)s:%(pass)s@" % self.proxy_info + proxy })
            opener = urllib.request.build_opener(proxy_support)
            urllib.request.install_opener(opener)
            url, ret, flag = self.get_data(url,headers=self.headers)
            if flag:
                if ret.code:
                    print("  Check %s is OK." %url )
                else:
                    print("  Check %s is ERROR: http_code error." %url )
            else:
                print("  Check %s is ERROR: GET error [ detail: %s ]." % (url, ret) )

    def check_proxy_main2(self,ip):
        requests.adapters.DEFAULT_RETRIES = 3
        try:
            proxies={
                "http":"http://%s"%ip,
                "https": "https://%s" % ip,
            }
            url="http://icanhazip.com/"
            # url='http://myip.ipip.net/'
            response = requests.get(url,timeout=self.timeout,proxies=proxies)
            proxy_ip = response.text.strip()#.encode(response.encoding).decode(response.apparent_encoding,errors = 'ignore')
            print(proxy_ip)
            if proxy_ip == ip.split(":")[0]:
                print("代理IP:%s 有效！"%ip)
                with open("G:/CSDN_L/python/案例/有效高匿代理.txt","a") as file:
                # //0，写入前指针为0
                    file.write(ip+"\n")  
                return 1
            else:
                print("%s 代理IP无效！"%ip)
                return 0
        except:
            print("error %s 代理IP无效！"%ip)
            return 0

import threading
if __name__ == '__main__':
    ips=[
        # '47.110.65.99:3100',  # 阿里ip(2019-03-22)
        # '47.110.225.239:3100',  # 阿里ip(2019-03-22)
        # '47.110.75.231:3100',  # 阿里ip(2019-03-22)
        # '106.57.23.132:5412'
    ]
    def rtxt():
        '''     
        读 
        r : 读取文件，若文件不存在则会报错
        '''
        global ips
        with open('G:/CSDN_L/python/案例/国内高匿代理.txt','r+') as file:
            while True:
                content=file.readline()
                if content:
                    content=content.replace('\n','')
                    data=str_json(content)
                    
                    #print(data) 
                    # content=content.replace('\n','')
                    ips.append(data["ip"]+":"+data["port"])
                #     print(data["port"])
                #     print(data["类型"])
                   # print(data["ip"]+":"+data["port"])
                time.sleep(0.5)
    t1=threading.Thread(target=rtxt)
    #t1.setDaemon(True)
    t1.start()
    def aaa():     
        try:
            CP=CheckProxy()
            for ip in ips:
                # CP.check_proxy_main1(proxy, foreign=0)
                CP.check_proxy_main2(ip)
        except Exception as e:
            import traceback
            ex_msg = '{exception}'.format(exception=traceback.format_exc())
            print(ex_msg)
    t2=threading.Thread(target=aaa)
    #t2.setDaemon(True)
    t2.start()