import json
import logging
import traceback
from threading import Thread
import socket
import threading
import time


logger = logging


class ElevStatusWsServer(Thread):
    def __init__(self, host, port):
        Thread.__init__(self, name="ElevStatusServer")
        self.host = host
        self.port = port
        self.logger = logger
        self.jsonTemplate = {
            "Command": "FORWARD_ELEV_INFO",
            "DeviceId": "C0002T",
            "ElevId": 1,
        }
        self.seqNo = 1
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        self.doConnect()
        while True:
            try:
                client, addr = self.server.accept()
                # self.recv_msg(client, addr)
                threading.Thread(target=self.send_msg, args=(client, addr)).start()
                threading.Thread(target=self.recv_msg, args=(client, addr)).start()
                print(threading.enumerate())
            except socket.error:
                traceback.print_exc()
                print('socket connect error, doing connect 2s host/port:{}/{}'.format(self.host, self.port))
                time.sleep(2)
            except Exception as e:
                print('other error occur:{}'.format(e))
                time.sleep(2)

    def doConnect(self):
        while True:
            try:
                # 防止socket server重启后端口被占用（socket.error: [Errno 98] Address already in use）
                self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.server.bind((self.host, self.port))
                self.server.listen(5)
                print('-----------------------------------------------------------')
                print("esWsServer host:{}/port:{} started listen...".format(self.host, self.port))
                print('-----------------------------------------------------------')
                break
            except Exception as e:
                time.sleep(1)
                print('start ws server error:{}'.format(str(e)))
                traceback.print_exc()

    def recv_msg(self, client, addr):
        try:
            # self.send_msg(client, addr)
            print('Accept new connection from {0}'.format(addr))
            while 1:
                data = client.recv(1024)
                msg = eval(data.decode("utf-8"))
                print('recv msg:', msg)
        except Exception as e:
            print('recv_msg:{}'.format(e))
            # client.close()

    def send_msg(self, client, addr):
        try:
            #while 1:
                #time.sleep(1)
            elevStatusDict = self.jsonTemplate.copy()
            msg2Elev = json.dumps(elevStatusDict).encode() + "\n".encode()
            client.sendto(msg2Elev, addr)
                #print('send msg to client:{}:{}'.format(addr, msg2Elev))
               #time.sleep(0.5)
        except Exception as e:
            print('send_msg:{}'.format(e))
            # client.close()

if __name__ == '__main__':
    es = ElevStatusWsServer('127.0.0.1', 8787).start()