#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:TCP时间戳（服务器）
# 创建一个TCP服务器，接收客户端的消息，然后在消息前加上时间戳前缀返回客户端

from socket import *
from time import ctime

HOST = ''
# HOST = '183.39.130.50'
PORT = 21567
BUFSIZ = 1024           #将缓冲区设置未1KB
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)        #创建服务器套接字
tcpSerSock.bind(ADDR)                           #套接字与地址绑定
tcpSerSock.listen(5)                            #监听连接

#单线程
while True:     #服务器无限循环
    print('等待连接···')
    tcpCliSock,addr = tcpSerSock.accept()       #接受客户端连接
    print('来自于{}的连接'.format(addr))

    while True:         #通信循环
        data = tcpCliSock.recv(BUFSIZ)      #对话（接收）
        if not data:        #无消息时，代表客户端已经退出
            break
        # print(data)           #data是bytes格式
        a = '[{}] {}'.format(ctime(),data.decode('utf-8'))          #将bytes格式的data先转换未str格式
        tcpCliSock.send(bytes(a,'utf-8'))       #对话（发送），send只能传输bytes格式

    tcpCliSock.close()                  #关闭客户端套接字
tcpSerSock.close()                      #关闭服务器套接字（一般不用）