import socket
 
target_host = '127.0.0.1' #这里是服务器端的ip
target_port = 9999
 
#建立一个socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
#连接客户端
client.connect((target_host, target_port))
 
while True:
#发送一些数据
    sendmsg = input("请输入：")
    if sendmsg == 'over':
        print("Game over!")
        break
    sendmsg = sendmsg
    client.send(sendmsg.encode("utf-8"))
    response = client.recv(2048)
    print(response.decode("utf-8"))
client.close()
