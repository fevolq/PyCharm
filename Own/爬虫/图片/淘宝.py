#!-*-coding:utf-8 -*-
#!@Author：fuq666@qq.com

import requests
import re
from bs4 import BeautifulSoup
import time,os

def get_response(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    response = requests.get(url,headers=headers)
    return response

#使用bs4找出每个块的链接和标题
def get_block(html):
    """找出每个块的url和title，可往内部继续前进"""
    soup = BeautifulSoup(html,'html.parser')
    block = soup.select('.item li')     #当前页面的所有块
    all_list = []
    for li in block:
        block_dic = {}
        a = li.find('a')     #每个块内的'a'标签
        block_url = a.get('href')   #每个块所对应的链接
        block_title = a.get('title')
        block_dic['block_url'] = block_url
        block_dic['block_title'] = block_title
        all_list.append(block_dic)
    return all_list     #[{url:url,title:title},···]

#使用bs4直接找出所有的photo_url和title
def get_photo_url(html):
    """直接在每个块中找到当前显示的图片url和title，只找当前页面显示的图片"""
    soup = BeautifulSoup(html, 'html.parser')
    block = soup.select('.item li')  # 当前页面的所有块
    all_list = []
    for li in block:
        block_dic = {}
        src = soup.select('.cpnt_center_img img')[0]
        Title = soup.select('.title_line')[0]
        photo_url = src.get('src')
        title = Title.get_text()
        block_dic['photo_url'] = photo_url
        block_dic['title'] = title
        all_list.append(block_dic)
    return all_list

#使用正则直接找出所有的photo_url和title
def get_url(html):
    all_all = []
    all_pattern = re.compile(r'"picUrl":"(.*?)",.*?"title":"(.*?)"')
    all_list = all_pattern.findall(html)
    for i in all_list:
        block_dic = {}
        photo_url = i[0]
        title = i[1]
        block_dic['photo_url'] = photo_url
        block_dic['title'] = title
        all_all.append(block_dic)
    return all_all

#图片保存
def save(response,title):
    path = 'C:\\Users\\15394\\Pictures\\爬虫\\淘宝'
    if os.path.exists(path):
        path = path + '\\'
    else:
        os.makedirs(path)
        path = path + '\\'
    with open(path+'{}.jpg'.format(title),'wb') as f:
        f.write(response.content)
        print('{}  已下载'.format(title))

#运行顺序
def main(start_url):
    html = get_response(start_url).text
    blocks = get_url(html)
    for block in blocks:
        photo_url = block['photo_url']
        title = block['title']
        try:
            response = get_response(photo_url)
            save(response,title)
            time.sleep(1)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    start_url = 'https://ai.taobao.com/search/index.htm?spm=a231o.7712113%2Fg.a3342.13.48834608eIcICg&prepvid=200_11.26.236.81_362_1571576298849&extra=&key=%E6%83%85%E8%B6%A3%E4%B8%9D%E8%A2%9C%E5%86%85%E8%A1%A3&pid=mm_10011550_2325296_9002527&unid=&clk1=&source_id=&app_pvid=200_11.26.236.81_362_1571576298849'
    main(start_url)
    print('\nDone')
