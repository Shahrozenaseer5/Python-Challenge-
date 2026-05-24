"""
================================================================================
Project: Python Dunder Methods Practice
Author : Shahroze
Date   : 2026-01-11
================================================================================

Description:
-------------
This file demonstrates practical usage of Python's "dunder" (double underscore)
or "magic" methods. It includes examples for:

1. __init__      : Object initialization
2. __str__       : User-friendly string representation
3. __repr__      : Developer-friendly representation
4. __len__       : Behavior with len()
5. __call__      : Making objects callable like functions
6. Custom module import (emp.py)

Classes included:
------------------
- Book
- Employee
- Person (imported from emp.py)
- Point
- Counter
- LengthChecker

Usage:
-------
- Run the script to see how each dunder method behaves.
- Modify or extend classes to experiment with other magic methods.

Notes:
-------
- __repr__ ideally returns a string that can recreate the object.
- __str__ is user-friendly output for print().
- __call__ allows objects to be invoked like functions.

================================================================================
"""

"""
Magic / Dunder Methods :
                        Dunder methods are special methods in Python whose names start and end with double underscores. 
                        “Dunder” just means double underscore.
                        Python calls them automatically behind the scenes.

Common dunder methdos :
                       __init__ → runs when an object is created
                       __str__ → what print(object) shows
                       __repr__ → developer-friendly representation
                       __add__ → behavior of +
                       __len__ → behavior of len()
                       __eq__ → behavior of ==
                       __getitem__ → indexing like obj[i]

Difference between __str__ and __repr__ :
                       __repr__ should return a string that ideally lets you recreate the object, 
                       if you pass that string back to Python.
                       repr(obj)  →  a string that could be used to rebuild obj
                       if str is missing then python executes repr

__call__ method :
                 __call__ lets you call an object like a function.

"""
from emp import Person # from emp.py, import Person class
import os
os.system('cls')
# Example 1
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __len__(self):
        return self.pages

b = Book('Python', 250)
print(str(b))
print(len(b))

# Example 2
class Employee :
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)
    
e = Employee("Annie")
print(e.name)
print(len(e))

# using imported file :
a = Person("Rohan Das", 33, "male")
print(str(a))
print(len(a))
print(repr(a))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(2,3)
print(repr(p))

# call method
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count

c = Counter()
print(c()) # 1
print(c()) # 2
print(c()) # 3

class LengthChecker:
    def __init__(self, min_length):
        self.min_length = min_length

    def __call__(self, text):
        return len(text) >= self.min_length

check = LengthChecker(5)

print(check("hello"))   # True because length = 5 
print(check("hi"))      # False
print(check("bestfriend")) # True because length > 5