#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:threading模块种的Thread的3种多线程的使用

import threading
from time import sleep,ctime
#不使用线程
def loop0():
    print('start loop 0 at：{}'.format(ctime()))
    sleep(4)
    print('loop 0 done at：{}'.format(ctime()))
def loop1():
    print('start loop 1 at：{}'.format(ctime()))
    sleep(2)
    print('loop 1 done at：{}'.format(ctime()))
def main():
    print('Strating at：{}'.format(ctime()))
    loop0()
    loop1()
    print('all Done at：{}'.format(ctime()))

#创建一个Thread实例，传给它一个函数
loops = [4,2]
def loop_1(nloop,nsec):
    print('start loop',nloop,'at:',ctime())
    sleep(nsec)
    print('loop',nloop,'done at:',ctime())
def main1():
    print('Starting at:',ctime())
    threads = []
    nloops = range(len(loops))

    #创建多个线程实例，但不开始运行（同步特性）
    for i in nloops:
        #创建Thread实例，传给它一个函数
        t = threading.Thread(target=loop_1,args=(i,loops[i]))     #target传入函数名，args传入参数。
        threads.append(t)

    #将每个线程都开始（同步）运行
    for i in nloops:
        threads[i].start()      #开始线程的执行

    for i in nloops:
        threads[i].join()       #确保所有线程结束或者超时，才会继续执行主线程

    print('all Done at:',ctime())

#创建一个Thread实例，传给它一个可调用的类对象。（更具面向对象的概念，当有多个函数需要线程时，更加的通用）
class ThreadFunc:   #自己创建的一个可被调用的类
    def __init__(self,func,args,name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        # apply(self.func,self.args)
        self.res = self.func(*self.args)
def loop_2(nloop,nsec):
    print('start loop',nloop,'at:',ctime())
    sleep(nsec)
    print('loop',nloop,'done at:',ctime())
def main2():
    print('Starting at:',ctime())
    threads = []
    nloops = range(len(loops))

    #创建多个线程实例，但不开始运行（同步特性）
    for i in nloops:
        #创建Thread实例，传给它一个可调用的类对象
        t = threading.Thread(target=ThreadFunc(loop_2,(i,loops[i]),loop_2.__name__))     #target传入自己创建的类名。
        threads.append(t)

    #将每个线程都开始（同步）运行
    for i in nloops:
        threads[i].start()      #开始线程的执行

    for i in nloops:
        threads[i].join()       #确保所有线程结束或者超时，才会继续执行主线程

    print('all Done at:',ctime())

#从Thread派生出一个子类，创建一个这个子类的实例
class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.res = self.func(*self.args)
def loop_3(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())
def main3():
    print('starting at:',ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop_3,(i,loops[i]),loop_3.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print('all Done at:',ctime())

if __name__ == '__main__':
    main3()