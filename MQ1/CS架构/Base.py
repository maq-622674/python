import time
import subprocess
import os
a=10
while True:
    a+=1
    print(a)
    time.sleep(1)
    if a==30:
        filename = r'G:\CSDN_L\python\MQ1\CS架构\update.bat'
        with open(filename, 'w') as file_object:
            file_object.write("TIMEOUT /T 5 /NOBREAK\n")
            file_object.write("C:/Users/jimuti/Desktop/MaQue/maque/MQ1/plug/7z.exe x G:/CSDN_L/python/MQ1/CS架构/Base.zip -y -oG:/CSDN_L/python/MQ1/CS架构/ -aoa\n")
            file_object.write("TIMEOUT /T 5 /NOBREAK\n")
            file_object.write("python G:/CSDN_L/python/MQ1/CS架构/Base.py\n")  
        p=subprocess.Popen("G:/CSDN_L/python/MQ1/CS架构/update.bat",shell=True)
        p.wait()
        os._exit(1)


    # import sys
    # import subprocess
    # dlurl="http://ls.jimuti.com:808/File/uploads/jimuti/MQ1.zip"
    # folder_tmp=fso.appfold("tmp")
    # fso.foldexist(folder_tmp)
    # dlres=sock.download(dlurl,"MQ1.zip",folder_tmp)
    # if not dlres:
    #     rejsl["result"]="false"
    #     rejsl["errmsg"]="MQ1.zip none"
    #     return   
    # filename = fso.appfold()+'/update.bat'
    # if fso.exist(filename):
    #     fso.del_path(filename)
    # with open(filename, 'w') as file_object:
    #     file_object.write("TIMEOUT /T 5 /NOBREAK\n")
    #     file_object.write("cmd /c"+fso.appfold()+'/plug/7z.exe'+' '+'x '+fso.appfold()+'/tmp/MQ1.zip'+' -y -o'+fso.appfold()+' -aoa'+'\n')
    #     file_object.write("TIMEOUT /T 5 /NOBREAK\n")
    #     file_object.write("python "+fso.appfold()+"/Base.py\n")  
    # p=subprocess.Popen(fso.appfold()+"/update.bat",shell=True)
    # p.wait()
    # os._exit(1)

filename = r'G:\CSDN_L\python\MQ1\CS架构\update.bat'
with open(filename, 'w') as file_object:
    file_object.write("TIMEOUT /T 5 /NOBREAK\n")
    file_object.write("python G:/CSDN_L/python/MQ1/CS架构/Base.py\n")  