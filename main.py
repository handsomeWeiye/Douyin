#需要导入的初始化包
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from airtest.core.api import *
import uiautomator2 as u2
import pandas as pd
import time


#程序准备的全局变量，包括文件路径，申请模板，和导入的路径的列号
excel_dir =  r"C:\Users\Administrator\Desktop\抖音美女排行榜.xlsx"
col_list = [0,1,13]

d = u2.connect()
print(d.device_info)


#日志函数
def log(str):
    time_stamp = time.time()
    local_time = time.localtime(time_stamp)
    str_time = time.strftime('%Y-%m-%d %H:%M:%S',local_time)
    print(str_time)
    with open('log.txt','a+') as f:
        logInfo = str_time +  "   " + str
        print(logInfo)
        f.write(logInfo +"\n")

#获取抖音红人号列表
def getInfoList(excel_dir,col_list):
    #数据函数，把excel列表中的数据转化为了一个列表
    provider_file = pd.read_excel(excel_dir,usecols=col_list)
    provider_list  = provider_file.values
    print("目前的读取到的数据是")
    print( provider_file.head())
    log('获取到excel数据，转化为了list'+"\n")

    return provider_list

def search(provider):
    print('目前搜索的抖音号是{}'.format(provider[1]+provider[2]))
    touch(Template(r"tpl1590593262953.png", record_pos=(0.424, -0.921), resolution=(1080, 2312)))
    poco("com.ss.android.ugc.aweme:id/ai3").set_text(provider[2])
    time.sleep(0.3)
    poco("com.ss.android.ugc.aweme:id/gna").click()
    poco(text="作品").click()
    poco(desc="视频1").click()
    poco("com.ss.android.ugc.aweme:id/exb").click()
    poco("android.widget.LinearLayout").offspring("com.ss.android.ugc.aweme:id/az").child("android.widget.LinearLayout")[4].offspring("com.ss.android.ugc.aweme:id/ewg").swipe([-1, -0.0034])
    poco("android.widget.LinearLayout").offspring("com.ss.android.ugc.aweme:id/az").child("android.widget.LinearLayout")[2].offspring("com.ss.android.ugc.aweme:id/ewg").click()



time.sleep(0.3)



if __name__ == "__main__":
    provider_list =  getInfoList(excel_dir,col_list)
    for i in provider_list:
        search(i)
