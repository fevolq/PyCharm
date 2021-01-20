# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class KuxuantvPipeline(object):
    def process_item(self, item, spider):
        content = dict(item)        #将scrapy格式的item转换为python的字典格式
        content_json = json.dumps(content,ensure_ascii=False) + ',\n'   #转换为json格式
        with open(r'C:\Users\15394\Desktop\kuxuanTV.json','ab') as f:
            f.write(content_json.encode('utf-8'))
        return item
