def calc(a, b):
    c = a + b
    return c

# 位置实参
result = calc(10, 20)
print(result)


# 关键字实参
res = calc(a = 20, b = 10)
print(res)
