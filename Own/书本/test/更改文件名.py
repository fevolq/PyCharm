#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:批量更改文件名

import shutil,os

path = r'C:\Users\15394\Desktop\新建文件夹'

OldNamelist = os.listdir(path)    #返回指定路径中包含的文件的名称（已字符串列表形式）

for OldName in OldNamelist:
    print(OldName)
    NewName = 'something' + OldName

    workingDir = os.path.abspath(path)
    old = os.path.join(workingDir,OldName)
    new = os.path.join(workingDir,NewName)
    shutil.move(old,new)        #执行更改的操作

print('\nDone')
