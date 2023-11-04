class Animal(object):
    def eat(self):
        print('动物会吃')

class Dog(Animal):
    def eat(self):
        print('狗吃骨头')

class Cat(Animal):
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print('猫吃鱼 %s' % self.name)


class Person():
    def eat(self):
        print('人吃五谷杂粮')

# 定义一个函数
def fun(obj):
    obj.eat()


# 开始调用函数
fun(Animal())
fun(Cat('shi'))
fun(Dog())
fun(Animal())
print('--------------------------------')
fun(Person())

# 静态语言与动态语言关于多态的区别
# 静态语言实现多态的必要条件
# 继承
# 方法重写
# 父类引用指向子类对象

# 动态语言的多态崇尚 鸭子类型 当看到一只鸟走起来像鸭子、游泳起来像鸭子、
# 收起来也像鸭子，那么这只鸟就可以被称为鸭子。在鸭子类型中，不需要关系对象是什么类型，
# 到底是不是鸭子，只关心对象的行为。

