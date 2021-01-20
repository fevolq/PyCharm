#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:2021.01.15
# Filename:定义操作系统类

import employee

class Syetem():
    def __init__(self):
        self.em_dicts = {}      #{员工工号:对应的员工对象}

    #显示菜单
    @staticmethod
    def __show_menu():
        print('1.新增员工信息')
        print('2.删除员工信息')
        print('3.修改员工信息')
        print('4.查询单个员工信息')
        print('5.查询所有员工信息')
        print('6.退出系统')

    #新增
    def __insert(self):
        #使用 input 获取员工信息
        em_id = input('请输入新增的员工的工号：')
        if em_id in self.em_dicts:
            print('该工号已存在，请确认后再操作···')
            return
        name = input('请输入员工姓名：')
        age = input('请输入员工年龄：')
        sex = input('请输入员工性别：')
        salary = input('请输入员工工资：')

        #使用获取的员工信息，创建员工对象,即将数据传给Employee类
        em = employee.Employee(em_id,name,age,sex,salary)

        #将员工对象添加到字典中
        self.em_dicts[em_id] = em

    #删除
    def __remove(self):
        em_id = input('请输入需要删除的员工的工号：')
        if em_id in self.em_dicts:
            del self.em_dicts[em_id]
            print('该工号员工信息已删除···')
        else:
            print('该工号不存在，请确认后再操作···')

    #修改
    def __modify(self):
        em_id = input('请输入需要修改的员工的工号：')
        if em_id in self.em_dicts:
            em = self.em_dicts[em_id]       #找出该工号的员工对象
            em.name = input('请输入新的员工姓名：')       #直接对对象的属性进行修改
            em.age = input('请输入新的员工年龄：')
            em.sex = input('请输入新的员工性别：')
            em.salary = input('请输入新的员工工资：')
            print('信息已修改完毕···')
        else:
            print('该工号不存在，请确认后再操作···')

    #查询单个
    def __search(self):
        em_id = input('请输入需要查询的员工的工号：')
        if em_id in self.em_dicts:
            em = self.em_dicts[em_id]
            print(em)
        else:
            print('该工号不存在，请确认后再操作···')

    #查询所有
    def __show_all(self):
        for em in self.em_dicts.values():
            print(em)
        print('已展示所有员工信息···')

    #保存员工信息至文本
    def __save(self):
        with open(r'C:\Users\15394\Desktop\employee.txt','w') as f:
            for em in self.em_dicts.values():
                f.write(str(em) + '\n')     #需要使用str()转换员工对象为字符串格式，调用了student类中的__str__方法

    #从文本读取员工信息
    def __load(self):
        with open(r'C:\Users\15394\Desktop\employee.txt','r') as f:
            lines = f.readlines()
        for line in lines:
            info = line.strip()     #移除每行的换行符
            info_list = info.split(',')     #以,为分隔符转换为列表
            #创建员工对象
            em = employee.Employee(info_list[0],info_list[1],info_list[2],info_list[3],info_list[4])
            em_id = info_list[0]
            #将员工对象添加到字典中
            self.em_dicts[em_id] = em

    #执行这个类。将类内的其他方法都定义为私有方法，避免在类外执行了这些方法
    def start(self):
        try:        #初次运行时没有这个文件
            self.__load()
        except:
            pass
        while True:
            self.__show_menu()    #调用上面的静态方法
            operation = input('请输入需要进行的操作对应的编号：')
            if operation == '1':
                # print('1.新增员工信息')
                self.__insert()
            elif operation == '2':
                # print('2.删除员工信息')
                self.__remove()
            elif operation == '3':
                # print('3.修改员工信息')
                self.__modify()
            elif operation == '4':
                # print('4.查询单个员工信息')
                self.__search()
            elif operation == '5':
                # print('5.查询所有员工信息')
                self.__show_all()
            elif operation == '6':
                # print('6.退出系统')
                self.__save()
                print('本次操作结束，欢迎下次使用···')
                break
            else:
                print('输入有误，请重新操作')
                continue

            input('······输入回车键继续······')

if __name__ == '__main__':
    sys = Syetem()
    sys.start()