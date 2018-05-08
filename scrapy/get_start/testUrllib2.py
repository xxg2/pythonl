# -*- coding=UTF-8 -*-

import urllib2
import time
import platform

def clear():
    time.sleep(3)
    os = platform.system()
    print os
    if os == 'Darwin':
        os.system('clear')
    else:
        os.system('cls')

def linkBaidu():
    url = 'http://www.baidu.com'
    try:
        response = urllib2.urlopen(url, timeout=3)
    except urllib2.URLError:
        print '网络地址错误'
        exit()
    with open('./baidu.txt', 'w') as fp:
        fp.write(response.read())
    print response.geturl()
    print response.getcode()
    print response.info()

if __name__ =='__main__':
    linkBaidu()