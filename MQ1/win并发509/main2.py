# import asyncio
# import aiohttp
#
#
# async def get_http(url):
#     async with semaphore:
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url) as res:
#                 global count
#                 count += 1
#                 print(count, res.status)
# def main():
#     pass
# if __name__ == '__main__':
#     count = 0
#
#     semaphore = asyncio.Semaphore(100)
#     loop = asyncio.get_event_loop()
#     url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&ch=&tn=baiduerr&bar=&wd={0}'
#     tasks = [get_http(url.format(i)) for i in range(600)]
#     loop.run_until_complete(asyncio.wait(tasks))
#     loop.close()

from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue

q = Queue(maxsize=100)

async def consumer():
    async for item in q:
        try:
            print('Doing work on %s' % item)
            await gen.sleep(0.01)
        finally:
            q.task_done()

async def producer():
    for item in range(5):
        await q.put(item)
        print('Put %s' % item)

async def main():
    # Start consumer without waiting (since it never finishes).
    IOLoop.current().spawn_callback(consumer)
    await producer()     # Wait for producer to put all tasks.
    await q.join()       # Wait for consumer to finish all tasks.
    print('完成')

IOLoop.current().run_sync(main)