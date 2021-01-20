# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class JdItem(scrapy.Item):
    #商品ID
    goods_id = scrapy.Field()
    #店铺
    shop = scrapy.Field()
    #名称
    goods_name = scrapy.Field()
    #价格
    price = scrapy.Field()
    #品牌
    brand = scrapy.Field()
    #参数
    parameter = scrapy.Field()  #商品详情页面的不同款式商品的参数
    #主图url
    image_figure = scrapy.Field()   ##商品详情页面的不同款式商品的主图
    pass
