#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:Twisted TCP（客户端）

from twisted.internet import protocol,reactor

HOST = '127.0.0.1'
PORT = 21589

class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = input('>>>')
        if data:
            print('发送的信息是：{}'.format(data))
            data = data.encode('utf-8')
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print(data.decode('utf-8'))
        self.sendData()

class TSClntFactory(protocol.ClientFactory):        #当需要关闭套接字时调用
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = lambda self,connector,reason:reactor.stop()

reactor.connectTCP(HOST,PORT,TSClntFactory())
reactor.run()