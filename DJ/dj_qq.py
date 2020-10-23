from fake_useragent import UserAgent
import requests
import bs4


A_TEXT=[]
class Atext():

    def __init__(self,url):
        ua = UserAgent()
        #1.随机请求头
        self.__headers={
            "User-Agent":ua.random
        }
        self.__datas={}
        self.__url=url
    def zhuaqu(self):
        #2.抓取网页信息
        response = requests.get(self.__url,headers=self.__headers)
        if response.status_code==200:
            self.chuli(response)
        #print("百度一下的按钮:",elements)
        # print(type(elements))
        # print(str(elements))
        # print(type(str(elements)))
        # print(response.status_code)  # 打印状态码
        # print(type(response.status_code))
        # print(response.url)          # 打印请求url
        # print(response.headers)      # 打印头信息
        # print(response.cookies)      # 打印cookie信息
        # print(response.text)  #以文本形式打印网页源码
        # print(response.content) #以字节流形式打印
                
    def chuli(self,response):
        #3.提取下载链接
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        title=str(soup.title)
        self.__datas["name"]=title.split('<title>')[1].split('</title')[0]
        elements = str(soup.select('.button-container'))
        if '.exe' in elements:
            data=elements.split('href=\"')[1].split('\"></a>')[0]
            self.__datas["link"]=data
        A_TEXT.append(self.__datas)
        self.__datas={}
           

aaa=Atext('https://im.qq.com/pcqq/')
aaa.zhuaqu()
print(A_TEXT)


# response = requests.get('https://im.qq.com/pcqq/')
# print(response.status_code)  # 打印状态码
# print(response.url)          # 打印请求url
# print(response.headers)      # 打印头信息
# print("cookie:",response.cookies)      # 打印cookie信息
# print(response.text)  #以文本形式打印网页源码
# print(response.content) #以字节流形式打印

