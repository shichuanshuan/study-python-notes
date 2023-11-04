scores = {'张三':100, '李四':98, '王五':45}

# 获取所有的 key
keys = scores.keys()
print('1 ', keys)
print('2 ', type(keys))
print('3 ', list(keys)) # 将所有的 key 组成的视图转成列表

# 获取所有的 value
values = scores.values()
print('4 ', values)
print('5 ', type(values))
print('6 ', list(values))

# 获取所有的 key-value 对
items = scores.items()
print('7 ', items)
print('8 ', list(items)) # 转换之后的列表元素是由元组组成的



