# 集合特点
# 无序、可变序列
# 元素不允许重复

# 第一种创建方式
# s = {2, 3, 4, 5, 5, 6, 7, 7}
s = {2, 3, 4, 5, 6, 7}
print(s)

# 第二种创建方式
s1 = set(range(6))
print('1 ', s1, type(s1))

s2 = set([1, 2, 3, 5, 5, 6, 6])
print('2 ', s2, type(s2))

s3 = set((1, 2, 4, 4, 5, 65)) # 集合中的元素是无序的
print('3 ', s3, type(s3))

s4 = set('python')
print('4 ', s4, type(s4))

s5 = set({12, 4, 34, 55, 66, 44, 4})
print('5 ', s5, type(s5))

s6 = {} # dict 字典类型
print(type(s6))

# 定义一个空集合
s7 = set()
print(type(s7))
