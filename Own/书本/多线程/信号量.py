#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:信号量

from random import randrange
from time import sleep,ctime
from atexit import register
from threading import BoundedSemaphore,Lock,Thread

# l = [randrange(2,5) for x in range(randrange(3,7))]     #随机生成3到6个在2到4之间的数
lock = Lock()
max = 5
candytray = BoundedSemaphore(max)       #糖果托盘(即，信号量)

def refill():
    lock.acquire()      #获取🔒
    print('添加糖果...')
    try:
        candytray.release()
    except ValueError:
        print('警告：糖果托盘已满')
    else:
        print('OK')
    lock.release()      #释放锁

def buy():
    #检测所有资源是否已消耗完（计数器的值不能小于0）
    lock.acquire()
    print('买走糖果...')
    #通过传入非阻塞的标志False，让调用不再阻塞，而在应当阻塞时返回一个False，指明没有更多的资源
    if candytray.acquire(False):
        print('OK')
    else:
        print('警告：糖果盘是空的')
    lock.release()

def producer(loops):        #生产
    for i in range(loops):
        refill()
        sleep(randrange(3))

def cunsumer(loops):        #消费
    for i in range(loops):
        buy()
        sleep(randrange(3))

def _main():
    print('开始于：',ctime())
    nloops = randrange(2,6)
    print('糖果盘最多能装{}个'.format(max))
    Thread(target=cunsumer,args=(randrange(nloops,nloops+max+2),)).start()
    Thread(target=producer, args=(nloops,)).start()

@register
def _atexit():      #注册一个退出函数，在程序退出时执行。（注意：需要提前导入该模块）
    print('结束于：',ctime())

if __name__ == '__main__':
    _main()
