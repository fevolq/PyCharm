#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:UDP时间戳（服务器）

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)     #创建服务器套接字
udpSerSock.bind(ADDR)                       #绑定服务器套接字

while True:
    print('等待客户端消息传入···')
    data,addr = udpSerSock.recvfrom(BUFSIZ)         #对话（接收）
    r = '[{}] {}'.format(ctime(),data.decode('utf-8'))
    udpSerSock.sendto(r.encode('utf-8'),addr)       #对话（发送）
    print('成功接收并返回来自{}的信息'.format(addr))

udpSerSock.close()