#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:
# Filename:

import pymysql
import json

config = {
            "host": "localhost",
            "user": "root",
            "password": "mysql",
            "database": "scrapy",
            # "charset": "utf-8",
        }
db = pymysql.connect(**config)
cursor = db.cursor()

try:
    create_table = """create table false_jd(
            id int primary key auto_increment,
            goods_id varchar(20)
            );"""
    cursor.execute(create_table)
    db.commit()
except:
    pass

a = {"goods_id": "646197", "shop": "美的京东自营官方旗舰店",
     "goods_name": "美的（Midea）电磁炉 滑控调节 火锅炉 2200W大火力 微晶面板   一键爆炒 定时功能 【赠炒锅+汤锅】",
     "image_figure": "https://img12.360buyimg.com/n1/jfs/t1/165883/11/3227/129468/6006ac77E5c9175bc/08684ef7d4b94304.jpg",
     "brand": "美的（Midea）",
     "parameter": {"商品名称": "美的C21-WK2102", "商品编号": "646197", "商品毛重": "5.15kg", "商品产地": "中国大陆", "操控方式": "滑控触摸式", "产品类别": "电磁炉", "面板样式": "一体面板", "火力档位": "6档-8档", "特色功能": "配套锅具，定时，过热保护"},
     "price": "169.00"}
b = {"goods_id": "2", "shop": "美的京东自营官方旗舰店",
     "goods_name": "美的（Midea）电磁炉 滑控调节 火锅炉 2200W大火力 微晶面板   一键爆炒 定时功能 【赠炒锅+汤锅】",
     "image_figure": "https://img12.360buyimg.com/n1/jfs/t1/165883/11/3227/129468/6006ac77E5c9175bc/08684ef7d4b94304.jpg",
     "brand": "美的（Midea）",
     "parameter": {"商品名称": "美的C21-WK2102", "商品编号": "646197", "商品毛重": "5.15kg", "商品产地": "中国大陆", "操控方式": "滑控触摸式", "产品类别": "电磁炉", "面板样式": "一体面板", "火力档位": "6档-8档", "特色功能": "配套锅具，定时，过热保护"},
     "price": "169.00"}
l = [a,b]
for i in l:
    goods_id = i['goods_id']
    shop = i['shop']
    goods_name = i['goods_name']
    brand = i['brand']
    price = i['price']
    image_figure = i['image_figure']
    parameter = i['parameter']
    p = json.dumps(parameter,ensure_ascii=False)

    try:
        sql_insert = """insert into jd(goods_id,shop,goods_name,brand,price,image_figure,parameter) values('{}','{}','{}','{}','{}','{}','{}')""".format(goods_id,shop,goods_name,brand,price,image_figure,p)
        cursor.execute(sql_insert)

    except:
        sql_insert = """insert into false_jd(goods_id) values('{}')""".format(goods_id)
        cursor.execute(sql_insert)
    db.commit()
db.close()