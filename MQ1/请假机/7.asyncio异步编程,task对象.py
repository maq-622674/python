'''
3.4
Task对象
白话:在事件循环中添加多个任务的

Task用于并发调度协程，通过asyncio.create_task(协程对象)的方式创建Task对象,这样可以让协程加入事件
循环中等待被调度执行，除了使用asyncio.create_task()函数以外,还可以用低层级的
loop.create_task()或ensure_future()函数,不建议手动实例化Task对象
'''

#实例1:
#用的很少
# import asyncio

# async def func():
#     print(1)
#     await asyncio.sleep(2)
#     print(2)
#     return '返回值'
# async def main():
#     print('main开始')

#     #创建Task对象,将当前执行func函数任务添加到事件循环
#     task1=asyncio.create_task(func())
#     #创建Task对象,将当前执行func函数任务添加到事件循环
#     task2 =asyncio.create_task(func())

#     print("main结束")
#     #当执行某协程遇到IO操作时,会自动化切换执行其他任务
#     #此处的await是等待相对应的协程全部执行完毕并获取结果
#     ret1=await task1
#     ret2=await task2
#     print("ret1:",ret1,"ret2:",ret2)

# asyncio.run(main())

#实例2:
# import asyncio

# async def func():
#     print(1)
#     await asyncio.sleep(2)
#     print(2)
#     return '返回值'
# async def main():
#     print('main开始')
#     task_list=[
#         asyncio.create_task(func()),
#         asyncio.create_task(func())
#     ]
    
#     print("main结束")
#     done,pending=await asyncio.wait(task_list,timeout=None)
#     print(done)
#     #print("ret1:",ret1,"ret2:",ret2)

# asyncio.run(main())

#实例3:
#实例2:
import asyncio

async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'

task_list=[
    func(),
    func(),
]
    

done,pending=asyncio.run(asyncio.wait(task_list))
print(done)
    #print("ret1:",ret1,"ret2:",ret2)
