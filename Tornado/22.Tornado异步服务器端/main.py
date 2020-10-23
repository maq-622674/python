# coding=utf-8

from tornado.web import RequestHandler,Application,gen
from tornado.ioloop import IOLoop

class IndexHandler(RequestHandler):
    @gen.coroutine
    def get(self,*args,**kwargs):
        self.write('hello')

app=Application([
    (r'^/$',IndexHandler)
])

app.listen(9994)

IOLoop.instance().start()