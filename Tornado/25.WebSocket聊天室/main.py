import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import os
import datetime
import time
import random

from tornado.web import RequestHandler
from tornado.options import define, options
from tornado.websocket import WebSocketHandler
import threading

define("port", default=9998, type=int)

class IndexHandler(RequestHandler):
    def get(self):
        self.render("index.html")

MSG=1

def loop():
    global MSG
    while True:
        MSG+=random.randint(0,9) 
        time.sleep(1)
        print(MSG)

t = threading.Thread(target=loop, name='LoopThread')



class ChatHandler(WebSocketHandler):
    cli = set()  # 用来存放在线用户的容器
    # def open(self):
    #     print(self.request)
    #     self.cli.add(self)  # 建立连接后添加用户到容器中
    #     for c in self.cli:  # 向已在线用户发送消息
    #         c.write_message(u"[%s]-[%s]-进入聊天室" % (self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # def on_message(self, message):
    #     for c in self.cli:  # 向在线用户广播消息
    #         c.write_message(u"[%s]-[%s]-说：%s" % (self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), message))

    # def on_close(self):
    #     self.cli.remove(self) # 用户关闭连接后从容器中移除用户
    #     for c in self.cli:
    #         c.write_message(u"[%s]-[%s]-离开聊天室" % (self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def open(self):
        print("self:",self)
        print("self.request",self.request)
        print("%s用户已上线"%(self)) 
        
        #time.sleep(1)
        #self.cli.add(self)
        # for c in self.cli:
        #     c.write_message()
    def msg(self):
            pass
    def on_message(self,message):
        while True:
            self.write_message(str(MSG))
        #self.write_message(MSG)
        # global MSG
        # MSG+=1
        # self.write_message(MSG)
        # for c in self.cli:#向在线用户广播数据
        #     c.write_message(self.("123"))
    def on_close(self):
        print("%s该用户已掉线"%(self))
        #self.cli.remove(self)          
    def check_origin(self, origin):
        return True  # 允许WebSocket的跨域请求


def thr():
    aaa=ChatHandler()
    bbb=aaa.open()
    t1=threading.Thread(target=bbb,name='ChatHandler')
    t1.start()
    
if __name__ == '__main__':
    tornado.options.parse_command_line()

    app = tornado.web.Application([
            (r"/", IndexHandler),
            (r"/chat", thr),
        ],
        static_path = os.path.join(os.path.dirname(__file__), "static"),
        template_path = os.path.join(os.path.dirname(__file__), "template"),
        debug = True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    t.start()    
    tornado.ioloop.IOLoop.current().start()
    