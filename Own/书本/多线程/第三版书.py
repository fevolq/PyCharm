#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:多线程练习题

#4-4
#a
def a_get_number(s,path):
    st = ''
    with open(path,'r') as f:
        l = f.readlines()
    for i in l:
        st += i
    num = st.count(s)        #字符串st中有多少个字符s
    return num

def a_4_4():
    s = input('输入一个字母：')
    path = 'C:\\Users\\15394\\Desktop\\test.txt'
    num = a_get_number(s, path)
    print(num)

if __name__ == '__main__':
    a_4_4()