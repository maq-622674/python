import socket
print("程序开始")
#   创建套接字
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   设置ip和端口
host = socket.gethostname()
port = 3333
#   连接到服务器
mySocket.connect((host, port))
print("连接到服务器")
 
while True:
    #   接收消息
    print("----------------------读取:", end="")# 不换行输出
    msg = mySocket.recv(1024)
    print("%s" % msg)
    print("读取完成")
    if msg == b"EOF":
        break
    if msg == b"quit":
        mySocket.close()
        print("程序结束\n")
        exit()
 
    #   发送消息
    msg = input("----------------------发送:")
    mySocket.send(msg.encode())
    print("发送完成")
    if msg == "EOF":
        break
    if msg == "quit":
        mySocket.close()
        print("程序结束\n")
        exit()
print("程序结束\n")