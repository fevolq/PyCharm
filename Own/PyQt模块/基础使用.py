#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:2020.09.01
# Filename:PyQt的基础使用

import sys
# 提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import *

#创建界面
def a():
    # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)

    # QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
    w = QWidget()

    # resize()方法调整窗口的大小。这离是250px宽150px高
    w.resize(500, 500)

    # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
    w.move(300, 300)

    # 设置窗口的标题
    w.setWindowTitle('Example')

    # 显示在屏幕上
    w.show()

    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())
    pass

from PyQt5.QtGui import QIcon
#做图标 并使用类方法
def b():
    class Example(QWidget):

        def __init__(self):
            super().__init__()
            self.initUI()   #界面的绘制交给initUI方法

        def initUI(self):
            #设置窗口的位置和大小
            self.setGeometry(300,300,500,400)      #前面两个参数是窗口的位置，后面两个是窗口的大小
            #设置窗口的标题
            self.setWindowTitle('图标')
            #设置窗口的图标（引用指定目录下的图片）
            self.setWindowIcon(QIcon('C:\\Users\\15394\\Pictures\\Saved Pictures\\乖.jpg'))

            #显示窗口
            self.show()

    #创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    pass

from PyQt5.QtGui import QFont
#设置按键
def c():
    class Botton(QWidget):

        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            #创建一个按键
            btn = QPushButton('按钮',self)
            #按键的尺寸
            btn.resize(btn.sizeHint())      #默认尺寸
            #按键的位置
            btn.move(50,50)

            #这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
            QToolTip.setFont(QFont('SansSerif', 10))
            #创建一个提示，我们称之为settooltip()方法。我们可以使用丰富的文本格式
            self.setToolTip('This is a <b>botton</b>')
            #对按钮使用此提示（方法）
            btn.setToolTip('This is a <b>botton</b>')

            self.setGeometry(300,300,500,400)
            self.setWindowTitle('按键')
            self.setWindowIcon(QIcon('C:\\Users\\15394\\Pictures\\Saved Pictures\\乖.jpg'))
            self.show()

    app = QApplication(sys.argv)
    ex = Botton()
    sys.exit(app.exec_())
    pass

from PyQt5.QtCore import QCoreApplication
#设置离开按键
def d():
    class Quit(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()
        def initUI(self):
            q_btn = QPushButton('Quit',self)
            q_btn.clicked.connect(QCoreApplication.instance().quit)
            q_btn.resize(q_btn.sizeHint())
            q_btn.move(100,100)

            self.setGeometry(300,300,500,400)
            self.setWindowTitle('Quit')
            self.show()

    app = QApplication(sys.argv)
    ex = Quit()
    sys.exit(app.exec_())
    pass

#消息确认框
def e():
    #以退出按钮为例
    #关闭窗口的时候,触发了QCloseEvent。我们需要重写closeEvent()事件处理程序。
    class Mess(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()
        def initUI(self):
            self.setGeometry(500,300,600,600)
            self.setWindowTitle('Message box')
            self.show()
        #显示一个消息框,两个按钮:“是”和“不是”。
        # 第一个字符串出现在titlebar。第二个字符串消息对话框中显示的文本。
        # 第三个参数指定按钮的组合出现在对话框中。
        # 最后一个参数是默认按钮，这个是默认的按钮焦点。
        def closeEvent(self,event):
            reply = QMessageBox.question(self,'确认框',
                                         '确认退出吗？',
                                         QMessageBox.No | QMessageBox.Yes,
                                         QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
                # event.ignore()
            else:
                event.ignore()
    app = QApplication(sys.argv)
    ex = Mess()
    sys.exit(app.exec_())

#放至于中心
def f():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('中心')
    w.resize(500,500)

    a = w.frameGeometry()       #获得窗口
    b = QDesktopWidget().availableGeometry().center()       #获得屏幕中心点
    a.moveCenter(b)             #显示到屏幕中心

    w.show()
    sys.exit(app.exec_())
    return

def f1():
    class Ct(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()
        def initUI(self):
            self.resize(500,500)
            self.center()           #调用center()方法
            self.setWindowTitle('中心')
            self.show()

        def center(self):
            #获得窗口
            qr = self.frameGeometry()
            #获得屏幕中心点
            cp = QDesktopWidget().availableGeometry().center()
            #显示到屏幕中心
            qr.moveCenter(cp)
            self.move(qr.topLeft())

    app = QApplication(sys.argv)
    ex = Ct()
    sys.exit(app.exec_())
    pass

if __name__ == '__main__':
    f()