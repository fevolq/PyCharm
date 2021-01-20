#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:2020.09.04
# Filename:

import sys

##########
#所有的GUI程序都是事件驱动的。
# 事件主要由用户触发，但也可能有其他触发方式：例如网络连接，窗口管理器或计时器。
# 当我们调用QApplication的exec_（）方法时程序进入主循环。
# 主循环会获取并分配事件。

#在事件模型中，有三个参与者：
# 事件源：事件源是状态发生变化的对象。它会生成事件。事件（对象）封装了事件源中状态的移动
# 事件对象：事件接收者是要通知的对象。
# 事件接收者：事件源对象将事件处理的工作交给事件接收者。

#PyQt5有一个独特的signal＆slot（信号槽）机制来处理事件。
# 信号槽用于对象间的通信。
# signal在某些特定事件发生时被触发，slot可以是任何callable对象相连的插槽。
############

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

#信号槽
def a():
    class example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()
        def initUI(self):
            self.setGeometry(300,300,500,450)
            self.setWindowTitle('信号槽')
            self.show()
    app = QApplication(sys.argv)
    ex = example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    a()