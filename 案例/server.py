import numpy as np
import datetime
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
 
from tornado.options import define, options
 
define("port", default=9998, help="run on the given port", type=int)
 
class sync_request(tornado.web.RequestHandler):
    def get_dict(self):
        id=np.random.randint(0,64,size=1)
        robotId=str(id)
        req_no=np.random.randint(0,10,size=1)
        request_No=str(req_no)
        rou_no=np.random.randint(0,20,size=1)
        route_No=str(rou_no)
        x=np.random.randint(0,200)
        y = np.random.randint(0, 100)
        coordinate={'x':x,'y':y}
        now_time = datetime.datetime.now()
        now_time_str=datetime.datetime.strftime(now_time,'%Y-%m-%d %H:%M:%S')
        new_time=now_time+datetime.timedelta(seconds=5)
        new_time_str=datetime.datetime.strftime(new_time,'%Y-%m-%d %H:%M:%S')
        sim_robot_time=now_time_str[11:19]
        real_robot_time = new_time_str[11:19]
        self.sync_inf={'RobotID':robotId,'Request_NO':request_No,'Route_NO':route_No,'Coordinate':coordinate,'Sim_Robot_Time'
        :sim_robot_time,'Real_Robot_Time':real_robot_time}
 
    def get(self):
        self.get_dict()
        self.write(self.sync_inf)
 
if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r"/sync_request", sync_request)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()