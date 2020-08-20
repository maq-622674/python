'''
find() 方法用于检索字符串中是否包含目标字符串，如果包含，则返回第一次出现该字符串的索引；反之，则返回 -1。

find() 方法的语法格式如下：

str.find(sub[,start[,end]])
此格式中各参数的含义如下：

    str：表示原字符串；
    sub：表示要检索的目标字符串；
    start：表示开始检索的起始位置。如果不指定，则默认从头开始检索；
    end：表示结束检索的结束位置。如果不指定，则默认一直检索到结尾。


【例 1】用 find() 方法检索 “c.biancheng.net” 中首次出现 “.” 的位置索引。 
'''
str="c.biancheeng.net"
print(str.find('.'))

#例2手动指定起始索引的位置
str="c.biancheng.net"
print(str.find('.',2))

#例3手动指定起始索引和结束索引的位置
print(str.find('.',2,-4))
'''
位于索引（2，-4）之间的字符串为“biancheng”，由于其不包含“.”，因此 find() 方法的返回值为 -1。

注意，Python 还提供了 rfind() 方法，与 find() 方法最大的不同在于，rfind() 是从字符串右边开始检索。例如： 
'''
print(str.rfind('.'))