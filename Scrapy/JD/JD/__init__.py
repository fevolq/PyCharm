###实现的功能
#爬取京东特定网址的商品信息（亦可爬取其他类的商品信息？？？未尝试）
#数据存为json文件（地址可在pipelines的line17更改），存入至mysql数据库（电脑需开启数据库服务）

###仍需
##原网页的翻页是javascrip，在html中没有，还为找到如何判别当前爬取的是否是最后一页
#页面只有30个商品。但执行下滑后，会出现另外30个，共60个，可以考虑在中间键文件中使用selenium模拟（https://blog.csdn.net/qq_42739440/article/details/102466551）。


###待改进
#对ip池的选择：当 当前ip无法连接或无法爬取时再使用下一个ip。（当前为使用ip池和UA池）


###备注
"""ip池与UA代理"""
#ip池和UA代理池放在setting中，在中间件middlewares需要导入这两个池才能使用
#同时，还需要导入他们的两个父类，且4个类均需在settings中的中间件使用中打开使用

"""数据库"""
#数据库的配置放在了管道文件pipelines中的JdPipeline_mysql，主要配置主机和库名等。
#数据存放的表可自行在数据库中创建，但此代码中已包含了创建表的命令。
#类中创建数据表的代码方法，有两个，一个表（jd）存放爬取的数据，另一个表（false_jd）存放一些存入jd表有误的数据的goods_id。
#jd表中设置了自增id，且goods_id字段唯一
#具体插入数据的操作在parse方法中

"""cookie"""
#cookie可以放在爬虫文件（jingdong.py）中直接使用，（亦可放在settings中，然后引用？）
#当爬虫失效时，可更换cookie重新尝试

#输出日志可用命令：scrapy crawl jd -s LOG_FILE=jd.log