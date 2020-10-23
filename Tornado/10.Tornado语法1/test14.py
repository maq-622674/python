from tornado.web import RequestHandler,Application
from tornado.ioloop import IOLoop
import os

class IndexHandler(RequestHandler):
    def get(self,*args,**kwargs):
        self.render('index.html',uname='render渲染方式',PWD='什么的什么')

app=Application([
    (r'^/$',IndexHandler)
],templates_path=os.path.join(os.getcwd(),'templates'))

app.listen(9995)

IOLoop.instance().start()