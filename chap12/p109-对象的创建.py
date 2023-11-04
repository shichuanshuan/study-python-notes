# 类的组成
# 类属性
# 实例方法
# 静态方法
# 类方法
class Student:
    native_pace = 'ShangHai' # 直接写在类里的变量，称为类属性

    def __init__(self, name, age):
        self.name = name    # self.name 称为实例属性（相当于随便定义的变量），进行了 一个赋值操作，将局部变量的 name 的值赋给实体属性
        self.age = age

    # 实例方法
    def eat(self):
        print('学生在吃饭...')

    # 静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod 进行修饰，所有我是静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了 classmethod 进行修饰')

# stu1 = Student('张三', 20)
# print(id(stu1))
# print(type(stu1))
# print(stu1)

# print('-------------------------------')
# print(id(Student))
# print(type(Student))
# print(Student)

stu1 = Student('张三', 20)
stu1.eat()  # 对象名.方法名()
print(stu1.name)
print(stu1.age)

print('-------------------------------')
Student.eat(stu1) # 类名.方法名

