#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:判断所给ip是否为教育网ip

import requests
import re
from bs4 import BeautifulSoup

def get_response(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response
    else:
        print('未响应')

#获取所有ip地址
def get_edu_ip(html):
    v_l_list = []
    v_r_list = []
    soup = BeautifulSoup(html, 'html.parser')
    dls = soup.select('.middle .list')
    for dl in dls:
        dds = dl.select('dd')
        # print(dds,len(dds))
        for i in dds:
            spans = i.select('span')
            # print(spans)
            v_l = spans[0].get_text()
            v_r = spans[1].get_text()
            v_l_list.append(v_l)
            v_r_list.append(v_r)
            # print(v_l,v_r,type(v_l),type(v_r))
    l = [v_l_list,v_r_list]
    return l

#输入ip
def input_ip():
    ip = input('请输入ip：')
    return ip

#判断输入ip是否符合标准
def whether_conform(ip):
    r = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    w = r.match(ip)
    if w:
        return ip
    else:
        print('请重新输入ip')
        ip = input_ip()
        whether_conform(ip)
    pass

#判断所给ip是否为教育网ip
def is_edu_ip(ip,ips):
    if ip in ips:
        print("输入的ip 是 教育网ip")
    else:
        print("输入的ip 不是 教育网ip")
    pass

def main(url):
    ip = input_ip()
    ip_right = whether_conform(ip)
    html = get_response(url).text
    l = get_edu_ip(html)
    ips = l[0] + l[1]   #所有的ip地址
    # print(ips)
    is_edu_ip(ip_right,ips)
    pass

if __name__ == '__main__':
    url = 'http://ipcn.chacuo.net/view/i_CERNET'
    main(url)