import socket  # 导入 socket 模块
from threading import Thread
 
ADDRESS = ('127.0.0.1', 8712)  # 绑定地址
 
g_socket_server = None  # 负责监听的socket
 
g_conn_pool = []  # 连接池

def init():
    """
    初始化服务端
    """
    global g_socket_server
    g_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建 socket 对象
    g_socket_server.bind(ADDRESS)
    g_socket_server.listen(50)  # 最大等待数（有很多人理解为最大连接数，其实是错误的）
    print("服务端已启动，等待客户端连接...")


def accept_client():
    """
    接收新连接
    """
    while True:
        client, _ = g_socket_server.accept()  # 阻塞，等待客户端连接
        # 加入连接池
        g_conn_pool.append(client)
        # 给每个客户端创建一个独立的线程进行管理
        thread = Thread(target=message_handle, args=(client,))
        # 设置成守护线程
        thread.setDaemon(True)
        thread.start()
    
   
# import time
# MSG=[]

# XINTIAOBAO=[]
def message_handle(client):
    """
    消息处理
    """ 
    # global MSG,msg,XINTIAOBAO
    #print("msg_bytes:",msg_bytes)
    #print("msg_bytes:",msg_bytes.decode(encoding='utf8'))
    #给客户端发送消息
    #MSG+=msg_bytes.decode(encoding='utf8')
    print("客户端已上线:",client)
    #time.sleep(1)
    client.sendall("连接服务器成功!".encode(encoding='utf8'))
    # xiaoxi={}
    # msg=''
    # xintiaobao={}
    while True:
        msg_bytes=client.recv(1024)
        
        msg_bytes=msg_bytes.decode(encoding='utf8')
        
        print(msg_bytes)
        if len(msg_bytes)==0:
            #time.sleep(10)
            g_conn_pool.remove(client)
            print("有一个客户端下线了。")
            break
        
        #print(msg_bytes.decode(encoding='utf8'))
        # if 'xintiaobao' in msg_bytes:
        #     pass
        #     # if xintiaobao[client] in XINTIAOBAO:
        #     #     print("设备保持连接")
        #     # if xintiaobao[client] not in XINTIAOBAO:
        #     #     xintiaobao[client]=msg_bytes.decode(encoding='utf8')
        #     #     XINTIAOBAO.append(xintiaobao)
        # if 'xiaoxi' in msg_bytes:
        #     msg+=msg_bytes
        #     print("msg",msg)
        #msg+=msg_bytes.decode(encoding='utf8')        
        #xiaoxi[client]=msg
        #MSG.append(xiaoxi)
        #print("MSG:",MSG)
    
    #     #print("客户端发的消息",MSG)
    #     if len(msg_bytes)==0:
    #         #time.sleep(10)
    #         g_conn_pool.remove(client)
    #         print("有一个客户端下线了。")
    #         break
    #     bytes = client.recv(1024)
    #     print("客户端消息:", bytes.decode(encoding='utf8'))
    #     if len(bytes) == 0:
    #         client.close()
    #         # 删除连接
    #         g_conn_pool.remove(client)
    #         print("有一个客户端下线了。")
    #         break

if __name__ == '__main__':
    init()
    # 新开一个线程，用于接收新连接
    thread = Thread(target=accept_client)
    thread.setDaemon(True)
    thread.start()
    # 主线程逻辑
    while True:
        cmd = input("""--------------------------
输入1:查看当前在线人数
输入2:给指定客户端发送消息
输入3:关闭服务端
""")
        if cmd == '1':
            print("--------------------------")
            print("当前在线人数：", len(g_conn_pool))
        elif cmd == '2':
            print("--------------------------")
            index, msg = input("请输入'索引,消息'的形式:").split(",")
            g_conn_pool[int(index)].sendall(msg.encode(encoding='utf8'))
        elif cmd == '3':
            exit()



'''
两个线程
1.先把服务端开启 √
2.(线程 每一个连接的客户端)执行第一个线程开启,死循环,进来一个客户端加入连接池
3.(线程 每一个客户端发的消息)
4.(线程 每一个客户端的断开)
'''

'''
服务端开启
1.知道每个客户端的什么时候连接
2.知道每个客户端的什么时候掉线
2.1掉线了几次
2.2什么时间掉线的 
2.3判断客户端几秒不发送心跳包认为他掉线了
3.判断哪些连接曾经连接过,再次上线

4.cmd
当前在线客户端个数
当前给指定客户端发送
'''