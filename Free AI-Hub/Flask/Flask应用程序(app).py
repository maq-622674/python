
from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def apptest():
    return 'Hello World Test!'
 
if __name__ == '__main__':
    pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple/ 
    app.run('0.0.0.0',80)