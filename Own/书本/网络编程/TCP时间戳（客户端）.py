#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:TCP时间戳（客户端）

from socket import *

# HOST = 'localhost'      #服务器的主机名
HOST = '192.168.153.1'
PORT = 21567            #服务器的端口号
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)        #创建客户端套接字
tcpCliSock.connect(ADDR)                    #尝试连接服务器

while True:             #通信循环
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())           #对话（发送）
    data = tcpCliSock.recv(BUFSIZ)          #对话（接收）
    if not data:
        break
    print(data.decode('utf-8'))         #接收过来的data是bytes格式，需要转换未str格式才能打印

tcpCliSock.close()      #关闭客户端套接字
