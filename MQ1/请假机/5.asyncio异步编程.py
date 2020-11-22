'''
3.2快速上手
协程函数,定义函数时候async def 函数名
协程对象,执行协程函数()得到的协程对象
'''
import asyncio
async def fun():
    print("快来告我吧")

result=fun()
#注意:执行协程函数创建协程对象,函数内部代码不会执行

# loop=asyncio.get_event_loop()
#loop.run_until_complete(fun())
# loop.run_until_complete(result)

asyncio.run(result)#python3.7之后