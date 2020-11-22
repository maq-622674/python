'''
2.协程的意义
在一个线程中如果遇到IO等待时间
线程不会傻傻等
利用空闲时间干点其他事
案例:去下载三张图片(网络IO)
'''

'''
1.普通方式(同步方式)
'''
# import requests
# def download_image(url):
#     print("开始下载:",url)
#     #发送网络请求，下载图片
#     response=requests.get(url)
#     print("下载完成")
#     #图片保存到本地文件
#     file_name=url.rsplit('_')[-1]
#     with open(file_name,mode='wb') as file_object:
#         file_object.write(response.content)
# if __name__=='__main__':
#     url_list=[
#         "https://www2.autoimg.cn/cardfs/product/g30/M04/36/E2/744x0_1_autohomecar__ChsEf19RsnKAUex4ACC74LZ94Oo636.jpg",
#         "https://www3.autoimg.cn/cardfs/product/g27/M09/8A/47/744x0_1_autohomecar__ChwFkV9RsTuAA80lAB397PfT7ds994.jpg",
#         "https://www3.autoimg.cn/cardfs/product/g2/M03/3C/D2/744x0_1_autohomecar__ChsEkF9RskqAVNMDACILd-5gXXA859.jpg"
#     ]
#     for item in url_list:
#         download_image(item)

'''
2.协程方式(异步方式)
aiohttp外部模块需要pip安装
'''
import aiohttp
import asyncio

async def fetch(session,url):
    print("发送请求",url)
    try:
        async with session.get(url,verify_ssl=False) as response: 
            content=await response.content.read()
            file_name=url.rsplit('_')[-1]
            with open(file_name,mode='wb') as file_object:
                file_object.write(content)
            print("下载完成",url)
    except:
        print("下载失败")
async def main():
    async with aiohttp.ClientSession() as session:
        url_list=[
        "https://www2.autoimg.cn/cardfs/product/g30/M04/36/E2/744x0_1_autohomecar__ChsEf19RsnKAUex4ACC74LZ94Oo636.jpg",
        "http",
        "https://www3.autoimg.cn/cardfs/product/g27/M09/8A/47/744x0_1_autohomecar__ChwFkV9RsTuAA80lAB397PfT7ds994.jpg",
        "https://www3.autoimg.cn/cardfs/product/g2/M03/3C/D2/744x0_1_autohomecar__ChsEkF9RskqAVNMDACILd-5gXXA859.jpg"
        ]
        tasks=[asyncio.create_task(fetch(session,url)) for url in url_list]
        await asyncio.wait(tasks)


if __name__=='__main__':
    asyncio.run(main())
