import ast
import time
def str_json(data):
    user_dict = ast.literal_eval(data)
    #data=json.loads(data)
    return user_dict

with open('G:/CSDN_L/python/案例/国内高匿代理/log.txt','r+') as file:  
    while True:
         print(file.readlines())
            # content=file.readline()
            # if content:
            #     content=content.replace('\n','')
            #     data=str_json(content)                       
            
    time.sleep(0.5)
            