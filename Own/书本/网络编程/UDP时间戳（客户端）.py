#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:UDP时间戳（客户端）

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)     #创建客户端套接字

while True:         #通信循环
    data = input('>>>')
    if not data:
        break
    udpCliSock.sendto(data.encode(),ADDR)       #对话（发送）
    data,ADDR = udpCliSock.recvfrom(BUFSIZ)     #接收
    if not data:
        break
    print(data.decode('utf-8'))

udpCliSock.close()