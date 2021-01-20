#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:Series

"""
Series是一种类似于一维数组的对象，
它由一组数据（各种NumPy数据类型）以及一组与之相关的数据标签（即索引）组成，即index和values两部分，
可以通过索引的方式选取Series中的单个或一组值。
索引(index)在左，数据(values)在右
索引是自动创建的
"""

import pandas as pd
import numpy as np
import string

#Series的创建
def A():
    """
    pd.Series(list,index=[ ])，第二个参数是Series中数据的索引，可以省略
    第一个参数可以是列表\ndarray等数据
    第一个参数可以是字典，字典的键将作为Series的索引
    第一个参数可以是DataFrame中的某一行或某一列
    """
    print('数组创建')
    arr = np.arange(1,10)
    s1 = pd.Series(arr)         #通过数组创建
    print(s1,'\n',type(s1))        #由于没有为数据指定索引，于是会自动创建一个0到N-1（N为数据的长度）的整数型索引

    print('列表创建')
    s2 = pd.Series(range(10))    #通过list构建Series，自动生成索引
    s3 = pd.Series(range(3),index=['a','b','c'])    #自定义索引
    print('自动生成索引：\n',s2) ; print('自定义索引：\n',s3)

    print('字典创建')
    dic = {'a':1,'b':2,'c':4,'d':3}     #通过字典创建，key为索引，value为元素。
    s4 = pd.Series(dic)
    print(s4)

    print('单个数据')
    s5 = pd.Series(1, index=list(range(4)), dtype='float32')
    print(s5)
    pass

#相关操作
def B():
    n = [a for a in range(1, 10)]
    a = string.ascii_lowercase
    dic = {n[i]: a[i] for i in range(0, 9)}
    s = pd.Series(dic)
    dic_ = {a[i]: n[i] for i in range(0, 9)}
    s_ = pd.Series(dic_)
    print(s)

    # series.head(n)，返回新Series，默认获取前五行
    print('获取前3行数据：',s.head(3))
    # series.tail(n)，返回新Series，默认获取后五行
    print('获取后3行数据：', s.tail(3))
    # series.index，获取索引
    print('获取索引：', s.index)
    # series.values，获取元素值
    print('获取元素值：', s.values)

    #运算
    print('翻倍：',s*2)    #返回新Series，索引不受影响（包括对应关系）
    print('比较：',s_>4)     #比较元素值，返回新的Series(bool)

    #索引
    print('索引：',s[3],s_['e'])   #返回对应的value值
    #切片
    print('切片：',s[2:5],s_['b':'f'])     #s_操作中按索引名切片时，是包含终止索引的
    #不连续索引
    print('不连续索引：',s[[1,3,5]],s_[['b','d','i']])
    #布尔索引
    s1 = s_ > 4
    print(s_[s1])

    #name属性
    print('name属性：',s.name,s.index.name)    #返回新Series

    pass

if __name__ == '__main__':
    A()