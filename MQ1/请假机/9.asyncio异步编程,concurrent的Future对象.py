'''
3.5
concurrent.futures.Future对象
使用线程池,进程池实现异步操作时用到的对象
'''

# import time
# from concurrent.futures import Future
# from concurrent.futures.thread import ThreadPoolExecutor
# from concurrent.futures.process import ProcessPoolExecutor
# def func(value):
#     time.sleep(1)
#     print(value)
#     return 123

# #创建线程池
# pool=ThreadPoolExecutor(max_workers=5)

# #创建进程池
# #或pool=ProcessPoolExecutor(max_workers=5)

# for i in range(10):
#     fut=pool.submit(func,i)
#     print(fut)

#以后写代码可能会存在交叉时间,例如
#:crm项目80%都是基于协程异步编程+MySQL(不支持)【线程,进程做异步编程】
import time
import asyncio
import concurrent.futures

def func1():
    #某个耗时操作
    time.sleep(2) 
    return 'SB'

async def main():
    loop=asyncio.get_running_loop()
    '''
    #1.Run in the default loop's executor(默认ThreadPoolExecutor)
    #第一步:内容会先调用ThreadPoolExecutor的submit方法去线程池中申请一个线程去执行func1函数,并返
    #回一个concurrent.futures.Future对象
    #第二步:调用asyncio.wrap_future将concurrent.futures.Future对象包装为asyncio.Future对象
    #因为concurrent.futures.Future对象不支持await语法,所以需要包装为asyncio.Future对象才能使用
    '''
    fut=loop.run_in_executor(None,func1)
    result=await fut
    print("default thread pool",result)
    #2.Run in a custom thread pool:
    #with concurrent.futures.ThreadPoolExecutor() as pool
    #   result=await loop.run_in_executor(
    #       pool,func1)
    #   print("custom thread pool",result)

    #3.Run in a custom process pool:
    #with concurrent.futures.ProcessPoolExecu
    #   result=await loop.run_in_executor(       
    #       pool,func1)
    #   print("custom process pool",result)

    
asyncio.run(main())



