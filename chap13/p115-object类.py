# objecit 类
# object类是所有类的父类，因此所有类都有object类的属性和方法
# 内置函数 dir() 可以查看指定对象所有属性

# object有一个 __str__() 方法，用于返回一个对于“对象的描述”，对应于内置函数 str() 
# 经常用于 print() 方法，帮我们查看对象的信息，所有我们经常会对 __str__() 进行重写

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '我的名字是{0},今年{1}岁'.format(self.name, self.age)

stu = Student('sds', 24)
print(dir(stu))
print("---------------------")
print(stu)
print(type(stu))
