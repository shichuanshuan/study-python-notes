# 可以输出数字
print(520)
print(3.14)

#可以输出字符串
print('hello world')
print("hello world")

# 可以输出表达式
print(3+4)

# 将数据输出文件中
fp = open('./text.txt', 'wb')
print('hello world', file=fp)
fp.close

# 不进行换行输出（输出内容在一行当中）
print('hello', 'world', 'Python')
