# remove 一次删除一个元素，重复元素只删除第一个 元素不存在报错
lst = [10, 20, 30, 40, 50, 60, 30]
lst.remove(30)
print('1. ',lst)

# pop 删除一个指定索引位置上的元素，指定不存在报错 不指定索引，删除列表中最后一个元素
lst.pop(2)
print('2. ',lst)

lst.pop()
print('3.', lst)

# 切片 一次至少删除一个元素
new_list = lst[1:3]
print('4. 原列表', lst)
print('5. 切片后的列表', new_list)

# 不产生新的列表对象，而是删除原列表中的内容
lst[1:3] = []
print('6. ', lst)

# clear 清空列表
lst.clear()
print('7. ', lst)

# del 删除列表
del lst
# print('8. ',lst)


