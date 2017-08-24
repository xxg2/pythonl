#_*_ coding:UTF-8 _*_
from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane
from hyperplane import Hyperplane

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def swap_rows(self, row1, row2):
        self.planes[row1], self.planes[row2] = self.planes[row2], self.planes[row1]

    def multiply_coefficient_and_row(self, coefficient, row):
        n = self[row].normal_vector
        k = self[row].constant_term
        new_normal_vector = n.times_scalar(coefficient)

        new_constant_term = k* coefficient

        self[row] = Plane(normal_vector=new_normal_vector, constant_term=new_constant_term)

    #交换等式，乘以非零系数

    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        n1 = self[row_to_add].normal_vector
        n2 = self[row_to_be_added_to].normal_vector
        k1 = self[row_to_add].constant_term
        k2 = self[row_to_be_added_to].constant_term

        new_normal_vector = n1.times_scalar(coefficient).plus(n2)
        new_constant_term = (k1*coefficient)+k2
        self[row_to_be_added_to] = Plane(normal_vector=new_normal_vector, constant_term=new_constant_term)

    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector.coordinates)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices
    
    #返回三角形的新方程组。获得方程组的副本
    def compute_triangular_form(self):
        system = deepcopy(self)
        num_equations = len(system)
        num_variables = system.dimension
        j=0
        for i in range(num_equations):
            while j < num_variables:
                c = MyDecimal(system[i].normal_vector.coordinates[j])
                if c.is_near_zero():
                    swap_succeeded = system.swap_with_row_below_for_nonzero_coefficient_if_able(i, j)
                    if not swap_succeeded:
                        j += 1
                        continue
                
                system.clear_coefficients_below(i, j)
                j += 1
                break
        return system

    def compute_solution(self):
        try:
            #return self.do_gaussian_elimination_and_extract_solution()
            return self.do_gaussian_elimination_and_parametrize_solution()
        except Exception as e:
            if(str(e) == self.NO_SOLUTIONS_MSG or str(e) == self.INF_SOLUTIONS_MSG):
                return str(e)
            else:
                raise e

    def do_gaussian_elimination_and_parametrize_solution(self):
        rref = self.compute_rref()
        rref.raise_exception_if_contradictory_equation()
        direction_vectors = rref.extract_direction_vectors_for_parametrization()
        basepoint = rref.extract_basepoint_for_parametrization()
        return Parametrization(basepoint, direction_vectors)

    #得出参数化形式的方向向量
    def extract_direction_vectors_for_parametrization(self):
        num_variables = self.dimension
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        free_variable_indices = set(range(num_variables)) - set(pivot_indices)
        direction_vectors = []
        for free_var in free_variable_indices:
            vector_coords = [0]* num_variables
            vector_coords[free_var] = 1
            for i, p in enumerate(self.planes):
                pivot_var = pivot_indices[i]
                if pivot_var<0:
                    break
                vector_coords[pivot_var] = -p.normal_vector.coordinates[free_var]
            direction_vectors.append(Vector(vector_coords))
        return direction_vectors

    #得出基准点，然后创建并返回相应的参数化对象
    def extract_basepoint_for_parametrization(self):
        num_variables = self.dimension
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        basepoint_coords = [0]*num_variables
        for i,p in enumerate(self.planes):
            pivot_var = pivot_indices[i]
            if pivot_var < 0:
                break
            basepoint_coords[pivot_var]=p.constant_term
        return Vector(basepoint_coords)

    def do_gaussian_elimination_and_extract_solution(self):
        rref = self.compute_rref()
        rref.raise_exception_if_contradictory_equation()
        rref.raise_exception_if_too_few_pivots()

        num_variables = rref.dimension
        solution_coordinates = [rref.planes[i].constant_term for i in range(num_variables)]
        return Vector(solution_coordinates)

    def raise_exception_if_contradictory_equation(self):
        for p in self.planes:
            try:
                p.first_nonzero_index(p.normal_vector.coordinates)
            except Exception as e:
                if str(e) == 'No nonzero elements found':
                    constant_term = MyDecimal(p.constant_term)
                    if not constant_term.is_near_zero():
                        raise Exception(self.NO_SOLUTIONS_MSG)
                else:
                    raise e

    def raise_exception_if_too_few_pivots(self):
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        num_pivots = sum([1 if index >=0 else 0 for index in pivot_indices])
        num_variables = self.dimension
        if num_pivots < num_variables:
            raise Exception(self.INF_SOLUTIONS_MSG)

    #算最简化的梯阵形式
    def compute_rref(self):
        tf = self.compute_triangular_form()
        num_equations = len(tf)
        pivot_indices = tf.indices_of_first_nonzero_terms_in_each_row()
        for i in range(num_equations)[::-1]:
            j = pivot_indices[i]
            if j<0:
                continue
            tf.scale_row_to_make_coefficient_equal_one(i,j)
            tf.clear_coefficients_above(i, j)
        return tf

    def clear_coefficients_above(self, row, col):
        for k in range(row)[::-1]:
            n = self[k].normal_vector
            alpha = -Decimal(n.coordinates[col])
            self.add_multiple_times_row_to_row(alpha, row, k)

    def scale_row_to_make_coefficient_equal_one(self, row, col):
        n = self[row].normal_vector
        beta = Decimal('1.0')/Decimal(n.coordinates[col])
        self.multiply_coefficient_and_row(beta, row)

    #查看给定下面的所有行，寻找给定变量的非零系数。如果找到不接近零的系数，则进行交换并返回true
    def swap_with_row_below_for_nonzero_coefficient_if_able(self, row, col):
        num_equations = len(self)
        for k in range(row+1, num_equations):
            coefficient = MyDecimal(self.planes[k].normal_vector.coordinates[col])
            if not coefficient.is_near_zero():
                self.swap_rows(row, k)
                return True
        return False

    # 清除行i下面的变量j的所有系数
    def clear_coefficients_below(self, row, col):
        num_equations = len(self)
        beta = MyDecimal(self[row].normal_vector.coordinates[col])
        for k in range(row+1, num_equations):
            n = self.planes[k].normal_vector
            gamma = n.coordinates[col]

            alpha = -MyDecimal(gamma)/beta
            self.add_multiple_times_row_to_row(alpha, row, k)

    #返回方程的个数
    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]

    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps

