from urllib import request
import json
from urllib import parse
import urllib
import time
#ZBH-FBABEE
def is_json(file):
    try:
        json.loads(file)
    except:
        return False
    return True
def str_json(data):
    data=json.loads(data)
    return data
def can_url_get_open(url,data):
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
        return data
    except:
        return 'error'
def url_get_open(data):
    '''
    如果打开网页,则返回打开网页的数据
    如果打不开网页,则返回error
    '''
    try:
        response=request.urlopen(data)  
        #print("查看 response 响应信息类型: ",type(response))
        page=response.read()
        page=page.decode('utf-8')
        #url解码
        data=parse.unquote(page)
        #print("data@@@@@@@@@@@@@@@@@@@@@@@@",data)
        return data
    except:
        return 'error'



DATA={}
def init():
    '''
    1.1
    初始化
    '''
    global DATA
    aaa=url_get_open(WJY_URL)
    if is_json(aaa):
        data=str_json(aaa)
        #print("初始化相关data:",data)
        #print("--------------------")
        data1={}
        for key,value in data.items():
            DATA[key]=value
            # data1[key]=value
            # DATA.append(data1)
            # data1={}
init()

DATA1=[]
DATA3=''
SCHOOLNOTICE=''
ONLINE_URL=''
CLASSNOTICE=''
GETCLASSKQ=''
LEAVE_URL=''

def login():
    '''
    2.1
    login接口
    '''
    global DATA1,DATA3,ONLINE_URL,SCHOOLNOTICE,CLASSNOTICE,GETCLASSKQ,LEAVE_URL
    aaa=url_get_open(DATA["login"])
    
    if  is_json(aaa):
        aaa=str_json(aaa)
       # print("aaa:",aaa['data']["LEAVE_URL"])
        LEAVE_URL=aaa['data']["LEAVE_URL"]
        DATA3=aaa["data"]["schoolnotice"]
        SCHOOLNOTICE=aaa["data"]["schoolnotice"]
        CLASSNOTICE=aaa["data"]["classnotice"]
        GETCLASSKQ=aaa["data"]["getclasskq"]
        ONLINE_URL=aaa["data"]["onlineurl"]
        #print("login:",aaa["data"]["schoolnotice"])
        for i in aaa["data"]["classInfo"]:
            DATA1.append(i)
           
login()


DATA2=[]
def init_class():
    '''
    2.2
    class接口
    '''
    global DATA2
    
    for i in DATA1:
        data={
            "classId":i["classId"]
        }
        aaa=can_url_get_open(DATA["class"],data)
        aaa=str_json(aaa)
        DATA2.append(aaa)
    #print("aaa",aaa)
        #print("--------------------")
init_class()

# print("data2",DATA1)
# print("data2",DATA2)

def check():
    '''
    2.3
    check接口
    '''
    cc=''
    cc1=''
    for i in DATA2:
        cc=i["data"]["childs"][0]["signId"]
       
        cc1=i["data"]["todaytimeset"][0]["start"]
        #print(i["data"]["todaytimeset"][0]["start"])
    data={
        "signId":cc,
        "signTime":cc1,
    }
    ccc=can_url_get_open(DATA["check"],data)
    #print(ccc)
# check()



def banner():
    '''
    2.4banner接口
    '''
    ccc=url_get_open(DATA["banner"])
    #print("ccc",ccc)
# banner()

def roomlist():
    '''
    2.5roomlist
    '''
    #print(DATA["roomlist"])
    ccc=url_get_open(DATA["roomlist"])
    #print("ccc",ccc)
roomlist()


def schoolnotice():
    '''
    2.6schoolnotice接口
    '''
    data={
        "createtime":int(time.time())
    }
    ccc=can_url_get_open(SCHOOLNOTICE+'&macid=ZBH-9843EE',data)
   # print("schoolnotice接口:",ccc)
schoolnotice()

def classnotice():
    '''
    2.7classnotice接口
    '''
    data={
        "createtime":int(time.time())
    }
    ccc=can_url_get_open(CLASSNOTICE+'&macid=ZBH-9843EE',data)
    #print("classnotice接口:",ccc)
classnotice()

def getclasskq():
    
    data={
        "createtime":int(time.time())
    }
    ccc=can_url_get_open(GETCLASSKQ+'&macid=ZBH-9843EE',data)
   
getclasskq()
def getleave():
    import urllib.request
    import urllib.parse
   
    import time
    try:
        url=LEAVE_URL+'&macid=ZBH-9843EE'     
        for i in DATA2: 
            for j in i["data"]["childs"]:
                 
                # if j["name"]:
                #     print("j",j["name"])
                if j["signId"]:
     
                    
                    if '#' not in j["signId"]:
                        data_dict={
                        "signtime":int(time.time()),
                        "iccode":j["signId"]
                        }
                        data_string=urllib.parse.urlencode(data_dict)
                        last_data=bytes(data_string,encoding='utf-8')
                        response=urllib.request.urlopen(url,data=last_data)
                        res=response.read().decode('utf-8')
                        
                        if is_json(res):
                            res=str_json(res)
                            res_code=res["data"]["openDoor"]
                     
                            if res_code==1:
                                pass
                               
                            if res_code==0:
                                print("请假人卡号:",j["signId"])
                                print("请假人卡号:",j["name"])
                                print("请假人照片:",j["card2icon"][j["signId"]])
                        
                        
                    if '#' in j["signId"]:
                        aaa=j["signId"].split('#')
                        for k in aaa:
                            if k:
                                data_dict={
                                    "signtime":int(time.time()),
                                    "iccode":k
                                }
                                from Armoury import sock
                                data_string=urllib.parse.urlencode(data_dict)
                                #将序列化后的字符串转换成二进制数据，因为post请求携带的是二进制参数
                                last_data=bytes(data_string,encoding='utf-8')
                                #如果给urlopen这个函数传递了data这个参数，那么它的请求方式则不是get请求，而是post请求
                                #print("*********",url,last_data)
                                response=urllib.request.urlopen(url,data=last_data)
                                #我们的参数出现在form表单中，这表明是模拟了表单的提交方式，以post方式传输数据
                                res=response.read().decode('utf-8')
                                # print(response.read().decode('utf-8'))
                                if is_json(res):
                                    res=str_json(res)
                                    res_code=res["data"]["openDoor"]
                                    # print(res_code)
                                    # print(type(res_code))                            
                                    if res_code==0:
                                        print("请假人卡号:",k)
                                        print("请假人名字:",j['name'])
                                        print("请假人照片:",j["card2icon"][k])
                                    if res_code==1:
                                        pass
                                       
                                                                       
                    #使用urlencode将字典参数序列化成字符串                   
    except:
        print("接口有问题")
    
getleave()
def online():
    '''
    3.0
    online接口
    '''
    data=url_get_open(ONLINE_URL+'&macid=ZBH-9843EE')    
online()






