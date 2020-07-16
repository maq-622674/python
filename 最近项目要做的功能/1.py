'''
#遇到的难题
#1.判断两个列表的内容 list
#2.判断两个字典的内容 dict
#3.
'''
import time



n=0
data=[]
data1=[]
while True:
    if(n==0):
        '''
        cli=devClass("debugdevice001",fso.appHome("pic"))
        arg=cli.getSchool() 
        for itm in arg["data"]["classInfo"]:
            rjs=cli.getStudents(cli.URL_CLASS,itm["classId"])   
            rjs=rjs["data"]["childs"]
        这里假装有多个动态的字典 例如d={"a":"1"}
        '''
        cli=devClass("debugdevice001",fso.appHome("pic"))
        arg=cli.getSchool() 
        for itm in arg["data"]["classInfo"]:
            rjs=cli.getStudents(cli.URL_CLASS,itm["classId"])   
            rjs=rjs["data"]["childs"]

            #1.把他加入到data里面
            data.append(rjs)   
        #2.第一次循环原样输出         
        print("第一次的数据为",data)
                       
        if(n>0):
            '''
            cli=devClass("debugdevice001",fso.appHome("pic"))
            arg=cli.getSchool()  
            for itm in arg["data"]["classInfo"]:
                rjs=cli.getStudents(cli.URL_CLASS,itm["classId"])   
                rjs=rjs["data"]["childs"]
            向服务器2~n次获取数据
            '''
            cli=devClass("debugdevice001",fso.appHome("pic"))
            arg=cli.getSchool()  
            for itm in arg["data"]["classInfo"]:
                rjs=cli.getStudents(cli.URL_CLASS,itm["classId"])   
                rjs=rjs["data"]["childs"]
                #加到新的列表里  
                data1.append(rjs)
            #和上一次的数据进行比较
            #如果一样原样输出
            if(data==data1):
                print("数据一样")
            else:
                #否则循环遍历这一次和上一次的数据
                #看哪个发生了变化
                for i,j in zip(data,data1):
                    if(i==j):
                        print("数据和上一次一样")
                    else:
                        print("更新前的数据",i)
                        print("更新后的数据",j)
            #比较完之后把上一次的数据覆盖到上上一次的数据上
            data=data1
            #再把上一次的数据置空
            data1=[]
    #3.等待服务器30秒
    time.sleep(30)
    #4.加一操作
    n=n+1


