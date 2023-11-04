# .py文件 --> 解释器 --> 文件操作 --> 磁盘

# 语法规则
# file 
# open
# filename
# mode
# encoding
# file = open(filename [,mode, encoding])

from os import read
file = open('129.txt', 'r')

# readlines 读到的内容放到列表中
print(file.readlines())
file.close()
