#coding:utf-8
import time,asyncio,aiohttp

a=0
url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&ch=&tn=baiduerr&bar=&wd='
async def hello(url,sem):
    global a
    a+=1
    print("发送请求", url + str(a))
    async with sem:
        async with aiohttp.ClientSession() as session:
            async with session.get(url+str(a)) as response:
                res=await response.read()
                print(res)




async def run():
    sem = asyncio.Semaphore(100) # 限制并发量为500
    to_get = [hello(url,sem) for _ in range(1000)] #总共1000任务
    await asyncio.wait(to_get)


if __name__ == '__main__':
#    now=lambda :time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()