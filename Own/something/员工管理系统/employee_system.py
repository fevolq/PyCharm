#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:2020.12.07
# Filename:制作员工信息表

#员工数据为内存虚拟数据，未保存到本地，使用时需自己新增数据。
#所有数据都为字符串类型，为对编号、工资等限定数字类型。

import copy

#菜单栏
def show_operation():
    print('\n',
          '操作菜单栏如下：','\n',
          'i：新增员工信息','\n',
          'd：删除员工信息','\n',
          'a：修改员工信息','\n',
          's：展示员工信息','\n',
          'so：显示操作菜单','\n',)
    return True

#如何操作
def operation(how):
    if how == 'i':
        increase()
        whether_continue()
    elif how == 'd':
        delete()
        whether_continue()
    elif how == 'a':
        alter()
        whether_continue()
    elif how == 's':
        show()
        whether_continue()
    elif how == 'so':
        show_operation()
        whether_continue()
    else:
        pass

#新增员工信息
def increase():
    number = input('\n请输入新增的员工编号（如：01）：')
    while number in employees:
        print('\n原员工表中已有该编号，请确认后重新输入')
        number = input('\n请输入新增的员工编号（如：01）：')
    name = input('请输入新增的员工姓名（如：张三）：')
    salary = input('请输入新增的员工工资（如：10000）：')
    while True:
        sex = input('请输入新增的员工性别（如：男或女）：')
        if sex == '男' or sex == '女':
            break
        else:
            print('\n性别输入错误，请输入男或女\n')
    message = [number,name,salary,sex]
    m = '编号：{}，姓名：{}，工资：{}，性别：{}'.format(message[0],message[1],message[2],message[3])
    print('\n所输入的信息为：')
    print(m,'\n')
    w = whether('是否确认增添（Y/N）：')
    if w:
        mes = {'编号':message[0],'姓名':message[1],'工资':message[2],'性别':message[3]}
        employee = {message[0]:mes}
        employees.update(employee)     #更新员工数据字典
        # print(employees)
        print('\n新增已完成')
        return True
    else:
        print('\n请重新输入')
        return increase()

#删除员工信息
def delete():
    number = input('\n请输入需要删除的员工的编号（如：01）：')
    if number not in employees:
        print('\n未找到此编号为{}的员工，请确认后再操作'.format(number))
        return delete()
    else:
        message = get_message(number)
        print('\n该编号的员工信息为：')
        print('编号：{}，姓名：{}，工资：{}，性别：{}'.format(message[0], message[1], message[2], message[3]),'\n')
        w = whether('是否确认删除（Y/N）：')
        if w:
            del employees[number]
            # print(employees)
            print('\n删除已完成')
            return True
        else:
            print('\n请重新输入')
            return delete()

#更改员工信息
def alter():
    number = input('\n请输入需要更改的员工的编号（如：01）：')
    if number not in employees:
        print('\n未找到此编号为{}的员工，请确认后再操作'.format(number))
        return alter()
    else:
        message = get_message(number)
        print('\n该编号的员工信息为：')
        print('编号：{}，姓名：{}，工资：{}，性别：{}'.format(message[0], message[1], message[2], message[3]),'\n')
    new_employees = copy.deepcopy(employees)
    print('new_employees：',new_employees)
    del new_employees[number]
    print('new_employees：', new_employees)
    new_number = input('请输入新的员工编号（如：01）：')
    while new_number in new_employees:
        print('\n原员工表中已有该编号，请确认后重新输入')
        new_number = input('\n请输入新的员工编号（如：01）：')
    new_name = input('请输入新的员工姓名（如：张三）：')
    new_salary = input('请输入新的员工工资（如：10000）：')
    while True:
        new_sex = input('请输入新的员工性别（如：男或女）：')
        if new_sex == '男' or new_sex == '女':
            break
        else:
            print('\n性别输入错误，请输入男或女\n')
    new_message = [new_number, new_name, new_salary, new_sex]
    m = '编号：{}，姓名：{}，工资：{}，性别：{}'.format(new_message[0], new_message[1], new_message[2], new_message[3])
    print('\n更改后的员工信息为：')
    print(m,'\n')
    w = whether('是否确认更改（Y/N）：')
    if w:
        new_mes = {'编号': new_message[0], '姓名': new_message[1], '工资': new_message[2], '性别': new_message[3]}
        new_employee = {new_number:new_mes}     #更改后的员工数据
        del employees[number]       #删除原数据
        employees.update(new_employee)      #加入更改后的员工数据
        print('\n更改已完成')
        return True
    else:
        print('\n请重新输入')
        return alter()

#展示员工信息
def show():
    w = input("\n展示所有员工信息请输入'all'，展示单条员工信息请输入该员工编号（如：01）：")
    if w == 'all':
        print('\n所有员工信息如下：')
        for a,b in employees.items():
            employee = b
            message = [employee['编号'],employee['姓名'],employee['工资'],employee['性别'],]
            print('编号：{}，姓名：{}，工资：{}，性别：{}'.format(message[0],message[1],message[2],message[3],))
        print('\n已展示所有')
        return True
    else:
        if w not in employees:
            print('\n员工表中不存在该编号，请确认后重新输入')
            return show()
        else:
            number = w
            message = get_message(number)
            print('\n该编号的员工信息为：')
            print('编号：{}，姓名：{}，工资：{}，性别：{}'.format(message[0], message[1], message[2], message[3], ),'\n')
            return True

#得到指定编号的员工信息
def get_message(number):
    employee = employees[number]
    message = [employee['编号'], employee['姓名'], employee['工资'], employee['性别'],]
    return message

#是否确认
def whether(m):
    w = input('{}'.format(m))
    if w =='Y' or w == 'y':
        return True
    elif w == 'N' or w == 'n':
        return False
    else:
        return whether(m)       #return必不可少

#是否继续操作
def whether_continue():
    w = whether('是否继续操作（Y/N）：')
    if w:
        main()
    else:
        pass

def main():
    show_operation()
    how = input('请根据所展示信息操作（如：需要新增员工信息则输入：i）：')
    l = ['i','d','a','s','so']
    if how in l:
        operation(how)
    else:
        print('\n请确认后再操作\n')
        main()

if __name__ == '__main__':
    employees = {}
    main()

'''
注意事项：递归函数中，在函数内部使用本身时最好使用return 本身
'''