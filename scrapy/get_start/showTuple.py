# -*- coding=UTF-8 -*-

class ShowTuple(object):
    def __init__(self):
        self.t1 = ()
        self.createTuple()  #创建元组
        self.subTuple(self.t1)  #元组分片
        self.tuple2List(self.t1) #元组列表转换

    def createTuple(self):
        print '创建元组'
        self.t1 = (1,2,3,4,5,6,7,8,9,10)
        print self.t1

    def subTuple(self):
        print '元组分片'
        print self.t1[3:]

    def tuple2List(self):
        print '元组转列表'
        l2 = list(self.t1)
        print l2
        l2.append(100)
        print tuple(l2)