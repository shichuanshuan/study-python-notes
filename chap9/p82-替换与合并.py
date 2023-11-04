s = 'hello,Python'
# 第一个参数指定被替换的子串，第二个参数指定替换的字符串
print(s.replace('Python', 'Java'))

s1 = 'hello,Python,Python,Python'
print(s1.replace('Python', 'Java', 2))

# 将列表或元组中的字符串合并成一个字符串
lst = ['hello', 'java', 'Python']
print('|'.join(lst))
print(''.join(lst))

t = ('hello', 'Jave', 'Python')
print(''.join(t))

print('*'.join('Python'))


