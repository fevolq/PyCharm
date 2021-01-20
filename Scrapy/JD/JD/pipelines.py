# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import pymysql

#数据存为json文件
class JdPipeline:
    def process_item(self, item, spider):
        content = dict(item)  # 将scrapy格式的item转换为python的字典格式
        content_json = json.dumps(content, ensure_ascii=False) + ",\n"  # 转换为json格式
        with open(r'C:\Users\15394\Desktop\jd.json', 'ab') as f:
            f.write(content_json.encode('utf-8'))
        return item

#数据保存到mysql数据库
class JdPipeline_mysql:
    def __init__(self):
        self.config = {
            "host": "127.0.0.1",
            "user": "root",
            "password": "mysql",
            "database": "scrapy",
            # "charset": "utf-8",
        }
        self.db = pymysql.connect(**self.config)
        self.cursor = self.db.cursor()
        #所用的表可于数据库中创建，也可放在此处创建。
        self.__create_table_jd()

    #创建存放数据的表
    def __create_table_jd(self):
        try:
            create_table = """create table jd(
                        id int primary key auto_increment,
                        goods_id varchar(100),
                        shop longtext,
                        goods_name longtext,
                        price varchar(20),
                        brand varchar(100),
                        parameter longtext,
                        image_figure longtext,
                        unique(goods_id)
                        );"""
            self.cursor.execute(create_table)
            self.db.commit()
            #对字符格式进行修改
            alter = """alter table jd convert to character set utf8mb4;"""
            self.cursor.execute(alter)
            self.db.commit()
        except:
            pass

    #创建一个存放失败数据的数据表，（即未成功存放在jd表内的数据）
    def __create_false_jd(self):
        try:
            create_table = """create table false_jd(
            id int primary key auto_increment,
            goods_id varchar(20)
            );"""
            self.cursor.execute(create_table)
            self.db.commit()
        except:
            pass

    def process_item(self, item, spider):
        content = dict(item)
        goods_id = content['goods_id']
        shop = content['shop']
        goods_name = content['goods_name']
        price = content['price']
        brand = content['brand']
        parameter = content['parameter']
        para = json.dumps(parameter,ensure_ascii=False)     #将字典格式转换为字符串格式，否则无法传入数据库的一个字段内
        image_figure = content['image_figure']
        try:
            sql_insert = """insert into jd(goods_id,shop,goods_name,price,brand,parameter,image_figure) 
                            values('{}','{}','{}','{}','{}','{}','{}');""".format(goods_id, shop, goods_name, price,
                                                                                  brand, para, image_figure)
            self.cursor.execute(sql_insert)
            self.db.commit()    #提交至数据库
        except Exception as e:
            # print(e)
            self.__create_false_jd()
            sql_insert = """insert into false_jd(goods_id) values('{}')""".format(goods_id)
            self.cursor.execute(sql_insert)
            self.db.commit()
        return item

    def close(self):
        self.db.close()