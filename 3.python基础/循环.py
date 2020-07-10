#循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

#range()生成整数序列
a=list(range(5))
print(a)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

#比如我们要计算100以内所有奇数之和，
# 可以用while循环实现：
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L=['Bart','Lisa','Adam']
for i in L:
    print("Hello,%s"%i)

#break
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

#continue
n = 0
while n < 10:
    n = n + 1
    print(n)

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

#小结
#循环是让计算机做重复任务的有效的方法。
#break语句可以在循环过程中直接退出循环，
#而continue语句可以提前结束本轮循环，
#并直接开始下一轮循环。这两个语句通常都必须配合if
#语句使用。
#要特别注意，不要滥用break和continue语句。
#break和continue会造成代码执行逻辑分叉过多，
# 容易出错。大多数循环并不需要用到break和
# continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，
# 去掉break和continue语句。
#有些时候，如果代码写得有问题，
# 会让程序陷入“死循环”，也就是永远循环下去。
# 这时可以用Ctrl+C退出程序，或者强制结束Python进程。

#请试写一个死循环程序。

