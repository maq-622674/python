import threading
import urllib
import time
import requests
import re
from lxml import etree
import os
from urllib import request
import bs4
class DAILI:
    def __init__(self,url):
        self.__URL=url    
    def is_json(self,file):
        '''
        判断是不是json
        '''
        try:
            json.loads(file)
        except:
            return False
        return True
    def str_json(self,data):
        data=json.loads(data)
        return data
    def get(self,url):
        '''
        get请求,不带参数
        '''
        try:
            response=request.urlopen(url)  
            #print("查看 response 响应信息类型: ",type(response))
            page=response.read()
            page=page.decode('utf-8')
            #url解码
            data=parse.unquote(page)
            #print("data@@@@@@@@@@@@@@@@@@@@@@@@",data)
            if self.is_json(data):
                data=self.str_json(data)
                return data
        except:
            return 'error'
        
    def gets(self,url,data):
        '''
        get请求,带参数
        '''
        try:
            # data = json.dumps(data)
            # print(data)
            data = bytes(urllib.parse.urlencode(data), encoding='utf8')
            response=request.urlopen(url=url,data=data)  
            #print("查看 response 响应信息类型: ",type(response))
            page=response.read()
            page=page.decode('utf-8')
            #url解码
            data=parse.unquote(page)
            #print("data@@@@@@@@@@@@@@@@@@@@@@@@",data)
            if self.is_json(data):
                data=self.str_json(data)
                return data
        except:
            return 'error'
    def post(self,url,data):
        '''
        post请求
        '''
        try:
           
            data_string=urllib.parse.urlencode(data)        
            last_data=bytes(data_string,encoding='utf-8')
            response=urllib.request.urlopen(url,data=last_data)
            data=response.read().decode('utf-8')
            #print(response.read().decode('utf-8'))
            if self.is_json(data):
                data=self.str_json(data)
                return data
        except:
            print("接口有问题")

def foldexist(abspath:str)->None:
    """
    判断当前路径文件夹是否存在，如果不存在会自动创建
    """
    if not os.path.exists(abspath):
        os.makedirs(abspath)    
#DATA=[]

def gaoni():
    foldexist('G:/CSDN_L/python/案例/国内高匿代理')    
    while True:
        global A
        A= A+1
        with open('G:/CSDN_L/python/案例/国内高匿代理/log.txt', 'w') as file:   # .txt可以不自己新建,代码会自动新建
                    file.write(str(A))
        resp= requests.get('https://www.kuaidaili.com/free/inha/'+str(A)+'/')
        soup = bs4.BeautifulSoup(resp.text, 'lxml')
        elements = soup.select('#list>table>tbody>tr')
        data={}
        for element in elements:
            ip = element.select('td')[0].string
            port = element.select('td')[1].string
            niming=element.select('td')[2].string
            leixing=element.select('td')[3].string
            weizhi=element.select('td')[4].string
            xiangyingsudu=element.select('td')[5].string
            zuihouyanzhengshijian=element.select('td')[6].string
            data["ip"]=ip
            data["port"]=port
            data["匿名度"]=niming
            data["类型"]=leixing
            data["位置"]=weizhi
            data["响应速度"]=xiangyingsudu
            data["最后验证时间"]=zuihouyanzhengshijian
            #DATA.append(data)
            bbb(data)
            data={}
        print("开始第%d次爬取"%(A))
        time.sleep(1)
def bbb(data):
    with open("G:/CSDN_L/python/案例/国内高匿代理/ip.txt","a") as file:
        file.write(str(data)+"\n")
