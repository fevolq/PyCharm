#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:https://blog.csdn.net/xiaodongxiexie/article/details/53123371

"""
柱形，散点，饼状，折线图；对一个DataFrame的几个列在不同画板同时作图；
画蜡烛图；画热图；散点气泡图；箱体图；雷达图；3D图；嵌套图；
区域图；区间图；饼状图及参数设计；
给不同段的线设置不同的颜色；同时给用来作图的不同列设置颜色；对数据作拟合曲线；
对图表添加描述，修改x轴y轴区间；图表添加描述或注释；
将不同y轴的两个series画在同一个画板上；
设置轴的线条颜色，隐藏轴边框；翻转x轴，y轴；隐藏x轴y轴；
突出指定坐标值；设定x轴坐标显示方式；
等其他······
"""

import numpy as np
from matplotlib import pyplot as plt

#绘制正弦波
def A():
    plt.rcParams['font.family'] = ['STFangsong']
    x = np.arange(0,3*np.pi,0.1)
    y = np.sin(x)       #余弦为cos
    plt.title('sin 函数')
    plt.plot(x,y)
    plt.show()
    pass

#条形图
def B():
    """
    pyplot 子模块提供 bar() 函数来生成条形图
    """
    x1 = [5,8,10]
    y1 = [12,16,6]
    x2 = [6,9,11]
    y2 = [6,15,7]
    plt.bar(x1,y1,align='center')
    plt.bar(x2,y2,color='g',align='center')
    plt.title('Bar graph')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()
    pass

#概率直方图
def C():
    """
    numpy.histogram() 函数是数据的频率分布的图形表示。
    水平尺寸相等的矩形对应于类间隔，称为 bin，变量 height 对应于频率。
    numpy.histogram()函数将输入数组和 bin 作为两个参数。
    bin 数组中的连续元素用作每个 bin 的边界。
    """
    a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
    np.histogram(a,bins=[0,20,40,60,80,100])
    hist,bins = np.histogram(a,bins=[0,20,40,60,80,100])
    # print(hist)
    # print(bins)

    plt.hist(a,bins=[0,20,40,60,80,100])
    plt.title('histogram')
    plt.show()
    pass

#饼状图和散点图
def D():
    fig = plt.figure(figsize=(10,8))    #建立一个大小为10*8的画板
    ax1 = fig.add_subplot(3,3,5)        #在画板上添加3*3个画布，位置是第5个
    ax1.pie(np.random.randint(1,15,5),explode=[0,0,0.2,0,0])    #饼状图
    ax2 = fig.add_subplot(3,3,2)        #在画板上添加3*3个画布，位置是第2个
    ax2.scatter(np.random.randn(10),np.arange(10),color='r')    #散点图
    plt.show()
    pass

if __name__ == '__main__':
    D()