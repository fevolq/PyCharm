#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:
# Filename:（批量）更改文件的名称或后缀

"""
指定文件夹路径path
更改文件后缀：which改为'1'，last为文件旧后缀
            new改为新后缀。如：.txt文件改为.mp4文件，则指定last='.txt'，new='.mp4'
            执行顺序：先判断文件的后缀是否为last，是则更改后缀为new，否则pass。
更改文件名称：which改为'2'或'3'，last为文件后缀
            选取旧名称的片段：which='2'，更改a,b。如：旧名称'gawr[ar42]awr'改为'ar42'，则a='['，b=']'
            指定新名称：which='3'，new改为指定的名称。如：指定new为'abc'，则会将文件名改为abc1,abc2,···
注：path,last都相关，which用于判断，new,a,b则为使用数据。
"""

import os,shutil

#找出指定文件夹内的所有文件的绝对路径，以列表形式
def get_files(path):
    """
    ['F:\\新建文件夹\\ha.txt', 'F:\\新建文件夹\\heth.txt', 'F:\\新建文件夹\\myrw.txt']
    """
    l = os.listdir(path)
    # print(l)
    workdir = os.path.abspath(path)
    # print(workdir)
    files = [os.path.join(workdir, i) for i in l]
    # print(files)
    return files,workdir

#改变文件的名称
def ChangeName(file,workdir,last,new=0,a=0,b=0):
    """
    选取原有名称中的一部分作为新名称
    如：原名称：123qwe456
    则，新名称：qwe或3qw或其他
    """
    if new == 0:    #选取
        oldname = file
        if a in file and b in file:
            try:
                one = file.index(a)
                two = file.index(b)
                new_name = file[one + 1:two] + last
                new_name = os.path.join(workdir, new_name)
                shutil.move(oldname, new_name)
            except:
                print('错误的文件：', file)
                pass
        else:
            pass
    else:       #新名称
        global i
        oldname = file
        new_name = new + str(i) + last
        new_name = os.path.join(workdir, new_name)
        shutil.move(oldname, new_name)
        pass
    return

#更改后缀
def ChangeLast(file,workdir,new,last):
    oldname = file
    if last in file:
        try:
            # l = len(last)
            if last == file[len(file)-len(last):len(file)]:     #判断指定后缀的文件
                new_name = file[0:-len(last)] + new
                new_name = os.path.join(workdir, new_name)
                shutil.move(oldname, new_name)
            else:
                pass
        except:
            print('错误的文件：', file)
    else:
        pass

def main(path,which,last,new='0',a='0',b='0'):
    g = get_files(path)
    files = g[0]
    workdir = g[1]
    if which == '1':    #改后缀
        for file in files:
            ChangeLast(file,workdir,new,last)
    else:           #改后缀
        for file in files:
            if which == '2':  # 选取旧名称片段（使用a,b）
                ChangeName(file, workdir, last, a=a, b=b)
            elif which == '3':  # 指定新名称（使用new）
                global i
                ChangeName(file, workdir, last, new=new)
                i += 1
            else:
                pass
    return

if __name__ == '__main__':
    path = r'F:\Own\new\18'
    which = '2'     # 1更改后缀，2选取旧名称片段，3改为新名称
    last = '.mp4'   # 旧后缀
    new = '.txt'    # 新后缀 或 新名称
    a = '《'
    b = '》'
    if which == '1':
        main(path,which,last,new=new)
    else:
        i = 1
        main(path, which, last, new=new, a=a, b=b)
