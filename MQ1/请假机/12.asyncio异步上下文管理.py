'''
3.8
此种对象通过定义__aenter__()和__aexit()__
方法来对async with语句中的环境进行控制
由PEP 492引入
'''
import  asyncio

class AsyncContextManager:
    def __init__(self):
        self.conn=conn
    async def do_something(self):
        #异步操作数据库
        return  666
    async def __aenter__(self):
        #异步链接数据库
        self.conn=await  asyncio.sleep(1)
        return  self
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        #异步关闭数据库链接
        await  asyncio.sleep(1)

async def func():
    async with AsyncContextManager() as f:
        result=await f.do_something()
        print(result)

asyncio.run(func())