'''
5.4爬虫
pip install aiohttp
'''
import aiohttp
import asyncio

async def fetch(session,url):
    print("发送请求",url)
    try:
        async with session.get(url,verify_ssl=False) as response:
            text=await response.text()
            print("得到结果", url, len(text))
            return  text
            
    except:
        print("下载失败")
async def main():
    async with aiohttp.ClientSession() as session:
        url_list=[
        "https://python.org",
        "https://www.baidu.com",
        "https://www.pythonav.com"
        ]
        tasks=[asyncio.create_task(fetch(session,url)) for url in url_list]
        done,pending=await asyncio.wait(tasks)


if __name__=='__main__':
    asyncio.run(main())