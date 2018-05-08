# -*- coding=UTF-8 -*-

import urllib2
import sys
import re

def testArgument():
    if len(sys.argv) != 2:
        print '只要一个参数就够了'
        tipUse()
        exit()
    else:
        tp = TestProxy(sys.argv[1])

def tipUse():
    print '输入一个参数'

class TestProxy(object):
    def __init__(self):
        self.proxy = proxy
        self.checkProxyFormat(self.proxy)
        self.url = 'http://www.baidu.com'
        self.timeout = 5
        self.flagWord = '百度'
        self.useProxy(self.proxy)

    def checkProxyFormat(self, proxy):
        try:
            proxyMatch = re.compile('http[s]?://[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}:[\d]{1,5}$')
            re.search(proxyMatch, proxy).group()
        except AttributeError:
            tipUse()
            exit()
        flag = 1
        proxy = proxy.replace('//', '')
        try:
            protocal = proxy.split(':')[0]
            ip = proxy.split(':')[1]
            port = proxy.split(':')[2]
        except IndexError:
            tipUse()
            exit()

        flag = flag and len(proxy.split(':')) == 3 and len(ip.split('.'))

    def useProxoy(self, proxy):
        protocal = proxy.split('//')[0].replace(':', '')
        ip = proxy.split('//')[1]
        opener = urllib2.build_opener(urllib2.ProxyHandler({protocal:ip}))
        urllib2.install_opener(opener)
        try:
            response = urllib2.urlopen(self.url, timeout=self.timeout)
        except:
            print '连接错误'
            exit()
        str = response.read()
        if re.search(self.flagWord, str):
            print '取得特征词'
        else:
            print '代理可用'

if __name__ == '__main__':
    testArgument()
