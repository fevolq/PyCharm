#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:https://blog.csdn.net/qq_40181592/article/details/86770960

import turtle
import time

##按照坐标走动
#绝对坐标
def A():
    """
    绝对坐标是以屏幕为坐标系，中心位置为（0，0）
    用turtle.goto(x,y)来从当前位置走到(x,y)
    """
    turtle.goto(100,100)
    turtle.goto(100, -100)
    turtle.goto(-100, -100)
    turtle.goto(-100, 100)
    turtle.goto(0, 0)
    pass

#海龟坐标
def B():
    """
    以海龟本身为参考系，初始为向左，海龟转向后，注意此时的参考系方向：
                    左侧方向（turtle.circle(r,angle)）
    后退方向(bk(d))    海龟          前进方向(fd(d))
                    右侧方向
    turtle.fd(d)：表示向前方（前进）
    turtle.bk(d)：表示向后方（后退）
    turtle.circle(半径，弧度)：表示海龟以左侧某一点为圆心的曲线方向
    """
    turtle.fd(100)
    time.sleep(2)
    turtle.circle(50,180)   #直径为100，画半圆
    time.sleep(2)
    turtle.bk(100)          #此时的海龟朝向与初始相反（向左），故bk仍然会向右
    time.sleep(2)
    turtle.circle(-50,180)  #半径为负，则以海龟右侧为圆心画曲线。此时的海龟朝向为向左，故会在上方画曲线。
    turtle.hideturtle()
    turtle.mainloop()
    pass

##更改海龟朝向
def C():
    """
    绝对坐标：turtle.seth(angle)来改变海龟的游走方向，只改变方向
                90/-270度
    180/-180度------海龟-------->0/360度
                270/-90度
    海龟坐标：turtle.left(angle),turtle.right(angle)来以海龟为参考系改变方向
            turtle.left(angle)
    --------------海龟--------------->
            turtle.right(angle)
    """
    turtle.left(45)     #海龟初始向右，故此步操作会使海龟方向向右上转45°
    turtle.fd(100*(2**0.5))
    time.sleep(1.5)
    turtle.seth(270)    #使用绝对坐标来更改海龟朝向，改为向下
    turtle.fd(200)
    time.sleep(1.5)
    turtle.right(135)   #此时海龟朝正下，需要朝右后方，故使用right
    turtle.fd(100*2**0.5)
    turtle.mainloop()
    pass

##画笔控制函数
def D():
    """
    turtle.penup() 画笔抬起；turtle.pendown() 画笔降下
    turtle.pensize(宽度) 画笔宽度
    turtle.pencolor(color) #画笔颜色  color为字符串 或者 R G B 的值
    turtle.speed(speed)：设置画笔移动速度，画笔绘制的速度范围[0,10]整数，数字越大越快。
    turtle.fillcolor(colorstring) 绘制图形的填充颜色
    turtle.color(color1,color2)同时设置画笔颜色color1, 填充颜色color2
    """
    turtle.goto(100,0)
    # turtle.penup()        #与pendown()组合使用，只有放下画笔后才能作画。
    #画笔函数抬起和降下一般成对存在，画笔设置后一直有效，直至下次重新设置
    turtle.goto(100,100)
    # turtle.pendown()
    turtle.speed(1)
    turtle.pensize(10)      #画笔宽度
    turtle.goto(0,100)
    turtle.pencolor('magenta')
    turtle.goto(0,0)

    turtle.mainloop()
    pass

##循环语句与range()函数
def E():
    #使画笔往左移动
    turtle.penup()
    turtle.fd(-300)
    turtle.pendown()
    #设置画笔宽度，颜色和速度
    turtle.pensize(10)
    turtle.pencolor('magenta')
    turtle.speed(3)
    #改变画笔初始方向
    turtle.right(90)    # 改变方向，向下
    #循环
    for i in range(3):
        turtle.circle(50,180)   #下半圆
        turtle.circle(-50,180)  #上半圆
    time.sleep(2)
    for i in range(3):
        turtle.circle(-50,180)      #此步的循环的海龟初始方向与上面不同
        turtle.circle(50,180)
    turtle.done()       #与turtle.mainloop()功用相同
    pass

if __name__ == '__main__':
    E()