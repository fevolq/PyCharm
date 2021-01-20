#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:Twisted TCP（服务器）

from twisted.internet import protocol,reactor
from time import ctime

PORT = 21589

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):       #获取客户端信息。当一个客户端连接到服务器时就会执行此方法。
        clnt = self.clnt = self.transport.getPeer().host
        print('来自于{}的连接'.format(clnt))
    def dataReceived(self, data):       #当服务器接收到客户端发送的数据时就会调用此方法。
        data = '[{}] {}'.format(ctime(),data.decode('utf-8'))
        self.transport.write(data.encode('utf-8'))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print('等待连接···')
reactor.listenTCP(PORT,factory)
reactor.run()