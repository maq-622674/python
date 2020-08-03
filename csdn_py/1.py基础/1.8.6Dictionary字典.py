#!/usr/bin/python3

# 定义一个字典
dict = {'Name': 'Python', 'Age': 17, 'Class': 'First'}

# 输出子典中的信息
print ("dict['Name']: ", dict['Name']) #Python
print ("dict['Age']: ", dict['Age'])   #17

# 输出错误信息：KeyError: 'Alice'
#print ("dict['Alice']: ", dict['Alice'])


# 修改和添加内容
dict['Age'] = 18;              # 更新 Age
dict['School'] = "云课堂"      # 添加信息

# 删除信息
del dict['Name'] # 删除键 'Name'一个元素值
dict.clear()     # 清空字典
del dict         # 删除字典

print('*'*10)

############找出字典的所有键###############
a={
    'name':"123",
    'age':"234",
    'sex':"345",
}
for i in a:
    print(i)

#############键值遍历######################
for i,j in a.items():
    print("key=%s,value=%s"%(i,j))

