import socket
import threading
import time
import traceback


class ElevClient(threading.Thread):

    def __init__(self, eClientId, host, port):
        threading.Thread.__init__(self, name="elevClient_" + eClientId)
        self.host = host
        self.port = port  # config.ZLAN_SERVER_PORT
        self.sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):

        self.doConnect()
        while True:
            try:
                self.recv_msg()
                self.send_msg()
            except OSError:
                traceback.print_exc()
                time.sleep(2)
                print('socket connect error, doing connect in 2s .... host/port:{}/{}'.format(self.host, self.port))
                self.sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.doConnect()
            except Exception as e:
                print('other error occur:{}'.format(e))
                traceback.print_exc()
                time.sleep(4)
                self.doConnect()

    def doConnect(self):
        while True:
            try:
                self.sck.connect((self.host, self.port))
                time.sleep(1)
                print('-----------------------------------------')
                print('client start connect to host/port:{}/{}'.format(self.host, self.port))
                print('-----------------------------------------')
                break
            except ConnectionRefusedError:
                print('socket server refused or not started, reconnect to server in 3s .... host/port:{}/{}'.format(
                    self.host, self.port))
                time.sleep(3)

            except Exception as e:
                traceback.print_exc()
                print('do connect error:{}'.format(str(e)))
                time.sleep(5)

    def send_msg(self):
        try:
            time.sleep(1)
            msg = str(time.time())
            self.sck.send(msg.encode())
            print('send msg:', msg)
        except Exception as e:
            print('send_msg:{}'.format(e))
            self.sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.doConnect()

    def recv_msg(self):
        try:
            data = self.sck.recv(1024)
            if data:
                print('recv data:{}'.format(data))
            else:
                print('data is none')
                time.sleep(1)
        except Exception as e:
            print('recv_msg:{}'.format(e))
            self.sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.doConnect()


if __name__ == '__main__':
    elevClient = ElevClient('1', '127.0.0.1', 8787).start()
    pass