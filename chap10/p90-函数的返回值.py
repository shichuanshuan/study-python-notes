def fun(num):
    odd = []
    even = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even

# 函数的调用
lst = [10, 29, 34, 33, 44, 53, 55]
print(fun(lst))

# 函数的返回值
# 1. 如果函数没有返回值 【函数执行完毕之后，不需要给调用出提供数据】 return 可以省略不写
# 2. 函数的返回值，如果是 1 个， 直接返回本身类型
# 3. 函数的返回值，如果是多个，返回的结果为元组

