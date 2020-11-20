import time
import subprocess
import os
a=10
while True:
    a+=1
    print(a)
    time.sleep(1)
    if a==30:
        filename = r'C:\update.bat'
        with open(filename, 'w') as file_object:
            file_object.write("TIMEOUT /T 5 /NOBREAK\n")
            file_object.write("C:/Users/pluC/7z.exe x C:/CS架构/Base.zip -y -oC:/CS架构/ -aoa\n")
            file_object.write("TIMEOUT /T 5 /NOBREAK\n")
            file_object.write("python C:/CS架构/Base.py\n")  
        p=subprocess.Popen("C:/CS架构/update.bat",shell=True)
        p.wait()
        os._exit(1)


filename = r'C:\CS架构\update.bat'
with open(filename, 'w') as file_object:
    file_object.write("TIMEOUT /T 5 /NOBREAK\n")
    file_object.write("python C:/CS架构/Base.py\n")  