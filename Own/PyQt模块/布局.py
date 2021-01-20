#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:2020.09.04
# Filename:页面布局

#布局有两种方式：绝对定位和布局类

import sys
from PyQt5.QtWidgets import *

#绝对定位
def a():
    """
    程序指定每个控件的位置和大小(以像素为单位)。

    绝对定位有以下限制:
    如果我们调整窗口，控件的大小和位置不会改变
    在各种平台上应用程序看起来会不一样
    如果改变字体，我们的应用程序的布局就会改变
    如果我们决定改变我们的布局,我们必须完全重做我们的布局
    """
    class Example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            lbl1 = QLabel('Zetcode', self)
            lbl1.move(15, 10)
            lbl2 = QLabel('tutorials', self)
            lbl2.move(35, 40)
            lbl3 = QLabel('for programmers', self)
            lbl3.move(55, 70)

            self.setGeometry(300, 300, 250, 150)
            self.setWindowTitle('绝对定位')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    return

#框布局
def b():
    """
    使用QHBoxLayout和QVBoxLayout，来分别创建横向布局和纵向布局。
    """
    class example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()
        def initUI(self):
            ok_btn = QPushButton('OK')
            cancel_btn = QPushButton('Cancel')
            #使用HBoxLayout和QVBoxLayout并添加伸展因子，在窗口的右下角显示两个按钮。
            h_box = QHBoxLayout()
            h_box.addStretch(1)
            h_box.addWidget(ok_btn)
            h_box.addWidget(cancel_btn)
            #创建一个水平布局和添加一个伸展因子和两个按钮。两个按钮前的伸展增加了一个可伸缩的空间。这将推动他们靠右显示。
            v_box = QVBoxLayout()
            v_box.addStretch(1)
            v_box.addLayout(h_box)
            #创建一个垂直布局，并添加伸展因子，让水平布局显示在窗口底部
            self.setLayout(v_box)

            self.setGeometry(300,300,500,450)
            self.setWindowTitle('框布局')
            self.show()

    app = QApplication(sys.argv)
    ex = example()
    sys.exit(app.exec_())
    return

#表格布局
def c():
    """
    表格布局将空间划分为行和列。我们使用QGridLayout类创建一个网格布局。
    """
    class example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()
        def initUI(self):
            #创建一个网格的按钮
            grid = QGridLayout()
            # 创建并设置应用程序窗口的布局
            self.setLayout(grid)
            #这些按钮的标签
            names = ['del','back','','close',
                     '7','8','9','/',
                     '4','5','6','*',
                     '1','2','3','-',
                     '0','.','=','+']
            #创建一个网格中的位置的列表
            positions = [(i,j) for i in range(5) for j in range(4)]
            #创建按钮并使用addWidget()方法添加到布局中。
            for position ,name in zip(positions,names):
                if name == '':
                    continue
                button = QPushButton(name)      #创建按钮
                grid.addWidget(button,*position)    #添加到布局

            self.move(300, 300)
            # self.setGeometry(300,300,500,400)
            self.setWindowTitle('表格布局')
            self.show()

    app = QApplication(sys.argv)
    ex = example()
    sys.exit(app.exec_())
    return

#表格布局中跨越多个行或列
def d():
    class example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()
        def initUI(self):
            title = QLabel('Title')
            author = QLabel('Author')
            review = QLabel('Review')

            titleEdit = QLineEdit()
            authorEdit = QLineEdit()
            reviewEdit = QTextEdit()
            #使用QGridLayout完成布局
            grid = QGridLayout()
            grid.setSpacing(10)
            #创建一个网格布局和设置在v见之间的间距
            grid.addWidget(title, 1, 0)
            grid.addWidget(titleEdit, 1, 1)

            grid.addWidget(author, 2, 0)
            grid.addWidget(authorEdit, 2, 1)

            grid.addWidget(review, 3, 0)
            grid.addWidget(reviewEdit, 3, 1, 5, 1)

            self.setLayout(grid)

            self.setGeometry(300, 300, 500, 400)
            self.setWindowTitle('跨越')
            self.show()
            pass
    app = QApplication(sys.argv)
    ex = example()
    sys.exit(app.exec_())
    return

if __name__ == '__main__':
    d()