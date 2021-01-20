#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:socketserver TCP客户端

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

while True:
    #由于socketServer的处理程序的默认行为是：接受连接，获取请求，然后关闭连接。所以每次向服务器发送请求时，都需要创建新的套接字
    tcpCliSock = socket(AF_INET,SOCK_STREAM)        #基于网络的面向连接的套接字
    tcpCliSock.connect(ADDR)
    data = input('>>>')
    if not data:
        break
    data = '{}\r\n'.format(data)        ###用户输入的是str格式，而传出时的格式需为bytes格式，所以用encode进行转化后再传输
    tcpCliSock.send(data.encode('utf-8'))      #服务器的处理程序类，对待套接字通信就像文件一样，所以要发送行终止符（回车和换行）
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    data = data.decode('utf-8')         ###返回的是bytes格式，而所要打印的格式为str格式，所以先用decode进行转换
    print(data.strip())             #当得到服务器的返回消息时，用strip()方法对其进行处理，换行符由print声明
    tcpCliSock.close()