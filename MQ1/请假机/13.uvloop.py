'''
4.uvloop
是asyncio的事件循环的替代方案,事件循环>默认asyncio的事件循环
需要pip安装
'''
import asyncio
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

#编写asyncio的代码,与之前写的代码一致

#内部的事件循环自动化会变为uvloop
asyncio.run()

#注意:一个asgi->uvicorn内部使用的就是uvloop
