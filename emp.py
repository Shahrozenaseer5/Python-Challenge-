"""
================================================================================
Module: emp.py
Author : Shahroze
Date   : 2026-01-11
================================================================================

Description:
-------------
This module defines the 'Person' class with practical examples of Python's
dunder (magic) methods:

1. __init__  : Initialize object attributes (name, age, gender)
2. __str__   : User-friendly string representation of the object
3. __repr__  : Developer-friendly / unambiguous representation
4. __len__   : Returns the length of the person's name

Notes:
-------
- __repr__ uses !r to get a raw representation of values.
- This module can be imported and used in other scripts to demonstrate
  dunder method behaviors.

================================================================================
"""

class Person :
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __len__(self):
        return len(self.name)
        
    def __str__(self):
        return f"person name is {self.name} person age is {self.age} person is a {self.gender}"
    
    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age}, gender = {self.gender})"
# Use !r to get raw representations of values