def aaa():
    #global DATA
    
    # PATTERN = re.compile(r'<div id="list"(.*?)>(.*?)</div>')
    # IP_PATTERN = re.compile(r'<td data-title="IP">(.*?)</td>')
    # PORT_PATTERN=re.compile(r'<td data-title="PORT">(.*?)</td>')
    # NIMINGDU_PATTERN=re.compile(r'<td data-title="匿名度">(.*?)</td>')
    # LEIXING_PATTERN=re.compile(r'<td data-title="类型">(.*?)</td>')
    # WEIZHI_PATTERN=re.compile(r'<td data-title="位置">(.*?)</td>')
    # XIANGYINGSUDU_PATTERN=re.compile(r'<td data-title="响应速度">(.*?)</td>')
    # UIHOUYANZHENGSHIJIAN_PATTERN=re.compile(r'<td data-title="最后验证时间">(.*?)</td>')

    #http://www.jishu5.com/
    
    foldexist('G:/CSDN_L/python/案例/国内高匿代理')    
    a=0
    while True:
        a=a+1
        with open('G:/CSDN_L/python/案例/国内高匿代理/log.txt', 'w') as file:   # .txt可以不自己新建,代码会自动新建
                file.write(str(a))
        resp= requests.get('https://www.kuaidaili.com/free/inha/'+str(a)+'/')
        soup = bs4.BeautifulSoup(resp.text, 'lxml')
        elements = soup.select('#list>table>tbody>tr')
        data={}
        for element in elements:
            ip = element.select('td')[0].string
            port = element.select('td')[1].string
            niming=element.select('td')[2].string
            leixing=element.select('td')[3].string
            weizhi=element.select('td')[4].string
            xiangyingsudu=element.select('td')[5].string
            zuihouyanzhengshijian=element.select('td')[6].string
            data["ip"]=ip
            data["port"]=port
            data["匿名度"]=niming
            data["类型"]=leixing
            data["位置"]=weizhi
            data["响应速度"]=xiangyingsudu
            data["最后验证时间"]=zuihouyanzhengshijian
                #DATA.append(data)
            bbb(data)
            data={}
        print("开始第%d次爬取"%(A))
        time.sleep(1)
              
            
                #print("DATA",DATA)               
        # except:
        #     with open('G:/CSDN_L/python/案例/国内高匿代理/log.txt','r+') as file:
        #         content=file.read()
        #         file.seek(0)
        #         file.write(str(int(content)+1))   
        #     aaa()  
                 
            #data = file.read()  
                
        
    #     ##url='https://www.kuaidaili.com/free/inha/'+str(a)+'/'
    #     # proxy = {'http': '175.42.129.130:9999'}
    #     # proxies = request.ProxyHandler(proxy)  # 创建代理处理器
    #     # opener = request.build_opener(proxies)  # 创建opener对象
        
    #     # resp = opener.open(url)
    #     resp= requests.get('https://www.kuaidaili.com/free/inha/'+str(a)+'/')

    #     soup = bs4.BeautifulSoup(resp.text, 'lxml')
    #     elements = soup.select('#list>table>tbody>tr')
    #     # print(elements)
    #     # print(type(elements))
    #     data={}
    #     for element in elements:
    #         ip = element.select('td')[0].string
    #         port = element.select('td')[1].string
    #         niming=element.select('td')[2].string
    #         leixing=element.select('td')[3].string
    #         weizhi=element.select('td')[4].string
    #         xiangyingsudu=element.select('td')[5].string
    #         zuihouyanzhengshijian=element.select('td')[6].string
    #         data["ip"]=ip
    #         data["port"]=port
    #         data["匿名度"]=niming
    #         data["类型"]=leixing
    #         data["位置"]=weizhi
    #         data["响应速度"]=xiangyingsudu
    #         data["最后验证时间"]=zuihouyanzhengshijian
    #         DATA.append(data)
    #         bbb(data)
    #         data={}
    #     print("开始第%d次爬取"%(a))
    #     print("DATA",DATA)
        
    #     time.sleep(1)
        
    #https://www.cnblogs.com/wxplmm/p/10319515.html
    # pattern= PATTERN.findall(resp.text)
    # ip = IP_PATTERN.findall(resp.text)
    # port = PORT_PATTERN.findall(resp.text)
    # niming = NIMINGDU_PATTERN.findall(resp.text)
    # leixing = LEIXING_PATTERN.findall(resp.text)
    # weizhi = WEIZHI_PATTERN.findall(resp.text)
    # xiangyingsudu = XIANGYINGSUDU_PATTERN.findall(resp.text)
    # yanzhengshijian=UIHOUYANZHENGSHIJIAN_PATTERN.findall(resp.text)

    # print(pattern)
    # print(ip)
    # print(port)
    # print(niming)
    # print(leixing)
    # print(weizhi)
    # print(xiangyingsudu)
    # print(yanzhengshijian)
    # for element in elements:
    #     span = element.select_one('.title')
    #     print(span.text)
    
    # res=urllib.request.urlopen("http://www.kuaidaili.com/free/inha/1/")
    # print(res.read().decode())
  
    # with open('G:/CSDN_L/python/案例/1.txt', 'w') as file:   # .txt可以不自己新建,代码会自动新建
    #     for i in DATA:
    #         file.write(str(i))     # 写入
    #         file.write('\n')
    #time.sleep(5)
def main():
    t1=threading.Thread(target=aaa) 
    
    t1.start()
   
    
   
if __name__ == "__main__":
    main()