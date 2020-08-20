print(dir(dict))
#1.keys(),values()和items()方法
# 将这三个方法放在一起介绍，是因为它们都用来获取字典中的特定数据：
# keys() 方法用于返回字典中的所有键（key）；
# values() 方法用于返回字典中所有键对应的值（value）；
# items() 用于返回字典中所有的键值对（key-value）。
scores = {'数学': 95, '语文': 89, '英语': 90}
print(scores.keys())
print(scores.values())
print(scores.items())
a = {'数学': 95, '语文': 89, '英语': 90}
b = list(a.keys())
print(b)
a = {'数学': 95, '语文': 89, '英语': 90}
for k in a.keys():
    print(k,end=' ')
print("\n---------------")
for v in a.values():
    print(v,end=' ')
print("\n---------------")
for k,v in a.items():
    print("key:",k," value:",v)

#2.copy()方法
a = {'one': 1, 'two': 2, 'three': [1,2,3]}
b = a.copy()
print(b)
print('*'*10)
a = {'one': 1, 'two': 2, 'three': [1,2,3]}
b = a.copy()
#向 a 中添加新键值对，由于b已经提前将 a 所有键值对都深拷贝过来，因此 a 添加新键值对，不会影响 b。
a['four']=100
print(a)
print(b)
#由于 b 和 a 共享[1,2,3]（浅拷贝），因此移除 a 中列表中的元素，也会影响 b。
a['three'].remove(1)

print(a)
print(b)

#3.update()方法
a = {'one': 1, 'two': 2, 'three': 3}
a.update({'one':4.5, 'four': 9.3})
print(a)

#4.pop()和popitem()方法
a = {'数学': 95, '语文': 89, '英语': 90, '化学': 83, '生物': 98, '物理': 89}
print(a)
a.pop('化学')
print(a)
# 对 popitem() 的说明
#其实，说 popitem() 随机删除字典中的一个键值对是不准确的，虽然字典是一种无须的列表，但键值对在底层也是有存储顺序的，popitem() 总是弹出底层中的最后一个 key-value，这和列表的 pop() 方法类似，都实现了数据结构中“出栈”的操作。
a.popitem()
print(a)

#5.setdefault()方法
a = {'数学': 95, '语文': 89, '英语': 90}
print(a)
#key不存在，指定默认值
a.setdefault('物理', 94)
print(a)
#key不存在，不指定默认值
a.setdefault('化学')
print(a)
#key存在，指定默认值
a.setdefault('数学', 100)
print(a)
