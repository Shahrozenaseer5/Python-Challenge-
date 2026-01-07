"""
Topic: Class Methods as Alternative Constructors

Description:
This file demonstrates how class methods can be used as alternative constructors
to create objects from data that comes in different formats (strings, file-like input, etc.).
Instead of complicating the __init__ method, parsing and transformation logic
is handled inside @classmethods, keeping object initialization clean and maintainable.

Concepts Covered:
- @classmethod usage
- Alternative constructors
- Data parsing before object creation
- Clean separation of initialization and data transformation

Examples Included:
- Employee creation from dash-separated string
- Person creation from comma-separated string
- User creation from age-based input
- Product creation from multiple data formats
- Student creation from file-style input

Author: Shahroze
"""

"""
Class methods as alternative constructors :
                                           Class methods as alternative constructors are clean, readable, and flexible ways
                                           to create objects when data comes in different forms without complicating __init__.
                                           We deal with data which is in different formats in class methods (@classmethod).
"""
import os 
os.system('cls')
class Employee :
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod # here we use class methods as alternative constructors
    def FromStr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))
e1 = Employee("Rehan", 20000)   
print(e1.name)
print(e1.salary)
# if data comes in different formats like :
string = "Rehan-20000"
# a = "Zobia, 20000, Python"
# separate = a.split(',') (if we apply .split() on any string, it will give us a list of items)
# print(separate)
e2 = Employee.FromStr(string)
print(e2.name)
print(e2.salary)

class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',') # here we are making an instance of class
        return cls(name, int(age))
    
a = Person.from_string("Rohan Das, 33")
print(a.name, a.age)

"""
Exercise 1: Date-based constructor

=> Create a User class with:

=> __init__(name, year_of_birth)
=> A class method from_age(name-age_string)

Example input:

=> "Ali-25"

Inside the class method:
=> Convert age into year of birth
=> Return the object using cls(...)

Goal: practice transforming data before object creation.
"""
class User:
    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth

    @classmethod
    def from_age(cls, string):
        name,age = string.split('-')
        year_of_birth = 2026-int(age)
        return cls(name, year_of_birth)
    
a1 = User.from_age("Shehroze-28")
print(a1.name)
print(a1.year_of_birth)

"""
Exercise 2: Multiple formats, same class

=> Create a Product class with:
=> __init__(name, price)
Add two alternative constructors:
=> from_dash("Laptop-120000")
=> from_comma("Mobile,90000")

Goal: understand why one __init__ + multiple class methods is powerful.
"""
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_dash(cls, string):
        name, price = string.split('-')
        return cls(name, int(price))
    
    @classmethod
    def from_comma(cls, string):
        name, price = string.split(',')
        return cls(name, int(price))
    
p1 = Product.from_dash("Laptop-120000")
print(p1.name)
print(p1.price)
p2 = Product.from_comma("Mobile,90000")
print(p2.name)
print(p2.price)

"""
Exercise 3: File-style input simulation

Create a Student class with:
=> __init__(name, marks)
Assume data comes like this:

=> "Ahmed|88"

Write:

=> from_file_line() class method that parses this format and returns an object

Goal: think like real-world data ingestion, not textbook input.
"""
class Student :
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @classmethod
    def from_file_line(cls, string) :
        name, marks = string.split('|')
        return cls(name, int(marks))

s1 = Student.from_file_line("Ahmed|88")  
print(s1.name)  
print(s1.marks)