#一.py创建字典
#1.使用{}创建字典
#使用字符串作为key
scores = {'数学': 95, '英语': 92, '语文': 84}
print(scores)
#使用元组和数字作为key
dict1 = {(20, 30): 'great', 30: [1,2,3]}
print(dict1)
#创建空元组
dict2 = {}
print(dict2)

#2.通过fromkeys()方法创建字典
knowledge = ['语文', '数学', '英语']
scores = dict.fromkeys(knowledge,60)
print(scores)

#3.通过dict()映射函数创建字典
# 创建空的字典
d = dict()
print(d)

#二.py访问字典
tup = (['two',26], ['one',88], ['three',100], ['four',-59])
dic = dict(tup)
print(dic)

dict1={'name':'Lara','age':18}
#判断键在不在字典中
for one in dict1:
   if 'name' in dict1:#或dict1.keys()
       print('key在字典中！')
       break
#判断值在不在字典中
for one in dict1:
   if 'Lara' in dict1.values():
       print('value在字典中！')
       break
# 除了上面这种方式外，Python 更推荐使用 dict 类型提供的 get() 方法来获取指定键对应的值。当指定的键不存在时，get() 方法不会抛出异常。
# get() 方法的语法格式为：
# dictname.get(key[,default])
# 其中，dictname 表示字典变量的名字；key 表示指定的键；default 用于指定要查询的键不存在时，此方法返回的默认值，如果不手动指定，会返回 None。
a = dict(two=0.65, one=88, three=100, four=-59)
print(a.get('one'))
a = dict(two=0.65, one=88, three=100, four=-59)
print(a.get('five', '该键不存在'))

# 三.py删除字典
a = dict(two=0.65, one=88, three=100, four=-59)
print(a)
del a


