#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:2021.01.05
# Filename:定义员工类

#定义员工对象，包含所需要的属性

class Employee():
    def __init__(self,em_id,name,age,sex,salary):
        self.em_id = em_id
        self.name = name
        self.age = age
        self.sex = sex
        self.salary = salary

    #返回一个对象的描述信息
    def __str__(self):
        return f"{self.em_id},{self.name},{self.age},{self.sex},{self.salary}"
    """__str__(self)方法作用：返回一个对象的描述信息。
    需要返回一个字符串，当作这个对象的描述信息。
    当使用print输出对象时，只要内部自己定义了__str__(self)方法，那么就会打印从这个方法中return的数据。
    """

if __name__ == '__main__':
    stu = Employee(1,'abc',24,'男',8000)
    print(stu)