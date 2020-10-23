import os
def jiance(wenjian):
    pipbao=os.popen("pip install -r requirements.txt")
    print("pipbao:",pipbao)
    # if "package" not in pipbao:
    #     pass
    # print("文件",wenjian)
   #wenjian=wenjian.replace("\\","/")
    
def main():
    wenjian=os.path.abspath(os.path.dirname(__file__))
    jiance(wenjian)
if __name__ == "__main__":
    main()