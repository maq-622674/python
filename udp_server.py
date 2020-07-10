#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('127.0.0.1', 3333))

#print('Bind UDP on 3333...')

while True:
    # 接收数据:
    #接收UDP数据，与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。
    data, addr = s.recvfrom(1024)
    
    #print('Received from %s:%s.' % addr)
    
    #print(data)
    print(data.decode())
  

    reply="Hello World!"
    #reply = 'Hello, %s!' % data.decode('utf-8')

    #发送UDP数据，将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。
    s.sendto(reply.encode('utf-8'), addr)