from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue
import time
q = Queue(maxsize=500)

async def consumer():
    print("10")
    async for item in q:
        try:
            print('Doing work on %s' % item)
            #await gen.sleep(0.01)
        finally:
            #task_done减少计数
            q.task_done()


async def producer():
    print("11")
    for item in range(50):
        #put增加计数
        await q.put(item)
        print('Put %s' % item)
    print("队伍数量producer",q.qsize())


async def main():
    # Start consumer without waiting (since it never finishes).
    print("123")
    IOLoop.current().spawn_callback(consumer)
    print("456")
    await producer()     # Wait for producer to put all tasks.
    print("789")
    await q.join()       # Wait for consumer to finish all tasks.
    time.sleep(10)
    print("队伍数量consumer", q.qsize())
    print('Done')

IOLoop.current().run_sync(main)