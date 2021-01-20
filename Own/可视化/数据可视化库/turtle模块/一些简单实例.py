#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:一些简单的画图实例

import turtle

#太阳花
def A():
    turtle.color('red','yellow')    #设置线的颜色和填充的颜色
    turtle.begin_fill()
    for i in range(50):
        turtle.forward(200)
        turtle.left(170)
    turtle.end_fill()
    turtle.mainloop()
    pass

#五角星
def B():
    turtle.pensize(5)
    turtle.color('yellow','red')
    # turtle.pencolor('yellow')
    # turtle.fillcolor('red')
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(200)
        turtle.right(144)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-150,-120)
    turtle.color('black')
    turtle.write('完成',font=('Arial',40,'normal'))

    turtle.mainloop()
    pass

#个人实操
def C():
    colors = ['yellow', 'red', 'black', 'blue', 'cyan', 'magenta', 'white']
    turtle.color('cyan', 'black')
    turtle.speed(0)  # 绘画速度
    turtle.begin_fill()  # 开始填充颜色

    for i in range(36):
        turtle.left(10)
        turtle.fd(200)
        turtle.right(20)
        turtle.fd(200)
        turtle.right(160)
        turtle.fd(200)
        turtle.right(20)
        turtle.fd(200)
        turtle.right(180)

    turtle.end_fill()
    turtle.hideturtle()  # 隐藏画笔
    turtle.done()

if __name__ == '__main__':
    C()