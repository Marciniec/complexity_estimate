from math import sqrt
from pydoc import locate
import timeit
from functools import partial
import numpy as np
import time
from matplotlib import pyplot
from mpmath import cbrt


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
        self.complexities = {}

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

        pyplot.plot(self.x, self.y, 'o')
        pyplot.show()

    @print_complexity
    def find_closest_function(self):
        self.complexities = dict([(self.polynomial_with_coefficients(self.x, 0), 'O(1)'),
                                  (self.polynomial_with_coefficients(self.x, 1), 'O(n)'),
                                  (self.polynomial_with_coefficients(self.x, 2), 'O(n^2)'),
                                  (self.polynomial_with_coefficients(self.x, 3), 'O(n^3)'),
                                  (self.polynomial_with_coefficients(np.log2(self.x), 1), 'O(logn)'),
                                  (self.polynomial_with_coefficients(self.x * np.log2(self.x), 1), 'O(nlogn)'),
                                  (self.polynomial_with_coefficients(np.sqrt(self.x), 1), 'O(sqrt(n))')])
        closest = min(list(self.complexities.keys()))
        return self.complexities.get(closest)

    def predicting_time(self):
        coefficients = []
        if self.complexities.get(min(list(self.complexities.keys()))) == 'O(1)':
            coefficients = np.asanyarray(np.polyfit(self.x, self.y, 0))
            print("Function: {0} ".format(coefficients[0]))
        elif self.complexities.get(min(list(self.complexities.keys()))) == 'O(n)':
            coefficients = np.asanyarray(np.polyfit(self.x, self.y, 1))
            print("Function: {0}x + {1} ".format(coefficients[0], coefficients[-1]))
        elif self.complexities.get(min(list(self.complexities.keys()))) == 'O(n^2)':
            coefficients = np.asanyarray(np.polyfit(self.x, self.y, 2))
            print("Function: {0}x^2 +{1} ".format(coefficients[0], coefficients[-1]))
        elif self.complexities.get(min(list(self.complexities.keys()))) == 'O(n^3)':
            coefficients = np.asanyarray(np.polyfit(self.x, self.y, 3))
            print("Function: {0}x^3  + {1} ".format(coefficients[0], coefficients[-1]))
        elif self.complexities.get(min(list(self.complexities.keys()))) == 'O(logn)':
            coefficients = np.asanyarray(np.polyfit(np.log2(self.x), self.y, 1))
            print("Function: {0}logx + {1} ".format(coefficients[0], coefficients[-1]))
        elif self.complexities.get(min(list(self.complexities.keys()))) == 'O(nlogn)':
            coefficients = np.asanyarray(np.polyfit(self.x * np.log2(self.x), self.y, 1))
            print("Function: {0}xlogx + {1} ".format(coefficients[0], coefficients[-1]))
        elif self.complexities.get(min(list(self.complexities.keys()))) == 'O(sqrt(n))':
            coefficients = np.asanyarray(np.polyfit(np.sqrt(self.x), self.y, 1))
            print("Function: {0}sqrtx + {1} ".format(coefficients[0], coefficients[-1]))
        coefficients[1:-1] = 0
        return np.poly1d(coefficients)

    def reversed_functions(self):

        if self.complexities.get(min(list(self.complexities.keys()))) == 'O(1)':
            coefficients = np.asanyarray(np.polyfit(self.x, self.y, 0))
            print("Function: {0} ".format(coefficients[0]))

        elif self.complexities.get(min(list(self.complexities.keys()))) == 'O(n)':
            coefficients = np.asanyarray(np.polyfit(self.x, self.y, 1))

            def inverse_function(y):
                return (y - coefficients[-1]) / coefficients[0]

            print("Function: {0}x + {0} ".format(coefficients[0], coefficients[1]))
        elif self.complexities.get(min(list(self.complexities.keys()))) == 'O(n^2)':
            coefficients = np.asanyarray(np.polyfit(self.x, self.y, 2))

            def inverse_function(y):
                return sqrt((y - coefficients[-1]) / coefficients[0])

            print("Function: {0}x^2+{0} ".format(coefficients[0], coefficients[1], coefficients[2]))
        elif self.complexities.get(min(list(self.complexities.keys()))) == 'O(n^3)':
            coefficients = np.asanyarray(np.polyfit(self.x, self.y, 3))

            def inverse_function(y):
                return cbrt((y - coefficients[-1]) / coefficients[0])

            print("Function: {0}x^3 + {0} ".format(coefficients[0], coefficients[1], coefficients[2],
                                                   coefficients[3]))
        elif self.complexities.get(min(list(self.complexities.keys()))) == 'O(logn)':
            coefficients = np.asanyarray(np.polyfit(np.log2(self.x), self.y, 1))

            def inverse_function(y):
                return pow(2, (y - coefficients[-1]) / (coefficients[0]))

            print("Function: {0}logx + {0} ".format(coefficients[0], coefficients[1]))
        elif self.complexities.get(min(list(self.complexities.keys()))) == 'O(nlogn)':
            coefficients = np.asanyarray(np.polyfit(self.x * np.log2(self.x), self.y, 1))

            def inverse_function(y):
                n =(y - coefficients[-1]) / coefficients[0]
                nsqare = sqrt((y - coefficients[-1]) / coefficients[0])
                return "Between {0} ".format(n) + "{0}".format(nsqare)

            print("Function: {0}xlogx + {0} ".format(coefficients[0], coefficients[1]))
        elif self.complexities.get(min(list(self.complexities.keys()))) == 'O(sqrt(n))':
            def inverse_function(y):
                return (sqrt(y) - coefficients[-1]) / coefficients[0]

            coefficients = np.asanyarray(np.polyfit(np.sqrt(self.x), self.y, 1))
            print("Function: {0}sqrtx + {0} ".format(coefficients[0], coefficients[1]))

        return inverse_function
