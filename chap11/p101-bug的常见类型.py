try:
    a = int(input('请输入第一个整数'))
    b = int(input('请输入第二个整数'))
    result = a / b
    print('result = ', result)
except ZeroDivisionError:
    print('除数不允许为 0')
except ValueError:
    print('只能输入数字串')
print('程序结束')

