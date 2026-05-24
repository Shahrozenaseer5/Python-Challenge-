
# Docstrings and pep-8

# These concepts are often asked in interviews
# Docstrings in Python are special string literals used to document your code. They explain what a function, class, or module does.
# They help us identify the functionality of a function, class, or module.
# Basically with docstrings, we can make description of function, which is helpful while working in a team.

# They’re written inside triple quotes (""" ... """ or ''' ... ''') right after
# the definition of a function, class, or module.
# They’re not comments — Python actually stores them in the object’s __doc__ attribute, 
# so you can access them later (for example, with the help() function).
# They make your code more understandable for others (and for yourself when you revisit it).

def square(n):
    '''This function returns square of the given number (n)'''
    print('Square of n is : ', n**2)

square(33)
print(square.__doc__)  # it will print docstring
help(square)  # Python will show the docstring along with the function signature


# Example function
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

help(add)
print(add(44, 56))  # calling add function


# PEP-8 :
# PEP-8 is a document that provides guidelines and best practices on how to write Python code.
# It was written in 2001 by Guido Van Rossum, Barry Warsaw and Nick Coghlan. 
# The primary focus of pep 8 is to improve the readability and consistency of python code.
# PEP stands for 'Python Enhancement Proposal' and there are several of them.


# The Zen of Python :
# The Zen of Python is a collection of guiding principles for writing Python code. 
# It’s like a set of philosophies that capture the “spirit” of Python.

import this  # prints a poem written by Tim Peters

# It prints only once per session unless you reload the module.
import importlib, this
importlib.reload(this)


# Multi-line docstring following PEP-257 conventions
def multiply(a, b):
    """
    Multiply two numbers.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The product of a and b.
    """
    return a * b

print(multiply.__doc__)
help(multiply)


# Alternative of 'import antigravity' in Colab
from IPython.display import Image
Image("https://imgs.xkcd.com/comics/python.png")
