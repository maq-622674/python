



# 定义两个必选参数的函数
def my_pow1(x, n):
    if not isinstance(x, (int, float)) or not isinstance(n, (int, float)):
        raise Exception("Input type error")
    result = 1
    for i in range(n):
        result *= x
    return result


print("3**5 = ", my_pow1(3, 5))
# 输出: 3**5 =  243
# print(my_pow1('A3', 5)) # raise error


# 定义一个必选参数和一个默认参数
def my_pow2(x, n=2):
    if not isinstance(x, (int, float)) or not isinstance(n, (int, float)):
        raise Exception("Input type error")
    result = 1
    for i in range(n):
        result *= x
    return result


print("3**2 = ", my_pow2(3))
# 输出: 3**2 =  9
print("3**5 = ", my_pow2(3, 5))
# 输出: 3**5 =  243


# 可变参数, 可变参数在函数调用时自动组装为一个tuple
# 可以直接传入, 也可以组装成一个list或tuple传入; 不管哪种形式, 最终都是以tuple形式传入
def my_product(*parameters):
    result = 1
    for p in parameters:
        result *= p
    return result


list_p = [1, 3, 5, 7]
tuple_p = (1, 3, 5, 7)
print(my_product(1, 3, 5, 7))  # 直接传入参数
# 输出: 105
print(my_product(*list_p))  # 传入list
# 输出: 105
print(my_product(*tuple_p))  # 传入tuple
# 输出: 105


# 关键字参数, 关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print("name:", name, "age:", age, "others:", kw)


person("Tom", 38, city="Beijing")
# 输出: name: Tom age: 38 others: {'city': 'Beijing'}
person("Tom", 38, city="Beijing", job="Engineer")
# 输出: name: Tom age: 38 others: {'city': 'Beijing', 'job': 'Engineer'}
# 也可以先组装出一个dict, 然后把该dict转换为关键字参数传进去
extra = {'city': 'Beijing', 'job': 'Engineer'}
person("Tom", 38, **extra)
# 输出: name: Tom age: 38 others: {'city': 'Beijing', 'job': 'Engineer'}


# 命名关键字参数, 例如, 只接收city和job作为关键字参数, 命名关键字参数可以有缺省值
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person2(name, age, *, city, job):
    print("name:", name, "age:", age, "city:", city, "job:", job)


person2("Tom", 38, city="Beijing", job="Engineer")
# 输出: name: Tom age: 38 city: Beijing job: Engineer
# person2("Tom", 38, city="Beijing") # 命名关键字参数后, 关键字参数接受不全会报错


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person3(name, age, *args, city, job):
    print("name:", name, "age:", age, "city:", city, "job:", job)


person3("Tom", 38, city="Beijing", job="Engineer")
# 输出: name: Tom age: 38 city: Beijing job: Engineer
person3("Tom", 38, "我是可变参数", city="Beijing", job="Engineer")
# 输出: name: Tom age: 38 city: Beijing job: Engineer

