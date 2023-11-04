s = 'hello,python'

# isidentifier() 判断指定的字符串是不是合法的标识符
print('1.', s.isidentifier()) # False
print('2.', 'hello'.isidentifier()) # True
print('3.', '石大栓_'.isidentifier()) # True
print('4.', '石大栓_123'.isidentifier()) # True


# isspace() 判断指定的字符串是否全部由空白字符组成 回车、换行、水平制表符
print('5.', '\t'.isspace()) # True

# isalpha() 判断指定的字符串是否全部由字母组成
print('6.', 'abc'.isalpha()) # True
print('7.', '石大栓'.isalpha()) # True
print('8.', '石大栓1'.isalpha()) # False

# isdecimal() 判断指定字符串是否全部由十进制的数字组成
print('9.', '123'.isdecimal()) 
print('10.', '123四'.isdecimal())

# isnumeric() 判断指定的字符串是否全部由数字组成
print('11.', '123'.isnumeric())
print('12.', '123四'.isnumeric())


# isalnum() 判读指定字符串是否全部由字母和数字组成
print('13.', 'abc1'.isalnum())
print('14.', '四123'.isalnum())
