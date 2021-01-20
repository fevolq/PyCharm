#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename: ndarray-多维数组对象的（详细）介绍

"""
NumPy中的ndarray是一个多维数组对象，该对象由两部分组成:
实际的数据
描述这些数据的元数据。
注：
数组对象内的元素类型必须相同
数组大小不可修改
"""

'''
常用创建数组：
numpy.arange(start,end,step)    起始，结束（不包含），步长。创建一维数组，若要多维，需在后面加上.reshape()
numpy.array([1,2,3])    [1,2,3]为一维数组
'''

import numpy as np

#与列表的对比
def a():
    def sum(n):
        a = list(range(n))
        b = list(range(n))
        c= []
        d = []
        for i in range(len(a)):
            c.append(a[i] * 2 + b[i] * 3)
            d.append(a[i] ** 2 + b[i] ** 3)
        return d
    def sum_np(n):
        a = np.arange(n)
        b = np.arange(n)
        c = a*2 + b*3
        d = a**2 + b**3
        return d
    print(sum(5))
    print(sum_np(5))

    l = [1,2,3,4,5,6]
    t = (5,6,7,8)
    print(np.asarray(l).reshape(2,3)) ; print(np.asarray(t))     #将列表和元组转换为数组
    arr = np.array([[1,2,3],[4,5,6]])
    print(arr.tolist())
    pass

#（创建）一维数组和二维数组
def b():
    #l = [1,2,3,4];print(l)
    one_arr = np.array([1,2,3,4])       #一维数组(“一维”表示维数，不表示维度大小)
    print(one_arr,'\n',\
          "维度大小：",one_arr.shape," 维数：",one_arr.ndim)

    two_arr = np.array([[1,2,3],[3,4,5]])   #二维
    print(two_arr,'\n',\
          "维度大小：",two_arr.shape," 维数：",two_arr.ndim)        #shape的返回值表示这是一个 二行三列 的数组

    t_arr = np.array([[1,2,3],[4,5,6],[7,8,9]])       #仍为二维数组
    print(t_arr, '\n', \
          "维度大小：", t_arr.shape, " 维数：", t_arr.ndim)

    arr = np.array([ [[1,2,3,0],[4,5,6,0],[7,8,9,0]] , [[1,2,3,4],[7,8,9,0],[3,4,5,6]] ])   #三维数组
    print(arr, '\n', \
          "维度大小：", arr.shape, " 维数：", arr.ndim)
    """
    关于shape的意思：
    (2,3) 表示两个一维数组组成的二维数组,每个一维数组长度为3
    (2,3,4) 表示两个二维数组组成的三维数组,每个二维数组有3个一维数组,每个一维数组长度为4
    (2,3,4,5) 表示两个三维数组组成的四维数组,每个三维数组有3个二维数组,每个二维数组有4个一维数组,一维数组长度为5
    """
    pass

#常用属性
def c():
    print(np.arange(5).shape)       #数组的维度大小（以元组形式）
    print(np.arange(6).dtype)       #数组元素的数据类型
    print(np.arange(7).size)        #数组元素的个数。itemsize返回数组中每个元素的字节单位长度
    print(np.arange(8).ndim)        #数组的维数
    #astype----转换数据类型；shape和reshape可改变维度的大小，即重塑数组。（详见数组转置···f方法）
    pass

