import os.path

filename = 'student.txt'

def main():
    while True:
        menm()
        choice = int(input('请选择'))
        if choice in range(8):
            if choice == 0:
                answer = input('您确定要退出系统吗? y/n\n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
            

def menm():
    print('='*22, "学生信息管理系统", '='*22)
    print('\t\t\t1.录入学生信息')
    print('\t\t\t2.查找学生信息')
    print('\t\t\t3.删除学生信息')
    print('\t\t\t4.修改学生信息')
    print('\t\t\t5.排序')
    print('\t\t\t6.统计学生总人数')
    print('\t\t\t7.显示所有学生信息')
    print('\t\t\t0.退出')

def insert():
    student_list = []
    while True:
        id = input('请输入ID')
        if not id:
            break
        name = input('请输入姓名')
        if not name:
            break

        try:
            english = input('请输入英语成绩')
            python = input('请输入python成绩')
            java = input('请输入java成绩')
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        # 将录入的学生信息保存到字典中
        student = {'id':id, 'name':name, 'english':english, 'python':python, 'java':java}
        # 将学生信息添加到列表中
        student_list.append(student)
        answer = input('是否继续添加? y/n \n')
        if answer == 'y':
            continue
        else:
            break
    
    # 调用 save 函数
    save(student_list)
    print('学生信息录入完毕!')

def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()

def search():
    pass

def delete():
    while True:
        student_id = input('请输入要删除的学生的ID:')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False # 标记是否删除
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item)) # 将字符串转成字典
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id 为 {student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到id 为 {student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()
            answer = input('是否继续删除? y/n\n')
            if answer == 'y':
                continue
            else:
                break

def modify():
    # show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('请输入要修改的学员的ID')
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('找到学生信息，可以修改他的相关信息了!')
                while True:
                    try:
                        d['name'] = input('请输入姓名')
                        d['english'] = input('请输入英语成绩')
                        d['python'] = input('请输入python成绩')
                        d['java'] = input('请输入java成绩')
                    except:
                        print('您的输入有误，请重新输入!!!')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功!!!')
            else:
                wfile.write(str(d) + '\n')
        answer = input('是否继续修改其他学生信息? y/n \n')
        if answer == 'y':
            modify()

def sort():
    pass

def total():
    pass

def show():
    pass

if __name__ == '__main__':
    main()