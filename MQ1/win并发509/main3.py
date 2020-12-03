import  asyncio
import aiohttp
async def asyncSpider(sem, url):
    """异步任务"""
    async with sem:
        print('Getting data on url', url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                html = await response.text()
                return html


async def taskManager():
    """异步任务管理器"""
    tasks = []
    sem = asyncio.Semaphore(10)  # 控制并发数
    for url in url_list:
        task = asyncio.create_task(asyncSpider(sem, url))
        task.add_done_callback(parseHTML)
        tasks.append(task)
    await asyncio.gather(*tasks)


def main():
    print('Task start! It is working...')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(taskManager())
    print('Finished!')