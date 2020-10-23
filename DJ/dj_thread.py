import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1)-->协程函数:
    r = yield from asyncio.sleep(1)  #此处为另外一个协程，不是休眠
    print("Hello again!")

# 获取EventLoop（事件循环器）:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()