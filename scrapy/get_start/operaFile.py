# -*- coding=UTF-8 -*-

import os

def operaFile():
    print '创建文件并写入文件'
    #os.system('rm test.txt')
    #os.system('ls -l test.txt')

if __name__ == '__main__':
    operaFile()
    fp = open('test.txt', 'w')
    fp.write('hello python')
    fp.close()
    os.system('ls -l test.txt')
    os.system('cat test.txt')
    print '\n'