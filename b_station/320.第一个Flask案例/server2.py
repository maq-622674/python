from flask import Flask

#创建Flask对象-Httpd WEB服务对象
#__name__可以是任意的小写字母,表示Flask应用对象名称
app = Flask(__name__)

#声明请求资源(动态的)
@app.route('/hi', methods=['GET', 'POST'])
def hi():
    #使用request请求对象,获取请求方法
    from flask import request
    # 获取平台参数:platform
    # 只支持Android手机访问
    platform = request.args.get('platform', 'pc')
    if platform.lower() != 'android':
        return """
            <h2>目前只支持Android设备</h2>
        """

    if request.method=='GET':
        return """
            <h1>用户登录页面</h1>
            <form action="/hi?platform=android" method="post">
                <input name="name" placeholder="用户名"><br>
                <input name="pwd" placeholder="口令"><br>
                <button>提交</button>
            </form>
        """
    else:
        #获取表单的参数
        name=request.form.get('name')
        pwd=request.form.get('pwd')

        if all((
            name.strip()=='disen',
            pwd.strip()=='987'
        )):
            return """
                <h2 style="color:blue;">登录成功</h2>
            """
        else:
            return """
                <h2 style="color:orange;">登录失败,<a href="/hi">重试</a></h2>
            """
#启动服务
app.run(host='localhost',port=5000)







