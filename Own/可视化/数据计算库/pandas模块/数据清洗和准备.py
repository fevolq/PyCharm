#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:

import numpy as np
import pandas as pd

arr = np.array([
    ['北京',100.0,77,'a'],
    ['武汉',111.1,66,'c'],
    ['杭州',222.2,88,'c'],
    ['深圳',111.1,88,'e'],
    ['成都',444.4,55,'b']
])
df = pd.DataFrame(arr,index=['c1','c2','c3','c4','c5'],
                  columns=['城市','环境','分数','排名'])

dic = {
        'id':[1,2,3,4,5],
        'city':['北京','上海','武汉','杭州','广州'],
        'age':[30,28,21,24,27],
        'ctg':['省','市','市','市','省'],
        'gender':['A','B','E','D','C']
    }
df_1 = pd.DataFrame(dic)

#处理数据缺失
def A():
    """
    .info()：查看数据的信息，包括每个字段的名称、非空数量、字段的数据类型。
    .isnull()：返回一个同样长度的值为布尔型的对象（Series或DataFrame），表示哪些值是缺失的，.notnull()为其否定形式
    """
    se = pd.Series(['abc','def',np.nan,None])
    # print(se)
    print('是否有缺失值：',se.isnull())

    '''
    .dropna()：删除缺失数据，返回新的对象，不改变原对象。
    对于Series对象，dropna返回一个仅含非空数据和索引值的Series。
    对于DataFrame对象，dropna默认删除含有缺失值的行；
        如果想删除含有缺失值的列，需传入axis = 1作为参数；
        如果想删除全部为缺失值的行或者列，需传入how='all'作为参数；
        如果想留下一部分缺失数据，需传入thresh = n作为参数，表示每行至少n个非NA值
    '''
    df_a = pd.DataFrame([[1.,6.5,3.],[1.,np.nan,np.nan],[np.nan,np.nan,np.nan],[np.nan,6.5,3.]])
    print('初始df：',df_a)
    print('删除含有缺失值的行：\n',df_a.dropna())
    print('删除全部为缺失值的行：\n',df_a.dropna(how='all'))

    df_a[4] = np.nan
    # print(df)
    print('删除全部为缺失值的列：\n',df_a.dropna(axis=1,how='all'))
    print('每行至少有两个非缺失值：\n',df_a.dropna(thresh=2))

    '''
    .fillna(value,method,limit,inplace)：填充缺失值。
        value为用于填充的值（比如0、'a'等）或者是字典（比如{'列':1,'列':8,……}为指定列的缺失数据填充值）；
        method默认值为ffill，向前填充，bfill为向后填充；
        limit为向前或者向后填充的最大填充量；
        inplace默认会返回新对象，修改为inplace=True可以对现有对象进行就地修改。
    '''

    pass

#数据转换
def B():
    #替换值
    #.replace(old,new)。若要一次性替换多个值，使用列表。
    #默认返回一个新对象，传入inplace=True可以对现有对象进行就地修改。

    #删除重复数据
    #.duplicated()：判断各行是否是重复行（前面出现过的行），返回一个布尔型Series
    #.drop_duplicates()：删除重复行，返回删除后的DataFrame对象。默认保留的是第一个出现的行，传入keep='last'作为参数后，则保留最后一个出现的行
    #两者都默认会对全部列做判断，在传入列索引组成的列表[ '列1' , '列2' , ……]作为参数后，可以只对这些列进行重复项判断

    #利用函数或字典进行数据转换
    #Series.map()：接受一个函数或字典作为参数。使用map方法是一种实现元素级转换以及其他数据清理工作的便捷方式
    pass

#数据提取
def C():
    """
    主要用到的三个函数：loc,iloc和ix，
    loc函数按标签值进行提取，iloc按位置进行提取，ix可以同时按标签和位置进行提取
    """
    df_c = pd.DataFrame(arr,columns=['城市','环境','分数','排名'])
    #按索引提取单行数值
    print('按索引提取单行：',df.loc['c3'])
    #按索引提取区域行数值
    print('按索引提取区域行：',df.iloc[0:2])
    #使用iloc按位置区域提取数据
    print('按位置区域提取数据：',df.iloc[:3,:2])
    #使用iloc按位置单独提起数据
    print('按位置单独提起数据：',df.iloc[[0,2,4],[1,3]])      #提取第1、3、5行，2、4列的数据
    #判断city列的值是否为北京
    print('判断列的值：',df['分数'].isin(['77','88']))
    #判断指定列里是否包含指定数据，然后将符合条件的数据提取出来
    print('提取符合条件的数据：',df.loc[df['分数'].isin(['77','88'])])
    pass

#数据筛选
def D():
    """
    使用与、或、非三个条件配合大于、小于、等于对数据进行筛选，并进行计数和求和
    """
    #“与”筛选
    print('与：\n',df_1.loc[(df_1['age']>25) & (df_1['city']=='上海'),['id','city','age','ctg','gender']])
    #“或”筛选
    print('或：\n',df_1.loc[(df_1['age']>25) | (df_1['ctg']=='市')])
    #“非”筛选
    print('非：\n',df_1.loc[(df_1['city'] != '北京')])
    #对筛选后的数据按列进行计数
    print('筛选后按列计数：\n',df_1.loc[(df_1['city'] != '北京')].ctg.count())
    #使用query函数进行筛选
    print('query筛选：\n',df_1.query("city==['北京','武汉']"))
    #对筛选后的结果按prince进行求和
    print('对结果按指定列求和：\n',df_1.query("city==['北京','武汉']").age.sum())
    pass

#数据汇总
def E():
    """
    主要函数是groupby和pivote_table
    """
    #对所有列进行计数汇总
    print('计数汇总：\n',df_1.groupby('ctg').count())
    #按城市对id字段进行计数
    print('按某字段对另一字段进行计数：\n',df_1.groupby('ctg')['id'].count())
    #对两个字段进行汇总计数
    print('对两个字段进行汇总计数：\n',df_1.groupby(['city','gender'])['id'].count())
    #对某字段进行汇总，并分别计算另一个字段的合计和均值
    print('合计和均值：\n',df_1.groupby('city')['age'].agg([len,np.sum,np.mean]))
    pass

if __name__ == '__main__':
    E()