#数组创建
def d():
    print(np.arange(5))                     #arange会创建一个array对象（一维）。可使用reshape()来指定维度大小，np.arange(12).reshape(3,4)
    print(np.arange(1,10,2))                #arange(start,stop,step,dtype)，包含起始，不含结束，步进，dtype可选（没有则使用输入数据的类型）
    print(np.array([(1,2,3),(4,0,6)]))      #创建一个数组。将输入数据（列表，元组，数组或其他序列类型）转换为数组。
    print(np.zeros(10))
    print(np.zeros((3,6)))          #numpy.zeros((a,b))创建a*b的零矩阵
    print(np.ones(10))
    print(np.ones((3,4)))           #同zeros，创建a*b的全1数组
    print(np.empty((2,3,4)))            #创建新数组，但只分配内存空间不填充任何值，所以初始出来的值是随机int8类型
    print(np.eye(4))                #同numpy.identity(n)，创建n*n的单位矩阵

    #从已有数据创建数组
    #numpy.asarray(arr, dtype = None, order = None)
    """
    arr       任意形式的输入参数，比如列表、列表的元组、元组、元组的元组、元组的列表
    dtype     输入出的数组类型，可选
    order   ‘C’为按行的C风格数组，’F’为按列的Fortran风格数组
    """
    arr = (1,2,3)
    print(np.asarray(arr, dtype=float, order='F'))

    #numpy.fromiter(iterable, dtype, count = -1)
    """
    iterable	任何可迭代对象
    dtype	    返回数组的数据类型
    count	    需要读取的数据数量，默认为-1，读取所有数据
    """
    b = range(5)
    #print(np.fromiter(b,i1))           #待解决

    #numpy.linspace(start, stop, num, endpoint, retstep, dtype)
    #根据已有范围创建等间距的数组
    """
    start	    范围的起始值
    stop	    序列的终止值，如果endpoint为true，该值包含于序列中
    num	        要生成的等间隔样例数量，默认为50
    endpoint	序列中是否包含stop值，默认为ture
    retstep	    如果为true，返回样例，以及连续数字之间的步长
    dtype	    输出ndarray的数据类型
    """
    pass

#自定义数据类型
def e():
    t = np.dtype([("name",np.str_,40),("items",np.int32),("price",np.float64)])         #创建一个数据类型(第一个的数据为40以内的str类型，32位整型，双精度浮点数)
    arr = np.array([("The meaning of life DVD",10,29.7),("I an your father",20,32.1)],dtype=t)  #创建一个数组，使用上述指定的数据类型
    print(arr)
    # int8、unit8(或i1、u1)有、无符号的8位（1个字节）整型
    #int16、unit16(i2、u2);int32(i4)···;int64(i8)···;
    #float16(f2)半精度浮点数；float32(f4或f)标准的单精度浮点数；float64(f8或d)标准的双精度浮点数

#其他
def f():
    #arange与array的区别
    #arange是一个数组版的range函数（arange对于array类似range对于list）
    a1 = list([3]);b1 = range(3)
    a2 = np.array([3]);b2 = np.arange(3)
    print(a1,b1,'\n',a2,b2)
    print(type(a1),type(b1))        #python3中range不会在内存中创建一个list
    print(type(a2),type(b2))
    print('\n\n')

    c = np.array([[1,2,3],[2,3,4]])
    c1 = np.array([[1,2,3],[2,3]])
    print(c,'\n',c1,'\n',type(c1),'\n')      #array要么推断出dtype，要么显示指定的dtype。默认直接复制输入数据。
    print(c1.dtype,'\n',c1.shape,'\n',c1.size,'\n',c1.ndim)

#四维数组（介绍shape的意义）
def g():
    # 判断维度可直接数中括号的数量，由外而内到单个元素（或其他），前提是这个数组是严格正确的
    arr = np.array([
        [
            [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]],
            [[1, 2, 3, 0, 0], [7, 8, 9, 0, 0], [3, 4, 5, 0, 0], [5, 6, 7, 0, 0]],
            [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
        ],
        [
            [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]],
            [[1, 2, 3, 0, 0], [7, 8, 9, 0, 0], [3, 4, 5, 0, 0], [5, 6, 7, 0, 0]],
            [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
        ]
    ])
    #print(arr)
    print(arr.shape,"\n维数为：",arr.ndim)
    #shape返回(2,3,4,5)，表示这是一个由2个三维数组组成的四维数组，
    # 每个三维内又由3个二维组成，二维由4个一维组成，一维的长度为5。

if __name__ == '__main__':
    a()