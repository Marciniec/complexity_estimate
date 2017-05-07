from math import sqrt
from pydoc import locate
import timeit
from functools import partial
import numpy as np
import time
from mpmath import cbrt
import logging
import complexitymeasureproject.custom_exeptions


def average(fun):
    def new(self, x, degree):
        logging.debug("Computing average absolute difference between measured"
                      " points and theoretical fitted function")
        return np.average(np.abs(fun(self, x, degree)))

    return new


def print_complexity(func):
    def measure(self):
        print('Approximated complexity of your function is {0}'
              .format(func(self)))

    return measure


class Complexity:
    def __init__(self, class_name, whole_time=30):
        logging.basicConfig(filename='log.txt', level=logging.DEBUG)
        logging.info("Start")
        class_name = class_name
        my_class = locate(class_name)
        logging.debug("Loading class")
        try:
            self.object = my_class()
            logging.debug("Creating loaded class object")
        except TypeError:
            logging.info("TypeError occurred probably due to wrong"
                         " class name")
            raise complexitymeasureproject.custom_exeptions. \
                WrongClassException("Class is invalid next time please "
                                    "input valid class")
        logging.debug("Initialising object variables")
        self.x = []
        self.y = []
        self.complexities = {}
        self.complexity = ''
        if whole_time >= 5:
            whole_time -= 2
        self.end_time = whole_time
        logging.debug("Setting time when loop should break")

    @average
    def polynomial_with_coefficients(self, x, degree):
        coefficients = np.asanyarray(np.polyfit(x, self.y, degree))
        coefficients[1:-1] = 0
        p = np.poly1d(coefficients)(x)
        return p - self.y

    def measure_time(self):
        logging.debug("Checking times for n in range from 1 to 100")
        for i in range(1, 100):
            if time.process_time() > self.end_time:
                break
            N = i
            self.object.set_up(N)
            test_n_Timer = timeit.Timer(partial(self.object.function))
            t = test_n_Timer.timeit(number=10)
            self.x.append(N)
            self.y.append(t)
            self.object.cleaning()
        logging.debug("After measurement self.x: " + str(self.x) + " self.y: "
                      + str(self.y))

    @print_complexity
    def find_closest_function(self):
        complexities = dict([(self.polynomial_with_coefficients(self.x, 0),
                              'O(1)'),
                             (self.polynomial_with_coefficients(self.x, 1),
                              'O(n)'),
                             (self.polynomial_with_coefficients(self.x, 2),
                              'O(n^2)'),
                             (self.polynomial_with_coefficients(self.x, 3),
                              'O(n^3)'),
                             (self.polynomial_with_coefficients(
                                 np.log2(self.x), 1), 'O(logn)'),
                             (self.polynomial_with_coefficients(
                                 self.x * np.log2(self.x), 1), 'O(nlogn)'),
                             (self.polynomial_with_coefficients(
                                 np.sqrt(self.x), 1), 'O(sqrt(n))')])
        closest = min(list(complexities.keys()))
        logging.debug("Getting smallest average in difference: " +
                      str(closest))
        logging.debug("Returning complexity")
        self.complexity = complexities.get(closest)
        return complexities.get(closest)

    def predicting_time(self):
        logging.debug("Initializing empty list with coefficients")
        coefficients = []
        if self.complexity == 'O(1)':
            coefficients = np.asanyarray(np.polyfit(self.x, self.y, 0))
            print("Function: {0} ".format(coefficients[0]))
        elif self.complexity == 'O(n)':
            coefficients = np.asanyarray(np.polyfit(self.x, self.y, 1))
            print("Function: {0}x + {1} ".format(coefficients[0],
                                                 coefficients[-1]))
        elif self.complexity == 'O(n^2)':
            coefficients = np.asanyarray(np.polyfit(self.x, self.y, 2))
            print("Function: {0}x^2 +{1} ".format(coefficients[0],
                                                  coefficients[-1]))
        elif self.complexity == 'O(n^3)':
            coefficients = np.asanyarray(np.polyfit(self.x, self.y, 3))
            print("Function: {0}x^3  + {1} ".format(coefficients[0],
                                                    coefficients[-1]))
        elif self.complexity == 'O(logn)':
            coefficients = np.asanyarray(np.polyfit(np.log2(self.x),
                                                    self.y, 1))
            print("Function: {0}logx + {1} ".format(coefficients[0],
                                                    coefficients[-1]))
        elif self.complexity == 'O(nlogn)':
            coefficients = np.asanyarray(np.polyfit(self.x * np.log2(self.x),
                                                    self.y, 1))
            print("Function: {0}xlogx + {1} ".format(coefficients[0],
                                                     coefficients[-1]))
        elif self.complexity == 'O(sqrt(n))':
            coefficients = np.asanyarray(np.polyfit(np.sqrt(self.x),
                                                    self.y, 1))
            print("Function: {0}sqrtx + {1} ".format(coefficients[0],
                                                     coefficients[-1]))
        coefficients[1:-1] = 0
        logging.debug("Computed accurate coefficients to our function: "
                      + str(coefficients))
        logging.debug("Returning function")
        return np.poly1d(coefficients)

    def reversed_functions(self):
        logging.debug("Beginning commuting inverse function")
        if self.complexity == 'O(1)':
            coefficients = np.asanyarray(np.polyfit(self.x, self.y, 0))

            def inverse_function(y):
                return coefficients[0] * y

            print("Inverse Function: {0} ".format(coefficients[0]))

        elif self.complexity == 'O(n)':
            coefficients = np.asanyarray(np.polyfit(self.x, self.y, 1))

            def inverse_function(y):
                return (y - coefficients[-1]) / coefficients[0]

            print("Inverse Function: (y -{0}) / {1} ".format(coefficients[-1],
                                                             coefficients[0]))
        elif self.complexity == 'O(n^2)':
            coefficients = np.asanyarray(np.polyfit(self.x, self.y, 2))

            def inverse_function(y):
                return sqrt((y - coefficients[-1]) / coefficients[0])

            print("Inverse Function: sqrt((y-{0})/{1}) ".format(
                coefficients[-1], coefficients[0]))
        elif self.complexity == 'O(n^3)':
            coefficients = np.asanyarray(np.polyfit(self.x, self.y, 3))

            def inverse_function(y):
                return cbrt((y - coefficients[-1]) / coefficients[0])

            print("Inverse Function: cbrt((i-{0})/{1}) ".format(
                coefficients[-1], coefficients[0]))
        elif self.complexity == 'O(logn)':
            coefficients = np.asanyarray(np.polyfit(np.log2(self.x),
                                                    self.y, 1))

            def inverse_function(y):
                try:
                    two_to_n = pow(2, (y - coefficients[-1]) /
                                   (coefficients[0]))
                except OverflowError:
                    raise complexitymeasureproject.custom_exeptions. \
                        OverFlow("Overflow occurred during computing "
                                 "reverse function to logn")
                return two_to_n

            print("Inverse Function: 2^((y-{0})/{1}) ".format(
                coefficients[-1], coefficients[0]))
        elif self.complexity == 'O(nlogn)':
            coefficients = np.asanyarray(np.polyfit(self.x * np.log2(self.x),
                                                    self.y, 1))

            def inverse_function(y):
                n = (y - coefficients[-1]) / coefficients[0]
                nsqare = sqrt((y - coefficients[-1]) / coefficients[0])
                return "Between {0} ".format(n) + "{0}".format(nsqare)

            print("There's no inverse function to nlogn")
        elif self.complexity == 'O(sqrt(n))':
            def inverse_function(y):
                return ((y - coefficients[-1]) / coefficients[0]) *\
                       ((y - coefficients[-1]) / coefficients[0])

            coefficients = np.asanyarray(np.polyfit(np.sqrt(self.x),
                                                    self.y, 1))
            print("Inverse Function: ((y - {0})/ {0})^2  ".format
                  (coefficients[0], coefficients[1]))

        logging.debug("Computed approximate inverse function and returning it")
        return inverse_function
