import socket
import threading
import time
print("程序开始")
#   创建套接字
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   设置IP和端口
host = socket.gethostname()
port = 3333
#   bind绑定该端口
mySocket.bind((host, port))
#   监听
mySocket.listen(10)
print("服务器开启,等待连接....")


FUWUDUAN=[]
MSG="哈喽"
class Client():
    def __init__(self,client,ip,port):
        self.__CLIENT=client
        self.__IP=ip
        self.__PORT=port
    def init_sahngxian(self):
        print("设备上线self.__CLIENT",self.__CLIENT)
        print("设备上线self.__IP",self.__IP)
        print("设备上线self.__PORT",self.__PORT)
        self.__CLIENT.send(MSG.encode())
        while True:
            msg = self.__CLIENT.recv(1024)
            print("----------------------读取:", msg)
            print("读取完成")
def deal_data():
    while True:
        if 
        time.sleep(3)
while True:
    #   接收客户端连接
    client, address = mySocket.accept()
    t = threading.Thread(target=deal_data, args=(client, address))

    aaa=Client(client,address[0],address[1])
    aaa.init_sahngxian()
    # print("IP is 上线%s" % address[0])
    # print("port is %d\n" % address[1])
    
    
    
    # while True:
    #     #   发送消息
    #     #msg = input("----------------------发送:")
    #    # client.send(msg.encode())
    #     print("发送完成")
    #     if msg == "EOF":
    #         break
    #     if msg == "quit":
    #         client.close()
    #         mySocket.close()
    #         print("程序结束\n")
    #         exit()
    #     #   读取消息
    #     msg = client.recv(1024)
    #     print("----------------------读取:", msg)
    #     print("读取完成")
    #     if msg == b"EOF":
    #         break
    #     if msg == b"quit":
    #         client.close()
    #         mySocket.close()
    #         print("程序结束\n")
    #         exit()
