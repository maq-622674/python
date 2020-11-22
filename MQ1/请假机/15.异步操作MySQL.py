'''
5.2异步Mysql
'''
# import asyncio
# import aiomysql
#
# async def excute():
#     #网络IO操作,连接MySQL
#     conn=await aiomysql.connect(host='127.0.0.1',port=3306,user='root',password='123',db='mysql',)
#
#     #网络IO操作:创建CURSOR
#     cur=await conn.cursor()
#
#     #网络IO操作:执行SQL
#     await cur.excute("SELECT Host,User FROM user")
#
#     #网络IO操作:获取SQL结束
#     result=await cur.fetchall()
#     print(result)
#
#     #网络IO操作:关闭连接
#     await cur.close()
#     conn.close()
# asyncio.run(excute())

#实例2:
import asyncio
import aiomysql

async def excute(host,password):
    #网络IO操作,连接MySQL
    conn=await aiomysql.connect(host=host,port=3306,user='root',password=password,db='mysql',)

    #网络IO操作:创建CURSOR
    cur=await conn.cursor()

    #网络IO操作:执行SQL
    await cur.excute("SELECT Host,User FROM user")

    #网络IO操作:获取SQL结束
    result=await cur.fetchall()
    print(result)

    #网络IO操作:关闭连接
    await cur.close()
    conn.close()
    print("结束",host)
task_list=[
    excute('47.93.41.197','root!2345'),
    excute('47.93.40.197','root!2345')
]
asyncio.run(asyncio.wait(task_list))