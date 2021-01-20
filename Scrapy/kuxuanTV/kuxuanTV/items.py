# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KuxuantvItem(scrapy.Item):
    # define the fields for your item here like:
    #电影名称
    name = scrapy.Field()
    #电影网址
    link = scrapy.Field()
    #更新日期
    update = scrapy.Field()
    #简介
    txt = scrapy.Field()
    pass
