class Car:
    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print('汽车已启动...')

car = Car('奥迪S7')
car.start()
print(car.brand)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age # 年龄不希望再类的外部被使用，所有加了两个_

    def show(self):
        print(self.name, self.__age)

stu = Student('张三', 20)
stu.show()

# 在类外使用name 与 age
print(stu.name)
# print(stu.__age)
# print(dir(stu))
print(stu._Student__age) # 在类的外部可以通过 _Student__age 进行访问

