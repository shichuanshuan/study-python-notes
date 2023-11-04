# MyContentMgr 实现了特殊方法 __enter__() __exit__() 称为该类对象遵守了上下文管理器协议
# 该类对象的实例对象，称为上下文管理器

# class MyContentMgr():
#     def __enter__(self):
#         print('enter method')

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exit method')

#     def show(self):
#         print('show method')


# with MyContentMgr() as file:
#     file.show()

# with 语句可以自动关了上下文资源，不论什么原因跳出 with 块，
# 都能确保文件的正确的关闭，一词来达到解放资源的目的

with open('a.txt', 'r') as file:
    print(file.read())
