#需要自己找密码字典放入password里面

import zipfile

#你要破解的.zip文件
a=""
#破解完放在哪里
b=""
#密码字典
c=""


zfile = zipfile.ZipFile(a)
passFile=open(c) #读取你设定的密码文件
for line in passFile.readlines():
  try:
    password = line.strip('\n')
    zfile.extractall(path=b, members=zfile.namelist(), pwd=password.encode('utf-8'))
    break
  except:
    print("又错了")
