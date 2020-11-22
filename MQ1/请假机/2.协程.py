'''
1.协程
协程不是计算机提供,程序员认为创造。

协程也可以称为微线程,是一种用户态内的上下文切换技术,简而言之,
其实就是通过一个线程实现代码块相互切换执行,例如:

实现协程有那么几种方法:
greenlet,早期模块
yield关键字
asyncio装饰器(py3.4)
async,await关键字(py3.5)推荐
'''


'''
1.1
greenlet实现协程
'''
# from greenlet import greenlet
# def func1():
#     print(1)        #第1步:输出1
#     gr2.switch()    #第3步:切换func2函数
#     print(2)        #第6步:输出2
#     gr2.switch()    #第7步:切换到func2函数,从上一次执行的位置继续向后执行

# def func2():
#     print(3)        #第4步:输出3
#     gr1.switch()    #第5步:切换到func1函数,从上一次执行的位置继续想后执行
#     print(4)        #第8步:输出4

# gr1=greenlet(func1)
# gr2=greenlet(func2)
# gr1.switch()        #第1步:去执行func1函数

print('*'*10)
'''
1.2
yield关键字
'''
# def func1():
#     yield 1
#     yield from fun2()
#     yield 2
# def fun2():
#     yield 3
#     yield 4

# f1=func1()
# for item in f1:
#     print(item)

# print('#'*10)

'''
1.3
asyncio
在python3.4之后的版本
'''
# import asyncio

# @asyncio.coroutine
# def func1():
#     print(1)
#     #网络IO请求:下载一张图片
#     yield from asyncio.sleep(2) #遇到IO耗时操作,自动化切换到tasks中的其他任务
#     print(2)

# @asyncio.coroutine
# def func2():
#     print(3)
#     #网络IO请求:下载一张图片
#     yield from asyncio.sleep(2) #遇到IO耗时操作,自动化切换到tasks中的其他任务
#     print(4)

# tasks=[
#     asyncio.ensure_future(func1()),
#     asyncio.ensure_future(func2())
# ]
# loop=asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
#注意:遇到IO阻塞自动切换

'''
1.4
async&await关键字
在python3.5及之后的版本
推荐使用1.1和1.4
'''
import asyncio


async def func1():
    print(1)
    #网络IO请求:下载一张图片
    await asyncio.sleep(2) #遇到IO耗时操作,自动化切换到tasks中的其他任务
    print(2)

async def func2():
    print(3)
    #网络IO请求:下载一张图片
    await asyncio.sleep(2) #遇到IO耗时操作,自动化切换到tasks中的其他任务
    print(4)

tasks=[
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))