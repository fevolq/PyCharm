#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:
# Filename:将文件夹内的文件按一定数量分成多个文件夹存放

"""
如：[1,2,3,4,5,6,7,8,9,a,b,c,q,w,ea,sd,]
存储为[1,2,3],[4,5,6],[7,8,9],[a,b,c],[q,w,ea],[sd]
"""

import os,shutil

#文件地址
def get_path(path):
    # path = r'E:\Music\音乐1'
    l = os.listdir(path)
    workdir = os.path.abspath(path)
    files = [os.path.join(workdir, i) for i in l]
    # print(l,'\n',workdir,'\n',files)
    return l,files

#进行移动
def move(path,n,l,files):
    i = 1
    while i <= len(l)//n + 1:
        new_path = path + '\\' + str(i)
        os.makedirs(new_path)
        workdir = os.path.abspath(new_path)
        # print(workdir)
        num = (i-1)*n + 0
        while num< n*i:
            file = os.path.join(workdir,l[num])
            # print(file)
            shutil.move(files[num],file)
            num += 1
            if num == len(l):
                break
        i += 1

def main(path,n):
    f = get_path(path)
    l = f[0]
    files = f[1]
    move(path,n,l,files)

if __name__ == '__main__':
    path = r'C:\Users\15394\Desktop\音乐1'   #文件夹地址
    n = 50      #每份包含多少个文件
    main(path,n)
    print('Done')
