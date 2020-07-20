#需要自己找密码字典放入password里面
import zipfile

zfile = zipfile.ZipFile("C:\\Users\\jimuti\\Desktop\\python\\80个Python练手项目列表\\12.Python实现Zip文件的暴力破解\\index.zip")

passFile=open('C:\\Users\\jimuti\\Desktop\\python\\80个Python练手项目列表\\12.Python实现Zip文件的暴力破解\\password.txt') #读取你设定的密码文件

for line in passFile.readlines():

  try:

    password = line.strip('\n')

    zfile.extractall(path='C:\\Users\\jimuti\\Desktop\\python\\80个Python练手项目列表\\12.Python实现Zip文件的暴力破解\\', members=zfile.namelist(), pwd=password.encode('utf-8'))

    break

  except:

    print("又错了")
