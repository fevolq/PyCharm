#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:

a = '123'       #str格式
print(type(a),'\n')

b = a.encode('utf-8')
print(type(b))          #<class 'bytes'>
print(b,'\n')           #b'123'         b代表byte

c = b.decode('utf-8')
print(type(c))          #<class 'str'>
print(c)                #123