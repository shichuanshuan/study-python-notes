# 特殊属性 __dict__ 
# 获得类对象或实例对象所绑定的所有属性和方法的字典

class A:
    pass

class B:
    pass

class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class D(A):
    pass

# 创建 C 类的对象
x = C('jack', 20) # x 是 C 类型的一个实例对象
print('1.', x.__dict__) # 实例对象的属性字典
print('2.', C.__dict__) # 实例对象的属性字典

print('----------------------------')
print('3.', x.__class__) # 输出了对象所属的类
print('4.', C.__bases__) # C 类的父类型的元素
print('5.', C.__base__) # 类的基类
print('6.', C.__mro__)  # 类的层次结构
print('7.', A.__subclasses__()) # 子类的列表
