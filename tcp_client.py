# 导入socket库:
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 3344))
# 发送数据:
while True:
    data=input("请输入通信内容:")
    if(data=='123'):
         s.close()

    data=bytes(data,encoding='utf8')
    s.send(data)
    # 接收数据:
    buffer = []
    while True:
        # 每次最多接收1k字节:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
# 关闭连接:

   

# 把接收的数据写入文件:
