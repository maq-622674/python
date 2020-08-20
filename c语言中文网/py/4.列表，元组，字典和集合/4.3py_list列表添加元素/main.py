#3种方法
language=["python","c++","java"]
birthday=[1991,1998,1995]
info=language+birthday

print("language=",language)
print("birthday=",birthday)
print("info=",info)

#第一种
#py append()方法添加元素
l=["python","c++","java"]
#追加元素
l.append('php')
print(l)
#追加元组，整个元组被当成一个元素
t=('javascript','c#','go')
l.append(t)
print(l)
#追加列表，整个列表也被当成一个元素
l.append(['ruby','sql'])
print(l)

#第二种
#py extend方法添加元素
#追加元素
l=['python','c++','java']
l.extend('c')
print(l)

#追加元组，元祖被拆分成多个元素
t=('javascript','c#','go')
l.extend(t)
print(l)

#追加列表，列表也被拆分成多个元素
l.extend(['Ruby', 'SQL'])
print(l)

#第三种
#py insert()方法插入元素
l = ['Python', 'C++', 'Java']
#插入元素
l.insert(1, 'C')
print(l)
#插入元组，整个元祖被当成一个元素
t = ('C#', 'Go')
l.insert(2, t)
print(l)
#插入列表，整个列表被当成一个元素
l.insert(3, ['Ruby', 'SQL'])
print(l)
#插入字符串，整个字符串被当成一个元素
l.insert(0, "http://c.biancheng.net")
print(l)