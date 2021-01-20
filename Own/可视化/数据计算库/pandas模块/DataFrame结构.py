#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:DataFrame

"""
DataFrame是一个表格型的数据结构，它含有一组有序的列，每列可以是不同类型的值。
既有行索引也有列索引，
它可以被看做是由Series组成的字典（共用同一个索引），
数据是以二维结构存放的，而不是列表、字典或别的一维数据结构。
"""
'''
类似多维数组/表格数据 (如，excel, R中的data.frame)
每列数据可以是不同的类型
索引包括列索引和行索引
'''

import pandas as pd
import numpy as np

#构建结构
def A():
    """
    pd.DataFrame(data,columns = [ ],index = [ ])
    columns和index为指定的列、行索引，并按照顺序排列，未指定则自动填充
    """
    #通过数组构建，只有数据（行列索引自动生成，可指定）
    arr = np.array([['qwe','rty','uio'],['asd','fgh','jkl'],['zxc','vbn','mp']])
    arr_pd = pd.DataFrame(arr,columns=['a','b','c'])
    print('数组构建：\n',arr_pd,'\n',pd.DataFrame(np.random.randn(4,3)))

    #通过字典构建，键为列索引，没有行索引（自动生成，可指定）
    print('字典构建：')
    dic = {
        'A': 1,
        'B': pd.Timestamp('20200707'),
        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
        'D': np.array([3] * 4, dtype='int32'),
        'E': ["Python", "Java", "C++", "C"],
        'F': 'tiger'
    }
    print(pd.DataFrame(dic))    #字典的键key为列标签（索引），值value为元素。自动生成行索引
    print(pd.DataFrame(dic,index=['a','b','c','d']))    #指定行标签。C列的原索引为0到3，此定义的行索引找不到，所以会在C列产生缺失值
    print(pd.DataFrame(dic,index=['a','b','c','d'],columns=['C','A','F','B','E','G','D']))      #创建时指定了columns和index索引，则按照索引顺序排列。传入的列找不到数据会产生缺失值。

    #通过嵌套字典创建，外层键为列索引，内层键为行索引
    print('嵌套字典构建：')
    d = {
        'a':{2:1.0,1:2.0,3:3.0},
        'b':{1:22,2:11,3:33},
        'c':{3:333,2:222,1:111}
    }
    print(pd.DataFrame(d))      #嵌套字典传给DataFrame，外层字典的键作为列，内层字典键则作为行索引
    p = pd.DataFrame(d)

    print('通过另一个DataFrame构建：')
    print(pd.DataFrame(p,index=[1,2,4]))          #索引会被沿用，除非显示指定其他索引
    pass

#索引、修改数据等
def B():
    arr = np.arange(1,21,dtype='f4').reshape(4,5)
    df = pd.DataFrame(arr,index=[1,2,3,4],columns=['a','b','c','d','e'])
    # print(df)

    #获取前n行。dataframe.head(n)，返回新Dataframe，默认获取前五行
    print('获取前2行：\n',df.head(2))
    # 获取后n行。dataframe.tail(n)，返回新Dataframe，默认获取后五行
    print('获取后2行：\n', df.tail(2))

    #获取行索引和列索引
    print('行索引：',df.index)
    print('列索引：', df.columns)

    #获取所有values。dataframe.values，返回一个二维数组
    print('所有values：\n',df.values)
    #获取列数据
    print('获取指定列数据：\n',df['b'],'\n',df.c)
    print('根据指定列生成新的dataframe：\n',df[['e']])    #只有一列，双重中括号
    #索引指定数据（根据行列索引具体数据，行在前。列在后）。loc根据行列标签索引查询，iloc根据默认生成的数字索引查询
    print('索引指定数据：',df.loc[2,'c'])
    print('查询多个行列：',df.loc[2,['a','c']])    #loc[[2,4],['b','d']]
    print('索引指定数据：',df.iloc[2,2])

    #增加或修改列数据，返回新的dataframe，类似dic的key-value
    df['f']=df['a']+100     #赋上一个整数、列表或数组（长度相匹配）、Series（会精确匹配索引，空位会填上缺失值）
    print(df)       #会直接改变原dataframe
    #修改某一元素
    print('修改指定元素：',df['b'][2]=666)     #df['列名'][行序号index]='新数据'
    #删除列数据，直接更改原dataframe
    del df['b']
    print('此时的列索引',df.columns)

    #不连续索引，返回一个新的dataframe
    print('不连续索引：',df[['a','e']])
    pass

#查看功能
def C():
    arr = np.arange(1, 21, dtype='f4').reshape(4, 5)
    df = pd.DataFrame(arr, index=[1, 2, 3, 4], columns=['a', 'b', 'c', 'd', 'e'])

    #查看维度，返回一个元组
    print('维度：',df.shape)
    #数据表基本信息
    print('查看基本信息',df.info)
    #查看列数据的格式
    print('每一列的格式：',df.dtypes) ; print('某一列的格式：',df['b'].dtype)
    #查看空值
    print('查看空值：',df.isnull())
    #查看某一列的唯一值
    print('查看唯一值：',df['b'].unique())
    pass

if __name__ == '__main__':
    C()

