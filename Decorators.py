# -----------------------------------------------------------
# File: decorators_practice.py
# Description: Practice code for Python decorators including
#              wrappers, *args/**kwargs usage, logging,
#              timing functions, access control, caching,
#              and other real-world examples.
#
# Author: Shahroze
# Date: 10 December 2025
# -----------------------------------------------------------

import os
os.system('cls')
# Decorators in python
"""
A decorator is a function that takes another function, adds extra behavior to it, and returns a new function.

Python decorators are a powerful and versatile tool that allows you to modify the behavior of functions and methods.
There are a way to extend the functionality of a function or method without modifying the source code.

A decorator is a function that takes another function as an argument and returns a new function that modifies the
behavior of original function. The new function is often referred as "decorated function". 

A decorator is a function that receives another function as input, defines a wrapper around it, 
adds whatever behavior you want before or after the original function runs, and then returns that wrapper.

Basic structure of decorator :
                              def decorator_name(func):
                                 def wrapper():
                                 # code before
                                   func()        # calling the original function
                                 # code after
                                 return wrapper

Using Decorator : 
                  @decorator_name
                  def my_function():
                    print("Hello")

                  my_function()


Basic syntax of using a decorator is :
                                      @decorator_function:
                                      def my_function():
                                      pass
@decorator_function notation is just a shorthand of :
                                                     def my_function():
                                                       pass   
                                                     my_function = decorator_function(my_function) 

Decorators are often used to add functionality to functions and methods, such as logging, memorization and access control.                              

"""
# if i want to make changings in a function, i can create a decorator function :
def greet(fx) :
    def mfx(*args, **kwargs) : # modified fx
# Whenever we use functions with arguments, we need to use *args, **kwargs.
      print("Starting ... ✊✊✊")
      fx(*args, **kwargs) # call the function
      print("Thanks for using this function 🙂")
    return mfx # return wrapper function, not inside mfx

@greet
def hello():
    print("Hi my friend")
hello()

@greet
def plus(a,b) :
   print(a + b) 
plus(5843, 5786)

#   OR

# def hello():
#     print("Hi my friend")
# greet(hello)()

# Both methods works perfectly fine

# Example 2 :
# def add_func(add) : # add_func is a decorator
#    def modified_add() : # modified_add() is a wrapper function
#      print('We are adding two numbers :')
#      add(22, 33) # original function
#      print('We have got the Answer')
#    return modified_add

# @add_func
# def add(a,b):
#     print(a+b)
# add()

# practical Use Case :
# One comon use of decorators is to add logging to a function. For example you could use a decorator to log the arguments
# and return value of a function each time it is called :
import logging
def log_function_call(func) :
   def decorated(*args, **kwargs) :
      logging.info(f'Calling {func.__name__} with args= {args}, kwargs= {kwargs}')
      result = func(*args, **kwargs)
      logging.info(f'{func.__name__} returned {result}')
      return result
   return decorated

@log_function_call
def my_function(a,b) :   
   return a + b

"""
In the above example, the log_function_call decorator takes a function as an argument and return a new function that
logs the function call before and after the original function is called. 
"""

# In a function, *args take arguments as a tuple and **kwargs take arguments as a key value pair (dictonary)
def adding_numbers(*args) : 
# *args is helpful when we don't know how many arguments will be passed
   return sum(args)
print(adding_numbers(1,33,4,5555,3453,353,53,5)) # it will pack all numbers in a tuple

# **kwargs
def introduce(**info):
   for key, value in info.items():
    print(key, '=', value)
print(introduce(name = "Shahroze", age = 28, profession = 'ML Engineer', hobbies = 'Snooker / Entertainment', Goal = 'Become successful'))

# Using *args and **kwargs together :
def func(*args, **kwargs):
    print(args)
    print(kwargs)
func(1, 2, 3, name="Shahroze", age=30)

# Why decorators use *args and **kwargs

#Decorators wrap another function. They don’t know what arguments that function will receive. So they write:

# def wrapper(*args, **kwargs):
#     return func(*args, **kwargs)

# This makes the decorator safe for any function shape.


# Exercise 1 : Timer Decorator
"""
=> Make a decorator named timer
=> Start a timer before the function runs
=> Stop the timer after the function finishes
=> Print something like:
                        add_numbers took 0.0021 seconds

=> Return the original function’s result

Test it on : 
def add_numbers(n):
    total = 0
    for i in range(n):
        total += i
    return total
"""
import time
def timer(multiply) :
   def count(*args, **kwargs) :
      start = time.time()
      print("Start Time : ", start)
      result = multiply(*args, **kwargs)
      end = time.time()
      print("End Time : ", end)
      print("Time Taken:", end - start)
      print("Function Result:", result)
      return result
   return count

@timer 
def multiply(a,b,c) :
   print("Result of multiplication of a, b and c is : ", a * b * c)
multiply(22, 44.45, 99)

@timer
def add_numbers(n):
    total = 0
    for i in range(1,n+1):
        total = total + i
    return total
add_numbers(9)   # sums 1 through 9

# Exercise 2 : Create a decorator that counts how many times a function is called
"""
Goal:
Track the number of times a function is used.

Task:
Write a decorator call_counter that prints:

=> The function name
=> How many times it has been called so far
=> Then apply it to at least two different functions and test them.

Example behavior (not the code):

add() called 1 times
add() called 2 times
multiply() called 1 times
"""

def call_counter(functi) : 
   count = 0
   def wrapper(*args, **kwargs) :
       nonlocal count
       count = count + 1 
       print(f'{functi.__name__} has been called {count} times')
       return functi(*args, **kwargs)
   return wrapper

@call_counter
def add_numbers(n):
    total = 0
    for i in range(1,n+1):
        total = total + i
    return total
add_numbers(9)   # sums 1 through 9

@call_counter
def multiply(a,b,c) :
   print("Result of multiplication of a, b and c is : ", a * b * c)
multiply(22, 44.45, 99)

# Exercise 3 : Authorization / Access Control Decorator
"""
Let a function run only if the user has the right role.

Goal :
If role != "admin", block the function.
If role == "admin", allow it.
"""

def require_admin(func) :
   def wrapper(role, *args, **kwargs) :
      if role != 'admin' :
         print('Access denied !')
         return None
   
      return func(role, *args, **kwargs)
   return wrapper

@require_admin
def delete_user(role, user_id) :
   print(f'{role} {user_id} deleted successfully')
delete_user("guest", 15)   # blocked
delete_user("admin", 15)   # allowed 

# Exercise 4 : Cache Decorator (Memoization)
"""
Store results of previous function calls.
If the same input comes again, return cached result instantly.

Goal :

Speed up expensive functions like factorial or Fibonacci.
"""
def Cache(func):
   memo = {}
   def wrapper(*args):
      if args in memo :
         print("Returning Cache Result...")
         return memo[args]
      result = func(*args)
      memo[args] = result
      return result
   return wrapper

@Cache
def slow_add(a, b):
    print("Calculating...")
    return a + b
print(slow_add(33, 13))
print(slow_add(33, 13))