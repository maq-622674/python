
import socket  # 导入 socket 模块
import time
s = socket.socket()  # 创建 socket 对象
s.connect(('127.0.0.1', 8712))
print(s.recv(1024).decode(encoding='utf8'))
while True:
    s.send("我是901".encode('utf8'))
    time.sleep(10)
# print(s.recv(1024).decode(encoding='utf8'))
