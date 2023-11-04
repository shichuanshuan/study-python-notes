s = 'hello,Python'
s1 = s[:5]
s2 = s[6:]
s3 = '!'
newstr = s1 + s2 + s3

print(s1)
print(s2)
print(newstr)
print('----------------------')
print(id(s1))
print(id(s2))
print(id(newstr))