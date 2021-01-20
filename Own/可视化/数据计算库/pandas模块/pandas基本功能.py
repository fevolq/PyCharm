#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:杂项

import pandas as pd
import numpy as np
import os

arr = np.array([
    ['北京',100.0,77,'a'],
    ['武汉',111.1,66,'c'],
    ['杭州',222.2,88,'c'],
    ['深圳',333.3,88,'e'],
    ['成都',444.4,55,'b']
])
df = pd.DataFrame(arr,index=['c1','c2','c3','c4','c5'],
                  columns=['城市','环境','分数','排名'])

#存储读取文件
def File(df):
    def save(df):
        """
        将DataFrame存储到csv文件，index表示是否显示行名(没有则默认为True)
        如果希望在不覆盖原文件内容的情况下将信息写入文件，可以加上mode="a"
        """
        path = 'C:\\Users\\15394\\Desktop\\'
        df.to_csv(path + 'test.csv',index=False,sep='|',mode='a')
        #df.to_excel(path + 'test.xlsx',index=False,)，保存为xlsx文件
        print('Done\n')
        return True

    def read():
        """
        读取csv文件中的数据
        """
        file_path = os.path.join('C:\\Users\\15394\\Desktop\\test.csv')
        data = pd.read_csv(open(file_path,'r',encoding='utf-8'),sep='|')
        name_list = []
        for column,row in data.iterrows():
            name_list.append(row['城市'])
            print(row['城市'])
        print(name_list)
        pass

    if save(df):
        read()
    pass

#遍历数据
def A():
    for index,row in df.iterrows():
        # print(index)
        # print(row)
        print(row['城市'])
    pass

#合并
def B():
    """
    一般方法有concat、join、merge
    pd.concat(objs, axis=0, join=‘outer’, join_axes=None, ignore_index=False,
                keys=None, levels=None, names=None, verify_integrity=False)
    objs：series，dataFrame或者是panel构成的序列list。
    axis：需要合并链接的轴，0是行，1是列。
    join： 连接的方式 inner，或者outer。
    """
    arr1 = [['a0','b0','c0','d0'],['a1','b1','c1','d1'],['a2','b2','c2','d2'],['a3','b3','c3','d3']]
    arr2 = [['a4','b4','c4','d4'],['a5','b5','c5','d5'],['a6','b6','c6','d6'],['a7','b7','c7','d7']]
    arr3 = [['a8','b8','c8','d8'],['a9','b9','c9','d9'],['a10','b10','c10','d10'],['a11','b11','c11','d11']]
    arr4 = [['b2','d2','f2'],['b3','d3','f3'],['b6','d6','f6'],['b7','d7','f7']]
    df1 = pd.DataFrame(arr1,index=[0,1,2,3],columns=['a','b','c','d'])
    df2 = pd.DataFrame(arr2, index=[4, 5, 6, 7], columns=['a','b','c','d'])
    df3 = pd.DataFrame(arr3, index=[8, 9, 10, 11], columns=['a','b','c','d'])
    df4 = pd.DataFrame(arr4,index=[2,3,6,7],columns=['b','d','f'])

    #concat属性
    #相同字段表首尾相接
    frames1 = [df1,df2,df3]
    result1 = pd.concat(frames1)
    # print(result1)
    #横向拼接（行对齐）
    frames2 = [df1,df4]
    result2 = pd.concat(frames2,axis=1)
    # print(result2)

    #join属性
    #inner，两表交集；outer，两表并集
    result3 = pd.concat(frames2,axis=1,join='inner')
    result4 = pd.concat(frames2, axis=1, join='outer')
    result5 = pd.concat(frames2, axis=0, join='inner')
    # print('行索引交集：\n',result3) ; print('列索引交集：\n',result5)
    # print('并集：\n',result4)
    #join_axes，指定根据那个轴对齐数据
    #join_axes  ??????

    #merge属性
    df_inner = pd.merge(df1,df4,how='inner')
    print('交集：',df_inner)       #行索引相同
    df_outer = pd.merge(df4,df1,how='outer')
    print('并集',df_outer)        #第一个的列索引在前，行索引自动生成
    df_left = pd.merge(df1,df4,how='left')
    print('左匹配：',df_left)
    df_right = pd.merge(df1, df4, how='right')
    print('右匹配：',df_right)
    pass

#排序
def C():
    """
    sort_values(by, ascending)
    by：列名，依旧该列进行排序
    ascending：确定排序方式，默认为True（降序）
    """
    print(df.sort_values(by='分数',ascending=True))
    pass

#删除指定行列
def D():
    """
    默认返回的是一个新对象。
    .drop()：能够删除Series和DataFrame指定行或列索引。
    删除一行或者一列时，用单引号指定索引，删除多行时用列表指定索引。
    如果删除的是列索引，需要增加axis=1或axis='columns'作为参数。
    增加inplace=True作为参数，可以就地修改对象，不会返回新的对象
    """
    print('删除行：',df.drop('c4'))
    print('删除列：',df.drop('环境',axis=1))

    '''
    改变、重排Series和DataFrame索引，会创建一个新对象，如果某个索引值当前不存在，就引入缺失值。
    df.reindex(index, columns ,fill_value, method, limit, copy )
    index/columns为新的行列自定义索引；fill_value为用于填充缺失位置的值；
    method为填充方法，ffill当前值向前填充，bfill向后填充；
    limit为最大填充量；copy 默认True，生成新的对象，False时，新旧相等不复制。
    '''
    nc = df.columns.delete(2)
    ni = df.index.insert(5,'c0')
    nd = df.reindex(index=ni,columns=nc).ffill()
    print('重构：',nd)
    pass

#算数运算
def E():
    """
    算术运算根据行列索引，对齐后运算，运算默认产生浮点数，对齐时缺项填充NaN (空值)。
    add加法(+)，sub减法(-)，mul乘法(*)，div除法(/)，floordiv底除(//)，pow指数(**)
    """
    pass

#其他
def F():
    df_f = pd.DataFrame([[1.,6.5,3.],[2.,np.nan,np.nan],[np.nan,np.nan,np.nan],[np.nan,6.5,3.]])
    #用数字0填充空值
    print(df_f.fillna(value=0))
    #使用列prince的均值对NA进行填充
    print(df_f[0].fillna(df_f[0].mean()))
    #大小写转换(换成大写：upper；换成小写：lower)
    df['排名'] = df['排名'].str.upper()
    print('大小写转换：',df)
    #更改数据格式
    print('更改数据格式：',df['分数'].astype('float'))
    #更改列名称
    print('更改列名称：',df.rename(columns={'环境':'大小'}))
    #删除后出现的重复值
    print('删除后出现的重复值：',df['环境'].drop_duplicates())
    # 删除先出现的重复值
    print('删除先出现的重复值：', df['环境'].drop_duplicates(keep='last'))
    #数据替换
    print('数据替换：',df['城市'].replace('深圳','广州'))
    pass

if __name__ == '__main__':
    B()