#!/usr/bin/python
#-*- coding:utf-8 -*-
'''
此脚本主要实现网页的点击量，除了实现次功能点外，还有三个知识点：
1、随机获取代理ip，通过代理ip访问指定站点，其目的是防止ip被封
2、访问一个页面后，随机休息几秒，再访问，其目的是防止网站前面有4-7层过滤设备拦截
3、修改http的user agent字段，有些网站和4-7层设备会检查
'''
 
import urllib,re,time,urllib,random,user_agents
import time
PROXYIPURL = 'http://www.goodips.com/?ip=&port=&dengji=&adr=%E7%94%B5%E4%BF%A1&checktime=&sleep=1%E7%A7%92%E5%86%85&cunhuo=48%E5%B0%8F%E6%97%B6%E4%BB%A5%E4%B8%8A&px='

class getProxyIP:
#   从网页抓去代理ip ，并整理格式
    def getProxyHtml(self):
#  抓去代理 ip页面的代码
        #9.打开PROXYIPURL网页
        page = urllib.urlopen(PROXYIPURL)
        #10.响应体内容
        html = page.read()
        #print html
        #11.返回内容
        return html
     
    def ipPortRe(self):
        #8.执行getProxyHtml()方法
#       从页面代码中取出代理 ip和端口
        html = self.getProxyHtml()
        #ip_re = re.compile(r'(((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?))')
        #12.正则表达式过滤
        ip_re = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).+\n.+>(\d{1,5})<')
        ip_port = re.findall(ip_re,html)
        return ip_port
         
         
    def proxyIP(self):
        #7.调用ipPortRe()方法
#       格式化输出代理 ip和端口
        ip_port = self.ipPortRe()        
        proxyIP = []
        #13.把将代理 ip整理成['221.238.28.158:8081', '183.62.62.188:9999']格式    
        for i in range(0,len(ip_port)):
            proxyIP.append(':'.join(ip_port[i]))   
             
#       14.将代理 ip整理成[{'http': 'http://221.238.28.158:8081'}, {'http': 'http://183.62.62.188:9999'}]格式        
        proxy_list = []
        for i in range(0,len(proxyIP)):
            a0 = 'http://%s'%proxyIP[i]
            a1 = {'http':'%s'%a0}
            proxy_list.append(a1)
        #15.返回可用的ip列表
        return proxy_list
 
def getHtml(url):
    #4.url从外层传过来
    #5.创建getProxyIP对象
    p = getProxyIP()
    #6.执行类里面的proxyIP方法
    proxy_list = p.proxyIP()

    #16.在proxy_list中随机取一个ip
    proxy_ip =random.choice(proxy_list) 
    #17.输出是哪个ip
    print(proxy_ip)    

    #18.设置代理ip
    proxy_support = urllib.ProxyHandler(proxy_ip)

    #19.1、build_opener 的作用
    # 要爬取的各种各样的网页，它们有一部填写需要验证码，有的需要cookie，还有更多许多高级的功能，它们会阻碍你爬，而我对于openurl单纯地理解就是打开网页。openurl打开一个网址，
    # 它可以是一个字符串或者是一个request对象。而build_opener就是多了handler，处理问题更专业,更个性化。

    opener = urllib.build_opener(proxy_support,urllib.HTTPHandler)

    #20.install_opener(opener)
    #安装不同的opener对象作为urlopen()使用的全局opener。
    urllib.install_opener(opener)

    #21.urllib.request可以用来发送request和获取request的结果
    request = urllib.Request(url)

    #22.在user_agents中随机取一个做user_agent
    user_agent = random.choice(user_agents.user_agents)  

    #23.修改user-Agent字段
    request.add_header('User-Agent',user_agent)
    print(user_agent)

    html = urllib.urlopen(request).read()
    print (proxy_ip)
    return proxy_ip
 
 
 
URLS = ['http://www.x'+x+'xxw.net/study.asp?vip=',
        'http://www.x'+x+'x'+x+'x'+'x.com/?fromuid=16',
        ]
 
count_True,count_False,count= 0,0,0
#1.无限循环
while True:
    #2.循环遍历URLS
    for url in URLS:
        #3.每次都让count+1 count初始值为0
        count +=1
        try:
            #如果执行错误except有报错提示
            proxy_ip=getHtml(url)            
        except urllib.URLError:
            #print 'URLError! The bad proxy is %s' %proxy_ip
            count_False += 1
        except urllib.HTTPError:
            #print 'HTTPError! The bad proxy is %s' %proxy_ip
            count_False += 1
        except:
             #print 'Unknown Errors! The bad proxy is %s ' %proxy_ip 
             count_False += 1

        #取1-10之间的随机浮点数
        randomTime = random.uniform(1,3) 
        #随机等待时间
        time.sleep(randomTime) 
        print ('%d Eroors,%d ok,总数 %d' %(count_False,count - count_False,count))
