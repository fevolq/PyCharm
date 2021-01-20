# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    #主播名称
    name = scrapy.Field()
    #主播房间号
    room_id = scrapy.Field()
    #主播图片地址
    photo_url = scrapy.Field()
    pass
