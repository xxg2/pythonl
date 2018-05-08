# -*- coding=UTF-8 -*-

class PrintTable(object):
    def __init__(self):
        self.print99()

    def print99(self):
        for i in xrange(1, 10):
            for j in xrange(1, i+1):
                print '%dX%d=%2s  ' % (j,i,i*j),
            print '\n'

if __name__ == '__main__':
    pt = PrintTable()