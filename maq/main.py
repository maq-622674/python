# -*- coding: utf-8 -*-

"""
加载cookies文件，使用requests库爬取数据并动态更新cookies，可以使cookies不失效
"""

import pickle
import time
import requests
import random

class Spider:
    def __init__(self,domain='maersk.com.cn'):
        self.headers_maersk={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'www.maersk.com.cn',
            'Referer': 'https://www.maersk.com.cn/',
            'sec-ch-ua': "Chromium\";v=\"86\", \"\\\"Not\\A;Brand\";v=\"99\", \"Google Chrome\";v=\"86",
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
        }
        self.s=requests.Session()
        self.s.headers=self.headers_maersk
        self.__domain = domain
        self.timeOut=30
        self.cookies={
            '_uetvid':'85079510352c11eb9b0dfbe3a7e12585'
        }


    def SetLoginDomain(self,domain='maersk.com.cn'):
        """设置登录域名"""
        self.__domain=domain
        return self.__domain

    def SetTimeOut(self,timeOut=30):
        self.__timeOut=timeOut
        return self.__timeOut

    def set_cookies(self):
        """读取cookie文件 该文件由另外一个登录程序获取"""
        # with open('/cookies.txt') as f:
        #     data=f.read()
        #     print(data)
        #     data=bytes(data,encoding='utf-8')
        #     print(data)
        #     cookies = pickle.loads(data)
        # for cookie in cookies:
        #     self.cookies[cookie['name']]=cookie['value']
        self.s.cookies.update(self.cookies)

    def open_url(self, url,data=None):
        """页面请求方法"""
        # 请求页面方法
        MaxTryTimes = 20
        waite_time = random.uniform(0, 1)  # 初始化等待时间
        content=''
        for i in range(MaxTryTimes):
            time.sleep(waite_time)
            try:
                req = self.s.post(url,data=data,headers=self.headers_maersk,timeout=self.timeOut)
                print("req:",req)
                content=req.text
                if req.cookies.get_dict():
                    self.s.cookies.update(req.cookies)
                break
            except:
                content = ''
        return content

if __name__ == '__main__':
    spider=Spider()
    spider.set_cookies()
    content=spider.open_url(url='https://www.maersk.com.cn')
    print(content)