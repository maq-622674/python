from urllib import request
import json
from urllib import parse
import urllib
import time
import json
class WJY:
    def __init__(self,macid):
        self.__MACID=macid
        self.__URL=""

        self.__SIGNID=[]
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
    def leave_url(self):
        data=self.get(self.__URL)   
        data=self.get(data["login"])
        url=data['data']["LEAVE_URL"]+'&macid='+self.__MACID
        return url
    def respon(self):
     
        # if data==0:
        #     pass
        # if data==1:
            pass
    def stu_code(self):
        '''
        '''  
        cc={}
        data=self.get(self.__URL)
        data1=self.get(data["login"])
        # print(data1)
        # print(type(data1))
        data2=data1["data"]["classInfo"]
        # print(data2)
        # print(type(data2))
        for i in data2:
            tmp={
                "classId":i["classId"]
            }
            data3=self.gets(data["class"],tmp)
            for j in data3:
                data4=data3["data"]["childs"]
                
                for k in data4:              
                    
                    if k["signId"]:
                        if '#' in k["signId"]:
                            kahao=k["signId"].split('#')  
                            for m in kahao:
                                if m:
                                    self.__SIGNID.append(m)                        
                                                        
                        if '#' not in k["signId"]:
                            cc["signId"]=k["signId"]
                            cc["name"]=k["name"]
                            cc[""]
                            self.__SIGNID.append(k["signId"])


        

        print(self.__SIGNID)
        
            
    
#设备参数
zbh=WJY('ZBH-9843EE')
zbh.stu_code()