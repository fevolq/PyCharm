# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
import os
from Douyu.settings import IMAGES_STORE as images_store

#继承处理图片的类（也可处理视频等）
class DouyuPipeline(ImagesPipeline):

    #重写父类的方法
    #保存图片
    def get_media_requests(self, item, info):
        photo_url = item['photo_url']
        #将获取的图片链接 传给引擎去获取图片数据，再返回给管道保存
        yield scrapy.Request(photo_url)

    #对图片进行重命名
    def item_completed(self,results,item,info):
        #主要是results参数
        # print(results)
        # print('\n\n\n')
        #提取results里图片信息中的图片路径的值,即原默认的图片名
        image_path = [x['path'] for w,x in results if w]

        #images_store 需要从settings内导入参数IMAGES_STORE
        old_path = images_store + '\\' + image_path[0]
        new_path = images_store + '\\斗鱼\\' + item['name'] + ' ' + item['room_id'] + '.jpg'

        os.renames(old_path,new_path)   #重命名


