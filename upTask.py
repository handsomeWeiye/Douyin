import pandas as pd
import requests
import asyncio
import json

url = "https://api2.bmob.cn/1/classes/tasker/"

httpHeader = {
    "Content-Type":"application/json",
    "X-Bmob-Application-Id":"a2e53b27e0d190aa9cb81f8b40cda7f6",
    "X-Bmob-REST-API-Key ":"0636791fbb6eaa44a228688e97213168"
}

def openFile():
    data = pd.read_excel("抖音美女排行榜.xlsx",usecols=[1,13])
    return data.values


def getDouyinId(data):
    infoList = []
    for item in data:
        info =[]
        a = item.tolist()
        douyinName = a[0]
        douyinId = a[1]
        if(str(douyinId)=='nan'):
            continue
        else:
            douyinId = a[1][4:]
        print(douyinId)
        # print(douyinName)
        info.append(douyinName)
        info.append(douyinId)
        infoList.append(info)
    print(infoList)
    return infoList

def postData(data):
    print(data)
    jsons = {}
    # print(data[0])
    # jsons['douyinName']=str(data[0]),
    # jsons['douyinId']=str(data[1]),
    # jsons['isDownloadedUrl']=False,
    jsons = {
        "douyinName":data[0],
        "douyinId":data[1],
        "isDownloadedUrl":False,
    }
    jsonData = json.dumps(jsons) 
    print(jsonData)
    r =  requests.post(url,headers=httpHeader,data=jsonData)
    print(r.text)


def main():
    origin = openFile()
    data = getDouyinId(origin)
    for item in data:
        postData(item)
    
        
if __name__ == "__main__":
    main()
