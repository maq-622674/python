# 2. 正则表达式基础语法介绍
# 2.1 原子
# 原子是正则表达式中最基本的组成单位，每个正则表达式中至少包含一个原子。
# 常见的原子类型有：
# 普通字符作为原子 如：a b c 字母
# 非打印字符作为原子 如：\n \t
# 通用字符作为原子 如：\d \D \w \W \s \S
# 原子表 如：多个原子拼接在一起
# 非打印字符：
# 字符	描述
# \cx	匹配由x指明的控制字符。例如， \cM 匹配一个 Control-M 或回车符。
# x 的值必须为 A-Z 或 a-z 之一。否则，将 c 视为一个原义的 'c' 字符。
# \f	匹配一个换页符。等价于 \x0c 和 \cL。
# \n	匹配一个换行符。等价于 \x0a 和 \cJ。
# \r	匹配一个回车符。等价于 \x0d 和 \cM。
# \s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
# \S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
# \t	匹配一个制表符。等价于 \x09 和 \cI。
# \v	匹配一个垂直制表符。等价于 \x0b 和 \cK。
# 通用字符:
# 字符	描述
# \d	匹配一个数字字符。等价于[0-9]。
# \D	匹配一个非数字字符。等价于[^0-9]。
# \s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [\f\n\r\t\v]。
# \S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
# \w	匹配字母、数字、下划线。等价于'[A-Za-z0-9_]'。
# \W	匹配非字母、数字、下划线。等价于 '[^A-Za-z0-9_]'。
# 2.2 元字符
# 所谓的元字符，就是正则表达式中具有一些特殊含义的字符，比如重复N次前面的字符等。
# 元字符：
# 字符	描述
# .	匹配除 "\n" 之外的任何单个字符。
# 要匹配包括 '\n' 在内的任何字符，请使用像"(.¦\n)"的模式。
# [xyz]	字符集合。匹配所包含的任意一个字符。例如， '[abc]' 可以匹配 "plain" 中的 'a'。
# [^xyz]	负值字符集合。匹配未包含的任意字符。例如， '[^abc]' 可以匹配 "plain" 中的'p'、'l'、'i'、'n'。
# [a-z]	字符范围。匹配指定范围内的任意字符。
# 例如，'[a-z]' 可以匹配 'a' 到 'z' 范围内的任意小写字母字符。
# [^a-z]	负值字符范围。匹配任何不在指定范围内的任意字符。
# 例如，'[^a-z]' 可以匹配任何不在 'a' 到 'z'范围内的任意字符。
# *	匹配前面的子表达式零次或多次。例如，zo 能匹配 "z" 以及 "zoo"。 等价于{0,}。
# +	匹配前面的子表达式一次或多次。
# 例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。
# ?	匹配前面的子表达式零次或一次。例如，"do(es)?" 可以匹配 "do" 或 "does" 。? 等价于 {0,1}。
# {n}	n 是一个非负整数。匹配确定的 n 次。
# 例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。
# {n,}	n 是一个非负整数。至少匹配n 次。例如，'o{2,}' 不能匹配 "Bob" 中的 'o'，但能匹配 "foooood" 中的所有 o。'o{1,}' 等价于 'o+'。'o{0,}' 则等价于 'o*'。
# {n,m}	m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。例如，"o{1,3}" 将匹配 "fooooood" 中的前三个 o。'o{0,1}' 等价于 'o?'。请注意在逗号和两个数之间不能有空格。
# \	将下一个字符标记为一个特殊字符、或一个原义字符、或一个向后引用、或一个八进制转义符。例如，'n' 匹配字符 "n"。'\n' 匹配一个换行符。序列 '\' 匹配 "\" 而 "(" 则匹配 "("。
# ^	匹配输入字符串的开始位置。如果设置了 RegExp 对象的 Multiline 属性，^ 也匹配 '\n' 或 '\r' 之后的位置。
# $	匹配输入字符串的结束位置。如果设置了RegExp 对象的 Multiline 属性，$ 也匹配 '\n' 或 '\r' 之前的位置。
# ?	当该字符紧跟在任何一个其他限制符 (*, +, ?, {n}, {n,}, {n,m}) 后面时，匹配模式是非贪婪的。非贪婪模式尽可能少的匹配所搜索的字符串，而默认的贪婪模式则尽可能多的匹配所搜索的字符串。例如，对于字符串 "oooo"，'o+?' 将匹配单个 "o"，而 'o+' 将匹配所有 'o'。
# (pattern)	匹配 pattern 并获取这一匹配。所获取的匹配可以从产生的 Matches 集合得到，在VBScript 中使用 SubMatches 集合，在JScript 中则使用 $0…$9 属性。要匹配圆括号字符，请使用 '(' 或 ')'。
# (?:pattern)	匹配 pattern 但不获取匹配结果，也就是说这是一个非获取匹配，不进行存储供以后使用。这在使用 "或" 字符 (¦) 来组合一个模式的各个部分是很有用。例如， 'industr(?:y¦ies) 就是一个比'industry¦industries'更简略的表达式。
# x¦y	匹配 x 或 y。例如，'z¦food' 能匹配 "z" 或 "food"。'(z¦f)ood' 则匹配 "zood" 或 "food"。

import re

rst = re.rearch('',str)
# 2.3 模式修正符
# 所谓模式修正符，即可以在不改变正则表达式的情况下，通过模式修正符改变正则表达式的含义，从而实现一些匹配结果的调整等功能。
# 修饰符	描述
# re.I	使匹配对大小写不敏感
# re.L	做本地化识别（locale-aware）匹配
# re.M	多行匹配，影响 ^ 和 $
# re.S	使 . 匹配包括换行在内的所有字符
# re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
# 实例：

string = "Python"
pat = "pyt"
rst = re.search(pat,string,re.I) # 第三个参数
print(rst)

# 2.4 贪婪模式与懒惰模式
# 贪婪模式的核心点就是尽可能多的匹配，而懒惰模式的核心点就是尽可能少的匹配。
# .*? 的使用