#1.index()方法
nums = [40, 36, 89, 2, 36, 100, 7, -20.5, -999]
#检索列表中的所有元素
print(nums.index(2))
#检索3~7之间的元素
print(nums.index(100, 3, 7))
#检索4之后的元素
print(nums.index(7, 4))
#检索一个不存在的元素
if 55 in nums:
    print(nums.index(55))

#2.count()方法
nums = [40, 36, 89, 2, 36, 100, 7, -20.5, 36]
#统计元素出现的次数
print("36出现了%d次" % nums.count(36))
#判断一个元素是否存在
if nums.count(100):
    print("列表中存在100这个元素")
else:
    print("列表中不存在100这个元素")