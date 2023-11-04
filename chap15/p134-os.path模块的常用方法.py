# abspath(path) 用于获取文件或目录的绝对路径
import os.path

print(os.path.abspath('p133-os2.py'))

# exists(path) 用于判断文件或目录是否存在，如果存在返回 True，否则返回 False
print(os.path.exists('p133-os2.py'), os.path.exists('demo13.py'))

# join(path,name) 将目录与目录或文件名拼接起来
print(os.path.join('f:\\Python\\src\\chap15', 'demo13.py'))

# split() 分离文件的名字
print('split = ',os.path.split('f:\\Python\\src\\chap15\\p133-os2.py'))

# splitext() 分离文件名或扩展名
print('splitext = ', os.path.splitext('f:\\Python\\src\\chap15\\p133-os2.py'))
print('splitext = ', os.path.splitext('p133-os2.py'))

# basename(path) 从一个目录中提取文件名
print('basename = ', os.path.basename('f:\\Python\\src\\chap15\\p133-os2.py'))

# dirname(path) 从一个路径中提取文件路径，不包括文件名
print('dirname = ', os.path.dirname('f:\\Python\\src\\chap15\\p133-os2.py'))

# isdir(path) 用于判断是否为路径
print('isdir = ', os.path.isdir('f:\\Python\\src\\chap15'))
print('isdir = ', os.path.isdir('f:\\Python\\src\\chap15\\p133-os2.py'))
