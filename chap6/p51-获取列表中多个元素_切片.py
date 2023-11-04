lst = [10, 20, 30, 40, 50, 60, 70, 80]
# print(lst[1:6:1], id(lst))

print('原列表:', id(lst))
lst2 = lst[1:6:1]
print('切的片段:', id(lst2))

#默认步长为 1
print(lst[1:6])
print(lst[1:6:])

print(lst[1:6:2])

print(lst[:6:2])

print(lst[1::2])

print('----------step 步长为负数的情况----------------')
print('原列表:', lst)
print(lst[::-1])

print(lst[7::-1])

print(lst[6::-2])


