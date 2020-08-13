from django.shortcuts import render  # 导入reder方法

def test_html(request):
    a={} #创建空字典，模板必须以字典的形式进行传参
    a['name']='C语言中文网'
    a['course']=["Python","C","C++","Java"]
    a['b']={'name':'C语言中文网','address':'http://c.biancheng.net/'}
    a['test_hello']=test_hello
    a['class_obj']=Website()
    return render(request,'test_html.html',a)
def test_hello():
    return '欢迎来到C语言中文网'
class Website:
    def Web_name(self):
        return 'Hello，C语言中文网!'
    #Web_name.alters_data=True #不让Website()方法被模板调用
