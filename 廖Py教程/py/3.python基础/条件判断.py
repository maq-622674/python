age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

'''
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
'''
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

x=True 
#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
# if x:
#     print('True')

# birth = input('birth: ')
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')
#这是因为input()返回的数据类型是str，str不能直接和整数比较，
# 必须先把str转换成整数。Python提供了int()函数来完成这件事情：

s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

#原来int()函数发现一个字符串并不是合法的数字时就会报错，程序就退出了。

while(True):
    a=float(input('请输入你的身高以cm为单位 如1.75     '))
    b=float(input('请输入体重kg 如80.5       '))
    bmi=b/(a*a)
    if bmi<18.5:
        print("您目前BMI指数为%d,体重偏轻，请注意饮食"%bmi)
    elif bmi<25:
        print("您目前BMI指数为%d,体重偏正常,注意保持"%bmi)
    elif bmi<28:
        print("您目前BMI指数为%d,体重过重，请加强锻炼"%bmi)
    elif bmi<32:
        print("您目前BMI指数为%d,体重肥胖，多注意户外运动，肥胖会带来各种疾病"%bmi)
    else:
        print("您目前BMI指数为%d,体重严重肥胖，身体是革命的本钱，再不锻炼身体，命不久矣"%bmi)

