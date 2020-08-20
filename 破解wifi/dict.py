#类
import os
import itertools as its
class Range(object):
    def __init__(self):
        self.current_address_1 = os.path.dirname(os.path.abspath(__file__))
        
    def text_create(self):

        #desktop_path = self.current_address_1  
        
        #full_path = desktop_path +'\\'+ name + '.txt'  # 也可以创建一个.doc的word文档
        #print(full_path)
        #file = open(full_path, 'w')
        # for item in self.zidian:
        #     print(item)
        #file.write("1")   
        #file.close()
           
     
       
        words="0123456789abcdefghijklmnopqrstuvwxyz"
        #生成密码本的位数，五位数，repeat=5
        r=its.product(words,repeat=6)
        #保存在文件中，追加
        dic=open("./password.txt","a")
        #i是元组
        for i in r:
            #jion空格链接
            dic.write("".join(i))
            dic.write("".join("\n"))
            print(i)
        dic.close()
        print("密码本已生成")
 
    

    def range_a(self):
        pass
        
    
def main():
  
    len=6
    p1=Range()
   # p1.range_a('zidian')
    p1.text_create()

if __name__ == "__main__":
    main()