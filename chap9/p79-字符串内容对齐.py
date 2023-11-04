s = 'hello,Python'

# center() 居中对齐，第一个参数指定宽度，第二个参数指定填充符
# 居中对齐
print(s.center(20, '*'))
print()

# ljust()
# 左对齐
print(s.ljust(20, '*'))
print(s.ljust(10))
print(s.ljust(20))
print()

# rjust()
# 右对齐
print(s.rjust(20, '*'))
print(s.rjust(10))
print(s.rjust(20))
print()

# zfill() 右对齐，左边用 0 填充，该方法只接受一个参数，用于指定字符串的宽度，如果指定的宽度小于等于字符串的长度，返回字符串本身
print(s.zfill(20))
print(s.zfill(10))
print('-8910'.zfill(8))



