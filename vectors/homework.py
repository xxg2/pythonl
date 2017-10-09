#_*_ coding:UTF-8_*_
import numpy as np
import random
from copy import deepcopy
from decimal import Decimal
from decimal import *
import unittest

I = [[1,0,0,0],
     [0,1,0,0],
     [0,0,0,1]]
B = [[1,2,3,5],
     [2,3,3,5],
     [1,2,5,1]]
#I = [[0.7468379794033546, 0.24346725651257206, 0.21025854360047402, 0.8948645214917378, 0.18253543282023932, 0.21343633704859166, 0.7416577926335844], [0.8018739012377868, 0.960471204370359, 0.2878531917447763, 0.8102127374527326, 0.7163568693720075, 0.0797768553771595, 0.4297364755543186], [0.12225946798428255, 0.2675566665138328, 0.5975364923195375, 0.20897450116775196, 0.5486768605679002, 0.9020184381306573, 0.4546135201200644], [0.6096927458428274, 0.6264041452976217, 0.3734443965109252, 0.04590378367802028, 0.06643598182469479, 0.33836608288435865, 0.3374521133209397], [0.1921020540729299, 0.7414290616980624, 0.7077150983432802, 0.5318305899080841, 0.5430332709536907, 0.7000730963213252, 0.16520468545521583], [0.44302484807041564, 0.7727907363500598, 0.46822829538811106, 0.521387356936503, 0.7952208984994631, 0.08863332733594309, 0.086282999708434], [0.09590358431486723, 0.016581013222257468, 0.789726568577093, 0.1465055082636879, 0.8617046203688582, 0.6858411854464436, 0.795050675649086], [0.9085649076133363, 0.20778892548974837, 0.8488408892616186, 0.2038228684865534, 0.14734226521423444, 0.9858456543943513, 0.31239166546826547], [0.04645483264095007, 0.9015123309244213, 0.8043763984217388, 0.02933452485174881, 0.25039862804669133, 0.6929477438373308, 0.6497563138452168], [0.6008869431327056, 0.2865040406955903, 0.8649448145950362, 0.09619810844632404, 0.4009313357109524, 0.9839596979292624, 0.36781498996352135], [0.9604268203172868, 0.6011175497774723, 0.8887935487585692, 0.628353127176312, 0.12375380019945326, 0.696212941954675, 0.8832951177437529], [0.3013414489405497, 0.42891699566486985, 0.7520421089857684, 0.5745009751228111, 0.47549919116807615, 0.02029907080303095, 0.7618935549856534], [0.7613422306996817, 0.49951616269811683, 0.19646452713028095, 0.25785727222469457, 0.5618510386985641, 0.942079338380266, 0.5145044945828158], [0.10806253971430402, 0.2699839017888237, 0.7031478910736572, 0.569349972134243, 0.4065896725574025, 0.4072528522111595, 0.8641038580743385], [0.27741919864167697, 0.4320951884149452, 0.6115123299736936, 0.6868142889248898, 0.3357934148088533, 0.6093315729599809, 0.4323618908314545], [0.05005213920571505, 0.4250920605822812, 0.9577374612121178, 0.13126582937220166, 0.8475433326315319, 0.2757566961164387, 0.9196930602534535], [0.42887854745330334, 0.3618527991211935, 0.020952466686375293, 0.723134885016592, 0.46474596370711585, 0.686964216161963, 0.8454537266689424], [0.2230868000957631, 0.9344894499934129, 0.6183653423192521, 0.6703118829113262, 0.20700834645607824, 0.6744588527160819, 0.7453891995320779], [0.6559356333905861, 0.4631500443856831, 0.9481504894981864, 0.9190326096889286, 0.21598438188255964, 0.546468546064394, 0.21596970430616347], [0.12166040060879102, 0.25229580108421856, 0.03783928593163011, 0.004232666934449569, 0.042436914203501264, 0.6390047506384097, 0.8260313955589227], [0.46069065586449764, 0.30279060247638234, 0.9237127684893364, 0.34334735990054666, 0.8528077862712292, 0.7631118476910346, 0.560883728940925], [0.6972466098619942, 0.10669668797445753, 0.5722322435708692, 0.13020227515730898, 0.4690999169346224, 0.11620289770904513, 0.37706188308576505], [0.5929768320020558, 0.8533531355814508, 0.8072567138936843, 0.31318237312271935, 0.36856646263381276, 0.641431651358603, 0.48317620069249156], [0.49240148980758147, 0.9224275613098799, 0.3713579672238624, 0.6441434432775786, 0.7935628936293861, 0.8430033356538298, 0.007522988393743213]]

# 返回矩阵的行数和列数
def shape(M):
    return len(M),len(M[0])
# print shape(I)

# 每个元素四舍五入到特定小数数位
# 直接修改参数矩阵，无返回值
def matxRound(M, decPts=4):
    for i in range(len(M)):
        for j in range(len(M[i])):
            M[i][j] = round(M[i][j], decPts)
    pass
matxRound(I, 2)
# print I

# 计算矩阵的转置
def transpose(M):
    # zip(*M)得到的数据结构是元组列表，元组元素是不可修改的，你后面一些原地修改的操作可能会因此出现异常
    return [list(col) for col in zip(*M)]
# print transpose(B)

I = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3]]
B = [[1,2,3],
     [2,3,3],
     [1,2,5],
     [5,5,5]]
# 计算矩阵乘法 AB，如果无法相乘则返回None
def matxMultiply(A, B):
    try:
        return [[sum(a * b for a, b in zip(a, b)) for b in zip(*B)] for a in A]
    except Exception as e:
        raise e
# print matxMultiply(I, B)


