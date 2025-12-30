# ============================================
# MATHEMATICS TOOLKIT - ALL IN ONE
# ============================================

import math
import statistics
from typing import List

# ============================================
# ARITHMETIC
# ============================================
class Arithmetic:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Division by zero not allowed")
        return a / b

    @staticmethod
    def power(a, b):
        return a ** b

    @staticmethod
    def modulo(a, b):
        return a % b


# ============================================
# NUMBER THEORY
# ============================================
class NumberTheory:

    @staticmethod
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def lcm(a: int, b: int) -> int:
        return abs(a * b) // NumberTheory.gcd(a, b)

    @staticmethod
    def factorial(n: int) -> int:
        if n < 0:
            raise ValueError("Negative factorial not defined")
        return math.factorial(n)


# ============================================
# ALGEBRA
# ============================================
class Algebra:

    @staticmethod
    def quadratic_roots(a, b, c):
        d = b**2 - 4*a*c
        if d < 0:
            return "Complex roots"
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        return root1, root2

    @staticmethod
    def linear_equation(a, b):
        if a == 0:
            raise ValueError("No solution")
        return -b / a


# ============================================
# TRIGONOMETRY
# ============================================
class Trigonometry:

    @staticmethod
    def sin(x):
        return math.sin(math.radians(x))

    @staticmethod
    def cos(x):
        return math.cos(math.radians(x))

    @staticmethod
    def tan(x):
        return math.tan(math.radians(x))


# ============================================
# CALCULUS (BASIC)
# ============================================
class Calculus:

    @staticmethod
    def derivative(f, x, h=1e-5):
        return (f(x + h) - f(x)) / h

    @staticmethod
    def integral(f, a, b, n=1000):
        h = (b - a) / n
        area = 0
        for i in range(n):
            area += f(a + i*h) * h
        return area


# ============================================
# STATISTICS
# ============================================
class Statistics:

    @staticmethod
    def mean(data: List[float]):
        return statistics.mean(data)

    @staticmethod
    def median(data: List[float]):
        return statistics.median(data)

    @staticmethod
    def variance(data: List[float]):
        return statistics.variance(data)

    @staticmethod
    def std_dev(data: List[float]):
        return statistics.stdev(data)


# ============================================
# LINEAR ALGEBRA
# ============================================
class LinearAlgebra:

    @staticmethod
    def dot_product(v1, v2):
        return sum(x*y for x, y in zip(v1, v2))

    @staticmethod
    def matrix_addition(A, B):
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
                for i in range(len(A))]

    @staticmethod
    def transpose(matrix):
        return list(map(list, zip(*matrix)))


# ============================================
# GEOMETRY
# ============================================
class Geometry:

    @staticmethod
    def area_circle(r):
        return math.pi * r * r

    @staticmethod
    def perimeter_circle(r):
        return 2 * math.pi * r

    @staticmethod
    def area_rectangle(l, w):
        return l * w

    @staticmethod
    def area_triangle(b, h):
        return 0.5 * b * h


# ============================================
# MAIN TESTING
# ============================================
if __name__ == "__main__":

    print("Arithmetic Add:", Arithmetic.add(10, 5))
    print("Prime Check:", NumberTheory.is_prime(17))
    print("Quadratic Roots:", Algebra.quadratic_roots(1, -5, 6))
    print("Sin 30°:", Trigonometry.sin(30))
    print("Derivative x^2 at x=2:", Calculus.derivative(lambda x: x**2, 2))
    print("Mean:", Statistics.mean([1, 2, 3, 4, 5]))
    print("Dot Product:", LinearAlgebra.dot_product([1,2], [3,4]))
    print("Circle Area:", Geometry.area_circle(7))
