import os
class Py_cmd():
    '''
    python调用CMD命令行
    '''    
    def __init__(self):
        pass        
    def cmd(self):
        '''
        '''      
        while True:
            data=input("请输入cmd命令:")
            a=os.system(data)
            print(a)
        
       
        
def main():
    # import builtwith
    # a=builtwith.parse('http://www.jimuti.com/')
    # print(a)
    p1=Py_cmd()
    p1.cmd()

if __name__ == "__main__":
    main()