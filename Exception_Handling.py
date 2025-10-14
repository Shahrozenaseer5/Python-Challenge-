
# Exception Handling in Python / Error Handling / Try-Except Code
# Exception handling is the process of responding to unwanted or ucexpected events when a computer program runs.
# Exception handling deals with these events to avoid the program or system crashing.
# And without this process, exception would disrupt the normal operation of a program.

# Exceptions in python :
  # python has many built-in exceptions that are raised when your program encounters an error.
  # When these exceptions occur, the python interpreter stops the current process and passes it to the calling process until it is handled.
  # If not handled, program will crash.

# Python try...except :
  # try...except blocks are used in python to handle errors and exceptions.
  # the code in try block runs when there is no error.
  # if try block catches the error, then the except block is executed.

# a = input('enter number')
# print(f'Multiplication of {a} is :')
# try :
#  for i in range(1,11) :
#    print(f'{a} * {i} = {int(a)*i}')
# except Exception as e :
# except :
#   print('Invalid input')
# print('Some lines of important code...')
# print('End of program')

# #Example :
# try :
#   b = int(input('enter number : '))
# except ValueError :
#   print('ValueError')
# # Now it is possible that multiple errors are occur in code, in this case, we can use multiple except to handle multiple exceptions
# try:
#   num = int(input('enter a number : '))
#   a = [3,5,7,8]
#   print(a[num])
# except ValueError:
#   print('ValueError')
# except IndexError:
#   print('IndexError')

# Exercise 1  :
# Division Program:
# Ask the user for two numbers and divide them.
# Handle both:

# ZeroDivisionError
# ValueError (if user enters a non-numeric value)
try :
  c = float(input('enter number : '))
  d = float(input('enter number : '))
  result = c / d
  print(f'Division of {c} and {d} is : ', result)
except ValueError :
  print('ValueError')
except ZeroDivisionError :
  print('ZeroDivisionError')
# manual error handling : 
# try:
#     c = float(input('Enter first number: '))
#     d = float(input('Enter second number: '))
#     if d == 0:
#         print('Cannot divide by zero.')
#     else:
#         print(f'Result: {c / d}')
# except ValueError:
#     print('Please enter numeric values only.')

# Exercise 2 : List Index Program
# Create a list [10, 20, 30, 40, 50].
# Ask the user for an index and print the value at that index.
# Handle these errors:

# IndexError (if the user enters an invalid index)
# ValueError (if the user enters something that’s not a number)
a = [10, 20, 30, 40, 50]
try :
  print(a[int(input('Enter number : '))])
except ValueError : 
  print('Invalid input value')
except IndexError : 
  print('Index not found')

# Exercise 3: File Reader
# Goal:
# Practice handling file-related errors using try and except.
# Task:
# Ask the user to enter a file name.
# Try to open and read the file.
# Handle the following exceptions:

# FileNotFoundError → if the file doesn’t exist
# PermissionError → if the program isn’t allowed to open it
try:
    filename = input("Enter file name: ")        # take user input
    with open(filename, "r") as file:            # try to open the file
        content = file.read()
        print("File content:
", content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
# Create a small program that:
# Asks the user for a filename to read.
# Reads the file and displays its content.
# Then asks for a new file name and writes the same content into it.
# Handles these exceptions:
# FileNotFoundError
# PermissionError
# IOError (for any general input/output error)
try:
    filename = input("Enter file name: ")        # take user input
    with open(filename, "r") as file:            # try to open the file
        content = file.read()
        print("File content:
", content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
try : 
    filename2 = input("Enter file name: ")
    with open(filename2, "r") as file:            # try to open the file
        content2 = file.read()
        print("File content:
", content2)
except IOError :
    print('Other error')
# Exercise 4: Custom Exception
# Negative Age Error:
# Write a program that asks for a person’s age.
# If the age is negative, raise your own exception:
try :
 PersonAge = int(input('Enter your age : '))
 if PersonAge < 0 :
  print('Invalid age. Age cannot be negative.')
 else :
  print('Your age is:', PersonAge)
except ValueError :
  print('Invalid age')

# Custom Exception :
# class NegativeAgeError(Exception):
#     pass

# try:
#     PersonAge = int(input('Enter your age: '))
#     if PersonAge < 0:
#         raise NegativeAgeError
#     print('Your age is:', PersonAge)
# except NegativeAgeError:
#     print('Invalid age. Age cannot be negative.')
# except ValueError:
#     print('Invalid input. Please enter a number.')

# Exercise 5 : else and Finally
# Square Root Calculator:
# Ask user for a number.
# If valid and non-negative, print the square root (use num ** 0.5).
# If invalid input → ValueError.
# If negative → handle with a message.
# Use else to print result
try:
    i = int(input('Enter number: '))
    if i < 0:
        print('Negative number')
    else:
        SquareRootCalculator = i ** 0.5
        print(f'Square root of {i} is: {SquareRootCalculator}')
except ValueError:
    print('Invalid input')
else:
    print('Square root calculated successfully.')
finally:
    print('Program ended.')
# ✅ 1. else block — runs only if no exception happens
# You use else when you have code that should only run if the try part succeeded completely (no errors raised).
# Example:
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid number.")
else:
    print("Division successful! Result:", result)

# 🔹 When to use else :
# When you want to separate your main logic from your error handling.
# Code in else is what happens if everything goes right.
# It keeps your try block clean — the try only includes risky operations.

# ✅ 2. finally block — runs no matter what happens

# You use finally when you want something to always happen — whether an error occurs or not.
# Example:
try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing file or cleaning up resources.")
    # file.close()  # (good place to close resources)

# 🔹 When to use Finally:
# To clean up — like closing files, releasing connections, or freeing memory.
# To print a final message or log result, even if something failed.

# ⚡ Summary Table
# Block	When it Runs	Purpose
# try :	Always	Contains risky code that may cause errors
# except :	Only if an exception occurs	Handles specific errors
# else :	Only if no exception occurs	Runs main logic that depends on successful try
# finally :	Always	Cleanup or final statements (like closing files)

# Mini Calculator:
# Make a small calculator that:
# Takes two numbers and an operator (+, -, *, /)
# Performs the operation using try-except
# Handles all possible input errors
# Prints "Calculation complete" in finally
try : 
  num1 = int(input('Enter first number : '))
  num2 = int(input('Enter second number : '))
  operator = input('Enter operator : ')
  if operator == '+':
        print('Result:', num1 + num2)
  elif operator == '-':
        print('Result:', num1 - num2)
  elif operator == '*':
        print('Result:', num1 * num2)
  elif operator == '/':
        print('Result:', num1 / num2)
  else:
        print('Invalid operator.')
except ValueError: 
  print('Invalid input')
except ZeroDivisionError : 
  print('Invalid input')
finally :
  print('Calculation complete.')
