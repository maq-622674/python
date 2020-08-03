
'''
只能一个用户
发送或接收多次数据
'''
#导入socket通信包
# import socket

 
# bind_ip = '127.0.0.1' #这里是服务器端的ip
# bind_port = 9999

# #1.首先，创建一个基于IPv4和TCP协议的Socket：
# # SOCK_STREAM表示的是TCP协议  SOCK_DGRAM表示的是UDP协议
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# #2.绑定地址（包括ip地址和端口号） 监听端口
# server.bind((bind_ip, bind_port))
 
# #3.设置监听数
# server.listen(1)
 
# print('Waiting for connection...')
# #4.进入监听状态，等待别人链接过来，有两个返回值，
# # 一个是对方的socket对象，一个是对方的ip以及端口

# client, addr = server.accept()
# #一般服务器都不需要关闭，所以加个while循环
# while True:
#     # recv表示接收，括号里是最大接收字节
#     request = client.recv(2048)
#     #字节转换为字符串
#     msg = request.decode("utf-8")
#     print("收到:" + msg)
#     #返还一个数据包
#     #服务端回他消息
#     ans = input("回复：")
#     if ans == 'over':
#         print("Game over!")
#         break
#     # send表示发送数据，发送的数据必须是二进制数据
#     client.send(ans.encode("utf-8"))
 
# client.close()

# try: # 如果对面强行关闭，为了程序不崩，就需要异常处理



'''
多个用户
'''
#导入socket通信包
import socket
import threading
import time

bind_ip = '127.0.0.1' #这里是服务器端的ip
bind_port = 9999

#1.首先，创建一个基于IPv4和TCP协议的Socket：
# SOCK_STREAM表示的是TCP协议  SOCK_DGRAM表示的是UDP协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
#2.绑定地址（包括ip地址和端口号） 监听端口
server.bind((bind_ip, bind_port))
 
#3.设置监听数
server.listen(5)
 
print('Waiting for connection...')
#4.进入监听状态，等待别人链接过来，有两个返回值，
# 一个是对方的socket对象，一个是对方的ip以及端口
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    while True:
      # recv表示接收，括号里是最大接收字节
      request = client.recv(2048)
      time.sleep(1)
      #字节转换为字符串
      msg = request.decode("utf-8")
      print("收到:" + msg)
      #返还一个数据包
      #服务端回他消息
      ans = input("回复：")
      if ans == 'over':
         print("Game over!")
         break
      # send表示发送数据，发送的数据必须是二进制数据
      client.send(ans.encode("utf-8"))

     
    # sock.send(b'Welcome!')
    # while True:
    #     data = sock.recv(1024)
    #     time.sleep(1)
    #     if not data or data.decode('utf-8') == 'exit':
    #         break
    #     sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    # sock.close()
    # print('Connection from %s:%s closed.' % addr)

#一般服务器都不需要关闭，所以加个while循环
while True:
    client, addr = server.accept()
    t = threading.Thread(target=tcplink, args=(client, addr))
    t.start()
    # recv表示接收，括号里是最大接收字节
    #request = client.recv(2048)
    #字节转换为字符串
    #msg = request.decode("utf-8")
    #print("收到:" + msg)
    #返还一个数据包
    #服务端回他消息
    #ans = input("回复：")
    #if ans == 'over':
      #  print("Game over!")
      #  break
    # send表示发送数据，发送的数据必须是二进制数据
    #client.send(ans.encode("utf-8"))
 
# #client.close()

