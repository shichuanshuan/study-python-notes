# 特殊方法
# __len__() 通过重写 __len__() 方法，让内置函数 len() 的参数可以是自定义类型
# __add__() 通过重写 __add__() 方法，可使用自定义对象具有 + 功能
# 实现了两个对象的加法运算 （因为在 Student 类中 编写 __add__() 特殊的方法）
# __new__() 用于创建对象
# __init__() 对创建的对象进行初始化

a = 20
b = 100
c = a + b
d = a.__add__(b)

print(c)
print(d)

class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)

stu1 = Student('jack')
stu2 = Student('李四')
s = stu1 + stu2
print(s)

print('------------------------------')
lst = [11, 22, 33, 44, 55]
print(len(lst)) # len 是内容函数 len
print(lst.__len__())
print(len(stu1))
