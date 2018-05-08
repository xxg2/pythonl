# -*- coding=UTF-8 -*-

class TryInput(object):
    def __init__(self):
        self.len = 10
        self.numList = self.createList()
        self.getNum()

    def createList(self):
        print '创建长度为%d的数字' % self.len
        numL = []
        while len(numL) < 10:
            n = raw_input('请输入一个整数：')
            try:
                num = int(n)
            except ValueError:
                print '输入错误'
                continue
            numL.append(num)
            print '现在的列表为:'
            print numL
        return numL

    def getNum(self):
        print '当前列表为'
        inStr = None
        while inStr != 'EXIT':
            print '输入EXIT退出'
            inStr = raw_input('输入列表下标[-10,9]:')
            try:
                index = int(inStr)
                num = self.numList[index]
                print '列表下表为%d的值为%d' % index, num
            except ValueError:
                print '输入错误'
                continue
            except IndexError:
                print '下标太大'
                continue

if __name__ == '__main__':
    a = TryInput()