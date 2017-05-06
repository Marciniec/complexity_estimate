from pydoc import locate
import timeit
from functools import partial
import numpy as np


def average(fun):
    def new(self, x, degree):
        return np.average(np.abs(fun(self, x, degree)))

    return new


def print_complexity(func):
    def measure(self):
        print('Approximated complexity of your function is {0}'.format(func(self)))

    return measure


class Complexity:
    def __init__(self, class_name):
        class_name = class_name
        my_class = locate(class_name)
        self.object = my_class()
        self.x = []
        self.y = []

    @average
    def polynomial_with_coefficients(self, x, degree):
        coefficients = np.asanyarray(np.polyfit(x, self.y, degree))
        coefficients[1:-1] = 0
        p = np.poly1d(coefficients)(x)
        return p - self.y

    def measure_time(self):
        for i in range(1, 100):
            N = i
            self.object.set_up(N)
            test_n_Timer = timeit.Timer(partial(self.object.function))
            t = test_n_Timer.timeit(number=10)
            self.x.append(N)
            self.y.append(t)

    @print_complexity
    def find_closest_function(self):
        complexities = dict([(self.polynomial_with_coefficients(self.x, 0), 'O(1)'),
                             (self.polynomial_with_coefficients(self.x, 1), 'O(n)'),
                             (self.polynomial_with_coefficients(self.x, 2), 'O(n^2)'),
                             (self.polynomial_with_coefficients(self.x, 3), 'O(n^3)'),
                             (self.polynomial_with_coefficients(np.log2(self.x), 1), 'O(logn)'),
                             (self.polynomial_with_coefficients(self.x * np.log2(self.x), 1), 'O(nlogn)'),
                             (self.polynomial_with_coefficients(np.sqrt(self.x), 1), 'O(sqrt(n))')])
        closest = min(list(complexities.keys()))
        return complexities.get(closest)
