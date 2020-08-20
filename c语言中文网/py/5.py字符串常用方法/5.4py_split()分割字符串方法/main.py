str="c语言中文网>>>c.biancheng.net"
print(str)
#1.采用默认分割符进行分割
list1=str.split()
print(list1)

#2.采用多个字符进行分割
list2=str.split('>>>')
print(list2)

#3.采用.号进行分割
list3=str.split('.')
print(list3)

#4.采用空格进行分割，并规定最多只能分割成4个子串
#不能用
list4 = str.split(' ',4)
print(list4)

#5.采用>字符进行分割
list5=str.split('>')
print(list5)

#需要注意的是，在未指定 sep 参数时，split() 方法默认采用空字符进行分割，但当字符串中有连续的空格或其他空字符时，都会被视为一个分隔符对字符串进行分割，例如：
#不能用
#包含3个连续的空格
str="c语言中文网>>>c.biancheng.net"
list6=str.split()
print(list6)