#1.使用urllib的GET获取58同城中关于python的招聘信息
from urllib import request
from urllib import error
import re

url = "http://bj.58.com/job/?key=python&final=1&jump=1"
req = request.Request(url)
try:
    response = request.urlopen(req)
    html = response.read().decode('utf-8')

    pat = '<span class="address" >(.*?)</span>  \| <span class="name">(.*?)</span>'
    dlist = re.findall(pat,html)

    #print(len(dlist))
    for v in dlist:
        print(v[0]+" | "+v[1])
except error.URLError as e:
    print(e.reason) #输出错误信息

print("ok")


#2.使用requests的GET获取58同城中关于python的招聘信息
import requests
import re

data = {
    'key':'python',
    'final':1,
    'jump':1,
}
url = "http://bj.58.com/job/"

res = requests.get(url,params=data)

html = res.content.decode('utf-8')

pat = '<span class="address" >(.*?)</span>  \| <span class="name">(.*?)</span>'
dlist = re.findall(pat,html)

print(len(dlist))

for v in dlist:
    print(v[0]+" | "+v[1])