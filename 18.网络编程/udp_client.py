#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
    data1=input("输入通信字")
    if(data1=='1'):
        s.close()
    data1=bytes(data1,encoding='utf8')
    s.sendto(data1, ('127.0.0.1', 3333))
    print(s.recv(1024).decode('utf-8'))
    



# for data in [b'Michael', b'Tracy', b'Sarah']:
#      # 发送数据:
#      print(data)
#      print(type(data))
#      s.sendto(data, ('127.0.0.1', 3333))
#      # 接收数据:
#      print(s.recv(1024).decode('utf-8'))

