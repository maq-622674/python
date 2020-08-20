'''
join() 方法也是非常重要的字符串方法，它是 split() 方法的逆方法，用来将列表（或元组）中包含的多个字符串连接成一个字符串。

想详细了解 split() 方法的读者，可阅读《Python split()方法》一节。
使用 join() 方法合并字符串时，它会将列表（或元组）中多个字符串采用固定的分隔符连接在一起。例如，字符串“c.biancheng.net”就可以看做是通过分隔符“.”将 ['c','biancheng','net'] 列表合并为一个字符串的结果。

join() 方法的语法格式如下：

newstr = str.join(iterable)
此方法中各参数的含义如下：

    newstr：表示合并后生成的新字符串；
    str：用于指定合并时的分隔符；
    iterable：做合并操作的源字符串数据，允许以列表、元组等形式提供。

'''
list=['c','biancheng','net']
print('.'.join(list))
dir = '','usr','bin','env'
print(type(dir))
print('/'.join(dir))