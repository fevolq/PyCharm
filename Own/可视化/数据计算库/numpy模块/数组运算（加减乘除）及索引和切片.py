#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:运算、索引及切片
"""
1.切片操作若改变了数据会影响到原数组
"""

import numpy as np

###运算（加减乘除）
def a():
    #数组与数组间
    #矢量化。大小相等的数组之间的任何算术运算都会将运算应用到元素级
    arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(arr)
    print(arr*arr)
    print(arr+arr)
    print(arr-arr)
    print(1/arr)
    #数组（矢量）与标量之间
    #会将那个标量值传播到各个元素
    print(arr*2)
    print(arr*0.5)

    arr_1 = np.array([1,1,1])
    print(arr+arr_1)        #第二个数组维度小于第一个，会自动扩展

    arr_2 = np.arange(12).reshape(2,3,2)
    print('维度求和：')
    print(arr_2.sum(axis=0))        #在第0维求和，得到一个(3,2)的数组
    print(arr_2.sum(axis=1))        #在第1维求和，得到一个(2,2)的数组
    print(arr_2.sum(axis=2))        #在第2维求和，得到一个(2,3)的数组
    print(arr_2.sum(axis=2,keepdims=True))  #keepdims为True可保持维度不变，为(2,3,1)

    print('总值：',arr_2.sum())
    print('有初始值：',arr_2.sum(initial=11))
    pass

def b():
    array = [1,2,3,4]
    print(array,type(array))
    print(array[::-1])
    pass

###（常规）索引与切片
#一维数组
def c():
    l = [i for i in range(10)]              #或l = list(range(10))
    arr = np.array([0,1,2,3,4,5,6,7,8,9])
    #a = np.arange(10);print(arr,a)
    #一维数组和Python列表功能差不多
    print(arr[5],arr[1:3])
    arr[5:8] = 12
    print(arr)      #当将一个标量赋给一个切片时，该值会自动传播（“广播”）到整个选区
    #和列表不同，数组切片是原始数组的视图，表明数据不会被复制，任何改动都会同步到原数组。
    arr_slice = arr[5:8]
    arr_slice[1] = 666
    print(arr)
    arr_slice[:] = 99
    print(arr)
    #若要得到一份副本，则需要显式的进行复制操作（.copy()）
    arr = np.arange(10)
    arr_slice_1 = arr[2:5].copy()
    arr_slice_1 = 111
    print(arr)
    arr_1 = arr[:]         #仍旧对原数组影响
    arr_1[3:6] = 0
    print(arr,arr_1)
    pass

#二/三维数组
def d():
    arr_1 = np.array([
        [[1,2,3],[4,5,6]],
        [[7,8,9],[10,11,12]]
    ])
    #print(arr_1,arr_1.shape,arr_1.ndim)
    print(arr_1[0])   #对于多维数组，省略后面的索引，则返回一个低纬度的数组
    old_value = arr_1[0].copy()
    arr_1[0] = 66     #标量和数组都能赋值给多维数组内的数组
    print(arr_1)
    arr_1[0] = old_value    #将数组返回初始
    print(arr_1[0,1])     #返回一个一维数组，类似列表[[1,2]]的元素索引
    print(arr_1[1,1,1])   #上层中再往内索引一层

    arr_2 = np.random.randint(1,10,size=(4,4))
    print(arr_2[[1,3]])     #多行索引。arr[[行索引列表]]：通过索引列表获取几行
    print(arr_2[[1,3],[0,2]])     #arr[[行索引列表],[列索引列表]]：每个行与列一一对应。参见下面的花式索引

    #切片
    print('\n')
    arr_2 = np.arange(1, 10).reshape(3, 3)    #同np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(arr_2[:2])      #切片处理，沿着axis0（行）来处理
    print(arr_2[:2,1:])   #一次传入多个切片。先沿着行处理，再按指定行进行列处理，得到相同维数的数组视图
    print(arr_2[1,:2])    #整数索引与切片混合。得到低纬度切片
    print(arr_2[:2,1])          ###先处理行，再处理列
    arr_2[1:2] = 66         #对切片表达式的赋值也会扩散到整个数组
    print(arr_2)
    pass

#切片
def h():
    arr = np.arange(24).reshape(2,3,4)
    print('初始数组：',arr)
    print(arr[:,:,-1])      #单独一个冒号表示选中所有，这里表示选中轴0和轴1所有
    print('有步长：',arr[:,::-1])      #两个冒号表示步长
    print('全部反转：',arr[::-1,::-1,::-1])      #全部反转

###布尔型索引
def e():
    arr = np.array(['a','b','c','a','d',])
    print(arr == 'a')      #数组的比较运算（==、！=、>、<）也是矢量化的，会产生一个布尔型数组
    data = np.empty((5,4))
    # print(data)
    print(data[arr == 'a'])     #布尔型数组的索引，布尔型数组的长度必须和被索引(data)的轴（行）长度一致。
    print(data[arr=='a',2:])    #布尔型数组可以跟切片、整数（或整数序列）混合使用
    #另，选取两个及以上条件时，需要与或非(&|!)之类的布尔运算符
    #通过布尔型索引选取的数组中的数据，总是创建数据的副本，即便返回一样的数组
    print(data<0)
    data[data<0] = 0        #通过布尔型数组设置值
    print(data)
    data[arr != 'a'] = 66   #通过一维布尔型数组设置整行或整列的值
    print(data)
    pass

###花式索引
def f():
    #花式索引不会将数据反映到原数组，会将数据复制到新数组中
    arr = np.empty((8,6))
    # print(arr)
    for i in range(8):
        arr[i] = i
    print(arr)
    print(arr[[3,0,6]])       #利用整数列表或整数数组选取特定顺序的子集
    print(arr[[-2,-3,-5]])      #与列表类似，从末尾开始-1，结果的排列顺序仍按列表内整数的顺序
    print('\n')

    arr_1 = np.arange(32).reshape((8,4))
    print(arr_1)
    print(arr_1[[1,5,7,2],[0,3,1,2]])   #使用多个索引数组，会返回一个一维数组（不论原数组有多少维），元素对应索引元组
    #1代表选取第二行，0代表选取第二行的第一个元素，其他依次类推

    print(arr_1[[1,5,7,2]][:,[0,3,1,2]])       #选取矩阵的行列子集
    #[[1,5,7,2]]代表选出的行，[:,[0,1,3,2]]代表选中所有行，但列的顺序要按[0,1,3,2]排列
    pass

###条件索引
def g():
    ##numpy.where()返回输入数组中满足给定条件的元素的索引
    arr = np.arange(9).reshape(3,3)
    print(arr)
    a = np.where(arr > 3)
    print('大于3的元素的索引元组：',a)
    #(array([1, 1, 2, 2, 2], dtype=int64), array([1, 2, 0, 1, 2], dtype=int64))
    #第一个元组的第一个“1”表示第二行，下一个元组的第一个“1”表示第二个元素，结合得到原始数组的具体元素位置。
    print('构造出大于3的元素组成的元组：',arr[a],'\n')     #一维数组

    ##numpy.extract()返回满足任何条件的元素
    condition = np.mod(arr,2) == 0      #定义条件。mod()是除法余数
    print('按元素的条件值：',condition)
    print('使用条件提取元素：',np.extract(condition,arr))    #一维
    pass

if __name__ == '__main__':
    a()