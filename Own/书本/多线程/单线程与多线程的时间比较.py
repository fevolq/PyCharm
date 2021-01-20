#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:单线程与多线程的时间比较

from mythread import MyThread
from time import sleep,ctime

def fib(x):     #斐波那契数列递归
    sleep(0.005)
    if x < 2:
        return 1
    return (fib(x-2) + fib(x-1))

def fac(x):     #x的阶乘
    sleep(0.1)
    if x<2:
        return 1
    return (x*fac(x-1))

def sum(x):     #x至1的累加
    sleep(0.1)
    if x<2:
        return 1
    return (x+sum(x-1))

funcs = [fib,fac,sum]
n = 12

def main():
    nfuncs = range(len(funcs))

    print('***单线程***')
    for i in nfuncs:
        print('starting',funcs[i].__name__,'at:',ctime())
        print(funcs[i](n))      #运行函数
        print(funcs[i].__name__,'finished at:',ctime())

    print('\n***多线程***')
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i],(n,),funcs[i].__name__)       #创建线程
        threads.append(t)

    for i in nfuncs:
        threads[i].start()      #同步开始线程

    for i in nfuncs:
        threads[i].join()
        print(threads[i].getResult())      #返回线程的结果

    print('all Done')

if __name__ == '__main__':
    main()