#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:

import numpy as np

#返回四舍五入到所需精度的值
def a():
    """
    numpy.around(arr,decimals)
    #arr:输入数组
    #decimals:要舍入的小数位数。若为负，整数将四舍五入到小数点左侧的位置
    """
    a = 1.042642
    b = [1.03642,7.345,2.9999]
    c = np.array([4.216,6.345,87.6741])
    print(np.around(a,2))
    print(np.around(b,2))
    print(np.around(c,2))
    print(np.around(572.645,-2))
    pass

#返回不大于输入参数的最大整数and返回输入值的上限
def b():
    arr = np.array([-1.6,0.6,-0.3,6.8,9])
    print('小于的整数：',np.floor(arr))
    print('大于的整数：',np.ceil(arr))
    pass

#算数
def c():
    #输入数组必须有相同的形状或符合数组广播规则
    a = np.arange(4,dtype=np.float_).reshape(2,2)
    b = np.array([10,10])
    # print(a,b)
    print('数组相加：',np.add(a,b))
    print('数组相减：',np.subtract(a,b))
    print('数组相乘：',np.multiply(a,b))
    print('数组相除：',np.divide(a,b))

    arr = np.array([1,2,3,4])
    print('幂运算：',np.power(arr,2))    #将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂

    c = np.array([10,20,30]) ; d = np.array([3,5,7])
    print('除法余数：',np.mod(c,d))      #返回输入数组中相应元素的除法余数
    pass

#复数
def d():
    """
    numpy.real()	返回复数类型参数的实部
    numpy.imag()	返回复数类型参数的虚部
    numpy.conj()	返回通过改变虚部的符号而获得的共轭复数
    numpy.angle()	返回复数参数的角度。 函数的参数是degree。 如果为true，返回的角度以角度制来表示，否则为以弧度制来表示
    """
    arr = np.array([-5.6j, 0.2j, 11., 1+1j])
    print('实部：',np.real(arr))
    print('虚部：', np.imag(arr))
    print('共轭：', np.conj(arr))
    print('角度：', np.angle(arr))
    print('角度制：', np.angle(arr,deg=True))
    pass

#统计方法
def e():
    """
    numpy.amin()	从给定数组中的元素沿指定轴返回最小值
    numpy.amax()	从给定数组中的元素沿指定轴返回最大值
    numpy.ptp()	    返回沿轴的值的范围(最大值 - 最小值)
    numpy.percentile()	百分位数是统计中使用的度量，表示小于这个值得观察值占某个百分比
    numpy.median()	定义为将数据样本的上半部分与下半部分分开的值
    numpy.mean()	返回数组中元素的算术平均值
    numpy.average()	根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值
    标准差	        标准差是与均值的偏差的平方的平均值的平方根
    """
    arr = np.array([[3,7,5],[8,4,3],[2,4,9]])
    #axis = 1，指的是沿着行求所有列，代表了横轴
    # axis = 0，就是沿着列求所有行，代表了纵轴。
    print('最小值和最大值：')
    print(np.amin(arr,0)) ; print(np.amin(arr,1),'\n')      #arr.argmin()最小值的下标
    print(np.amax(arr,0)) ; print(np.amax(arr,1),'\n')      #arr.argmax()最大值的下标

    # 不传轴的时候默认返回所有数据的对比；对比纵轴；对比横轴
    print('值的范围(最大值-最小值)：')
    print(np.ptp(arr)) ; print(np.ptp(arr,0)) ; print(np.ptp(arr,1),'\n')

    #numpy.percentile(arr, q, axis)
    #百分位数是统计中使用的度量，表示小于这个值得观察值占某个百分比
    #q 要计算的百分数，在0 ~ 100间
    #axis 沿着它计算百分位数的轴
    arr = np.array([[30,40,70],[80,20,10],[50,90,60]])
    # print(arr)
    print('百分位数：')
    print(np.percentile(arr,50))
    print(np.percentile(arr, 50,axis=1)) ; print(np.percentile(arr, 50,axis=0),'\n')

    #numpy.median(arr, axis)定义为将数据样本的上半部分与下半部分分开的值
    print('中间值：')
    print(np.median(arr))       #即位于指定轴的所有数据的中间值
    print(np.median(arr,axis=1)) ; print(np.median(arr,axis=0),'\n')

    #numpy.mean(arr, axis)返回数组中元素的算术平均值
    print('算数平均值：')
    print(np.mean(arr))
    print(np.mean(arr,axis=1)) ; print(np.mean(arr,axis=0),'\n')

    # 标准差：标准差是与均值的偏差的平方的平均值的平方根
    print('标准差：')
    print(np.std([1, 2, 3, 4]))

    # 方差：方差是偏差的平方的平均值。标准差是方差的平方根
    print('方差：')
    print(np.var([1, 2, 3, 4]),'\n')

    #numpy.average(arr,weights,returned)根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值
    #weights：指定权重
    #returned：参数为True，则返回权重的和。默认为False
    #加权平均值是由每个分量乘以反映其重要性的因子得到的平均值
    print('加权平均值：')
    a = np.array([1,2,3,4]) ; wts = np.array([4,3,2,1])
    print(np.average(a))    #不指定权重时相当于 mean 函数
    print('指定权重时：',np.average(a,weights=wts))
    print('权重的和：',np.average(a,weights=wts,returned=True),'\n')

    pass

