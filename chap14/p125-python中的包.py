# 包与目录的区别
# 包 __init__.py 含文件的目录称为包
# 目录里通常不包含 __init__.py 文件

# 包的导入
# import 包名.模块名

# 导入带有包的模块时注意事项
# 使用 import 方式导入时，只能跟包名或模块名
# import pageage
# import calc
import python.module_A as ma
print(ma.add())

# 使用 from ... import 可以导入包、模块、函数、变量
# from pageage import module
# from pageage.model import a 
from python import module_A
print(module_A.add())

from python.module_A import add
print(add())


