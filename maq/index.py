
import requests
import random

user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7',
    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0',
]
agent = random.choice(user_agents) # 随机获取一个浏览器用户信息
# 代理IP地址
proxy = {'HTTP':'117.85.105.170:808','HTTPS':'117.85.105.170:808','HTTP':'103.76.18.146:7878','HTTP':
'61.186.65.179:8888','HTTP':'163.204.247.24:9999','HTTP':'121.232.148.167:9000','HTTP':'1.198.73.77:9999','HTTP':'1.198.73.87:9999'}
# header头信息
headers = {
    'Host': 'blog.csdn.net',
    'User-Agent':agent,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.baidu.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}
# 请求url地址
url = "http://blog.csdn.net"
#www.sdyoocai.com
#url="http://www.sdyoocai.com/"
#url="https://www.jd.com/"

# 提交请求爬取信息

response = requests.get(url,headers=headers,proxies=proxy)
print(response.text)
# 获取响应码
print(response.status_code)







