import argparse
from pydoc import locate
from complexity import  Complexity
parser = argparse.ArgumentParser()
parser.add_argument('cl', help="your class")
arguments = parser.parse_args()
print(arguments.cl)
x = Complexity(arguments.cl)
x.measure_time()
x.find_closest_function()


# def my_import(name):
#     components = name.split('.')
#     mod = __import__(components[0])
#     for comp in components[1:]:
#         mod = getattr(mod, comp)
#     return mod
#
#
# mo = my_import('BasicClass.Basic')
#
