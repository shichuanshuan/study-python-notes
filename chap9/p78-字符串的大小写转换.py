s = 'hello,python'

# upper() 把字符串中所有字符都转成大写字母
# 转大写后，会产生一个新的字符串对象
a = s.upper()
print(a, id(a))
print(s, id(s))

# lower() 把字符串中所有字符都转成小写字母
print(s.lower(), id(s.lower()))
print(s, id(s))

# swapcase() 把字符串中所有大写字母转成小写字母，把所有小写字符转成大写字母
s2 = 'hello,Python'
print(s2.swapcase())

# capitalize() 把第一个字符转换为大写，把其余字符转换为小写
print(s2.capitalize())

# title() 把每个单词的第一个字符转换为大写，把每个单词的剩余字符转换为小写
print(s2.title())
