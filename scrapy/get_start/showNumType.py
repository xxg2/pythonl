# -*- coding=UTF-8 -*-

class ShowNumType(object):
    def __init__(self):
        self.showInt()
        self.showLong()
        self.showFloat()
        self.showComplex()

    def showInt(self):
        print '#############显示整数############'
        print '十进制'
        print '%-20d, %-20d, %-20d' % (-10000, 0, 10000)
        print '二进制'
        print '%-20s, %-20s, %-20s' % (bin(-10000), bin(0), bin(10000))
        print '八进制'
        print '%-20s, %-20s, %-20s' % (oct(-10000), oct(0), oct(10000))
        print '十六进制'
        print '%-20s, %-20s, %-20s' % (hex(-10000), hex(0), hex(10000))

    def showLong(self):
        print '#############显示长整数############'
        print '十进制'
        print '%-20Ld, %-20Ld, %-20Ld' % (-1000000000000000000000000, 0, 1000000000000000000000000)
        print '二进制'
        print '%-20s, %-20s, %-20s' % (bin(-1000000000000000000000000), bin(0), bin(1000000000000000000000000))
        print '八进制'
        print '%-20s, %-20s, %-20s' % (oct(-1000000000000000000000000), oct(0), oct(1000000000000000000000000))
        print '十六进制'
        print '%-20s, %-20s, %-20s' % (hex(-1000000000000000000000000), hex(0), hex(1000000000000000000000000))

    def showFloat(self):
        print '#############显示浮点数############'
        print '%-20.10f, %-20.10f, %-20.10f' % (bin(-100.001), bin(0), bin(100.001))

    def showComplex(self):
        print '#############显示复数型############'
        var = 3+4j
        print 'var的实部是：%d\t var的虚部：%d' % (var.real, var.imag)