#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:数据存储为文件

"""
numpy提供了便捷的内部文件存取，将数据存为np专用的npy(二进制格式)或npz(压缩打包格式)格式
"""

import numpy as np

#存储与读取（.npy或.npz格式）
def a():
    """
    npy格式以二进制存储数据的，在二进制文件第一行以文本形式保存了数据的元信息（维度，数据类型），可以用二进制工具查看查看内容
    npz文件以压缩打包文件存储，可以用压缩软件解压
    """
    arr_1 = np.array([
        ['张三','李四','王五','赵六'],
        ['11','12','13','14']
    ])
    arr_2 = np.arange(24).reshape(2,3,4)
    # print(arr_1,arr_2)

    #存储
    np.save('arr_1.npy',arr_1)      #存为.npy文件
    np.savez('arr_1.npz',a0=arr_1,a1=arr_2)    #多个数组存入一个.npz压缩包

    #读取
    arr_3 = np.load('arr_1.npy')
    arr_4 = np.load('arr_1.npz')
    print('arr_3：',arr_3) ; print('arr_4：',arr_4)
    # print(arr_4['a0'])        #单独输出数组

    pass

#存储与读取CSV文件
def b():
    """
    ###csv文件只能存储一维、二维数据，不能存储多维数据
    #np.savetxt()并不是专为生成CSV文件用的，可以生成任何带特定分隔符的文本文件，但CSV文件使用比较广泛

    存储CSV文件
    存储csv文件,本身是ASCII字符，不能存储非ASCII字符串
    np.savetxt(frame,array,fmt='%.18e',delimiter=None)
    frame    存储文件、字符串或产生器的名字，可以是.gz或.bz2的压缩文件，对大型数据有用，压缩后存储或读取，节省存储资源
    array    存入文件的数组
    delimiter 分隔字符串，默认是任何空格，需要改为 逗号
    fmt      写入文件中每个元素的字符串格式，如：%s--ASCII字符；%d--整数；%.2f--2位小数的浮点数；%.18e--科学计数法

    读取CSV文件
    np.loadtxt(frame,dtype=np.float,delimiter=None,skiprows=0,usecols=None,unpack=False)
    frame    同上
    dtype    数据类型，可选，CSV的字符串以什么数据类型读入数组中，默认 np.float
    delimiter 同上
    skiprows 跳过前x行，一般跳过第一行表头
    usecols  读取指定的列，索引，元组类型
    unpack   默认为False。若为True，读入属性将分别写入不同数组变量；若为False，读入数据只写入一个数组变量。
    """
    arr = np.arange(6).reshape(2,3)
    np.savetxt('arr.gz',arr,fmt='%d',delimiter=',')         #存储为CSV文件
    print('Done')
    np.loadtxt('arr.gz',dtype=np.int,delimiter=',',unpack=True)     #读取CSV文件

    pass

if __name__ == '__main__':
    a()