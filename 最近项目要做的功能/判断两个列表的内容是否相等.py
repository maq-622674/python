'''
列表长度相等的时候
'''
data=['a','b','c']
data1=['a','b','c']

if(data==data1):
    print("data和data1两个列表内容相等")




data2=['a','b','c']
data3=['a','b','d']

if(data2==data3):
    print("data2和data3两个列表内容相等")
else:
    for i,j in zip(data,data1):
        
        print("data2的数据:",i)
        print("data3的数据:",j)






# data2=['a','b','c']
# data3=['a','b']

# if(data==data1):
#     print("data2和data3两个列表内容相等")
# else:
#     print("data2和data3两个列表内容相等")
#     for i,j