#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:
# Filename:调用资源管理器选择路径或文件

'''
如：要保存一个文件时，想要用户自主选择保存路径时使用
'''

import tkinter as tk
from tkinter import filedialog

def select_path():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    Folderpath = filedialog.askdirectory()

    return Folderpath

path = select_path()
print(path)