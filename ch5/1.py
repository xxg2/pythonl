import math
import random
from decimal import Decimal
import decimal
from fractions import Fraction
# python支持的数字类型有: 整数，浮点数，复数，固定精度的十进制，有理分数，集合，布尔类型，无穷的整数精度，各种数字内置函数和模块
# 1234, -24, 0, 999999999999999
# 1.23, 1., 3.14e-10, eE210, 4.0e+210
# 0177, 0x9ff, 0b101010    # 八进制，十六进制，二进制
# 3+4j, 3.0+4.0j, 3J # 复数
int(3.1415)
float(3)
"""
变量在他第一次赋值时创建
变量在表达式中使用将被替换为他们的值
变量在表达式中使用以前必须已赋值
变量像对象一样不需要在已开始进行声明
"""
print(4/5)
print(4/(2.0 + 3))
num = 1 / 3.0
print(num)

'%e' % num
'%4.2f' % num
'{0:4.2f}'.format(num)
# repr和str都把任意对象变成他们的字符串表达式。str用于一般用途，repr用于额外细节

X = 2
Y = 4
Z = 6
X < Y < Z  # True
X < Y and Y < Z # True
X < Y > Z # False
X < Y and Y > Z # False

10 / 4  # 2.5
10 // 4 # 2
10 / 4.0 # 2.5
10 // 4.0  # 2.0

math.floor(2.5)  # 2
math.floor(-2.5) # -3
math.trunc(2.5) # 2
math.trunc(-2.5) # -2

#函数实现进制转换
oct(64), hex(64), bin(64)

math.pi, math.e
math.sin(2*math.pi/180)
math.sqrt(144), math.sqrt(2)
pow(2,4), 2 ** 4
abs(-42.0)
sum((1,2,3,4))
min(3,1,2,4)
max(3,1,2,4)

random.random()
random.randint(1, 10)
random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life'])

Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') # Decimal('0.0')

decimal.Decimal(1)
decimal.getcontext().prec = 2
pay = decimal.Decimal(str(1999 + 1.33))

decimal.Decimal('1.00')/decimal.Decimal('3.00')
decNum = 0
with decimal.localcontext() as ctx:
    ctx.prec = 2
    decNum = decimal.Decimal('1.00')/decimal.Decimal('3.00')
print(decNum)

# -----------------有理数，分数的使用
x = Fraction(1, 3)   # number, denominator
y = Fraction(4, 6)
x + y # Fraction(1, 1)
x - y # Fraction(-1, 3)
x * y # Fraction(2, 9)
Fraction('.25')  # Fraction(1, 4)
Fraction('1.25') # Fraction(5, 4)
Fraction('.25')+Fraction('1.25') # Fraction(3,2)

(2.5).as_integer_ratio() # (5,2)
Fraction.from_float(1.75) # Fraction(7, 4)

# ---------------------set----------
X = set('abcde')
Y = set('bdxyz')
'e' in X # True
X - Y # set(['a', 'c', 'e'])
X | Y # set('a', 'c', 'b', 'e', 'd', 'y', 'x', 'z')
X & Y # set('b', 'd')
X ^ Y # set(['a', 'c', 'e', 'y', 'x', 'z'])
z = X.intersection(Y) # same as X & Y. output set(['b', 'd'])
z.add('SPAM') # set(['b', 'd', 'SPAM'])
z.update(set(['x', 'y'])) # set(['y', 'x', 'b', 'd', 'SPAM'])
z.remove('b') # set(['y', 'x', 'd', 'SPAM'])

for item in set('abc'): print(item * 3)
S = set([1,2,3])
S.union([3,4])  # set([1,2,3,4])
S.intersection((1,3,5)) #set([1,3])
S.issubset(range(-5, 5)) # True

# -------------------bool-----
type(True) # <class 'bool'>
isinstance(True, int) # True
True == 1  # True
True is 1 # False
True + 4 # 5