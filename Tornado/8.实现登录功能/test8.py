# coding=utf-8

import tornado.web
import tornado.ioloop
import MySQLdb

class LoginHandler(tornado.web.RequestHandler):
    def initialize(self,conn):
        self.conn=conn
    def prepare(self):
        #判断当前请求方式
        if self.request.method=='POST':
            #获取请求参数
            self.uname=self.get_argument('uname')
            self.pwd= self.get_argument('pwd')    
        print('123')
    def get(self,*args,**kwargs):
        self.render('templates/login.html')
    def post(self,*args,**kwargs):
        cursor=self.conn.cursor()
        cursor.execute('select * form t_auser where uname="%s" and pwd="%s"'%(self.uname,self.pwd))
        user=cursor.fetchone()
        if user:
            self.write(u"登陆成功!")
        else:
            self.write(u"登陆失败!")
    def write_error(self,status_code,**kwargs):
        self.render('templates/error.html')
    def set_default_headers(self):
        self.set_header('Server','SXTServer/1.0')
        
settings={'debug':True}
dbconfig={
    'host':'127.0.0.1',
    'user':'root',
    'password':'123456',
    'db':'tornado20180830',
    'port':3306
}

app=tornado.web.Application([
    (r'^/login/$',LoginHandler,{'conn':MySQLdb.connect(**dbconfig)})
],**settings)

app.listen(9997)

tornado.ioloop.IOLoop.instance().start()
