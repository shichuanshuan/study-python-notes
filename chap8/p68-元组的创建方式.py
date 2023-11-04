# 第一种创建方式 使用()
t = ('Python', 'world', 98)
print('1 ', t)
print('2 ', type(t))

t2 = 'Python', 'world', 98  # 省略了小括号
print('3 ', t2)
print('4 ', type(t2))

t2 = ('Python',)  # 省略了小括号
print('5 ', t2)
print('6 ', type(t2))

# 第二种创建方式 使用内置函数 tuple()
t1 = tuple(('Python', 'world', 98))
print('7 ', t1)
print('8 ', type(t1))

# 空元组
t4=()
t5=tuple()
