#一.py创建set集合
#1.使用{}创建
a = {1,'c',1,(1,2,3),'c'}
print(a)

#2.set()函数创建集合
set1 = set("c.biancheng.net")
set2 = set([1,2,3,4,5])
set3 = set((1,2,3,4,5))
print("set1:",set1)
print("set2:",set2)
print("set3:",set3)

#二.py访问set集合元素
a = {1,'c',1,(1,2,3),'c'}
for ele in a:
    print(ele,end=' ')
#三.py删除set集合
print('\n'+'*'*10)
a = {1,'c',1,(1,2,3),'c'}
print(a)
del(a)
