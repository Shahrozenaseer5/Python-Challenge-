# ============================================
# Project: Lambda Functions in Python
# Author : Shahroze
# Date   : 2025-11-12
# Description:
#   This script demonstrates the use of Python
#   lambda (anonymous) functions. Examples include:
#     - Assigning lambda functions to variables
#     - Passing lambda functions as arguments to other functions
#     - Performing simple calculations like double, cube, average, and product
# ============================================

# == Lambda Functions ==

"""
In Python, a lambda function is a small anonymous function without a name. 
It is defined using the 'lambda' keyword and has the following syntax:

    lambda arguments : expression

Lambda functions are often used in situations where a small function is required for a short period of time.
They are commonly used as arguments to higher-order functions such as map(), filter(), reduce(), etc.
Basically, lambda functions are used to perform mini tasks like square, double, divide, etc.
"""

import os
os.system('cls')

# Example:
# def double(x):
#     return x*2

double = lambda x: x * 2  # a lambda function will take x and return x*2
# 👉 “We can assign a lambda function to a variable using the lambda keyword.”

cube = lambda y: y * y * y
avg = lambda x, y, z: (x + y + z / 3)
multiple = lambda x, y: x * y

print(double(6))
print(cube(10))
print(avg(4, 8, 12))
print(multiple(44, 22))

# We need to create a lambda function first and then call it to see the desired output

# We can pass a function to a function:
def appl(fx, value):
    return 6 + fx(value)

"""
Inside appl(), it does:
6 + fx(value)
So it calls the function fx() with the argument value,
and then adds 6 to the result.

When you call:
appl(cube, 2)
you’re passing the function cube and the number 2.
Assuming your cube function is defined like this:

def cube(x):
    return x ** 3

then fx(value) becomes cube(2), which is 8.
Finally, 6 + fx(value) becomes:
6 + 8 = 14
"""

# print(appl(cube , 2))
# Or we can write:
print(appl(lambda x: x * x * x, 2))  # output will be same
# Anonymous means 'without name'. Lambda function is an anonymous function until we assign it to a variable.
print(appl(lambda x: x * x, 2))  # 6 + 2*2 = 10

# Lambda function to calculate product of two numbers with additional print statement:
a = 68
b = int(input('Enter number: '))
(lambda a, b: print(f"{a} * {b} = {a * b}"))(a, b)
# Just writing a lambda defines it — it won’t run until you call it.
# Lambda function is limited to a single expression.
