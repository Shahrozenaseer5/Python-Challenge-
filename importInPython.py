# How import works in python
# Importing in python is the process of loading code from a python module into the current script.
# This allows you to use the functions and variables defined in the module in our current script.
# As well as any additional modules that the imported module may depends on.

# To import a module in python, we write : 'import math'
# Once module is imported, we can use variables and functions defined in the module by using dot notation.import math
result = math.sqrt(9)* math.pi # we can access any function of math module by using math.(function_Name)
print(result)  # 3.0 will be printed

# We can also import specific functions or variables from a module by using 'from' keyword.
# To import only 'sqrt' function from math module, we can write :
from math import sqrt, pi
result = sqrt(7777)
print(f'Result of our expression is : {result}')
result_pi = result*pi
print(f'Result of given expression is : {result_pi}')

# We can import everything from the module by writing :
from math import *
res = floor(67.09 + 89.56)
print(f'Result of floor division is : {res}')
# Note : importing all funtions of a module is not recommended because in bigger projects, we need to import required modules only.

# as keyword :
# We can use short name of our module or functions / variables in module.
import pandas as pd
# pd.read_csv('filename.csv')
import math as m
result1 = m.sqrt(66)
print(f'Result of sqrt is : {result1}')
from math import sqrt as s,pi
result2 = s(99) * pi
print(f'Result of sqrt is : {result2}')
print(m.pi)
# sometimes, we give long name to our module or function/variable in module, so other people can easily understand it.
import math as math_builtin_python
print(math_builtin_python.pi)

# dir function :
# python has a built in fuction called dir that we can use to view the names of all the functions and variables defined in a module.
# This can be helpful for exploring and understanding the contents of a new module.
import tensorflow
print(dir(tensorflow)) # it will print all functions and variables of tensorflow module.
print(dir(math))
import pandas
print(dir(pandas))

# we can find out type or other information about a function / variable in a module.
print(math.nan)
# here nan stands for not a number.
print(type(math.nan))
# we can check whether a value is a number or not.
print(math.isnan(676))
# math.nan = a float representing “no valid number.”
# Useful for missing, undefined, or invalid numeric results.
