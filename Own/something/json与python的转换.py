#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:
# Filename:json格式与python格式间的转换

#json格式的字符串必须使用的是双引号
"""
对应关系：json---python：
object---dict
arrray---list
string---str
number(int)---int,long
number(real)---float
null---none
true,false---True,False
"""

import json

###python转为json
def p_j():
    python_obj = '[{"a":1},{"b":2},{"c":"3"},{"d":"日"}]'   #一个python的字符串

    #python类型的数据转换为json字符串
    json_obj = json.dumps(python_obj,ensure_ascii=False)
    # print(type(python_obj),type(json_obj))
    print(python_obj,json_obj)  #json_obj整体是一个字符串，使用双引号括起来

    #python的数据以json格式写入文件
    with open(r'C:\Users\15394\Desktop\translate.json','w') as f:
        json.dump(python_obj,f,ensure_ascii=False)


###json转换为python类型数据
def j_p():
    #把json字符串转换为python数据
    json_str = '''[{"a":1},{"b":2},{"c":"3"},{"d":"日"}]'''  #单引号内部的json格式字符串，由于需要写在python中，所以使用单引号括起来
    python_obj = json.loads(json_str)
    print(python_obj,type(python_obj))
    print(type(json_str))

    #把json格式文件转换为python类型数据
    with open(r'C:\Users\15394\Desktop\translate.json') as f:
        python_list = json.load(f)
        print(python_list)
        print(type(python_list))

if __name__ == "__main__":
    p_j()
    j_p()
