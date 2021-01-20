#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:更改数组的数据或数据类型或数组类型（形状，可更改维数）

import numpy as np

###“转为”一维
def a():
    arr = np.arange(24).reshape(2,3,4)
    # print(arr)
    print(arr.flat[5])      #flat[]，将数组“变成”一维，再索引出元素。不改变原数组
    print(arr.flatten())    #flatten('order')，返回折叠为一维的数组副本，不改变原数组。
                            #可接受以下参数：C--按行；F--按列；A--原顺序；K--元素在内存中的出现顺序
    print(arr.ravel())      #ravel('order')，返回展开的一维数组，并按需生成副本，返回的数组和输入数组有相同的数据类型。可接受参数同上。
    print('\n')
    # print(arr)
    pass

###翻转维度（轴对换）
#轴转置
def b():
    """
    numpy.transpose(arr,axes)
    arr:要转置的数组
    axes:整数的列表，对应维度，通常所有维度都会翻转
    """
    arr = np.arange(24).reshape(2,3,4)
    print(arr)
    print(np.transpose(arr))        #等同于print(arr.T)。shape为(4,3,2)

#轴滚动
def c():
    """
    numpy.rollaxis(arr,axis,start)
    arr:输入数组
    axis:要向后滚动的轴，其他轴的相对位置不变
    start:默认为0，表示完整的滚动，会滚动到特定位置
    """
    arr = np.arange(8).reshape(2,2,2)
    print(arr)
    print(np.rollaxis(arr,2))       #将轴2滚动到轴0（整体滚动，想象成一个立方体）
    print(np.rollaxis(arr,2,1))     #将轴0滚动到轴1（x轴和y轴互换，但z轴上的数据顺序不变）
    pass

#轴对换
def d():
    """
    numpy.swapaxes(arr,axis1,axis2)
    arr:输入数组
    axis1:对应的第一个轴的整数（0，1，2，···）
    axis2:对应的第二个轴的整数
    """
    arr = np.arange(8).reshape(2,2,2)
    # print(arr)
    print(np.swapaxes(arr,2,0))     #交换轴0和轴2
    # print(np.swapaxes(arr,0,2))
    print(arr)                  #表明不改变原数组，只返回一个视图
    print(np.swapaxes(arr,0,1))         ###??????????
    print(np.swapaxes(arr, 1,2))        ###??????????
    pass

###删除一维条目（[[[1],[2]]]，删除“不必要”的第三维）
def e():
    """
    numpy.squeeze(arr,axis)
    arr:输入数组
    axis:整数或整数元组，用于选择形状中单一维度条目的子集
    """
    arr = np.arange(9).reshape(1,3,3)
    print(arr)
    a = np.squeeze(arr)
    print(a)
    print(arr.shape,a.shape)
    pass

###改变维度（重塑数组，但不改变原数据）
def f():
    arr = np.arange(24).reshape(2,3,4)
    print(arr)
    print('降为一维：',arr.flatten())
    arr.shape = (6,4)
    print('改变维度大小：',arr)
    arr.resize((2,12))
    print('改变维度大小：',arr)
    print('反转数组：',arr.transpose())  #使用此函数前的arr数组的shape为(2,12)

if __name__ == '__main__':
    f()