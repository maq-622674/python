import time
import queue
import random
import asyncio
import traceback
import collections
import json
from urllib import parse,request
from aiohttp import ClientSession, TCPConnector, client_exceptions, ClientTimeout

queue_data = queue.Queue()
timeout_domains = []
unknown_error_domains = []
start_time_list = []
import aiohttp


class WJY:
    def __init__(self, ip_port, macid):
        self.__WJY_URL = "" + macid
        self.__MACID_ID = "&macid=" + macid
        self.__CLASS = ''
        self.__LEAVE_URL = ''

    def is_json(self, file):
        try:
            json.loads(file)
        except:
            return False
        return True

    def str_json(self, data):
        data = json.loads(data)
        return data

    def en_code(self):
        pass

    def de_code(self, page):
        page = page.decode('utf-8')
        data = parse.unquote(page)
        if self.is_json(data):
            data = self.str_json(data)
        return data

    def get(self, data):
        try:
            response = request.urlopen(data)
            # print("查看 response 响应信息类型: ",type(response))
            page = response.read()
            page = page.decode('utf-8')
            # url解码
            data = parse.unquote(page)
            if self.is_json(data):
                data = self.str_json(data)
            # print("data@@@@@@@@@@@@@@@@@@@@@@@@",data)
            return data
        except:
            return 'error'

    def gets(self):
        pass

    def post(self):
        pass

    def init(self):
        print("开始初始化")
        res = self.get(self.__WJY_URL)
        print("初始化结束")
        return res

    def login(self, data):
        print("login接口开始")
        res = self.get(data)
        print(res)
        if res['data']["LEAVE_URL"]:
            self.__LEAVE_URL = res['data']["LEAVE_URL"]
        if res["data"]["classInfo"]:
            print("login接口结束")
            return res["data"]["classInfo"]

    def init_class(self, data):
        print("init_class接口开始")
        print(self.__CLASS)
        print(data)

        # asyncio.run(self.async_init_class(data))
        # t1=threading.Thread(target=)
        # t1.start()
        DATA2 = []
        if data:
            for i in data:
                aaa = self.get(self.__CLASS + '&classId=' + i["classId"])
                DATA2.append(aaa)
        # print(DATA2)
        print("init_class接口结束")
        return DATA2

    def getleave(self, data):
        print("getleave接口开始")
        url = self.__LEAVE_URL + self.__MACID_ID
        print(url)
        # asyncio.run(self.async_getleave())
        print("getleave接口结束")
    def login_data(self,data):
        DATA2 = []
        for i in data:
            aaa = self.__CLASS + '&classId=' + i["classId"]
            DATA2.append(aaa)
        # print(DATA2)
        print("init_class接口结束")
        return DATA2
    def face(self):
        data = self.init()
        print(data)
        if data["class"]:
            self.__CLASS = data["class"]
        if data["login"]:
            login = self.login(data["login"])
            login_data = self.login_data(login)
            #asyncio.run(self.async_login(login_data))
            return login_data
            # ccc=self.init_class(login)
            # print(ccc)





    async def classid_fetch(self,session, n, url):
        start_time = time.time()
        # noinspection PyBroadException
        print("第二个异步请求(每个班级发送请求看每个班有多少学生)",url)
    async def fetch(self,session, n, url):
        """
        :param session:  aiohttp.ClientSession
        :param n: task编号
        :param url: 请求url
        """
        start_time = time.time()
        # noinspection PyBroadException
        print("第一个异步请求(多少个班级发起的异步请求)", url)
        # try:
        #     async with session.get(url, verify_ssl=False) as response:
        #         content = await response.content.read()
        #         # content = self.async_decode(content)
        #         # content = self.async_getleave(content)
        #         print(content)
        #     # await self.async_getleave_data(content)
        # except:
        #     print("失败")

        try:
            async with session.get(url=url, verify_ssl=False) as response:
                r = await response.read()
                end_time = time.time()
                cost = end_time - start_time
                r=self.de_code(r)
                msg = "第{}个查询请求，花费时间: {}s, 返回信息: {}".format(n, cost, r)
                #print(msg)
                queue_data.put(1)
                return r

        except client_exceptions.ServerTimeoutError as timeout_error:
            print("request timeout error: {}, url: {}".format(timeout_error, url))
            timeout_domains.append(url)
        except Exception:
            print("request unknown error: {}".format(traceback.format_exc()))
            unknown_error_domains.append(url)
        finally:
            # task_done减少计数
            pass
        start_time_list.append(str(start_time).split(".")[0])

    def stu_data(self,data):
        #print("data1", data["data"]["childs"])
        if data["data"]["childs"]:
            for i in data["data"]["childs"]:
                if i["signId"]:
                    print(i)

        # print(data)
        # print(type(data))
        # if data["classId"]:
        #     aaa=self.__CLASS+'&classId=' + data["classId"]
        #     return aaa
    async def chunks(self,sem, session, i, url):
        """
        限制并发数
        """
        async with sem:
            data=await self.fetch(session, i, url)
            data=self.stu_data(data)

            #await self.classid_fetch()


    # def get_domains():
    #     urls = []
    #     for _ in range(1000):
    #         urls.append("http://127.0.0.1:5000/?delay={}".format(random.randint(1, 8)))
    #     return urls


    async def main(self,urls):
        sem = asyncio.Semaphore(400)
        timeout = ClientTimeout(total=10, connect=2, sock_connect=15, sock_read=5)
        async with ClientSession(connector=TCPConnector(limit=400), timeout=timeout) as session:
            tasks = [asyncio.create_task(self.chunks(sem, session, index, url)) for index, url in enumerate(urls)]
            await asyncio.wait(tasks)


if __name__ == '__main__':
    IPP = "192.168.101.208:9527"
    IPP="47.106.243.10:30153"
    MACID = 'wjydebug201116'
    MACID='ZBHL-45F8A7'
    ccc = WJY(IPP, MACID)
    #ccc.face()

    # domains = get_domains()
    domains=ccc.face()
    #print(domains)
    asyncio.run(ccc.main(domains))
    print("success number: {}, timeout number: {}, unknown_error number: {}".format(queue_data.qsize(),
                                                                                    len(timeout_domains),
                                                                                    len(unknown_error_domains)))

    print(sorted(collections.Counter(start_time_list).items(), key=lambda item:item[0]))
    # 1. 没有超时的，第一批400个同一秒发起， 再往后就看response相应与读取速度
    # success number: 1000, timeout number: 0, unknown_error number: 0
    # [('1593246892', 400), ('1593246894', 48), ('1593246895', 55), ('1593246896', 55), ('1593246897', 76),
    #  ('1593246898', 74), ('1593246899', 90), ('1593246900', 96), ('1593246901', 106)]
    # 2. 有超时的
    # success number: 517, timeout number: 483, unknown_error number: 0
    # [('1593248067', 400), ('1593248068', 36), ('1593248069', 43), ('1593248070', 75), ('1593248071', 64),
    # ('1593248072', 168), ('1593248073', 126), ('1593248074', 69), ('1593248075', 19)]