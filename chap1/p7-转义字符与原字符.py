print('hello\nworld')
print()

print('hello\tworld')
print('helloooo\tworld')

print('hello\rworld') # world 将 hello 进行了覆盖

print('hello\bworld') #\b 是退一个格，将 o 退没了
print()

# 原子符，不希望字符串中的转义字符起作用，就是用原子符 就是在原子符之前加上r 或R
print(r'hello\nworld')

# 注意事项，最后一个字符不能是反斜杠
# print(r'hello\nworld\')
print(r'hello\nworld\\')

