"""
================================================================================
Project      : Walrus Operator Exercises
File Name    : walrus_operator.py
Author       : Shahroze
Created On   : 2026-03-03
Description  : 
    This Python file contains multiple exercises demonstrating the use of 
    the Walrus Operator (:=) introduced in Python 3.8. It includes:
        1. User input validation loops
        2. File reading with conditional filtering
        3. Efficient numeric computations
        4. Data parsing and filtering (ML-style)
        5. Combined file reading and numeric filtering exercises
    Each exercise illustrates real-world scenarios where the walrus operator
    improves code readability and efficiency.

Python Version: 3.8+
================================================================================
"""

"""
Walrus-Operator : 
                 is a new addition in python 3.8 and allows you to assign a value to a variable within an expression.
                 This can be useful when you need to use a value multiple times in a loop, but don't want to repeat 
                 calculation.
                 Walrus-Operator is represented by :=
                 It can be used in a variety of contexts like if statements and loop .

"""
import os
os.system('cls')
a = True
print(a:=False) # walrus operator within an expression

numbers = [1,2,3,4,5,6,7]
while (n := len(numbers)) > 0 :
    print(numbers.pop())
"""
In this example, the length of 'numbers' list is assigned to the variable 'n' using the walrus operator. 
Value of 'n' is then used in the condition of while loop, so that the loop will continue to execute until the numbers 
list is empty. 
"""

happy = False
print(happy)

# Before Walrus operator :
# foods = list()
# while True :
#   food = input("What food you like ? ")
#   if food == 'quit' :
#      break
#   foods.append(food)

# After Walrus Operator :
foods = list()
while (food := input("What food you like ? ")) != 'quit' :
  foods.append(food)

"""
In this example, we assign input value to 'food' variable, under a while loop.
After this, we have added a condition, if user input is not equal to 'quit', it will print input until
user give input 'quit'.
"""

"""
Exercise 1 : User Input Validation Loop

Write a program that:
=> Keeps asking the user to enter a number
=> Stops only when the user enters a number greater than 100
=> Prints: "Accepted:" and the number

Constraint:
=> Use walrus inside the while condition.
"""
while True:
    try:
        if (n := int(input("Enter number : "))) > 100:
            break
        print("Accepted :", n)
    except ValueError:
        print("Invalid input")
"""
flow is:
=> input() runs
=> Converted to int
=> Assigned to n
=> Compared with <= 100
=> Loop continues or stops
"""


# Exercise 2 : File Reading (Avoid Double Work)
# => You have a file data.txt.
# Write a program that:
# => Reads lines one by one
# => Prints only lines whose length is greater than 20 characters
# Constraint:
# => Use walrus to assign the line inside the loop condition
# => Avoid calling readline() twice

filename = "data.txt"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        pass
print("File created successfully")

# Check if the file exists
if os.path.exists(filename):
    # Open the file and read line by line
    with open(filename, "w") as f:
      f.write("This is a very long line example to test.\nAnother short line.\nYet another long line for testing.\n")

with open(filename, "r") as f:
    while (line := f.readline()):
        if len(line.strip()) > 20:
            print(line.strip())

# Exercise 3 : Efficient Computation Check
# You have a list of numbers:
# numbers = [5, 12, 7, 30, 18]

# Write a program that:
# => Loops through numbers
# => Prints numbers whose square is greater than 200
# Constraint:
# => Calculate the square only once using walrus
# => Don’t repeat num ** 2

numbers = [5, 12, 7, 30, 18]
for num in numbers :
  if (square := num**2) > 200 :
    print(square)

# Exercise 4 : Simple Data Filtering (ML-style thinking)

# we have:
# data = ["42", "hello", "100", "world", "256"]

# Write a program that:
# => Converts items to integers when possible
# => Prints only numbers greater than 50

# Constraint:
# => Use walrus inside if
# => Avoid converting the same string twice
# => Handle conversion safely (hint: try/except)

data = ["42", "hello", "100", "world", "256"]
for i in data :
  try :
    if (num := int(i)) > 50 :
      print(num)
  except ValueError :
    pass

# Exercise 5: Filter Large Numbers from a File
# Scenario :
# You have a file called numbers.txt containing one number per line, some lines might be empty
# or non-numeric.

# You want to:
# => Read the file line by line
# => Convert each line to an integer if possible
# => Only keep numbers greater than 50
# => Print them immediately
# => Do all of this using walrus operator.

# Task : 
# => Use a try/except block for conversion
# => Assign the integer to a variable inside the if condition using walrus
# => Only print numbers > 50

filename1 = "numbers.txt"

# Ensure file exists with some sample content
if not os.path.exists(filename1):
    with open(filename1, "w") as f:
        f.write("42\nhello\n100\n30\n256\n\n50\nabc")

# Open the file and process
with open(filename1, "r") as f:
    while (line := f.readline()):
      try :
          if (num := int(line)) > 50 :
            print(num)
      except ValueError :
        pass