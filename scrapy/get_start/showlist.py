# -*- coding=UTF-8 -*-

class ShowList(object):
    def __init__(self):
        self.l1 = []
        self.l2 = []

        self.createList()
        self.insertData()
        self.appendData()
        self.deleteData()
        self.subList()

    def createList(self):
        print '创建列表'
        print 'l1=list("abcdefg")'
        self.l1 = list('abcdefg')
        for i in xrange(0, 10):
            self.l2.append(i)
        self.l1 = list('abcdefg')
        print self.l1
        print self.l2

    def insertData(self):
        print '插入数据'
        self.l1.insert(3, 100)
        print self.l1
        self.l2.insert(10, 'python')
        print self.l2

    def appendData(self):
        print '追加数据'
        self.l1.append([1,2,3])
        print self.l1
        self.l2.append(('a', 'b', 'c'))
        print self.l2

    def deleteData(self):
        print '删除数据'
        self.l1.pop()
        print self.l1
        self.l1.pop(0)
        print self.l1
        self.l2.pop()
        print self.l2
        self.l2.pop(3)
        print self.l2

    def subList(self):
        print '列表分片'
        print self.l1[2:]
        print self.l2[1:-1:2]