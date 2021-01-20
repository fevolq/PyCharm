#!-*-coding:utf-8 -*-
#!@Author：fuq666@qq.com

import random
import string

def generate_txt(path):
    with open(path,'w+') as f:
        s1 = list(string.ascii_letters)     #所有大小写字母的合集
        s2 = [0,1,2,3,4,5,6,7,8,9]
        s2 = [str(i) for i in s2]
        s3 = ['\n',',','.','.','?','!',' ',' ',' ',]
        l = s1 + s2 + s3*2
        for i in range(10**5):
            f.write(random.choice(l))

def b(path,l):
    with open(path, 'w+') as f:
        for i in l:
            f.write(i)

if __name__ == '__main__':
<<<<<<< HEAD
    # path = 'C:\\Users\\15394\\Desktop\\正则.txt'
    path = '正则.txt'
=======
    path = 'C:\\Users\\15394\\Desktop\\正则.txt'
>>>>>>> bceee81269a20e23945060d8f405645e3a05a638
    generate_txt(path)
    print('Done')