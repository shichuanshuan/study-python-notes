# 创建模块
# 新建一个.py文件，名称尽量不要与 python 自带的标准模块名称相同


# 导入模块
# import 模块名称 [as 别名]
import math # 关于数学运算

import math

from math import pi

print(id(math))
print(type(math))
print(math)
print(math.pi)
print('------------------------------------')

print(dir(math))
print(math.pow(2, 3))
print(math.ceil(9.00001))
print(math.floor(9.9999))


# from 模块名称 import 函数/变量/类
from math import pi # 只能使用 math 中的 pi变量
print(pi)
print(pow(2, 3))