# 构造增广矩阵，假设A，b行数相同
def augmentMatrix(A, b):
    matrix = deepcopy(A)
    for index in range(len(A)):
        for col in range(len(b[index])):
            matrix[index].append(b[index][col])
    return matrix
    # 更好的实现方式  return [ra + rb for ra,rb in zip(A,b)]
I = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3]]
B = [[1,2,3],
     [2,3,3],
     [1,2,5]]
# print augmentMatrix(I, B)

def swapRows(M, r1, r2):
    arr = M[r1]
    M[r1] = M[r2]
    M[r2] = arr
    pass
I = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3]]
# swapRows(I,0,2)
# print I

def scaleRow(M, r, scale):
    if scale == 0:
        raise ValueError
    M[r] = [scale*x for x in M[r]]
    pass
I = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3]]
# scaleRow(I,0,2)
# print I

# r1 <--- r1 + r2*scale
# 直接修改参数矩阵，无返回值
def addScaledRow(M, r1, r2, scale):
    if scale == 0:
        raise ValueError
    for index in range(len(M[r1])):
        M[r1][index] = M[r1][index] + scale * M[r2][index]
    pass
I = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3]]
# addScaledRow(I,0,2,5)
# print I

# 实现 Gaussain Jordan 方法求解 Ax = b
""" Gaussian Jordan 方法求解 Ax = b.
    参数
        A: 方阵 
        b: 列向量
        decPts: 四舍五入位数，默认为4
        epsilon: 判读是否为0的阈值，默认 1.0e-16
        
    返回列向量 x 使得 Ax = b 
    返回None，如果 A，b 高度不同
    返回None，如果 A 为奇异矩阵
"""

def gj_Solve(A, b, decPts=4, epsilon = 1.0e-16):
    if len(A) != len(b):
        return None
    matrix = augmentMatrix(A, b)
    for index in range(len(matrix)):
        rowIndex = index
        maxIndex = index
        while rowIndex < len(matrix):
            if abs(matrix[maxIndex][index]) < abs(matrix[rowIndex][index]):
                maxIndex = rowIndex
            rowIndex += 1
        if abs(matrix[maxIndex][index]) < epsilon:
            return None
        else:
            swapRows(matrix, index, maxIndex)
            scaleRow(matrix, index, 1./(matrix[index][index]))

        rowIndex = index
        while rowIndex < len(matrix)-1:
            if abs(matrix[rowIndex+1][index]) < epsilon:
                rowIndex += 1
                continue
            addScaledRow(matrix, rowIndex+1, index, -1.*matrix[rowIndex+1][index]/matrix[index][index])
            rowIndex += 1
        rowIndex = 0
        while rowIndex < index:
            if abs(matrix[rowIndex][index]) < epsilon:
                rowIndex += 1
                continue
            addScaledRow(matrix, rowIndex, index, -1.*matrix[rowIndex][index]/matrix[index][index])
            rowIndex += 1
        print "i={},matrix={}".format(index, matrix)
    matxRound(matrix, decPts)
    result = []
    for index in range(len(matrix)):
        result.append(matrix[index][len(matrix[index])-1])
    return result

A = [[-7, -3, 1, -9],
     [0, 0,0, 0],
     [-2,7, 7,-3],
     [8,-5, -6,3]]
b = [[1],[1],[1],[1]]
x = gj_Solve(A, b)
print x
#     r = np.random.randint(low=3,high=4)
#     A = np.random.randint(low=-10,high=10,size=(r,r))
#     b = np.arange(r).reshape((r,1))
#
#     x = gj_Solve(A.tolist(),b.tolist())
#     Ax = np.dot(A,np.array(x))
#     loss = np.mean((Ax - b)**2)
#     print "x={}, loss<0.01={}, Matrix A is singular={}".format(x, loss<0.01, x == None)

class LinearRegressionTestCase(unittest.TestCase):

    def test_gj_Solve(self):
        testA = []
        testb = []
        for _ in range(100):
            r = np.random.randint(low=3,high=10)
            A = np.random.randint(low=-10,high=10,size=(r,r))
            b = np.arange(r).reshape((r,1))
            testA.append(A)
            testb.append(b)
            x = gj_Solve(A.tolist(),b.tolist())
            if np.linalg.matrix_rank(A) < r:
                self.assertEqual(x,None,"Matrix A is singular")
            else:
                self.assertNotEqual(x,None,"Matrix A is not singular")
                self.assertEqual(np.array(x).ndim,2,"x have to be two-dimensional Python List")
                Ax = np.dot(A,np.array(x))
                loss = np.mean((Ax - b)**2)
                self.assertTrue(loss<0.01,"Regression result isn't good enough")

def linearRegression(points):
    X = [[x, 1] for x, y in points]
    Y = [[y] for x, y in points]
    XT = transpose(X)
    return gj_Solve(matxMultiply(XT, X), matxMultiply(XT, Y))

# 构造线性函数 y = mx + b
m = 3.25
b = 7
# 构造 100 个线性函数上的点，加上适当的高斯噪音
points = [[random.gauss(x, 2), random.gauss(m*x+b, 2)] for x in range(100, 200)]
# 对这100个点进行线性回归，
newm,newb = linearRegression(points)
# 将线性回归得到的函数和原线性函数比较
# print "difference value m:{}".format(Decimal(newm[0]) - Decimal(m), Decimal(newb[0]) - Decimal(b))
# for i in range(10000):
#     num = random.gauss(1, 0.95)

# if __name__ == '__main__':
#     unittest.main()
# normalNum = 0
# excNum = 0
# mean = 0
# for i in range(10000):
#     num = random.gauss(1, 0.95)
#     mean += num
#     if num >0.5 and num < 1.5:
#         normalNum += 1
#     else:
#         excNum += 1
# print "normalNum={}, excNum={}, mean={}".format(normalNum, excNum, mean/10000.0)
