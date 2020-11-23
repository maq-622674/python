'''
3.3
await
await+可等待的对象(协程对象,Future,Task对象->IO等待)
'''
#示例1:
# import asyncio

# async def func():
#     print("来玩啊")
#     response = await asyncio.sleep(2)
#     print("结束",response)

# asyncio.run(func())

#示例2:

# import asyncio
# async def others():
#     print("start")
#     await asyncio.sleep(2)
#     print('end')
#     return '返回值'

# async def func():
#     print('执行协程函数内部代码')

#     #遇到IO操作挂起当前协程(任务),等IO操作完成之后再继续往下执行,当前协程挂起时,
#     #事件循环可以去执行其他协程(任务)
#     response=await others()
#     print("IO请求结束,结果为:",response)
# asyncio.run(func())

#示例3:
import asyncio
async def others():
    print("start")
    await asyncio.sleep(2)
    print('end')
    return '返回值'

async def func():
    print('执行协程函数内部代码')
    #遇到IO操作挂起当前协程(任务),等IO操作完成之后再继续往下执行,当前协程挂起时,
    #事件循环可以去执行其他协程(任务)
    response1=await others()
    print("IO请求结束,结果1为:",response1)

    response2=await others()
    print("IO请求结束,结果2为:",response2)

asyncio.run(func())

#await就是等待对象的值得到结果之后再继续向下走