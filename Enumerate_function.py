# Enumerate Function in Python
# The enumerate() function in Python is used when you want to loop through a sequence (like a list, tuple, or string)
# and also keep track of the index (position) of each item at the same time.
# syntax : enumerate(iterable, start=0)
# Parameters:

# iterable → the sequence you want to loop over (list, tuple, string, etc.)
# start → the index number you want to start counting from (default is 0)

# linter in python : A linter in Python is a static code analysis tool that examines your Python source code to 
# identify potential errors, bugs, stylistic issues, and suspicious constructs without actually executing the code.

marks = [12, 33, 67, 78, 44, 26, 99]
# index = 0
# for mark in marks :
#   print(mark)
#   try :
#   # if (mark == 78) :
#     if (index == 6) :
#      print('Shahroze, You are awesome !')
#     index += 1    
#   except NameError : 
#     print('index is not defined')

# same code by using enumerate function :
for index,mark in enumerate(marks) :
  print(mark)
  try :
  # if (mark == 78) :
    if (index == 6) :
     print('Shahroze, You are awesome !')   
  except NameError : 
    print('index is not defined')

# Example 3 :
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
  print(index,fruit,)
print('
')
# In python, starting index is always 0 but we can customize starting index using enumerate function by passing value to start parameter in enumerate.
colors = ['red', 'yellow', 'brown', 'purple', 'pink', 'blue', 'white']
for index, color in enumerate(colors, start = 2) : # now index starts from 2.
  print(index,color)
print('
')
# Exercise 1: Print with index
fruits = ["apple", "banana", "cherry", "mango"]
for index, fruit in enumerate(fruits) :
  print(index , fruit)
print('
')
# Exercise 2: Start numbering from 1
fruits = ["apple", "banana", "cherry", "mango"]
for index, fruit in enumerate(fruits, start = 1) :
  print(index , fruit)
print('
')

# Exercise 3: Find index of a specific value
marks = [45, 67, 78, 90, 56, 78]
for index, mark in enumerate(marks) :
  if mark == 78 :
    print(f"Value 78 found at index {index}")
print('
')

# Exercise 4: Modify list elements using index
# numbers = [2, 4, 6, 8, 10]
# Use enumerate() to double each value in the list in place.
# After your loop, numbers should become: [4, 8, 12, 16, 20]
numbers = [2, 4, 6, 8, 10]
for index, num in enumerate(numbers) :
  numbers[index] = num*2
print(numbers)
print('
')

# Exercise 5: Enumerate over a string
# word = "PYTHON"
# Task:
# Print each character with its index.
lang = "PYTHON"
for index, a in enumerate(lang) :
  print(index, a)
print('
')  

# Exercise 6: Combine two lists manually
# names = ["Ali", "Sara", "Omar"]
# scores = [88, 92, 79]
names = ["Ali", "Sara", "Omar"]
scores = [88, 92, 79]
for index, name in enumerate(names):
    print(f"{name} scored {scores[index]} in the exam")
