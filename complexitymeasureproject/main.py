import complexitymeasureproject.custom_exeptions
import sys

from complexitymeasureproject.complexity import Complexity


def show_complexity(cl, t=30):
    try:
        x = Complexity(cl, t)
    except complexitymeasureproject.custom_exeptions.WrongClassException as e:
        print(e)
        sys.exit()
    x.measure_time()
    x.find_closest_function()


def predict_time(cl, val, t=30):
    try:
        x = Complexity(cl, t)
    except complexitymeasureproject.custom_exeptions.WrongClassException as e:
        print(e)
        sys.exit()
    x.measure_time()
    x.find_closest_function()
    print("Function to compute predicted time for input x elements")
    return abs(x.predicting_time()(val))


def predict_elements(cl, val, t=30):
    try:
        x = Complexity(cl, t)
    except complexitymeasureproject.custom_exeptions.WrongClassException as e:
        print(e)
        sys.exit()
    x.measure_time()
    x.find_closest_function()
    print("Function to compute predicted number of elements for input y "
          "seconds")
    return abs(x.reversed_functions()(val))
