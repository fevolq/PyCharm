import scrapy
from JD.items import JdItem
import json
import time

class JDSpider(scrapy.Spider):
    name = 'jd'
    base_url = 'https://list.jd.com/list.html?cat=737,752,757&page='
    offset = 1
    start_urls = [base_url+str(offset)]
    cookies = {
        'shshshfpa':'b70110d9-5992-2c2e-f965-320c9d09a934-1610947353',
        'shshshfpb':'mbNN0XOJULkG9WDWOehYTjg%3D%3D',
        '__jdv':'76161171|baidu|-|organic|not set|1610947388668',
        '__jdu':'1610947218465729594943',
        'areaId':'19',
        'PCSYCityID':'CN_440000_0_0',
        '3AB9D23F7A4B3C9B':'AJYKXYRXHLWSE76NWNGR2GYGZX6A27D6PB4IRZBTL5NKQRMLDNXYMUI3E3CKOI25LCPDPMNQ7WTT55MDC3X4A6ETCQ',
        'shshshfp':'9b483cc760e8c2572fdea20d841a4527',
        'ipLoc-djd':'19-1607-4773-62121',
        'mt_xid':'V2_52007VwMVUlxQV1wcSRBZAmMFEVpZUFdSGkspDwxjARtQWV1OCE0bSUAAYwASTg0IVg0DGRgOATdRG1tZCwYJL0oYXwV7AhJOXVBDWhlCGVwOZQIiUG1YYlgfSR5ZA2cKF1VtWFReGw%3D%3D',
        '__jda':'122270672.1610947218465729594943.1610947218.1611124210.1611128281.14',
        '__jdc':'122270672',
        'shshshsID':'ea12c2ec8c70c99da63bea9d10499343_3_1611129280367',
        '__jdb':'122270672.6.1610947218465729594943|14.1611128281'
    }

    def parse(self,response):
        #获取spu_id
        li_list = response.xpath("//div[@id='J_goodsList']/ul[1]/li")
        for li in li_list:
            item = JdItem()
            goods_id = str(li.xpath("./@data-sku").extract()[0])
            #商品ID
            item["goods_id"] = goods_id
            # print(goods_id)
            url = 'https://item.jd.com/{}.html'.format(goods_id)
            yield scrapy.Request(url,callback=self.parse_info,cookies=self.cookies,meta={'item':item,'goods_id':goods_id})
            # yield scrapy.Request(url, callback=self.parse_info,meta={'item': item, 'goods_id': goods_id})

        # if len(response.xpath("//a[@class='pn-next']").extract()) == 0:     #当前页是最后一页
        #     return
        # else:
        self.offset += 1
        new_url = self.base_url + str(self.offset)
        yield scrapy.Request(new_url,callback=self.parse,cookies=self.cookies)
        # yield scrapy.Request(new_url, callback=self.parse)

    def parse_info(self,response):
        # goods_id = response.meta['goods_id']
        # print(goods_id)
        # print(response.text)
        # time.sleep(100)
        item = response.meta['item']
        goods_id = response.meta['goods_id']
        # 店铺
        item["shop"] = response.xpath("//div[@id='crumb-wrap']/div/div[2]/div[2]/div[1]/div/a/@title").extract()[0]
        # 商品名//div[@class='sku-name']/text()
        goods_name = response.xpath("//div[@class='p-info lh']/div[@class='p-name']/text()").extract()[0]
        item["goods_name"] = self.remove_non(goods_name)
        # 主图
        item["image_figure"] = 'https:' + response.xpath("//img[@id='spec-img']/@data-origin").extract()[0]
        #品牌
        item["brand"] = response.xpath("//div[@class='p-parameter']/ul[1]/li/@title").extract()[0]
        #参数
        info = {}
        li_list = response.xpath("//div[@class='p-parameter']/ul[2]/li")
        for li in li_list:
            txt = li.xpath("./text()").extract()[0]
            txt_dict = self.to_json(txt)    #返回一个字典
            info.update(txt_dict)
        item["parameter"] = info
        #价格url
        price_url = 'https://item-soa.jd.com/getWareBusiness?skuId={}'.format(goods_id)
        yield scrapy.Request(price_url,callback=self.parse_price,cookies=self.cookies,meta={'item':item})
        # yield scrapy.Request(price_url, callback=self.parse_price,meta={'item': item})

    # 找到价格
    def parse_price(self, response):
        item = response.meta['item']
        data_response = json.loads(response.body)  # 将json数据转换为python格式
        price = data_response["price"]["p"]
        item["price"] = price
        yield item

    #去除文本内容两端的空格符
    def remove_non(self,txt):
        new_txt = txt.strip()
        return new_txt

    #转换为字典
    def to_json(self,txt):
        txt_list = txt.split("：")
        info = {txt_list[0]:txt_list[1]}
        return info