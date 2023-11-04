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


stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print(stu1.native_pace)
print(stu2.native_pace)

# 类属性：类中 方法外 的变量称为类属性，被该类的所有对象所共享
Student.native_pace = '天津'
print(stu1.native_pace)
print(stu2.native_pace)

print('-----------类方法的使用方式-------------------')
# 类方法：使用 @classmethod 修饰的方法，使用类名直接访问的方法
Student.cm()
print()

print('-----------静态方法的使用方式------------------')
# 静态方法：使用 @staticment 修饰的方法，使用类名直接访问的方法
Student.method()
