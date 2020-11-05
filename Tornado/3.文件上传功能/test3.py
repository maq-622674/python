# coding=utf-8
import tornado.web
import tornado.ioloop
import time
import random

class UploadHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.set_header("Access-Control-Allow-Origin", "*") # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        cpu=random.randint(0,100)
        self.write({'result':'ok', 'cpu': cpu})
    def post(self,*args,**kwargs):
        #获取请求参数
        print("self:",self)
        print("self.request:",self.request)
        print("self.request.files:",self.request.files)
        print("self.request.files[\"img1\"]:",self.request.files["img1"])
        
        img1=self.request.files['img1']
        for img in img1:
            body=img.get('body','')
            content_type=img.get('content_type','')
            filename=img.get('filename','')
           
        '''
        这里需要手动创建files文件,后期修复
        '''
        #将图片存放至files目录中
        import os
        dir=os.path.join(os.getcwd(),'files',filename)

        with open(dir,'wb') as fw:
            fw.write(body)

        #将图片显示到浏览器页面中
        #设置响应头信息
        self.set_header('Content-Type',content_type)
        self.write(body)

        

app=tornado.web.Application([
    (r'/upload/',UploadHandler)
])

app.listen(9998)

tornado.ioloop.IOLoop.instance().start()















# def parse_icon(filePath, file):

#     print(file)
#     print(FOLDER_MAIN)
#     zong = FOLDER_MAIN.replace('\\', '/')
#     print(zong+"/img/icon_"+file+".bmp")
#     large, small = win32gui.ExtractIconEx(filePath, 0)
#     win32gui.DestroyIcon(small[0])
#     hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
#     hbmp = win32ui.CreateBitmap()
#     hbmp.CreateCompatibleBitmap(hdc, 32, 32)
#     hdc = hdc.CreateCompatibleDC()
#     hdc.SelectObject(hbmp)
#     hdc.DrawIcon((0, 0), large[0])
#     hbmp.SaveBitmapFile(hdc, zong+"/img/icon_"+file+".bmp")


# def parse_iconall():
#     path = FOLDER_MAIN+"/upload/"
#     folds = os.listdir(path)
#     for subfold in folds:
#         fpath = path + subfold
#         if os.path.isdir(fpath):
#             result = os.listdir(fpath)
#             print("result", result)
#             if result != '':
#                 for file in result:
#                     if file[-4:] == '.exe':
#                         parse_icon(fpath+"/"+file, file)