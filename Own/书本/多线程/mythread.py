#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
<<<<<<< HEAD
#!Filename:从Thread派生出一个子类，用于被调用
=======
#!Filename:从Thread派生出一个子类，可以被调用
>>>>>>> bceee81269a20e23945060d8f405645e3a05a638

import threading
from time import sleep,ctime

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
<<<<<<< HEAD
        print('开始',self.name,'于：',ctime())
        self.res = self.func(*self.args)
        print(self.name,'结束于：',ctime())
=======
        print('starting',self.name,'at:',ctime())
        self.res = self.func(*self.args)
        print(self.name,'finisjed at:',ctime())
>>>>>>> bceee81269a20e23945060d8f405645e3a05a638
