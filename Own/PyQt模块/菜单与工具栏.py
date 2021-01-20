#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:2020.09.04
# Filename:菜单与工具栏

#QMainWindow 类提供了一个主要的应用程序窗口。你用它可以让应用程序添加状态栏,工具栏和菜单栏。

import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import QIcon

#状态栏
def a():
    '''
    QMainWindow类第一次调用statusBar()方法创建一个状态栏。
    后续调用返回的状态栏对象。
    showMessage()状态栏上显示一条消息。
    '''
    class example(QMainWindow):
        def __init__(self):
            super().__init__()
            self.initUI()
        def initUI(self):
            #用QMainWindow创建状态栏的小窗口
            self.statusBar().showMessage('ready')
            self.setGeometry(300,300,500,400)
            self.setWindowTitle('状态栏')
            self.show()
    app = QApplication(sys.argv)
    ex = example()
    sys.exit(app.exec_())
    return

#菜单栏
def b():
    class example(QMainWindow):
        def __init__(self):
            super().__init__()
            self.initUI()
        def initUI(self):
            #QAction可以操作菜单栏,工具栏,或自定义键盘快捷键
            #创建一个事件和一个特定的图标和一个“退出”的标签
            exitAction = QAction(QIcon('C:\\Users\\15394\\Desktop\\1.png'), '&Exit', self)
            #定义该操作的快捷键
            exitAction.setShortcut('Ctrl+Q')
            # 创建一个鼠标指针悬停在该菜单项上时的提示
            exitAction.setStatusTip('Exit application')
            exitAction.triggered.connect(qApp.quit)

            self.statusBar()

            # 创建一个菜单栏
            menubar = self.menuBar()
            # 添加菜单
            fileMenu = menubar.addMenu('&File')
            # 添加事件
            fileMenu.addAction(exitAction)

            self.setGeometry(300, 300, 300, 200)
            self.setWindowTitle('Menubar')
            self.show()

    app = QApplication(sys.argv)
    ex = example()
    sys.exit(app.exec_())
    return

#工具栏
def c():
    '''
    #创建一个工具栏，有一个关闭窗口的按钮
    '''
    class example(QMainWindow):
        def __init__(self):
            super().__init__()
            self.initUI()
        def initUI(self):
            #创建一个QAction事件。该事件有一个标签、图标和快捷键。退出窗口的方法
            exitAction = QAction(QIcon('C:\\Users\\15394\\Desktop\\1.png'), 'Exit', self)
            exitAction.setShortcut('Ctrl+Q')
            exitAction.triggered.connect(qApp.quit)

            self.toolbar = self.addToolBar('Exit')
            self.toolbar.addAction(exitAction)

            self.setGeometry(300, 300, 300, 200)
            self.setWindowTitle('Toolbar')
            self.show()

    app = QApplication(sys.argv)
    ex = example()
    sys.exit(app.exec_())
    pass

#集合
def d():
    class example(QMainWindow):
        def __init__(self):
            super().__init__()
            self.initUI()
        def initUI(self):
            textEdit = QTextEdit()
            self.setCentralWidget(textEdit)

            exitAction = QAction(QIcon(''),'Exit',self)
            exitAction.setShortcut('Ctrl+Q')
            exitAction.setStatusTip('Exit application')
            exitAction.triggered.connect(self.close)

            self.statusBar()

            menubar = self.menuBar()
            fileMenu = menubar.addMenu('&File')
            fileMenu.addAction(exitAction)

            toolbar = self.addToolBar('Exit')
            toolbar.addAction(exitAction)

            self.setGeometry(300,300,500,400)
            self.setWindowTitle('window')
            self.show()
    app = QApplication(sys.argv)
    ex =  example()
    sys.exit(app.exec_())
    pass

if __name__ == '__main__':
    d()