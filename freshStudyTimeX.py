# coding=utf-8
#!/usr/bin/python3

import requests
import configparser
import threading
import os
import sys

from requests.api import get
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 读取配置文件

config = configparser.ConfigParser()
config.read('config.ini')


name = config.get('info', 'name')
pwd = config.get('info', 'pwd')

cookieall = ""
cookies = []


loginurl = "https://aq.fhmooc.com/api/common/Login/login?schoolId=wtsoawgsg6nln8gez7e4g&userName=" + \
    name+"&userPwd="+pwd+""

url = "https://aq.fhmooc.com/api/design/LearnCourse/statStuProcessCellLogAndTimeLong"


def freshStudyTimeThread():

    cookieall = "schoolId=; userName=; userPwd=-1; ASP.NET_SessionId=" + \
        cookies[0]+"; auth="+cookies[1]

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
        "Cookie": cookieall,
        "Referer": "https://aq.fhmooc.com/catalogPreview/amifawcspkfh3ziyldznq/zbsnahys77pfqqrf5kf2eq/yavahys45zi6srusezpva",
        "videoTimeTotalLong": "0"
    }

    data = {
        "courseId": "qkcfawcsxyrom0zrwghhwq",
        "moduleIds": "amifawcspkfh3ziyldznq",
        "cellId": "yavahys45zi6srusezpva",
        "auvideoLength": "0"
    }
    print(cookieall)
    for i in range(1, 300):
        res = requests.post(url, headers=header, data=data)
        if "\"code\":1" in res.text:
            print(threading.current_thread().name +
                  " time:" + str(i) + " ok")
        else:
            print(threading.current_thread().name +
                  " time:" + str(i) + " ERROR")


def getCookie():

    Hostreferer = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'
    }
    # urllib或requests在打开https站点是会验证证书。 简单的处理办法是在get方法中加入verify参数，并设为False
    html = requests.get(loginurl, headers=Hostreferer, verify=False)
    # 获取cookie:DZSW_WSYYT_SESSIONID
    if html.status_code == 200:
        for tcookie in html.cookies:
            cookies.append(tcookie.value)


def main():

    # 获取cookie
    getCookie()

    # written by Polarisjl 2021.12.15
    t0 = threading.Thread(target=freshStudyTimeThread, name='Thread0')
    t1 = threading.Thread(target=freshStudyTimeThread, name='Thread1')
    t2 = threading.Thread(target=freshStudyTimeThread, name='Thread2')
    t0.start()
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
