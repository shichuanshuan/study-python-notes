# split() 从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回值都是一个列表
# 以通过参数 sep 指定劈分字符串的劈分符
# 通过 maxsplit 指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独作为一部分

s = 'hello world Python'
lst = s.split()
print(lst)

s1 = 'hello|world|Python'
print(s1.split(sep='|'))
print(s1.split(sep='|', maxsplit=1))

print(s.rsplit())
print(s1.rsplit('|'))
print(s1.rsplit('|', maxsplit=1))