#排序
def f():
    """
    numpy.sort(arr, axis, kind, order)返回输入数组的排序副本
    # arr 要排序的数组
    # axis 沿着它排序数组的轴，如果没有数组会被展开，沿着最后的轴排序
    # kind 默认为'quicksort'(快速排序)
    # order 如果数组包含字段，则是要排序的字段
    """
    arr = np.array([
        [3,7],[9,1],[6,6]
    ])
    print(arr)
    arr_sort = np.sort(arr)
    print('调用sort()函数：',arr_sort)
    # print(arr)      #不改变原始数组
    print('沿轴0排序',np.sort(arr,axis=0))

    dt = np.dtype([('name','S10'),('age',int)])
    arr_1 = np.array([('dga',20),('adh',23),('dar',18)],dtype=dt)       #创建时注意指定dtype
    print(arr_1)
    print('按name排序：',np.sort(arr_1,order='name'))


    #numpy.argsort()对输入数组沿给定轴执行间接排序，并使用指定排序类型返回数据的索引数组。
    a = np.array([6,2,9])
    print('初始数组：',a)
    b = np.argsort(a)
    print('排序后的元素对应初始数组的索引数组：',b)
    print('根据索引数组重构原始数组：',a[b])     #按排序后的顺序
    print('原始数组：',a)        #表明排序不改变初始数组

    #numpy.lexsort()函数使用键序列执行间接排序
    pass

#线性代数
def g():
    #矩阵乘法、矩阵分解、行列式以及其他方阵数学等
    a = np.array([[1,2,3],[4,5,6]])
    b = np.array([[6,23],[-1,7],[8,9]])
    print('点积：',a.dot(b))     #点积。m行k列的数组 点乘 k行n列的数组，得到一个m行n列的数组。（k必须对应相等）
    print('多维·一维：',np.dot(a,np.ones(3)))   #多维乘以一维，得到一维数组
    '''
    diag	以一维数组的形式返回方阵的对角线(或非对角线)元素，或将一维数组转换为方阵(非对角线元素为0)
    dot	    矩阵乘法
    trace	计算对角线元素和
    det	    计算矩阵行列式
    eig	    计算方阵的本征值和本征向量
    inv	    计算方阵的逆
    pinv	计算方阵的Moore-Penrose伪逆
    qr	    计算QR分解
    svd	    计算奇异值分解(SVD)
    solve	解线性方程组Ax=b，其中A为一个方阵
    lstsq	计算Ax=b的最小二乘解
    '''
    pass

#三角函数
def h():
    pass

#类似数组（相同形状，不同数据）
def i():
    """
    empty_like	返回形状和类型与给定数组相同的新数组。(值为内存中的原垃圾值)
    ones_like	返回形状与类型与给定数组相同的数组。(1填充)
    zeros_like	返回形状与类型与给定数组相同的数组。(0填充)
    """
    arr = np.arange(9).reshape(3,3)
    print('垃圾值：',np.empty_like(arr))
    print('1填充：', np.ones_like(arr))
    print('0填充：', np.zeros_like(arr))
    pass

#随机创建
def j():
    """
    np.random.randint(start, end, size)创建基于随机的数组
    start - 随机范围的下边界
    end - 随机范围的上边界
    size - 随机结果的形态
    """
    arr = np.random.randint(5,15,size=(4,4))
    print(arr)      #元素为5到15(不包含)内，shape为(4,4)

    arr_1 = np.random.normal(size=(4,4))
    print('正态（高斯）分布样本值：',arr_1)

    '''
    seed	    确定随机数生成器的种子
    permutation	返回一个序列的随机排列
    shuffle	    对一个序列就地随机排列
    rand	    产生均匀分布的样本值
    randint	    给定的上下限范围内随机选取整数
    randn	    产生正态分布(平均值为0，标准差为1)的样本值，类似于MATLAB接口
    binomial	产生二项分布的样本值
    normal	    产生正态(高斯)分布的样本值
    beta	    产生Beta分布的样本值
    chisquare	产生卡方分布的样本值
    gamma	    产生Gamma分布的样本值
    uniform	    产生在[0, 1)中均匀分布的样本值
    '''
    pass

#对角创建
def k():
    """
    np.eye(N, M=None, k=0, dtype=float, order='C')
    创建一个类单位矩阵，即对角线上为1，其余为0的数组。指定形状即可创建
    N - 输出的行数
    M - 输出的列数。如果为空，默认大小等于N
    k - 设定对角线索引位置。默认为主对角线，即0。正值，是上对角线；负值是下对角线。
    dtype - 指定填充值的数据类型
    order - 在内存中存储是否以行为主的C风格或者以列为主的Fortran风格
    """
    arr = np.eye(5)
    arr_1 = np.eye(5,k=-2)
    arr_2 = np.eye(5,k=2)
    print('不偏移:\n',arr) ; print('左移:\n',arr_1) ; print('右移:\n',arr_2)
    pass

if __name__ == '__main__':
    g()