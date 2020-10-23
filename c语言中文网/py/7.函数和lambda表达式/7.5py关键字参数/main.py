'''
目前为止，我们使用函数时所用的参数都是位置参数，即传入函数的实际参数必须与形式参数的数量和位置对应。而本节将介绍的关键字参数，则可以避免牢记参数位置的麻烦，令函数的调用和参数传递更加灵活方便。

关键字参数是指使用形式参数的名字来确定输入的参数值。通过此方式指定函数实参时，不再需要与形参的位置完全一致，只要将参数名写正确即可。
因此，Python 函数的参数名应该具有更好的语义，这样程序可以立刻明确传入函数的每个参数的含义。
'''
def dis_str(str1,str2):
    print("str1:",str1)
    print("str2:",str2)
#位置参数
dis_str("http://c.biancheng.net/python/","http://c.biancheng.net/shell/")
#关键字参数
dis_str("http://c.biancheng.net/python/",str2="http://c.biancheng.net/shell/")
dis_str(str2="http://c.biancheng.net/python/",str1="http://c.biancheng.net/shell/")