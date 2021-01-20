#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:两个相同维度的数组的连接和分割

import numpy as np

###数组的连接（不改变原数组）
def a():
    arr_1 = np.arange(4).reshape(2,2)
    arr_2 = np.arange(4,8).reshape(2,2)
    # print(arr_1);print(arr_2)

    #numpy.concatenate((a1,a2,···),axis) 沿指定轴连接相同形状的两个或多个数组。仍为原维数
    print(np.concatenate((arr_1,arr_2)))        #沿轴0连接
    print(np.concatenate((arr_1,arr_2),1))
    print('\n')

    #numpy.stack(arrays, axis) 沿新轴连接（堆叠）数组序列。增加一个新的维数
    print(np.stack((arr_1,arr_2),0))        #沿轴1堆叠
    print(np.stack((arr_1, arr_2), 1))
    print('\n')

    #numpy.hstack —— numpy.stack函数的变体，通过堆叠来生成水平的单个数组
    print(np.hstack((arr_1,arr_2)))         #效果相同于np.concatenate
    #numpy.vstack —— numpy.stack函数的变体，通过堆叠来生成竖直的单个数组
    print(np.vstack((arr_1, arr_2)))        ##效果相同于np.concatenate((arrays),1)
    pass

###数组分割
def b():
    #numpy.split(ary, indices_or_sections, axis):将一个数组分割为多个子数组
    #ary:被分割的数组
    #indices_or_sections:可以是整数，表明要从输入数组创建的，等大小的子数组的数量
    #axis:默认为0
    arr = np.arange(9)
    print(arr)
    a = np.split(arr,3)
    print("分为3个大小相等的数组：",a)
    # print(arr)        #不改变原数组
    b = np.split(arr,[4,7])
    print("将数组在一维数组中表明的位置分割：",b)

    #numpy.hsplit是split()函数的特例，其中轴为 1 表示水平分割，无论输入数组的维度是什么
    arr_1 = np.arange(16).reshape(4,4)
    print(arr_1)
    c = np.hsplit(arr_1,2)
    print("水平分割：",c)

    #numpy.vsplit是split()函数的特例，其中轴为 0 表示竖直分割，无论输入数组的维度是什么
    d = np.vsplit(arr_1,4)
    print("竖直分割：",d)
    print(np.vsplit(arr_1,2))
    pass

if __name__ == '__main__':
    b()