class Parametrization(object):
    BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM_MSG = ('The basepoint and direction vectors should all live in the same dimension')

    #传入向量形式的基准点和向量列表，即方向向量
    def __init__(self, basepoint, direction_vectors):
        self.basepoint = basepoint
        self.direction_vectors = direction_vectors
        self.dimension = self.basepoint.dimension
        try:
            for v in direction_vectors:
                assert v.dimension == self.dimension

        except AssertionError:
            raise Exception(self.BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        output = ''
        if self.basepoint.coordinates:
            for i in range(self.basepoint.dimension):
                output += 'x_{} = {} '.format(i+1, round(self.basepoint.coordinates[i], 3))
                for j in range(len(self.direction_vectors)):
                    output += '+ {}t_{} '.format(round(self.direction_vectors[j].coordinates[i], 3), j+1)
                output += '\n'
        return output

#测试多维向量的时候，需要将linsys中的Plane统一换成Hyperplane，确保basepoint能够找到
p1 = Hyperplane(normal_vector=Vector(['0.786','0.786']), constant_term='-0.714')
p2 = Hyperplane(normal_vector=Vector(['-0.131','-0.131']), constant_term='0.319')
s = LinearSystem([p1,p2])
print 'System 1 solution:\n{}'.format(s.compute_solution())
#-------------------------------------------------------
# p1 = Plane(normal_vector=Vector(['0.786','0.786','0.588']), constant_term='-0.714')
# p2 = Plane(normal_vector=Vector(['-0.131','-0.131','0.244']), constant_term='0.319')
# s = LinearSystem([p1,p2])
# print 'System 1 solution:\n{}'.format(s.compute_solution())
# p1 = Plane(normal_vector=Vector(['8.631','5.112','-1.816']), constant_term='-5.113')
# p2 = Plane(normal_vector=Vector(['4.315','11.132','-5.27']), constant_term='-6.775')
# p3 = Plane(normal_vector=Vector(['-2.158','3.01','-1.727']), constant_term='-0.831')
# s = LinearSystem([p1,p2,p3])
# print 'System 2 solution:\n{}'.format(s.compute_solution())
# p1 = Plane(normal_vector=Vector(['0.935','1.76','-9.365']), constant_term='-9.955')
# p2 = Plane(normal_vector=Vector(['0.187','0.352','-1.873']), constant_term='-1.991')
# p3 = Plane(normal_vector=Vector(['0.374','0.704','-3.746']), constant_term='-3.982')
# p4 = Plane(normal_vector=Vector(['-0.561','-1.056','5.619']), constant_term='5.973')
# s = LinearSystem([p1,p2,p3,p4])
# print 'System 3 solution:\n{}'.format(s.compute_solution())
#------------------------------------------------------------------
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
# s = LinearSystem([p1,p2])
# r = s.compute_rref()
# if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term='-1') and
#                 r[1] == p2):
#     print 'test case 1 failed'
#
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
# s = LinearSystem([p1,p2])
# r = s.compute_rref()
# if not (r[0] == p1 and
#                 r[1] == Plane(constant_term='1')):
#     print 'test case 2 failed'
#
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
# p4 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
# s = LinearSystem([p1,p2,p3,p4])
# r = s.compute_rref()
# if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term='0') and
#                 r[1] == p2 and
#                 r[2] == Plane(normal_vector=Vector(['0','0','-2']), constant_term='2') and
#                 r[3] == Plane()):
#     print 'test case 3 failed'
#
# p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
# s = LinearSystem([p1,p2,p3])
# r = s.compute_rref()
# if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term=Decimal('23')/Decimal('9')) and
#                 r[1] == Plane(normal_vector=Vector(['0','1','0']), constant_term=Decimal('7')/Decimal('9')) and
#                 r[2] == Plane(normal_vector=Vector(['0','0','1']), constant_term=Decimal('2')/Decimal('9'))):
#     print 'test case 4 failed'
#---------------------------------------------------------------------
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
# s = LinearSystem([p1,p2])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and t[1] == p2):
#     print 'test case 1 failed'
#
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
# s = LinearSystem([p1,p2])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and t[1] == Plane(constant_term='1')):
#     print 'test case 2 failed'
#
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
# p4 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
# s = LinearSystem([p1,p2,p3,p4])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#                 t[1] == p2 and
#                 t[2] == Plane(normal_vector=Vector(['0','0','-2']), constant_term='2') and
#                 t[3] == Plane()):
#     print 'test case 3 failed'
#
# p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
# s = LinearSystem([p1,p2,p3])
# t = s.compute_triangular_form()
# if not (t[0] == Plane(normal_vector=Vector(['1','-1','1']), constant_term='2') and
#                 t[1] == Plane(normal_vector=Vector(['0','1','1']), constant_term='1') and
#                 t[2] == Plane(normal_vector=Vector(['0','0','-9']), constant_term='-2')):
#     print 'test case 4 failed'
#

#---------------------------------------------------------
# p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
# p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
# p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
#
# s = LinearSystem([p0,p1,p2,p3])
# s.swap_rows(0,1)
# if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
#     print 'test case 1 failed'
#
# s.swap_rows(1,3)
# if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
#     print 'test case 2 failed'
#
# s.swap_rows(3,1)
# if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
#     print 'test case 3 failed'
#
# s.multiply_coefficient_and_row(1,0)
# if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
#     print 'test case 4 failed'
#
# s.multiply_coefficient_and_row(-1,2)
# if not (s[0] == p1 and
#                 s[1] == p0 and
#                 s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#                 s[3] == p3):
#     print 'test case 5 failed'
#
# s.multiply_coefficient_and_row(10,1)
# if not (s[0] == p1 and
#                 s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
#                 s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#                 s[3] == p3):
#     print 'test case 6 failed'
#
# s.add_multiple_times_row_to_row(0,0,1)
# if not (s[0] == p1 and
#                 s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
#                 s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#                 s[3] == p3):
#     print 'test case 7 failed'
#
# s.add_multiple_times_row_to_row(1,0,1)
# if not (s[0] == p1 and
#                 s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
#                 s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#                 s[3] == p3):
#     print 'test case 8 failed'
#
# s.add_multiple_times_row_to_row(-1,1,0)
# if not (s[0] == Plane(normal_vector=Vector(['-10','-10','-10']), constant_term='-10') and
#                 s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
#                 s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#                 s[3] == p3):
#     print 'test case 9 failed'
# print s
    # print s.indices_of_first_nonzero_terms_in_each_row()
    # print '{}\n{}\n{}\n{}'.format(s[0],s[1],s[2],s[3])
    # print "# of equations in the system: {}".format(len(s))
    # print s
    #
    # s[0] = p1
    # print s[0]
    #
    # print '1e-9 is near zero: {}'.format(MyDecimal('1e-9').is_near_zero())
    # print '1e-11 is near zero: {}'.format(MyDecimal('1e-11').is_near_zero())