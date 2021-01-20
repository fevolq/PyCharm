#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

#隐式创建figure对象
def A():
    """
    当第一次执行plt.xxx()画图代码时，系统会去判断是否已经有了figure对象，
    如果没有，系统会自动创建一个figure对象，并且在这个figure之上，自动创建一个axes坐标系
    (注意：默认创建一个figure对象，一个axes坐标系)
    就是说，如果不设置figure对象，那么一个figure对象上，只能有一个axes坐标系，即我们只能绘制一个图形。
    """
    x = [1,3,5,7]
    y = [4,9,6,8]
    plt.plot(x,y)       #由plot()函数绘制
    plt.show()          #图形由show()函数显示（pycharm中必须要加这句代码才能显示）。
    pass

#显示创建figure对象
def B():
    """
    显示创建一个对象，则可以绘制多个图形，从而可以调用每个位置上的axes对象。
    """
    figure = plt.figure()
    axes1 = figure.add_subplot(2,1,1)
    axes2 = figure.add_subplot(2,1,2)
    axes1.plot([1,3,5,7],[4,9,6,8])
    axes2.plot([1,3,5,7],[6,1,4,2])
    figure.show()

    x = np.arange(1,5)
    y1 = x*2
    y2 = x**2
    #建立网格，高为2，宽为1
    #第一个网格
    plt.subplot(2,1,1)
    plt.plot(x,y1)
    plt.title('First')
    #第二个网格
    plt.subplot(2,1,2)
    plt.plot(x,y2)
    plt.title('Second')
    plt.show()

    pass

#添加画布标题，轴名等
def C():
    plt.rcParams['font.family'] = ['STFangsong']    #设置字体，使用系统的文字
    x = np.arange(1,11)
    y = 2*x + 5
    plt.title("测试")
    plt.xlabel("X轴")
    plt.ylabel("Y轴")
    plt.plot(x,y)
    plt.show()
    pass

#改变颜色和格式（使用原点和颜色）
def D():
    """
    'b'-蓝色，'g'-绿色，'r'-红色，'c'-青色，'m'-品红色，'y'-黄色，'k'-黑色，'w'-白色
    """
    figure = plt.figure()
    axes1 = figure.add_subplot(2, 1, 1)
    axes2 = figure.add_subplot(2, 1, 2)

    x = np.arange(1,11)
    y = x*2 + 5
    plt.title('Mat')        #只会给最后一个图命名
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    axes1.plot(x,y,'r')      #用线来显示
    axes2.plot(x,y,'or')     #用点来显示。作为线性图的替代，可以通过向 plot() 函数添加格式字符串来显示离散值
    plt.show()
    """
    '-'实线样式，'--'短横线样式，'-.'点划线样式，':'虚线样式，'.'点标记，','像素标记，'o'圆标记，
    'v'倒三角标记，'^'正三角标记，'&lt;'左三角标记，'&gt;'右三角标记，
    '1'下箭头标记，'2'上箭头标记，'3'左箭头标记，'4'右箭头标记，
    's'正方形标记，'p'五边形标记，'*'星形标记，'h'六边形标记1，'H'六边形标记2，
    '+'加号标记，'x'X标记，'D'菱形标记，'d'窄菱形标记，
    '&#124;'竖直线标记，'_'水平线标记
    """
    pass

#保存画布
def E():
    fig = plt.figure()
    axes1 = fig.add_subplot(2,1,1)
    axes2 = fig.add_subplot(2, 1, 2)
    x = np.arange(1,6)
    y1 = x*2
    y2 = x**3
    axes1.plot(x,y1)
    axes2.plot(x,y2,color='m')
    plt.show()
    #保存到指定路径，dpi-像素，bbox_inches-剪除当前图表周围空白,facecolor-背景颜色
    fig.savefig(r'C:\Users\15394\Desktop\画布.png',
                dpi=400,bbox_inches='tight',facecolor='m')
    pass

if __name__ == '__main__':
    E()