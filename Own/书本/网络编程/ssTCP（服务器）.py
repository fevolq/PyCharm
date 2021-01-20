#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:socketserver TCP服务器

from socketserver import (
TCPServer as TCP,StreamRequestHandler as SRH
)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST,PORT)

class MyRequestHandler(SRH):        #请求处理程序
    def handle(self):       #当接收到一个来自客户端的消息时，就会调用handle()方法
        print('来自于{}的连接'.format(self.client_address))
        #使用readline()来获取客户端信息，并利用write()方法将字符串发送回客户端
        data = '[{}] {}'.format(ctime(),self.rfile.readline().decode('utf-8'))  ###客户端传送过来的数据是bytes格式，而ctime()是str格式，所以先转换为一致
        self.wfile.write(data.encode('utf-8'))      ###上一步的data是str格式，所以要转换为bytes格式，才能传输到客户端

tcpServ = TCP(ADDR,MyRequestHandler)
print('等待连接···')
tcpServ.serve_forever()         #无限循环等待客户端
