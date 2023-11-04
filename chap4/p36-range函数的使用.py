# ranage() 三种创建方式
# 优点是无论多少元素，占用内存空间是一样的，除非元素拿出来

# 1. 默认从 0 开始，默认步长为 1
r = range(10)
print(r)
print(list(r))  # 用于查看 range 对象中的整数序列

# 2. 给两个参数，指定了起始值和结束值，但不包括结束值，默认步长为 1
r = range(2, 10)
print(list(r))

# 3. 指定起始值、结束值和步长
r = range(1, 10, 2)
print(list(r))

# 判断指定的整数 在序列中是否存在
print(10 in r)
print(9 in r)

print(10 not in r)

