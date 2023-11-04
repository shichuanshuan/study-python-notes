# python 的驻留机制对相同的字符串只保留一份拷贝、
# 后续创建相同字符串是，不会开辟新空间，
# 而是把该字符串的地址赋给新创建的变量
a = 'Python'
b = 'Python'
c = 'Python'
print(a, id(a))
print(b, id(b))
print(c, id(c))
print()

# 驻留机制的几种情况 (交互模式)
# 字符串的长度为 0 或 1 时
s1 = ''
s2 = ''
print(s1 is s2)

s1 = '%'
s2 = '%'
print(s1 is s2)

# 符合标识符的字符串
s1 = 'abc%'
s2 = 'abc%'
print(s1 == s2)
print(s1 is s2)

# 字符串只在编译时进行驻留，而非运行时
# [-5, 256] 之间的整数数字