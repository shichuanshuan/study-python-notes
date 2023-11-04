scores = {'sds':24, 'cky':23, 'three':3}

# 方式一 使用 []
print(scores['sds'])
# 元素不存在会报错
# print(scores['ssss'])

# 方式二 使用 get 方法
print(scores.get('sds'))
print(scores.get('ssss')) #None

# 99 是在查找 麻七 所对的 value 不存在时，提供的一个默认值
print(scores.get('麻七', 99))