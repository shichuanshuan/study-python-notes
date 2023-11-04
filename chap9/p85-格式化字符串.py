# 1. % 占位符
name = '石大栓'
age = 18
print('我叫%s 今年%d岁' % (name, age))

# 2. {}
print('我叫{0} 今年{1}岁'.format(name, age))

# 3. f-string
print(f'我叫{name} 今年{age}岁')


# 精度
print('%10d' % 99)
print('%.3f' % 3.1415926)

print('%10.3f' % 3.1415926) # 一共总宽度 10 小数点后 3 位

print('{0:.3}'.format(3.1415926)) # .3 表示一共是 3 位数

print('{:.3f}'.format(3.1415926)) # .3f 表示是3位小数

print('{:10.3f}'.format(3.1415926))



