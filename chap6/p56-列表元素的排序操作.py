lst = [20, 40, 10, 98, 54]
print('排序前', lst, id(lst))
# 默认按照升序排序
lst.sort()
print('排序后', lst, id(lst))

# 通过指定关键字参数，将列表中的元素进行降序排序
lst.sort(reverse=True) 
print('1. ', lst)

print('------------使用内置函数 sorted 对列表进行排序 将产生一个新的列表对象------------')
new_list = sorted(lst)
print('2. ', lst)
print('3. ', new_list)

# 指定关键字参数，实现列表元素的降序排序
desc_list = sorted(lst, reverse=True)
print('4. ', desc_list)


