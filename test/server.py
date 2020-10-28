import socket  
print("Server is starting")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.bind(('127.0.0.1', 9998))  #配置soket，绑定IP地址和端口号
sock.listen(5) #设置最大允许连接数，各连接和server的通信遵循FIFO原则
print("Server is listenting port 8001, with max connection 5") 