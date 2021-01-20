#python3.7
#Filename:12306站点对应的编码.py

import requests,re

url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9053"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36"}
res = requests.get(url,headers=headers)

station_re = re.compile(r"'(.*)'")
station = station_re.findall(res.text)
l = "".join(station).split("|")
#print(l)

name = []
for i in range(1,len(l),5):
    name.append(l[i])
    
code = []
for i in range(2,len(l),5):
    code.append(l[i])

#print(code)

#对应的字典
def dic():
    name_code = dict((name[i],code[i]) for i in range(len(name)))
    code_name = dict((code[i],name[i]) for i in range(len(name)))
    return name_code,code_name

def search(a):
    """查询"""
    if a in dic()[0]:
        print(dic()[0][a])
    elif a in dic()[1]:
        print(dic()[1][a])
    else:
        print("不存在此站点")
    return None


if __name__ == "__main__":
    print("结束时请输入“结束”或“over”")
    while True:
        a = input("请输入要查询的站点：")
        if a == "结束" or a == "over":
            break
        else:
            search(a)
    
