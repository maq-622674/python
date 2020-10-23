import tornado.escape
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.options
import time
import logging
import uuid
import sys,os
from tornado.options import define, options


define('port', default=9999, help="The tornado server port", type=int)


class WebSocketSever(tornado.websocket.WebSocketHandler):
    bao_cons = set()
    bao_waiters = {}
    global con_key
    def open(self):
        '''
        1.open()
        这个方法是在刚开始连接过来的时候会触发这个方法，我们可以在这个方法中去实现自己想在连接刚上线的时候需要做的事情。
        '''
        sole_id = str(uuid.uuid4()).upper()
        print(sole_id)
        self.con_key = sole_id
        self.bao_waiters["{}".format(sole_id)] = self
        self.bao_cons.add(self)
        self.write_message({"websocket_sole_id": sole_id})
        logging.info("websocket opened!")
        print(self.bao_cons)

    def on_message(self, message):
        '''
        3.这个方法是在接受到来自客户端的数据的时候触发的方法，在这个方法里面我们可以去实现对数据的判断从而调用对应的方法，去处理该做的事情。
        '''
        print(type(message))
        if message == "close":
            self.close()
            return
        try:
            parse_data = tornado.escape.json_decode(message)
            if parse_data["user"] and parse_data["content"]:
                user = parse_data["user"]
                content = parse_data["content"]
                if not user or not content:
                    logging.info("Date is wrong!")
                    return
                else:
                    for key in self.bao_waiters.keys():
                        if key == user:
                            try:
                                self.bao_waiters[key].write_message("{}".format(content))
                            except Exception as e:
                                logging.info(e)
                            finally:
                                logging.info("process finished!")
        except:
            for con in self.bao_cons:
                con.write_message(message)

    def check_origin(self, origin: str):
        return True

    def allow_draft76(self):
        return True

    def on_close(self):
        '''
        2.看名字就知道这个方法是在连接断掉的时候触发的方法，当然了，你也可以在这个方法里面去写在连接断开的时候需要做的事情。
        '''
        self.bao_cons.remove(self)
        self.bao_waiters.pop(self.con_key)

        logging.info("websocket closed!")
        print(self.bao_cons)


class Application(tornado.web.Application):
    def __init__(self, handlers, setting):
        super(Application, self).__init__(handlers, **setting)


def main():
    options.parse_command_line()
    handlers = [
        (r"/websocket", WebSocketSever)
    ]
    setting = dict(xsrf_cookies=False)
    app = Application(handlers, setting)
    print(options.port)
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
if __name__ == '__main__':
    main()