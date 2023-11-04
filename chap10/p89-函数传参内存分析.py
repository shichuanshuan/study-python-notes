def fun(arg1, arg2):
    print('arg1 = ', arg1)
    print('arg2 = ', arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1 = ', arg1)
    print('arg2 = ', arg2)

# 在函数调用过程中，进行参数的传递

# 如果不可变对象，在函数体的修改不会影响实参的值 arg1 的修改为 100， 不会影响 n1 的值
# 如果是可变对象，在函数体的修改会影响到实参的值 arg2 的修改 append(10) ，会影响到 n2 的值
n1 = 11
n2 = [22, 33, 44]
fun(n1, n2)

print('n1 ', n1)
print('n2 ', n2)
