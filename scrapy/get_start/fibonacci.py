# -*- coding=UTF-8

class Fibonacci(object):
    def __init__(self):
        self.fList = [0,1]
        self.main()

    def main(self):
        listLen = raw_input('请输入数列长度')
        self.checkLen(listLen)
        while len(self.fList) < int(listLen):
            self.fList.append(self.fList[-1] + self.fList[-2])
        print '%s ' % self.fList

    def checkLen(self, length):
        lenList = map(str, xrange(3, 51))
        if length in lenList:
            print '输入长度符合标准'
        else:
            print '只能输入3-50长度'
            exit()

if __name__ == '__main__':
    f = Fibonacci()