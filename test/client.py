
# import socket  # 导入 socket 模块
 
# s = socket.socket()  # 创建 socket 对象
# s.connect(('127.0.0.1', 8712))
# print(s.recv(1024).decode(encoding='utf8'))
# s.send("我是902".encode('utf8'))
# print(s.recv(1024).decode(encoding='utf8'))
# input("")




# print(s.recv(1024).decode(encoding='utf8'))
import socket
s=socket.socket()
s.connect(('127.0.0.1',8712))
while True:
    msg=input("--------------------------")
    s.send(msg.encode())
    print("发送完成")
    if msg=='q':
        s.close()
        print("退出")
        exit()