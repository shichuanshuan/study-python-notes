s = {10, 20, 30, 40, 50}

# 集合元素的判断操作
print(10 in s)
print(10 not in s)

# 集合元素的新增操作
# add 一次添加一个元素
s.add(80)
print('1 ', s)

# update 一次至少添加一个元素
s.update({100, 400, 300})
print('2 ', s)

s.update([100, 99, 8])
s.update([78, 64, 56])
print('3 ', s)


# 集合元素的删除操作
# remove 删除操作，集合中没有的元素会报错，而使用 discard 不会报错
s.remove(100)
print('4 ', s)

s.discard(500)
s.discard(300)
print('5 ', s)

# pop 随机删除一个元素，不能指定参数
s.pop()
print('6 ', s)

s.clear()
print('7 ', s)
