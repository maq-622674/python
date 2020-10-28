class classRequest:
    def __init__(self,method:str,ismobile:bool,url:str,remote_addr:str,environ:dict):
        self.METHOD = method
        self.IS_MOBILE = ismobile
        self.MOBILE_OS = "PC"
        self.CONTENT_TYPE = "text/plain"
        self.REMOTE_ADDR = "0.0.0.0"
        self.URL = ""
        self.DATA_GET = {}
        self.DATA_PORT = {}
        self.ENVIRON = environ

    def render(self,html_path:str,**args_key)->str:
        """
        """
        with open(html_path,"r",encoding="utf-8") as ff:
            rall=ff.read()
        for arg,vul in args_key.items():
            # {{args}}=vul
            print("替换",arg," => ",vul)
            rall=rall.replace(r"{{"+arg+r"}}",str(vul))
        return rall


class classWSGI:
    def __init__(self,ip:str,port):
        if ip=="":
            ip="0.0.0.0"
        self.BINDIP=ip
        #1.绑定的ip
        self.BINDPORT=int(port)
        #2.绑定的端口
        self.ROUTE_LIST = {
            "/url":callable
        }
        #3.路由列表
        self.ROUTE_LIST.clear()
        #4.清除
        self.ROUTE_FILE_LIST={
            "/File/url/*":"abs_path"
        }
        #5.路由文件列表
        self.ROUTE_FILE_LIST.clear()
        #6.清除
        self.SERVER_NAME = ""
        #7.服务器名字
        ######################################
        #8.请求重启程序
        self.REQ_RESTART = False
        #9.请求重启系统
        self.REQ_RESTARTSYS = False
        #10.请求传入ts时间戳参数，用户管理时需要进行传入
        self.REQ_TS = False
        # 特殊变量：客户端来源地址
        # 当本变量不为空，会在jsl添加一个键值对，键名为本变量的字符串，值为来源ip
        self.FROMIP = ""
        ######################################
        # API相关变量
        self.API_PAGE = "/API"
        #11.命令参数
        self.__cmd_list = {
            "ask":{
                "funpt": "<fun_obj>",
                "args": [],      # 必选项参数，不带-与:的参数作为必选参数，在调用接口的时候必须选择
                "optargs":[],    # 可选项参数，在添加参数的时候，前面带-则为可选项参数
                "help":{
                    "action":"all help","arg1":"help1"
                }
            }
        }    # 帮助文档，前面带:的参数为接口帮助文档，arg:则为指定的arg项添加帮助文档
        self.__cmd_list.clear()
        self.PLUG_API_PAGE="/PLUG_API"
        self.__plug_list = {
            "plug_name": {
                "ask": {
                    "funpt": "<fun_obj>",
                    "args": [],      # 必选项参数，不带-与:的参数作为必选参数，在调用接口的时候必须选择
                    "optargs":[],    # 可选项参数，在添加参数的时候，前面带-则为可选项参数
                    "help":{
                        "action":"all help",
                        "arg1":"help1"
                    }
                }
            }      # 帮助文档，前面带:的参数为接口帮助文档，arg:则为指定的arg项添加帮助文档
        }
        self.__plug_list.clear()

    def load_cmd(self,action:str,ptrfun:callable,*check_argus:str):
        """加载指定命令到指定函数，函数的参数格式固定。
        func (argu_jsl , return_jsl)
        return_jsl={"result":"false"}
        """
        args = []
        optargs= []
        helpjs={"action":"no help."}
        for itm in check_argus:
            if itm[:1]=="-":
                # 可选择参数
                optargs.append(itm.replace("-",""))
            elif ":" in itm:
                # 帮助文档
                spts=itm.split(":")
                if spts[0]!="":
                    helpjs[spts[0]]=spts[1]
                else:
                    helpjs["action"]=spts[1]
            else:
                # 必选参数
                args.append(itm)
        self.__cmd_list[action] = {"funpt": ptrfun, "args": args,"optargs":optargs,"help":helpjs}

    def load_plug(self, plug_name, plug_cmd, function_point, *check_argus):
        """
        加载插件级别命令，会多出 plug 参数，plug=plug_name ,action=plug_cmd
        当判定plug参数在url中时，不会把命令送到主线程命令进行判断
        """
        args = []
        optargs= []
        helpjs={"action":"no help."}
        for itm in check_argus:
            if itm[:1]=="-":
                # 可选择参数
                optargs.append(itm.replace("-",""))
            elif ":" in itm:
                # 帮助文档
                spts=itm.split(":")
                if spts[0]!="":
                    helpjs[spts[0]]=spts[1]
                else:
                    helpjs["action"]=spts[1]
            else:
                # 必选参数
                args.append(itm)
        if plug_name not in self.__plug_list:
            self.__plug_list[plug_name] = {}
        self.__plug_list[plug_name][plug_cmd] = {
            "funpt": function_point, 
            "args": args,
            "optargs":optargs,
            "help":helpjs}

    def load_pluglist(self, plug_name, plug_cmd, function_point, check_argus_list):
        """
        加载插件级别命令，会多出 plug 参数，plug=plug_name ,action=plug_cmd
        当判定plug参数在url中时，不会把命令送到主线程命令进行判断
        """
        args = []
        optargs= []
        helpjs={"action":"no help."}
        for itm in check_argus_list:
            if itm[:1]=="-":
                # 可选择参数
                optargs.append(itm.replace("-",""))
            elif ":" in itm:
                # 帮助文档
                spts=itm.split(":")
                if spts[0]!="":
                    helpjs[spts[0]]=spts[1]
                else:
                    helpjs["action"]=spts[1]
            else:
                # 必选参数
                args.append(itm)
        if plug_name not in self.__plug_list:
            self.__plug_list[plug_name] = {}
        self.__plug_list[plug_name][plug_cmd] = {
            "funpt": function_point, 
            "args": args,
            "optargs":optargs,
            "help":helpjs}

    def route(self,url:str,ptrfun:callable):
        """
        """
        if url[:1]!="/":
            url="/"+url
        self.ROUTE_LIST[url]=ptrfun

    def route_file(self,url:str,folder_path:str):
        """
        将指定的路径指向到某个静态文件夹，需要使用绝对路径
        不需要后缀带/，自动补前缀/
        """
        if url[:1]!="/":
            url="/"+url
        if not os.path.exists(folder_path):
            return
        self.ROUTE_FILE_LIST[url]=folder_path


    def __check_argu(self, jsf, argu_list)->str:
        """
        检查送入的字典是否包含指定的键，不存在则返回非空字符串
        """
        returnstr = ""
        for ar in argu_list:
            if ar not in jsf and ar[:1]!="-":
                returnstr = returnstr + "|" + ar
        return returnstr

    def __cmd_REQ_RESTART(self):
        """
        请求重启
        """
        thr=Thread(target=self.__thr_REQ_RESTART)
        thr.start()
        
    def __thr_REQ_RESTART(self):
        """
        线程：重启准备
        """
        time.sleep(2)
        from Core.Tool import run
        run.run_delay(3)
        os._exit(0)

    def __cmd_REQ_RESTARTSYS(self):
        """
        请求重启
        """
        thr=Thread(target=self.__thr_REQ_RESTART)
        thr.start()
        
    def __thr_REQ_RESTARTSYS(self):
        """
        线程：重启准备
        """
        time.sleep(2)
        os.popen("reboot -f")
        os._exit(0)


    def __file_process(self,environ,start_response):
        """
        文件处理函数，如果存在文件，则返回文件绝对路径
        如果不存在文件，则返回空字符串
        """
        # 静态文件路由
        requrl=environ["PATH_INFO"]
        # 查找文件
        fpath=""
        for furl,fold in self.ROUTE_FILE_LIST.items():
            if furl in requrl:
                chkpth=requrl.replace(furl,"")
                fil=fold + chkpth
                if os.path.exists(fil) and os.path.isfile(fil):
                    fpath=fil
        if fpath=="":
            return ""
        mime = requrl.split('.')[-1].lower()
        # application/octet-stream
        ftype=FILE_TYPE.get(mime,"application")
        m = [('content-type', ftype+'/'+mime),("Server",self.SERVER_NAME)]  
        start_response('200 OK', m)
        return fpath


    def __eventin_routing(self,environ,start_response):
        """总路由
        """
        
        reqpath=environ["PATH_INFO"]
        # if "action=time" not in environ["QUERY_STRING"]:
        #     print(">>>>>>>>>>>",reqpath)
        if reqpath==self.API_PAGE and "action=" in environ["QUERY_STRING"]:
            # API请求
            return self.__page_api(environ,start_response)
        elif (reqpath==self.PLUG_API_PAGE and 
                "plug="in environ["QUERY_STRING"] and 
                "action=" in environ["QUERY_STRING"]):
            return self.__page_plug(environ,start_response)
        elif reqpath not in self.ROUTE_LIST and "." not in reqpath:
            # 404页面
            return self.__page_404(reqpath,start_response)
        if "." in reqpath:
            # 静态文件路由
            return self.__page_file(reqpath,environ,start_response)
        # for k,v in environ.items():
        #     print(k,"  =>  ",v)
        return self.__page_html(reqpath,environ,start_response)

    def __load_data_get(self,getdata)->dict:
        """
        加载当前请求中的GET数据
        """
        rjs={}
        if getdata=="":
            return rjs
        getdatas=getdata.split("&")
        for itm in getdatas:
            kvs=itm.split("=",1)
            if len(kvs)==2 and kvs[0]!="":
                rjs[kvs[0]]=kvs[1]
        return rjs

    def __page_200_api(self,start_response,res_data:dict)->bytes:
        """
        """
        status = "200 OK"
        response_headers = [('Content-Type', 'application/json;charset=utf-8'),("Server",self.SERVER_NAME)]
        # response_headers = [('Content-Type', 'text/html;charset=utf-8'),("Server",self.SERVER_NAME)]
        start_response(status, response_headers)
        if "REQ_RESTART" in res_data:
            del res_data["REQ_RESTART"]
            self.__cmd_REQ_RESTART()
        return [json.dumps(res_data).encode()]
    

    def __page_404(self,pth,start_response)->str:
        status = "404 NoT FounD"
        response_headers = [('Content-Type', 'text/html'),("Server",self.SERVER_NAME)]
        start_response(status, response_headers)
        return [("<h1> Page Not Found : "+pth).encode()]

    def __page_api(self,env,start_response):
        """API请求处理函数
        """
        jsl=self.__load_data_get(env["QUERY_STRING"])
        returnstr = {"result": "false"}
        ok = "ok"
        if "action" not in jsl:
            return self.__page_404(env["PATH_INFO"],start_response)
        act = jsl["action"]
        returnstr["action"] = act
        ######[特殊指令]########
        if act == "apihelp" or act=="apihelplist":
            # 特殊参数，用于直接控制接口
            return self.__page_200_api(start_response,self.__apicmd_in(jsl))
        # elif act == "apiecho":
        #     # 特殊参数，用于强制打印当前调试窗口
        #     self.SHOWECHO=not self.SHOWECHO
        #     return {"result":"ok","echo":str(self.SHOWECHO).lower()}
        ########################
        for itm in self.__cmd_list:
            if itm == act:
                chkarg = self.__check_argu(jsl, self.__cmd_list[itm]["args"])
                if chkarg != "":
                    returnstr["errmsg"] = chkarg
                    return self.__page_200_api(start_response,returnstr)
                self.__cmd_list[itm]["funpt"](jsl, returnstr)
                if "result" not in returnstr:
                    returnstr["result"] = "false"
                else:
                    if returnstr["result"] == "true" or returnstr["result"] == True:
                        returnstr["result"] = ok
                return self.__page_200_api(start_response,returnstr)
        returnstr["errmsg"] = "unknow_action"
        return self.__page_200_api(start_response,returnstr)
    
    def __page_plug(self,env,start_response):
        """
        plug命令处理部分
        plug=plugname
        action=ctl_cmd
        """
        jsl=self.__load_data_get(env["QUERY_STRING"])
        returnstr = {"result": "false"}
        ok = "ok"
        plugname = jsl["plug"]
        returnstr["plug"] = plugname

        if plugname not in self.__plug_list:
            returnstr["errmsg"] = "unknow_plugname"
            return self.__page_200_api(start_response,returnstr)
        if "action" not in jsl:
            returnstr["errmsg"] = "no_plugaction"
            return self.__page_200_api(start_response,returnstr)
        act = jsl["action"]
        returnstr["action"] = act

        if act == "apihelp" or act=="apihelplist":
            # 特殊参数，用于直接控制接口
            return self.__page_200_api(start_response,self.__plugapicmd_in(jsl, plugname))
        ###############
        for itm in self.__plug_list[plugname]:
            if itm == act:
                chkarg = self.__check_argu(
                    jsl, self.__plug_list[plugname][itm]["args"])
                if chkarg != "":
                    returnstr["errmsg"] = chkarg
                    return self.__page_200_api(start_response,returnstr)
                self.__plug_list[plugname][itm]["funpt"](jsl, returnstr)
                if "result" not in returnstr:
                    returnstr["result"] = "false"
                else:
                    if returnstr["result"] == "true" or returnstr["result"] == True:
                        returnstr["result"] = ok
                return self.__page_200_api(start_response,returnstr)
        returnstr["errmsg"] = "unknow_plug_action"
        return self.__page_200_api(start_response,returnstr)

    def __apicmd_in(self, jsl):
        """
        """
        returnstr = {"result": "ok"}
        # cmd=jsl["apihelp"]
        # if cmd=="help":
        # 打印cmd的所有action
        lst=[]
        if jsl["action"]=="apihelp":
            for itm in self.__cmd_list:
                lst.append({itm: self.__cmd_list[itm]["args"]})
        elif jsl["action"]=="apihelplist":
            for itm in self.__cmd_list:
                lst.append({itm:{   "args":self.__cmd_list[itm]["args"],
                                    "optargs":self.__cmd_list[itm]["optargs"],
                                    "help":self.__cmd_list[itm]["help"]}})
        if len(lst) > 0:
            returnstr["list"] = lst
            # if jsl["action"]=="apihelplist":
            #     self.__print_help(lst)
        return returnstr
        
    def __plugapicmd_in(self, jsl, plugname):
        """
        """
        returnstr = {"result": "ok"}
        # cmd=jsl["apihelp"]
        # if cmd=="help":
        # 打印cmd的所有action
        lst = []
        if plugname not in self.__plug_list:
            returnstr["result"] = "false"
            returnstr["errmsg"] = "unknow plugname"
            return returnstr
        
        if jsl["action"]=="apihelp":
            for itm in self.__plug_list[plugname]:
                lst.append({itm: self.__plug_list[plugname][itm]["args"]})
        elif jsl["action"]=="apihelplist":
            for itm in self.__plug_list[plugname]:
                lst.append({itm:{   "args":self.__plug_list[plugname][itm]["args"],
                                    "optargs":self.__plug_list[plugname][itm]["optargs"],
                                    "help":self.__plug_list[plugname][itm]["help"]}})
        if len(lst) > 0:
            returnstr["list"] = lst
            # if jsl["action"]=="apihelplist":
            #     self.__print_help(lst)
        return returnstr

    def __page_html(self,reqpth,environ,start_response):
        """正常网页处理函数

        """
        req=classRequest(environ["REQUEST_METHOD"],False,reqpth,environ["REMOTE_ADDR"],environ)
        for itm in filter_mobile:
            if itm in environ["HTTP_USER_AGENT"]:
                req.IS_MOBILE=True
                req.MOBILE_OS = itm
                break
        req.URL = reqpth
        req.DATA_GET = self.__load_data_get(environ["QUERY_STRING"])
        length=environ.get('CONTENT_LENGTH', '0')
        if length=="":
            length = 0
        else:
            length= int(length)
        # if length!=0:
        #     body= environ['wsgi.input'].read(length)
            # req.load_date_post(body)
        # 开始执行路由函数
        res_data=self.ROUTE_LIST[reqpth](req)
        if res_data==None:
            res_data="<h1>no data</h1>"
        status = "200 OK"
        response_headers = [('Content-Type', 'text/html;charset=utf-8'),("Server",self.SERVER_NAME)]
        start_response(status, response_headers)
        return [res_data.encode()]

    def __page_file(self,pth:str,env,start_response):
        """静态文件处理

        直接返回本函数执行结果即可
        """
        # 静态文件路由
        file_path=self.__file_process(env,start_response)
        if file_path=="":
            # 404页面
            return self.__page_404(pth,start_response)
        image = open(file_path, "rb") 
        if 'wsgi.file_wrapper' in env: 
            return env['wsgi.file_wrapper'](image, 1024) 
        else: 
            return iter(lambda: image.read(1024), '')

    def start(self):
        """
        """
        server = make_server('0.0.0.0', self.BINDPORT, self.__eventin_routing)
        print("WSGI HTTP SERVER on port ",self.BINDPORT,"...")
        server.serve_forever()

PORT_WEB=9987
JWS=classWSGI("",80)
def init_web():
    global JWS
    JWS=classWSGI("",PORT_WEB)
    #JWS.route("/",page_index)
    #JWS.route_file("/files",page_upload)
    JWS.load_cmd

