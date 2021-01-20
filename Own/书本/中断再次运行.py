#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:用于测试某些代码的功能

from 爬虫.文本 import txt as t

path = 'C:\\Users\\15394\\Documents\\Spider'
url = 'https://www.114txt.cc/0/580/'
n = 87

while True:
    i = t.main_other(n,url,path)
    if i:       #主程序中断
        print('主程序异常')
        n = i
    else:
        break

print('\nDone')
