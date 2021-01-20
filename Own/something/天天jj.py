#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:2021.01.04
# Filename:爬取天天基金网的基金走势图

#当运行时间为周六日或节假日时，判断命名时间

import requests
from bs4 import BeautifulSoup
import time,os,re
from threading import Thread

def get_response(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding
    return response

def get_photo_url(html):
    soup = BeautifulSoup(html,'html.parser')
    img = soup.select('#estimatedNap img')
    print(img)

#得到基金名称
def get_code_name(html):
    soup = BeautifulSoup(html, 'html.parser')
    # h4 = soup.select('.col-left .title')[0]
    # code_name = h4.select('a')[0].get_text()
    code_name = soup.select('.fundDetail-header .fundDetail-tit')[0].get_text()
    return code_name

#得到或创建（以代码和名字命名的）文件夹地址
def get_path(path,code_name):
    path = path + '\\' + code_name
    if os.path.exists(path):
        path = path + '\\'
    else:
        os.makedirs(path)
        path = path + '\\'
    return path

#基金更新日期(网站上的日期，根据净值日)
def get_time(html):
    soup = BeautifulSoup(html, 'html.parser')
    span = soup.select('.dataItem02 dt')[0].select('p')[0]
    txt = span.get_text()
    # print(txt)
    re_com = re.compile(r'\((.*?)\)')
    t = re_com.findall(txt)
    # print(t)
    net_time = t[0]
    return net_time

#经过比较得到用于命名图片的时间
def save_time(net_time):
    nowtime = time.time()       #当前时间戳
    now_time = time.localtime() #当前的结构化时间
    time_9 = (now_time.tm_year,now_time.tm_mon,now_time.tm_mday,8,50,0,0,0,0,)   #当日早8点50的结构化时间
    t_9 = time.mktime(time_9)   #当日早8点50的时间戳
    time_15 = (now_time.tm_year, now_time.tm_mon, now_time.tm_mday, 15, 0, 0, 0, 0, 0,)  # 当日15点的结构化时间
    t_15 = time.mktime(time_15)  # 当日15点的时间戳

    if nowtime < t_9:
        #使用网站上给的日期
        picture_time = net_time
        return picture_time
    elif nowtime >= t_15:
        #使用当日日期
        picture_time = time.strftime("%Y-%m-%d",now_time)
        return picture_time
    else:
        #不运行
        return False

#处理图片的命名
def solve_name(i,picture_time):
    '''
    1.每日净值变化图
    2.过往半年走势图
    '''
    if i == 0:
        name = '每日净值变化图'
    else:
        name = '过往半年走势图'
    name = picture_time + name
    return name

#保存图片
def save(path,name,response):
    with open(path + '{}.jpg'.format(name),'wb') as f:
        f.write(response.content)

def main(code,path):
    # url_1 = 'http://fundf10.eastmoney.com/jjjz_{}.html'.format(code)
    url_1 = 'http://fund.eastmoney.com/{}.html?spm=search'.format(code)
    html = get_response(url_1).text
    code_name = get_code_name(html)     #基金名称
    net_time = get_time(html)       #更新日期
    picture_time = save_time(net_time)
    if picture_time:
        pass
    else:
        print("请于9点前或15点后运行")
        return
    path = get_path(path,code_name)
    urls = ['http://j4.dfcfw.com/charts/pic6/{}.png','http://j3.dfcfw.com/images/JJJZ1/{}.png']
    for i in range(1):      #只要第一个每日净值走势图，需要过往走势图时，改为2
        url = urls[i].format(code)
        response = get_response(url)
        name = solve_name(i,picture_time)
        save(path,name,response)
    print('{}已完成'.format(code))

if __name__ == '__main__':      #多线程
    # s = time.time()
    path = r'F:\something\基金\天天基金'
    # codes_name = ['招商中证白酒','国泰食品饮料','景顺成长混合',
    #               '农银新能源','嘉实新能源A','融通新能源',
    #               '中欧医药混合A','汇添富医药','招商生物医药',
    #               '中欧先锋A','国投瑞银安全','银华精选混合',
    #               '前海金银珠宝','中欧混合成长','诺安成长混合',
    #               '宝盈人工智能',]
    codes = ['161725','160222','260108',
             '002190','003984','005668',
             '003095','006113','161726',
             '001938','001838','180031',
             '001302','166006','320007',
             '005962',]
    threads = []
    l = len(codes)
    for i in range(0, l):
        code = codes[i]
        t = Thread(target=main, args=(code, path))
        threads.append(t)
    for i in range(len(threads)):
        threads[i].start()  # 开始线程
    for i in range(len(threads)):
        threads[i].join()
    print('\nDone')
    # e = time.time()
    # print('耗时{}'.format(e-s))   #耗时4.51529598236084
