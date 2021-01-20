# -*- coding: utf-8 -*-
import scrapy
from test1.items import Test1Item

class TestSpider(scrapy.Spider):
    name = 'test'       #爬虫名，启动时需要
    #allowed_domains = ['baidu.com']     #限制域，可选
    start_urls = ['http://pic.netbian.com/']      #可迭代对象，起始url，可包含多个，每个url都会执行parse方法

    def parse(self, response):
        lis = response.xpath("//div[@class='slist']/ul/li")

        #items = []
        for li in lis:
            item = Test1Item()      #创建item字段对象，用来存储信息，以便中转器转给管道

            #需要的信息
            name = li.xpath('./a/@title').extract()  #extract()将xpath对象转换为字符串，返回列表
            photo_url = li.xpath('./a/@href').extract()

            #注意items文件内定义的字段
            item['name'] = name[0]
            item['photo_url'] = self.start_urls[0] + photo_url[0]

            yield item      #返回item数据给管道处理，同时还会回来继续执行for循环
            #items.append(item)
        #return items
        ###注意：此时可以在for循环内使用yield item，也可在for循环外使用return items(此时需要把所有item数据都放到items列表内才能返回)
        ###yield生成器会当出现一个item就会传给管道，然后继续执行for循环，继续传送item
        ###return items则会在for执行完后直接一次性传送所有item数据给管道

        #item对象或者return方法 都会直接识别然后传送到管道