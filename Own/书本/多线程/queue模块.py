#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:queue模块

from random import randint
from time import sleep
from queue import Queue
from mythread import MyThread
from atexit import register

def writeQ(qu):
    print('生产一个对象...')
    qu.put('xxx',1)     #将item放入到队列
    print('现在的队列大小：',qu.qsize())

def readQ(qu):
    val = qu.get(1)     #从队列中取得元素
    print('消耗一个对象')
    print('现在的队列大小：',qu.qsize())

def writer(qu,loops):
    for i in range(loops):
        writeQ(qu)
        sleep(randint(1,3))

def reader(qu,loops):
    for i in range(loops):
        readQ(qu)
        sleep(randint(2,5))

funcs = [writer,reader]
nfuncs = range(len(funcs))

def _main():
    nloops = randint(2,5)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i],(q,nloops),funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

@register
def _atexit():
    print('\nDone')

if __name__ == '__main__':
    _main()
