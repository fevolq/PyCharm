#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:ftplib.FTP类的方法

import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error,socket.gaierror) as e:
        print('错误：不能连接{}'.format(HOST))
        return
    print('***连接到 "{}"'.format(HOST))
    try:
        f.login()
    except ftplib.error_perm:
        print('错误：不能登入')
        f.quit()
        return
    print('***"anonymously" 已登入')

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print('错误：不能设置路径到"{}"'.format(DIRN))
        f.quit()
        return
    print('***更换到 {} 路径'.format(DIRN))

    try:
        f.retrbinary('RETR {}'.format(FILE),open(FILE,'wb').write)
    except ftplib.error_perm:
        print('错误：不能读取文件夹"{}"'.format(FILE))
        os.unlink(FILE)
    else:
        print('***下载 "{}" 到CWD'.format(FILE))
    f.quit()

if __name__ == '__main__':
    main()