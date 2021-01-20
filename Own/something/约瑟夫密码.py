#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:约瑟夫密码问题

"""
问题描述：编号为1、2、3、...、N的N个人按顺时针方向围坐一圈，每人持有一个密码（正整数）。从指定
编号为1的人开始，按顺时针方向自1开始顺序报数，报到指定数M时停止报数，报M的人出列，并将
他的密码作为新的M值，从他在顺时针方向的下一个人开始，重新从1报数，依此类推，直至所有的
人全部出列为止。请设计一个程序求出出列的顺序，其中N≤30，M及密码值从键盘输入。
"""

#人数
while True:
    try:
        n = int(input("请输入一共有多少人（<=30）："))
        if 0 < n <= 30:
            break
        else:
            print("请输入一个小于等于30的正整数")
    except:
        print("请输入一个小于等于30的正整数")

#密码
peoples_dic = {}        #{编号：密码}
i = 1
while i<=n:
    try:
        m = int(input("请“依次”输入每个人所对应的密码（为正整数，输入一个按下回车）："))
        if m>0:
            peoples_dic[i] = m
            i += 1
        else:
            print("请输入正整数")
    except:
        print("请输入正整数")

#初始M值
while True:
    try:
        m = int(input("请输入初始M值（正整数）："))
        if 0 < m:
            break
        else:
            print("请输入一个正整数")
    except:
        print("请输入一个正整数")

peoples = {}            #{编号：1}
for i in range(0,n):
    peoples[i+1] = 1

number = 1               #报的数字
leave = []           #离开的人
i = 1               #编号
while i <= n+1:
    if len(leave) == n:      #所有人均已出列
        break
    elif i == n+1:
        i = 1           #队列最后一个人已报数，从头再来，编号从1开始，报数不变
    else:
        if peoples[i] == 0:         #此人之前已出列
            i += 1                  #进行下一个，编号+1，报数不变
        elif number == m:                #此人之前未出列，但此轮的报数为m值，则此轮出列
            peoples[i] =0           #对应的人的值改为0
            leave.append(i)         #对应的人的编号放入出列的列表中
            m = peoples_dic[i]      #替换m值
            i += 1                  #继续下一个人
            number = 1              #报的数字恢复到1
        else:       #在列的报数不为m值的
            i += 1           #下一个编号+1
            number += 1      #下一个报数+1

if __name__ == '__main__':
    print("共有{}人\n出列的顺序为：{}".format(n,leave))
    m1 = []
    m2 = []
    for i in range(1,n+1):
        m1.append(peoples_dic[i])
    for i in leave:
        m2.append(peoples_dic[i])
    print("初始密码顺序为：{}\n排序后的密码顺序为{}".format(m1,m2))