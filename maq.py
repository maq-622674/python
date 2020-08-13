a=[
    {"a":"val1","b":"val2"},
    {"a":"val1","b":"val2"},
    {"c":"val1","d":"val2"},
    {"e":"val1","f":"val2"},
    {"e":"val1","f":"val2"},
]
bbb=[]
max_bbb=[]
first=0
for i in range(len(a)):
    if(i==0):
        first=a[i]
    if(i>0):
        if(a[i]==first):
            print("1",first)
            print("2",a[i])
            bbb.append(first)
            bbb.append(a[i])
        else:
            pass
        first=a[i]
print(bbb)
max_bbb.append(bbb)     
print(max_bbb)
    #print(i) 
#1.循环第一次保存数据然后跳出循环
#2.循环第二次和第一次的数据进行比较
#2.1如果数据相等 则输出
#2.2如果数据不相等 什么也不干
#2.3清空第一次保存的数据
#2.4将第二次的数据赋给第一次的