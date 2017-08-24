#_*_ coding:UTF-8 _*_
from math import sqrt,acos,pi
from decimal import Decimal

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError('The coordinates must be nonempty')
        except TypeError:
            raise TypeError('The coordinates must be iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        return Vector([Decimal(x)+Decimal(y) for x, y in zip(self.coordinates, v.coordinates)])

    def minus(self, v):
        return Vector([Decimal(x)-Decimal(y) for x, y in zip(self.coordinates, v.coordinates)])

    def times_scalar(self, c):
        return Vector([c*Decimal(x) for x in self.coordinates])

    #求向量的模
    def magnitude(self):
        return sqrt(sum([Decimal(x)**2 for x in self.coordinates]))

    #求向量的单位向量
    def direction(self):
        try:
            return self.times_scalar(1./self.magnitude())
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    #求内积
    def dot(self, v):
        return sum([Decimal(x) * Decimal(y) for x, y in zip(self.coordinates, v.coordinates)])

    #求夹角
    def angle_with(self, v, in_degrees=False):
        try:
            aaa =  Decimal(self.dot(v))
            bbb =  Decimal(self.magnitude() * v.magnitude())
            if abs(aaa - bbb)< 1e-10:
                angle_in_radians = acos(1)
            else:
                angle_in_radians = acos(aaa/bbb)

            if in_degrees:
                degrees_per_radian = 180. / pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians
        except ZeroDivisionError:
            raise Exception('Cannot angle the zero vector')

    #是否平行
    def is_parallel_to(self, v):
        return self.is_zero() or v.is_zero() or self.angle_with(v) == 0 or self.angle_with(v) == pi

    #是否正交
    def is_orthogonality(self, v):
        return abs(self.dot(v)) < 1e-10

    def is_zero(self):
        return self.magnitude() < 1e-10

    def component_cos(self, v):
        try:
            aaa =  self.dot(v)
            bbb =  self.magnitude() * v.magnitude()
            return aaa/bbb
        except ZeroDivisionError:
            raise Exception('Cannot angle the zero vector')

    def component_unit_vector(self):
        try:
            return self.direction()
        except ZeroDivisionError:
            raise Exception('Cannot angle the zero vector')

    def component_projection(self, v):
        return v.direction().times_scalar(self.magnitude()*self.component_cos(v))

    def component_height(self, v):
        return self.minus(self.component_projection(v)).magnitude()

    def cross_product(self, v):
        x_1, y_1, z_1 = self.coordinates
        x_2, y_2, z_2 = v.coordinates
        return Vector([y_1*z_2-y_2*z_1, -(x_1*z_2-x_2*z_1), x_1*y_2-x_2*y_1])

    def area_cross_product(self, v):
        return self.component_height(v)*v.magnitude()

# print '----------------------------'
# vector11 = Vector([3.039, 1.879])
# vector12 = Vector([0.825, 2.036])
# print vector11.component_projection(vector12)
# vector13 = Vector([-9.88, -3.264, -8.159])
# vector14 = Vector([-2.155, -9.353, -9.473])
# print vector13.minus(vector13.component_projection(vector14))
# vector15 = Vector([3.009, -6.172, 3.692, -2.51])
# vector16 = Vector([6.404, -9.144, 2.759, 8.718])
# print vector15.component_projection(vector16)
# print vector15.minus(vector15.component_projection(vector16))
#
# print '----------------------------'
# vector41 = Vector([8.462, 7.893, -8.187])
# vector42 = Vector([6.984, -5.975, 4.778])
# print vector41.cross_product(vector42)
# vector43 = Vector([-8.987, -9.838, 5.031])
# vector44 = Vector([-4.268, -1.861, -8.866])
# print vector43.area_cross_product(vector44)
# vector45 = Vector([1.5, 9.547, 3.691])
# vector46 = Vector([-6.007, 0.124, 5.772])
# print vector45.area_cross_product(vector46)/2
#
#
# my_vector = Vector([1,2,3])
# print my_vector
# my_Vector2 = Vector([1,2,3])
# my_vector3 = Vector([-1,2,3])
# print my_Vector2 == my_vector3
# print my_Vector2.plus(my_vector3)
# threed = zip([1,2,3], [-1,2,3], [6,6,7])
# print Vector([x+y+z for x,y,z in zip([1,2,3], [-1,2,3], [6,6,7])])
# print my_vector3.times_scalar(3)
#
# vector1 = Vector([8.218, -9.341])
# vector2 = Vector([-1.129, 2.111])
# print vector1.plus(vector2)
# print '----------------------------'
# vector21 = Vector([-0.221, 7.437])
# vector22 = Vector([8.813, -1.331, -6.247])
# print vector21.magnitude()
# print vector22.magnitude()
# vector23 = Vector([5.581, -2.136])
# vector24 = Vector([1.996, 3.108, -4.554])
# print vector23.direction()
# print vector24.direction()
# print '----------------------------'
# vector31 = Vector([7.887, 4.138])
# vector32 = Vector([-8.802, 6.776])
# print vector31.dot(vector32)
# vector33 = Vector([-5.955, -4.904, -1.874])
# vector34 = Vector([-4.496, -8.755, 7.103])
# print vector33.dot(vector34)
# vector35 = Vector([3.183, -7.627])
# vector36 = Vector([-2.668, 5.319])
# print vector35.angle_with(vector36)
# vector37 = Vector([7.35, 0.221, 5.188])
# vector38 = Vector([2.751, 8.259, 3.985])
# print vector37.angle_with(vector38, True)

