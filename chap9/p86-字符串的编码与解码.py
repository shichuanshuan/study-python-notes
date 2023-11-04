# 编码:将字符串转换为二进制数据 bytes
# 解码:将 bytes 类型的数据转换成字符串类型

s = '天上人间'

# 编码
print(s.encode(encoding='GBK')) # 在 GBK 这种编码格式中，一个中文占两个字节
print(s.encode(encoding='UTF-8')) # 在 UTF-8 这种编码格式中，一个中文占三个字节

# 解码
# bytes 代表就是一个二进制数据 (字节类型的数据)
byte = s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))

byte = s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))
