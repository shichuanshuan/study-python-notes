# 方法一 append() 在列表的末尾添加一个元素
lst = [10, 20, 30]
print('添加元素之前:', lst, id(lst))
lst.append(100)
print('添加元素之后:', lst, id(lst))

# 方法二 extend() 在列表的末尾至少添加一个元素
lst2 = ['hello', 'world']
lst.append(lst2)
print('='*30)
print(lst)

lst.extend(lst2)

# 方法三 insert() 在列表选择位置添加一个元素
lst.insert(1, 90)
print(lst)

# 方法四 切片 在列表任意位置添加至少一个元素
lst3 = [True, False, 'hello']
lst[1:] = lst3
print(lst)
