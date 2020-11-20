import threading
import urllib
import time
import requests
import re
from lxml import etree
import os
from urllib import request
import bs4
import configparser
import json


class DAILI:
    def __init__(self, url):
        self.__URL = url

    def is_json(self, file):
        '''
        判断是不是json
        '''
        try:
            json.loads(file)
        except:
            return False
        return True

    def str_json(self, data):
        data = json.loads(data)
        return data

    def get(self, url):
        '''
        get请求,不带参数
        '''
        try:
            response = request.urlopen(url)
            # print("查看 response 响应信息类型: ",type(response))
            page = response.read()
            page = page.decode('utf-8')
            # url解码
            data = parse.unquote(page)
            # print("data@@@@@@@@@@@@@@@@@@@@@@@@",data)
            if self.is_json(data):
                data = self.str_json(data)
                return data
        except:
            return 'error'

    def gets(self, url, data):
        '''
        get请求,带参数
        '''
        try:
            # data = json.dumps(data)
            # print(data)
            data = bytes(urllib.parse.urlencode(data), encoding='utf8')
            response = request.urlopen(url=url, data=data)
            # print("查看 response 响应信息类型: ",type(response))
            page = response.read()
            page = page.decode('utf-8')
            # url解码
            data = parse.unquote(page)
            # print("data@@@@@@@@@@@@@@@@@@@@@@@@",data)
            if self.is_json(data):
                data = self.str_json(data)
                return data
        except:
            return 'error'

    def post(self, url, data):
        '''
        post请求
        '''
        try:

            data_string = urllib.parse.urlencode(data)
            last_data = bytes(data_string, encoding='utf-8')
            response = urllib.request.urlopen(url, data=last_data)
            data = response.read().decode('utf-8')
            # print(response.read().decode('utf-8'))
            if self.is_json(data):
                data = self.str_json(data)
                return data
        except:
            print("接口有问题")


def foldexist(abspath: str) -> None:
    """
    判断当前路径文件夹是否存在，如果不存在会自动创建
    """
    if not os.path.exists(abspath):
        os.makedirs(abspath)
# DATA=[]


def gaoni():
    foldexist('G:/CSDN_L/python/案例/国内高匿代理')
    while True:
        global A
        A = A+1
        with open('G:/CSDN_L/python/案例/国内高匿代理/log.txt', 'w') as file:   # .txt可以不自己新建,代码会自动新建
                    file.write(str(A))
        resp = requests.get('https://www.kuaidaili.com/free/inha/'+str(A)+'/')
        soup = bs4.BeautifulSoup(resp.text, 'lxml')
        elements = soup.select('#list>table>tbody>tr')
        data = {}
        for element in elements:
            ip = element.select('td')[0].string
            port = element.select('td')[1].string
            niming = element.select('td')[2].string
            leixing = element.select('td')[3].string
            weizhi = element.select('td')[4].string
            xiangyingsudu = element.select('td')[5].string
            zuihouyanzhengshijian = element.select('td')[6].string
            data["ip"] = ip
            data["port"] = port
            data["匿名度"] = niming
            data["类型"] = leixing
            data["位置"] = weizhi
            data["响应速度"] = xiangyingsudu
            data["最后验证时间"] = zuihouyanzhengshijian
            # DATA.append(data)
            bbb(data)
            data = {}
        print("开始第%d次爬取" % (A))
        time.sleep(1)


def bbb(data):
    with open("G:/CSDN_L/python/案例/国内高匿代理/ip.txt", "a") as file:
        file.write(str(data)+"\n")


def rini(data, data1, data2):

    abspath = "G:/CSDN_L/python/py必备模块整理100/log.ini"
    # if not os.path.exists(abspath):
    #     with open(abspath,"a") as file:
    #         pass
    # else:
    #     pass

    config = configparser.ConfigParser()
    config.read(abspath)
    try:
        config.add_section(data)
        config.set(data, data1, data2)
        # config.set("School","Mask","255.255.255.0")
        # config.set("School","Gateway","10.15.40.1")
        # config.set("School","DNS","211.82.96.1")
    except configparser.DuplicateSectionError:
        print("Section 'School' already exists")


def aaa():
    DATA = []
    with open('G:/CSDN_L/python/py必备模块整理100/log.ini', 'w') as file:   # .txt可以不自己新建,代码会自动新建
            file.write('')
    url = 'https://blog.csdn.net/jiahaoangle/article/details/102740223?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522160566879919724836716796%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=160566879919724836716796&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v28-1-102740223.pc_first_rank_v2_rank_v28&utm_term=python%E5%BF%85%E5%A4%87%E6%A8%A1%E5%9D%97%E6%95%B4%E7%90%86100&spm=1018.2118.3001.4449'

    data = request.urlopen((url)).read()  # 读取url响应结果
    data = data.decode('utf-8')  # 将响应结果用utf8编码

    soup = bs4.BeautifulSoup(data, 'lxml')

    elements = soup.select('#content_views>table>tbody')
    # print("el",elements)

    for element in elements:
        el = element.select('tr')
        for i in el:
            el_data = []
            iii = i.select('td')

            for j in iii:
                el_data.append(j.string)

            DATA.append(el_data)

            # print(iii)

            # print("el_data",el_data)
    print('------------------')
    #print("DATA", DATA)

    for k in DATA:
        print(k[1])
        print(type(k[1]))
        # k2=json.dumps(k[2])
        # print(k2)
        k3=str(k[1]).encode('utf8')
        # rini(k[1],k[2],k[3])
        print('------------------1')
        print(k3)

            # print(m)
            # rini('')

    # print("DATA:",DATA)
            # print(el.string)


    #     ip = element.select('td')[0].string
    #     port = element.select('td')[1].string
    #     niming=element.select('td')[2].string
    #     leixing=element.select('td')[3].string
    #     weizhi=element.select('td')[4].string
    #     xiangyingsudu=element.select('td')[5].string
    #     zuihouyanzhengshijian=element.select('td')[6].string
    #     data["ip"]=ip
    #     data["port"]=port
    #     data["匿名度"]=niming
    #     data["类型"]=leixing
    #     data["位置"]=weizhi
    #     data["响应速度"]=xiangyingsudu
    #     data["最后验证时间"]=zuihouyanzhengshijian
    #         #DATA.append(data)
    #     bbb(data)
    #     data={}
    # print("开始第%d次爬取"%(A))




def main():
    aaa()
if __name__ == "__main__":
    main()
