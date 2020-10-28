from urllib import parse
import urllib.request
import json
def is_json(file):
    try:
        json.loads(file)
    except:
        return False
    return True
while True:
    jsl_id=input("请输入")
        
    # try:
    #     response= urllib.request.urlopen("https://www.daren007.com/huxiao/index.php?macid="+jsl_id)
        
        #print("查看 response 响应信息类型: ",type(response))
        # page = response.read()
        # page=page.decode('utf-8')
        # data=parse.unquote(page)
        # print("data:",data)
    url="http://www.daren007.com/huxiao/index.php?macid="
    try:
        response = urllib.request.urlopen(url+jsl_id, timeout=3)
        page = response.read()
        page=page.decode('utf-8')
        #print(page)
        print(is_json(page))
        data=parse.unquote(page)
        print(is_json(data))
        print("data:",data) 
    except:
        print("错误")

