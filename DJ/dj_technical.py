
import builtwith
import ssl
import whois
'''
识别网站所用的技术
'''
a=builtwith.parse('http://www.jimuti.com/')
print(a)

ssl._create_default_https_context = ssl._create_unverified_context
a=builtwith.parse('https://www.jianshu.com/')
print(a)


whois.whois('baidu.com')
