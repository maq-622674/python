import ssl
import urllib3
from fake_useragent import UserAgent
import json
# ssl._create_default_https_context = ssl._create_unverified_context


# request = urllib.request.Request(url='...', headers={...}) 
# context = ssl._create_unverified_context()
# web_page = urllib.request.urlopen(request, context=context)


def funcname():
    """
    使用https的时候,需要ssl证书,这是全局取消
    """
    ssl._create_default_https_context = ssl._create_unverified_context
def funcname1():
    """
    使用https的时候,需要ssl证书,这是局部取消
    """
    ssl._create_default_https_context = ssl._create_unverified_context
    return ssl._create_default_https_context

def funcname2():
    '''
    浏览器随机请求头
    返回数据:类似这样的Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1
    ''' 
    ua = UserAgent()  
    return ua.random

def funcname3():
    '''
    作用:json.dumps()用于将字典形式的数据转化为字符串
    参数数据类型为:dict
    返回数据类型为:str
    '''
    data={
        'abc':'123'
    }
    data = json.dumps(data)
    return data
def funcname4():
    '''
    json.loads()用于将字符串形式的数据转化为字典
    参数数据类型为:str
    返回数据类型为:dict
    '''
    data='{\
        "abc":"123"\
    }'
    data=json.loads(data)
    return data



# http=urllib3.PoolManager(num_pools=5,headers={'User-Agent':'ABCDE'})
# resq1=http.request('GET','http://www.baidu.com')
# print(resq1.data.decode())