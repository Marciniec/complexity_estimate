import argparse
import custom_exeptions
from pydoc import locate

import sys

from complexity import Complexity

parser = argparse.ArgumentParser()
parser.add_argument('cl', help="your class you want to load [Package].[Module].[Class]")
parser.add_argument('-t', type=int, help="time out after program has to stop (default 30s)")
parser.add_argument('-f', type=int, help="Number of elements in order to measure expected time")
parser.add_argument('-i', type=int, help="Time for which you want to determine number of elements")
arguments = parser.parse_args()

try:
    if arguments.t:
        x = Complexity(arguments.cl, arguments.t)
    else:
        x = Complexity(arguments.cl)
except custom_exeptions.WrongClassException as e:
    print(e)
    sys.exit()
x.measure_time()
x.find_closest_function()
print("Function to compute predicted time for input x elements")
func = x.predicting_time()
print("Function to compute predicted number of elements for input y seconds")
inverse = x.reversed_functions()
if arguments.f:
    try:
        v = func(arguments.f)
    except ValueError as e:
        print(e)
        sys.exit()
    print("Expected time for {0} elements is {1}".format(arguments.f, abs(v)))
if arguments.f:
    try:
        w = inverse(arguments.f)
    except custom_exeptions.OverFlow as e:
        print(e)
        sys.exit()
    except ValueError as f:
        print(f)
        sys.exit()
    print("Expected elements for {0} elements are {1}".format(arguments.f, abs(w)))
