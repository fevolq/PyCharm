#!-*-coding:utf-8 -*-
#!python3.7
#!@Author:fuq666@qq.com
#!Update time:
#!Filename:

import requests
import re,os

def get_response(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    response = requests.get(url,headers=headers)
    return response

def save(response):
    print('开始保存...')
    with open('C:\\Users\\15394\\Desktop\\抖音\\' + '{}.mp4'.format(3),'wb') as f:
        f.write(response.content)
    print('Done')

def main():
    #无水印视频地址，如何在原始视频地址或视频分享地址找到他？？？？？？？
    # url = 'http://v3-dy-c.ixigua.com/38fdd39bfe6ace4f36353712dd55b14b/5f1ff41b/video/tos/cn/tos-cn-ve-15/53faba696467463785de5a5193e5ccc8/?a=1128&br=2928&bt=976&cr=0&cs=0&dr=0&ds=6&er=&l=202007281646590100120601561901F55A&lr=&mime_type=video_mp4&qs=0&rc=M3B0M3ZvNDY5djMzZmkzM0ApZDxlaTM6aDxnNzszNmZoNWdxcS5pLmtncC1fLS1fLS9zczMyYGBjMC42Y2I2NV4yLi06Yw%3D%3D&vl=&vr='
    url = 'http://v26-dy.ixigua.com/b178166fb5f8af5ff9c78a9003afa49b/5f204328/video/tos/cn/tos-cn-ve-15/c7147e15232f4f748d06bfe0bf1cab67/?a=1128&br=4215&bt=1405&cr=0&cs=0&dr=0&ds=6&er=&l=202007282224120100190180360539C06D&lr=&mime_type=video_mp4&qs=0&rc=ajh4dXlrb241djMzN2kzM0ApaDdkaDxoaTxlNzM5ZWRlM2dgb2cuaHBta2JfLS0tLS9zcy9gNmA1MGA0NDFjY2AtLV46Yw%3D%3D&vl=&vr='
    response = get_response(url)
    save(response)


if __name__ == '__main__':
    url = 'https://v.douyin.com/J2QWExy/'
    main()