# ======================================================
# Title  : Local vs Global Variables in Python
# Author : Shahroze
# Date   : 7 November 2025
# ======================================================

"""
Variable:
A variable is a named location in memory that stores a value.
In Python, we assign values to variables using the assignment operator '='.
Example:
    x = 56
    y = 'Hi! my friend.'

Local Variable:
A local variable is defined within a function and is only accessible inside that function.
It is created when the function is called and destroyed when the function returns.

Global Variable:
A global variable is defined outside a function and can be accessed anywhere in the code.
"""

import os
os.system('cls')  # Clears console screen (works on Windows)

# ======================================================
# Example 1: Local vs Global Variables
# ======================================================

# x = 4
# print(f'Global variable (x) = {x}')  # Global variable

# def logic():
#     x = 67  # Local variable
#     y = 1
#     print(f'Local variable (x) = {x}')
#     print('Hi! Good to see you.')

# print(f'Global variable (x) = {x}')
# logic()
# print(f'Global variable (x) = {x}')
# print(y)  # ❌ Error: 'y' is local and cannot be accessed outside 'logic()'

# ======================================================
# Example 2: Using the 'global' Keyword
# ======================================================

x = 10  # Global variable

def my_function():
    global x  # Declares that 'x' refers to the global variable
    x = 33    # Modifies the global variable
    y = 5     # Local variable
    print(y)

my_function()
print(x)
# print(y)  # ❌ Error: 'y' is local and not accessible outside the function

# Note:
# It is not recommended to modify global variables inside functions,
# as it can lead to confusion and make code harder to debug.

# ======================================================
# Example 3: Comparing with and without 'global'
# ======================================================

x = 10  # Global variable

def without_global():
    x = 20  # Local variable (does not affect global x)
    print("Inside without_global:", x)

def with_global():
    global x
    x = 30  # Modifies the global variable
    print("Inside with_global:", x)

without_global()
print("After without_global:", x)

with_global()
print("After with_global:", x)

# ======================================================
# Summary
# ======================================================

print("\nSummary: Local variables exist only inside their function, "
      "while global variables exist throughout the program.")
