"""
Title: Python Introspection Tools (dir, __dict__, help)
Author: Shahroze
Description:
    This script demonstrates Python's built-in introspection tools used to
    inspect and understand objects at runtime.

    Covered concepts:
    - dir(): Lists available attributes and methods of an object
    - __dict__: Shows the internal attribute dictionary of user-defined objects
    - help(): Displays official documentation for objects, classes, and methods

Purpose:
    The goal of this file is to build clarity around object inspection,
    debugging, and exploration — essential skills for writing readable,
    maintainable Python code and working with external libraries.

Notes:
    This is an exploratory and learning-focused script, not intended for
    production use.
"""

"""
dir, __dict__, help methods :
                             These three are built-in tools Python gives you to inspect and understand objects
                             while you’re learning or debugging. Think of them as ways to “look inside” things.

dir() method : 
            dir function returns a list of all attributes and methods(including dunder methods) available for an object.
            It is a useful tool for discovering what you can do with an object.

__dict__ attribute : 
                    dict attribute returns a dictionary representation of an object's attributes.
                    (all attributes like self.name etc)

help() method :
               help function is used to get help documentation for an object, including a description of it's attributes
               and methods. it tell us whole story behind an object.
"""
import os
os.system('cls')
# dir method
x = [1, 2, 3]
print(dir(x)) # it will show a list of methods we can perform on this object 'x'
print(x.__ne__)
print(x.__setattr__)
print(x.__init_subclass__)
y = (1, 2, 3)
print(dir(y))
print(y.__getitem__)

# __dict__ attribute
class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1.4

p = Person("John", 33)
print(p.__dict__)
# By using __dict__ , we can get all attributes we set in class for this object(P)

# help() method
# print(help(str))
# For Person class
print(help(Person))