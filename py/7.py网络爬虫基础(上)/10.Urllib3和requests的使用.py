# 10. urllib3和requests的使用
# Python3 默认提供了urllib库，可以爬取网页信息，但其中确实有不方便的地方，如：处理网页验证和Cookies，以及Hander头信息处理。

# 为了更加方便处理，有了更为强大的库 urllib3 和 requests, 本节会分别介绍一下，以后我们着重使用requests。

# urllib3网址：https://pypi.org/project/urllib3/

# requests网址：http://www.python-requests.org/en/master/

# 1. urllib3库的使用：
# 安装：通过使用pip命令来安装urllib3
#     pip install urllib3

import urllib3
import re

# 实例化产生请求对象
http = urllib3.PoolManager()
# get请求指定网址
url = "http://www.baidu.com"
res = http.request("GET",url)
# 获取HTTP状态码
print("status:%d" % res.status)
# 获取响应内容
data = res.data.decode("utf-8")
# 正则解析并输出
print(re.findall("<title>(.*?)</title>",data))



#其他设置: 增加了超时时间，请求参数等设置
import urllib3
import re

url = "http://www.baidu.com"
http = urllib3.PoolManager(timeout = 4.0) #设置超时时间

res = http.request(
       "GET",
        url,
        #headers={
        #    'User-Agent':'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
        #},
        fields={'id':100,'name':'lisi'}, #请求参数信息
    )

print("status:%d" % res.status)
data = res.data.decode("utf-8")
print(re.findall("<title>(.*?)</title>",data))





#2.2. requests库的使用：
# 安装：通过使用pip命令来安装requests
#     pip install requests

import requests
import re

url = "http://www.sdyoocai.com/"

# 抓取信息
res = requests.get(url)

#获取HTTP状态码
print("status:%d" % res.status_code)

# 获取响应内容
data = res.content.decode("utf-8")

#解析出结果
print(re.findall("<title>(.*?)</title>",data))
print(data)



import random
#1.通过随机请求头反爬虫
#2.随机IP
#3.动态页面的反爬虫
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36 Chrome 41.0.2227.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
]

#从列表中随机选择一个
User_Agent = random.choice(USER_AGENTS)

headers = {
    'Host': 'blog.csdn.net',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.baidu.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}
print(headers)

if __name__ == "__main__":
   pass