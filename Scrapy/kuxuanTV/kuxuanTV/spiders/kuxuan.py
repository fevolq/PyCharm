# -*- coding: utf-8 -*-
import scrapy
from kuxuanTV.items import KuxuantvItem


class KuxuanSpider(scrapy.Spider):
    name = 'kuxuan'
    # allowed_domains = ['wo1115.com']
    start_urls = ['http://www.wo1115.com/dongzuo/']

    def parse(self, response):
        lis = response.xpath("//ul[@class='clist']/li")
        for li in lis:
            # print(li)
            # print('\n\n\n')
            item = KuxuantvItem()
            item['name'] = li.xpath("./h2/a/text()").extract()[0]
            item['link'] = 'http://www.wo1115.com' + li.xpath("./a/@href").extract()[0]
            item['update'] = li.xpath("./p[3]/text()").extract()[0]
            item['txt'] = li.xpath("./div/text()").extract()[0]
            yield item

        #再执行下一页的网址
        if len(response.xpath(".//em[@class='nolink']")) == 0:
            url = 'http://www.wo1115.com' + response.xpath(".//div[@class='page']/a[7]/@href").extract()[0]
            yield scrapy.Request(url,callback = self.parse)
        elif response.xpath(".//em[@class='nolink']/text()").extract()[0] == '首页':
            url = 'http://www.wo1115.com' + response.xpath(".//div[@class='page']/a[5]/@href").extract()[0]
            yield scrapy.Request(url,callback = self.parse)