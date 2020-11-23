'''
3.7
异步迭代器
__aiter__()和__anext__()方法的对象,__anext__
必须返回一个awaitable对象,async for会处理异步
迭代器的__anext__()方法所返回的可等待对象,
知道其引发一个StopAsyncIteration异常,由
PEP 492引入

什么是异步可迭代对象?
可在async for 语句中被使用的对象,必须通过它的__aiter__()
方法返回一个asynchronous iterator ,由PEP 492引入
'''
import asyncio
class Reader(object):
    '''
    自定义异步迭代器(同时也是异步可迭代对象)
    '''
    def __init__(self):
        self.count=0
    async def readline(self):
        #await asyncio.sleep(1)
        self.count+=1
        if self.count==100:
            return  None
        return self.count
    def __aiter__(self):
        return self
    async def __anext__(self):
        val=await  self.readline()
        if val==None:
            raise  StopAsyncIteration
        return  val
async def func():
    obj=Reader()
    async for item in obj:
        print(item)
asyncio.run(func())
