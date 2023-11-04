# 使用 traceback 模块打印异常信息
import traceback
try:
    print('-------------------------')
    print(1 / 0)
except:
    traceback.print_exc()


