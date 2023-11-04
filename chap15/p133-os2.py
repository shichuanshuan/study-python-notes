# getcwd 返回当前的工作目录
import os
print(os.getcwd())

# listdir(path) 返回指定路径下的文件和目录信息
lst = os.listdir('f:\\Python\\src\\chap15')
print(lst)

# mkdir(path[,mode]) 创建目录
# os.mkdir('newdir')

# makedirs(path1/path2...[,mode]) 创建多级目录 A里面有B B里面有C
# os.makedirs('A/B/C')

# rmdir(path) 删除目录
# os.rmdir('newdir')

# removedirs(path1/path2...) 删除多级目录
os.removedirs('A/B/C')

# chdir(path) 将 path 设置为当前工作目录
# os.chdir('')
