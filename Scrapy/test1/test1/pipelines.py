# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Test1Pipeline(object):
    def process_item(self, item, spider):   #item参数会获取到每个返回的item
        # print(type(item))
        # print(item)
        name = item['name']
        photo_url = item['photo_url']
        txt = name + '  ' + photo_url + '\r\n'
        with open(r'C:\Users\15394\Desktop\scrapy教程\1.txt','ab') as f:
            f.write(txt.encode('utf-8'))
        return item     #必须有return item。若有下个class管道类要继续处理item，则传给下个类，否则传给引擎，表示管道已处理完毕，可传入下一个item。
