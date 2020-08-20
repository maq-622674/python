url = 'http://c.biancheng.net/python/'
#获取索引为10的字符
print(url[10])
#获取索引为 6 的字符
print(url[-6])

url = 'http://c.biancheng.net/java/'
#获取索引从3处22（不包含22）的子串
print(url[7: 22]) # 输出 zy
#获取索引从7处到-6的子串
print(url[7: -6]) # 输出 zyit.org is very
#获取索引从-7到6的子串
print(url[-21: -6])
#从索引3开始，每隔4个字符取出一个字符，直到索引22为止
print(url[3: 22: 4])

url = 'http://c.biancheng.net/java/'
#获取从索引7开始，直到末尾的子串
print(url[7: ])
#获取从索引-21开始，直到末尾的子串
print(url[-21: ])
#从开头截取字符串，直到索引22为止
print(url[: 22])
#每隔3个字符取出一个字符
print(url[:: 3])