# key 的判断
scores = {'张三':100, '李四':98, '王五':45}
print('张三' in scores)
print('张三' not in scores)

# 删除指定的 key-value 对
del scores['张三']

# 清空字典的元素
# scores.clear()
print(scores)

# 新增元素
scores['sds'] = 24
print(scores)


# 修改元素
scores['sds'] = 23
print(scores)
