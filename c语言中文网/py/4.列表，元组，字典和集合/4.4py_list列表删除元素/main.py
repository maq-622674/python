#1.del根据索引值删除元素
lang = ["Python", "C++", "Java", "PHP", "Ruby", "MATLAB"]
#使用正数索引
del lang[2]
print(lang)
#使用负数索引
del lang[-2]
print(lang)

lang = ["Python", "C++", "Java", "PHP", "Ruby", "MATLAB"]
del lang[1: 4]
print(lang)
lang.extend(["SQL", "C#", "Go"])
del lang[-5: -2]
print(lang)

#2.pop()根据索引值删除元素
nums = [40, 36, 89, 2, 36, 100, 7]
nums.pop(3)
print(nums)
nums.pop()
print(nums)

#3.remove()根据元素值进行删除
nums = [40, 36, 89, 2, 36, 100, 7]
#第一次删除36
nums.remove(36)
print(nums)
#第二次删除36
nums.remove(36)
print(nums)
#删除78
if 78 in nums:
    nums.remove(78)
print(nums)

#4.clear()删除列表所有元素
url = list("http://c.biancheng.net/python/")
url.clear()
print(url)