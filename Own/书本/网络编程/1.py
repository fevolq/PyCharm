#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:

import socket

tcpSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #基于网络的面向连接的套接字对象
udpSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)       #基于网络的无连接的套接字对象