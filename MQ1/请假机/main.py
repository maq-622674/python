import time
from threading import Thread
from urllib import request
from urllib import parse
import json
import asyncio
import aiohttp
class WJY:
    def __init__(self,ip_port,macid):
        self.__WJY_URL="URL"+macid
        self.__MACID_ID="&macid="+macid
        self.__CLASS=''
        self.__LEAVE_URL=''
    def is_json(self,file):
        try:
            json.loads(file)
        except:
            return False
        return True
    def str_json(self,data):
        data=json.loads(data)
        return data
    def en_code(self):
        pass
    def de_code(self,page):
        page=page.decode('utf-8')      
        data=parse.unquote(page)
        if self.is_json(data):
            data=self.str_json(data)
        return data
    def get(self,data):
        try:
            response=request.urlopen(data)  
            #print("查看 response 响应信息类型: ",type(response))
            page=response.read()
            page=page.decode('utf-8')
            #url解码
            data=parse.unquote(page)
            if self.is_json(data):
                data=self.str_json(data)
            #print("data@@@@@@@@@@@@@@@@@@@@@@@@",data)
            return data
        except:
            return 'error'
    def gets(self):
        pass
    def post(self):
        pass
    def init(self):
        print("开始初始化")
        res=self.get(self.__WJY_URL)
        print("初始化结束")
        return res       
    def login(self,data):
        print("login接口开始")     
        res=self.get(data)
        print(res)
        if res['data']["LEAVE_URL"]:
            self.__LEAVE_URL=res['data']["LEAVE_URL"]
        if res["data"]["classInfo"]:
            print("login接口结束")  
            return res["data"]["classInfo"]
    def init_class(self,data):
        print("init_class接口开始")    
        print("init_class接口结束")
                
    def getleave(self,data):
        print("getleave接口开始")
        url=self.__LEAVE_URL+self.__MACID_ID
        print(url)
        # asyncio.run(self.async_getleave())
        print("getleave接口结束")
    def face(self):
        data=self.init()
        if data["class"]:
            self.__CLASS=data["class"]
        if data["login"]:
            login=self.login(data["login"])
            self.init_class(login)
        
            
def main():
    IPP="192.168.101.208:9527"
    MACID='wjydebug201116'
    ccc=WJY(IPP,MACID)
    ccc.face()
if __name__ == "__main__":
    main()
