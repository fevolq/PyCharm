# -*- coding: utf-8 -*-
import scrapy
from Douyu.items import DouyuItem
import json


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    base_url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        data_response = json.loads(response.body)    #将json数据转换为python格式
        data_list =data_response['data']     #提取data数据

        if len(data_list) == 0:  #当没有提取到数据时，url结束
            return

        for data in data_list:
            item = DouyuItem()

            item['name'] = data['nickname']
            item['room_id'] = data['room_id']
            item['photo_url'] = data['vertical_src']

            yield item

        self.offset += 20
        #还需要传入新的链接时，使用Request，
        # 参数为新的url和执行response的方法parse(若需要另外的方法，可自定义新的处理方法，此时使用新的名字)
        yield scrapy.Request(self.base_url + str(self.offset),callback=self.parse)
