# -*- codding=UTF-8 -*-

class ShowDict(object):
    def __init__(self):
        self.spiderMan = self.createDict()
        self.insertDict(self.spiderMan)
        self.modifyDict(self.spiderMan)
        self.operationDict(self.spiderMan)
        self.deleteDict(self.spiderMan)

    def createDict(self):
        print '创建字典'
        spiderMan = {'name':'Peter', 'sex':'male','Nation':'U.S.A.', 'college':'MIT'}
        self.showDict(spiderMan)
        return spiderMan

    def showDict(self, spiderMan):
        print spiderMan
        print '\n'

    def insertDict(self, spiderMan):
        spiderMan['age']=31
        self.showDict(spiderMan)

    def modifyDict(self, spiderMan):
        spiderMan['college'] = 'Empire State University'
        self.showDict(spiderMan)

    def operationDict(self, spiderMan):
        keyList = spiderMan.keys()
        print keyList
        valueList = spiderMan.values()
        print valueList
        itemList = spiderMan.items()
        print itemList
        college = spiderMan.get('college')
        print 'college is %s' % college

    def deleteDict(self, spiderMan):
        del(self.spiderMan['Nation'])
        self.showDict(spiderMan)
        self.spiderMan.clear()
        self.showDict(spiderMan)
        del(spiderMan)
        try:
            self.showDict(spiderMan)
        except NameError:
            print 'spiderMan 未定义'