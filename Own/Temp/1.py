#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:
# Filename:

import sys,time

# for line in sys.stdin:
#     print(line)
#     list_in = line.strip().split()
#     # print(list_in)
#     print(int(list_in[0]) + int(list_in[1]))

# t = int(input())
# for i in range(t):
#     a = list(map(int,input().split(' ')))
#     print(a)
#     print(sum(a))

# for line in sys.stdin:
#     line_in = line.strip().split()
#     if line_in == ['0','0']:
#         break
#     else:
#         print(int(line_in[0]) + int(line_in[1]))

# while True:
#     line_in = list(map(int,input().split(' ')))
#     if line_in[0]:
#         print(sum([line_in[i+1] for i in range(line_in[0])]))
#     else:
#         break

# t = int(input())
# for line in range(t):
#     try:
#         line_in = list(map(int, input().split(' ')))
#         print(sum([line_in[i + 1] for i in range(line_in[0])]))
#     except Exception as e:
#         print(e)

# while True:
#     try:
#         line_in = list(map(int,input().split(' ')))
#         print(sum(line_in))
#     except Exception as e:
#         # print(e)
#         break

# t = int(input())
# line = input()
# line_in = line.strip().split()
# line = line_in[:t]
# line.sort()
# print(' '.join(line))

# for line in sys.stdin:
#     line_in = line.strip().split(',')
#     line_in.sort()
#     print(','.join(line_in))

# while True:
#     try:
#         line_in = list(map(int,input().split(' ')))
#         print(sum(line_in))
#     except Exception as e:
#         break

def whether(m):
    w = input('{}'.format(m))
    if w =='Y' or w == 'y':
        print('是')
        return True
    elif w == 'N' or w == 'n':
        print('否')
        return False
    else:
        return whether(m)

# import re
#
# txt = '单位净值 (2020-12-18)'
#
# re_com = re.compile(r'\((.*?)\)')
# a = re_com.findall(txt)
# print(a)

# s='s=%s%s%s;print(s%s(chr(39),s,chr(39),chr(37)))'
# print(s%(chr(39),s,chr(39),chr(37)))

# import time
#
# n = time.time()
# print("当前时间戳：",n)
# n1 = time.localtime()
# print("当前结构化时间",n1)
# t = n1.tm_year
# # print(t)
# t1 = (n1.tm_year,6,23,9,0,0,0,0,0,)
# # t2 = time.mktime(t1)
# # print("当日9点的时间戳",t2)
# # print("当日9点的结构化时间",time.localtime(t2))
# #
# # t3 = (n1.tm_year,n1.tm_mon,n1.tm_mday,15,0,0,0,0,0,)
# # t4 = time.mktime(t3)
# # print("当日15点的时间戳",t4)
# # print("当日15点的结构化时间",time.localtime(t4))
# # picture_time = '{}-{}-{}'.format(n1.tm_year,n1.tm_mon,n1.tm_mday)
# picture_time = time.strftime("%Y-%m-%d",t1)
# print(picture_time)

txt = """
                                                            苏泊尔（SUPOR）电磁炉 京东纪念款 2200w大功率 多档调节 低噪音电磁灶火锅炉 C22-IH66E8（赠汤锅+炒锅）                """
new_txt = txt.strip()
print(new_txt)