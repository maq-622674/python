'''
asyncio+不支持异步的模块
'''
import asyncio
import requests

async def download_image(url):
    #发送网络请求，下载图片，遇到网络下载图片的IO请求，自动化切换到其他任务
    print("开始下载:",url)
    loop=asyncio.get_event_loop()
    #requests模块默认不支持异步操作，所以就使用线程池来配合实现了
    future=loop.run_in_executor(None,requests.get,url)
    reponse=await future
    print("下载完成")
    #图片保存到本地文件
    file_name=url.rsplit('_')[-1]
    with open(file_name,mode='wb') as file_object:
        file_object.write(reponse.content)
    
if __name__=='__main__':
    url_list=[
        "https://www2.autoimg.cn/cardfs/product/g30/M04/36/E2/744x0_1_autohomecar__ChsEf19RsnKAUex4ACC74LZ94Oo636.jpg",
        "http",
        "https://www3.autoimg.cn/cardfs/product/g27/M09/8A/47/744x0_1_autohomecar__ChwFkV9RsTuAA80lAB397PfT7ds994.jpg",
        "https://www3.autoimg.cn/cardfs/product/g2/M03/3C/D2/744x0_1_autohomecar__ChsEkF9RskqAVNMDACILd-5gXXA859.jpg"
    ]
    tasks=[download_image(url) for url in url_list]
    loop=asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
