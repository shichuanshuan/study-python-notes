s = 'hello,hello'

# index() 查找子串 substr 第一次出现的位置，如果查找的子串不存在时，则抛出 ValueError
print(s.index('lo')) # 3

# rindex() 查找子串 substr 最后一次出现的位置，如果查找的子串不存在时，则抛出 ValueError
print(s.rindex('lo')) # 9

# find() 查找子串 substr 第一次出现的位置，如果查找的子串不存在时，则返回 -1
print(s.find('lo')) # 3

# rfind() 查找子串 substr 最后一次出现的位置，如果查找的子串不存在时，则返回 -1
print(s.rfind('lo')) # 9

