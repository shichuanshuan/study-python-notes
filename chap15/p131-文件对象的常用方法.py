# read([size]) 从文件中读取 size 个字节或字符的内容返回。若省略 seze，则读取到文件末尾，即一次读取所有内容
file = open('a.txt', 'r')
# print(file.read())
print(file.read(2))
file.close()
print()

# readline() 从文件中读取一行内容
file = open('a.txt', 'r')
print(file.readline())
file.close()

# readlines() 把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表返回
file = open('a.txt', 'r')
print(file.readlines())
file.close()


# write(str) 将字符串 str 内容写入文件
file = open('a.txt', 'a')
file.write('shuan')
file.close()
print()

# writelines(s_list) 将字符串列表 s_list 写入文本文件，不添加换行符
file = open('c.txt', 'a')
lst = ['go', 'python', 'c']
file.writelines(lst)
file.close()
print()

# seek(offset[,whence]) 把文件指针移动到新的位置，offset 表示相对于 whence 的位置：
                        # offset: 为正，往结束方向移动，为负，往开始方向移动
                        # whence 不同的值代表不同含义:
                        # 0: 从文件头开始计算 默认值
                        # 1: 从当前位置开始计算
                        # 2: 从文件尾开始计算
file = open('a.txt', 'r')
file.seek(2)
print(file.read())
file.close()
print()

# tell() 返回文件指针的当前位置
file = open('a.txt', 'r')
file.seek(2)
print(file.read())
print(file.tell())
file.close()
print()

# flush() 把缓冲区的内容写入文件，但不关闭文件
file = open('d.txt', 'a')
file.write('hello')
file.flush()
file.write('world')
file.close()

# close()



