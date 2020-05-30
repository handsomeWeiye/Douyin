import random
import pandas as pd
import requests
import time
import re
import os

excel_dir =  R"C:\Users\Administrator\Desktop\2020-3-31-2-52-44-12534992983000-管件学堂-卡耐夫管道系统（上海）有限公司-采集的数据-后羿采集器.xlsx"
col_list = [0,1]

def log(str):
    #日志函数
    time_stamp = time.time()
    local_time = time.localtime(time_stamp)
    str_time = time.strftime('%Y-%m-%d %H:%M:%S',local_time)
    print(str_time)
    with open('log.txt','a+') as f:
        logInfo = str_time +  "   " + str
        print(logInfo)
        f.write(logInfo +"\n")

def getInfoList(excel_dir,col_list):
    #数据函数，把excel列表中的数据转化为了一个列表
    provider_file = pd.read_excel(excel_dir,usecols=col_list)
    provider_list  = provider_file.values
    print("目前的读取到的数据是")
    print( provider_file.head())
    log('获取到excel数据，转化为了list'+"\n")

    return provider_list

htmls = getInfoList(excel_dir,col_list)

def mkdir(path):
    # 引入模块
    import os
 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print (path+' 创建成功')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 创建成功')
        return False


def getImg(html):
    imgResult = []
    reg = r'img src="(.+?\.png)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    for i in imglist:
        if(i[0:5] != 'http:'):
            url = 'http://www.kanaif.com.cn/'+i
            print(url)
            imgResult.append(url)
    return imgResult

def saveImg(imagelist,title):
    
    mkpath="C:\\Users\\Administrator\\Desktop\\"+"图片\\" + title
    mkdir(mkpath)
    for index,i in enumerate(imagelist[0:-1]):
        print(i)
        img  = requests.get(i)
        with open(mkpath+'\\'+ str(index)+'.jpg', 'wb') as f:
            f.write(img.content)
    

for item in htmls:
    html = item[1]
    title = item[0]
    r  = requests.get(html)
    imglist  = getImg(r.text)
    saveImg(imglist,title)

