num_a = int(input('input first num '))
num_b = int(input('input second num '))
# 
# if num_a >= num_b:
#     print(num_a, '大于等于', num_b)
# else:
#     print(num_a, '小于', num_b)

print('使用条件表达式进入比较')
# 条件为真，执行前面一个，否则执行后面一个
print(str(num_a) + '大于等于' + str(num_b)   if num_a >= num_b else    str(num_a) + '小于' + str(num_b))

