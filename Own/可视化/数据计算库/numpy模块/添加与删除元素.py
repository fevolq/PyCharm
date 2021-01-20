#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:往数组中添加或删除元素

"""
resize	返回指定形状的新数组
append	将值添加到数组末尾
insert	沿指定轴将值插入到指定下标之前
delete	返回删掉某个轴的子数组的新数组
unique	去重，寻找数组内的唯一元素，删减保留唯一一项
~       去掉缺失值，在函数前使用波浪号~，表示"反义"
"""

import numpy as np

def Resize():
    """
    numpy.resize(arr, shape)返回指定大小的新数组.如果新大小大于原始大小，则包含原始数组中的元素的重复副本
    arr:要修改的输入数组
    shape:返回数组的新形状
    """
    arr = np.arange(1,7).reshape(2,3)
    print("初始数组：",arr)
    a = np.resize(arr,(3,2))
    print("更改形状的数组a：",a)
    b = np.resize(arr,(3,3))
    print("更改形状的数组b：",b)       #尺寸变大，所以数据重复出现
    print("原始数组：",arr)            #表明不改变原数组
    pass

def Append():
    """
    numpy.append(arr, values, axis)在输入数组的末尾添加值
    arr：输入数组
    values：要向arr添加的值，比如和arr形状相同(除了要添加的轴)
    axis：沿着它完成操作的轴。如果没有提供，两个参数都会被展开
    附加操作不是原地的，而是分配新的数组。
    此外，输入数组的维度必须匹配否则将生成ValueError
    """
    arr = np.arange(1,7).reshape(2,3)
    print('初始数组：',arr)
    a = np.append(arr,[7,8,9])
    print('向数组中添加元素：',a)
    # print('原始数组：',arr)        #不更改原始数组
    b = np.append(arr,[[7,8,9]],axis=0)
    print('沿轴0添加元素：',b)
    # print(np.append(arr,[[7,8,9],[6,6,6]],axis=0))
    # print(np.append(arr, [[7, 8]], axis=0))     #大小匹配，产生错误
    c = np.append(arr,[[5,5,5],[7,8,9]],axis=1)
    print('沿轴1添加元素：',c)
    # print(np.append(arr,[[5,5,5]],axis=1))      #维度不匹配，产生错误
    pass

def Insert():
    """
    numpy.insert(arr, obj, values, axis)在给定索引之前，沿给定轴在输入数组中插入值
    # arr：输入数组
    # obj：在其之前插入值的索引
    # values：要插入的值
    # axis：沿着它插入的轴，如果未提供，则输入数组会被展开
    不改变原数组
    """
    arr = np.arange(1,7).reshape(3,2)
    print('初始数组',arr)
    a = np.insert(arr,3,[11,12])
    print('未传入轴参数：',a)
    # print('原始数组：',arr)
    b = np.insert(arr,1,[11],axis=0)
    print('沿轴0广播：',b)           #有轴参数时，索引为按轴指定的索引
    print(np.insert(arr,1,11,axis=0))
    print(np.insert(arr, 1, [11,12], axis=0))
    print(np.insert(arr, 1, [11, 12], axis=0))
    c = np.insert(arr,1,11,axis=1)
    print('沿轴1广播：',c)
    # print(np.insert(arr, -1, [11, 12], axis=1))     #出错。插入的数据与原始数组形状不对等
    pass

def Delete():
    """
    numpy.delete(arr,odj,axis)返回从输入数组中删除指定子数组的新数组.与insert()情况一样。
    # arr：输入数组
    # obj：可以被切片，整数或者整数数组，表明要从输入数组删除的子数组
    # axis：沿着它删除给定子数组的轴，如果未提供，则输入数组会被展开
    不改变原数组。
    """
    arr = np.arange(12).reshape(3,4)
    print('初始数组：',arr)
    a = np.delete(arr,5)
    print('未传递轴参数：',a)
    # print('原始数组：',arr)
    b = np.delete(arr,1,axis=1)
    print('删除第二列：',b)

    arr_1 = np.arange(1,11)
    print('初始数组：',arr_1)
    c = np.delete(arr_1,np.s_[::2])
    print(arr_1[::2])
    print('包含从数组中删除的替代值的切片',c)
    pass

def Unique():
    """
    numpy.unique(arr, return_index, return_inverse, return_counts)
    返回输入数组中的去重元素数组.
    # arr：输入数组，如果不是一维数组则会展开
    # return_index：如果为true，返回输入数组中的元素下标
    # return_inverse：如果为true，返回去重数组的下标，它可以用于重构输入数组
    # return_counts：如果为true，返回去重数组中的元素在原数组中的出现次数
    该函数能够返回一个元组，包含去重数组和相关索引的数组。
    索引的性质取决于函数调用中返回参数的类型。
    不改变原数组。
    """
    arr = np.array([5,2,6,2,7,5,6,8,2,9])
    print(arr,arr.shape)
    a = np.unique(arr)
    print('去重后的数组',a)
    # print(arr)
    b,b1 = np.unique(arr,return_index=True)     #np.unique(arr,return_index=True)的返回值有两个，去重数组和去重数组的索引数组
    print(b,'去重数组的索引数组：',b1)    #索引取位于原数组第一个符合的元素的索引
    c,c1 = np.unique(arr,return_inverse=True)
    print(c,'原数组中的元素在去重数组中的索引数组：',c1)
    print('使用索引数组重构原始数组：',c[c1])    #重新构造出原始数组
    d,d1 = np.unique(arr,return_counts=True)
    print(d,'去重元素的重复数量组成的数组：',d1)            #与去重数组对应
    pass

def a():
    arr = np.array([1,2,3,np.nan,4,5,6,np.nan,9])
    print('初始数组：',arr)
    print('去掉缺失值：',arr[~np.isnan(arr)])
    pass

#去除所有重复值
def b():
    arr = np.random.randint(0,15,size=(4,4))
    print('初始数组：',arr)
    un = np.unique(arr,return_counts=True)
    print('去除所有重复值(不包含有重复的数)：',un[0][un[1]==1])
    print('去除所有重复值：', np.array(set(arr.flatten().tolist())))
    pass

if __name__ == '__main__':
    b()