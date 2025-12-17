"""
================================================================================
Project         : Python Access Modifiers Examples
Author          : Shahroze
Date Created    : 2025-12-18
Description     : 
This file contains examples and exercises demonstrating Access Modifiers in Python.
It covers:
    1. Public Access Modifiers
    2. Private Access Modifiers
    3. Protected Access Modifiers

Exercises included:
    - Public: Book class with title and author attributes
    - Private: BankAccount class with private PIN and public account number
    - Protected: Employee and Manager classes demonstrating inheritance and protected members

Purpose:
    - To understand how to control access to class variables and methods
    - To learn how access modifiers help in designing clean, maintainable, and secure code
    - To provide ready-to-run examples for learning and portfolio use

Usage:
    - Run this script to see public, private, and protected access modifiers in action
    - Modify or extend classes to practice access control and inheritance
================================================================================
"""

# Access Modifiers in Python
import os
os.system('cls')
"""
Access modifiers or access specifiers in python programing are used to limit access of class variables 
and class methods outside of class while implementing the concepts of inheritance.

Types of access specifiers :
=> Public Access Modifiers
=> Private Access Modifiers
=> Protected Access Modifiers

Public Access Modifiers :
                         All the variables and methods(member function) in python are by default public. 
                         Any instance variable in a class followed by the 'self' keyword. i.e self.var_name are public accessed.
"""
# self.variable_name
class Student:
    def __init__(self, name, age):
        self.name = name # public variable
        self.age = age  # public variable

    def info(self):
        print(f'{self.name} is {self.age} years old')

obj = Student('Ainee', 33)
print(obj.name)
print(obj.age)
obj.info() 
# self.var_name is public because we can access it from outside the class.
"""
Private Access Modifiers :
                          By definition, private members of a class(variables or methods) are those members which are only accessible 
                          inside the class. We can't use private members outside the class. 

                          In Python, there is no strict concept of 'private' access modifiers like in some other programing 
                          languages. However a convention has been established to indicate that a variable or method should be 
                          considered private by prefixing it's name with double underscore '__'. This is known as a 
                          'weak internal use indicator' and it is a convention only, not a strict rule. Code outside the class can 
                          still access these 'private' variables and methods, but it is generally understood that they should not
                          be accessed or modified.
"""
# self.__var_name (self.__) 
class Student_1:
    def __init__(self, name, age):
        self.__age = age # an indication of private variable (age)
        self.name = name # public variable (by default)
    def __function(self):
        self.y = 34
        print(self.y)

class Subject(Student_1):
    pass

obj1 = Student_1('Hania', 23)
obj2 = Subject

# calling by object of class Student_1
# print(obj1.__age) throws an error because age is private attribute
# print(obj1.__function()) throws an error because function is private method

# # calling by object of class Subject
# print(obj2.__age) throws AttributeError
# print(obj2.__function()) throws AttributeError

"""
Private members of a class can't be accessed or inferited outside of class. If we try to access or to inferit the properties
of private members to child class(derived class), then it will throw an error.
"""

"""
Name Mangling : 
               Name Mangling in python is a technique used to protect class-private and super-class private attributes from being
               accidentally overwritten by sub_classes. Names of class-private and superclass private attributes are transformed by the
               addition of a single leading underscore and a double leading underscore respectively.
"""
class MyClass:
    def __init__(self):
        self._private_attribute = "I am a private attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()
print(my_object._private_attribute) # Output : I am a private attribute
# print(my_object.__mangled_attribute) Throwa an AttributeError
print(my_object._MyClass__mangled_attribute) # Output : I am a mangled attribute
"""
In the above example, the attribute (_private_attribute) is marked as private by convention, but can still be accessed from
outside the class. The attribute (__mangled_attribute) is private and it's name is "mangled" to (_MyClass__mangled_attribute), so it
can't be accessed directly from outside the class, but you can access it by calling (_MyClass__mangled_attribute)
"""

# Protected Access Modifiers
"""
Protected access specifiers in Python use a single underscore to indicate that a member is intended for internal use and inheritance,
not for public access. 
A protected member is written with a single underscore (_) before its name.
"""
class Employee:
    def __init__(self, name, salary):
        self._name = name        # protected
        self._salary = salary    # protected

    def _show_salary(self):     # protected method
        print(f"Salary: {self._salary}")

class Manager(Employee):
    def show_details(self):
        print(f"Manager Name: {self._name}")
        self._show_salary()

m = Manager("Ali", 80000)
m.show_details()
"""
Mini rule to remember :
=> Public: default
=> Protected: inheritance
=> Private: safety
"""

# Exercise 1 – Public
"""
Scenario:
A library tracks books. Each book has a title and author, and we want to display them freely.

Task:
=> Create a Book class with public attributes title and author.
=> Add a method show_book() that prints both.
=> Create 2 book objects and access both attributes directly and via method.
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def show_book(self):
        print(f'{self.title} is written by {self.author}')

atr_1 = Book('Rich dad Poor dad', 'Robert Kiyosaki')
print(atr_1.title)
print(atr_1.author)
atr_1.show_book()   

atr_2 = Book("The Alchemist", "Paulo Coelho")
atr_2.show_book()   

# Exercise 2 – Private
"""
Scenario:
A bank account stores a PIN number. This should never be accessed outside the class directly.

Task:
=> Create a BankAccount class with private attribute __pin and public attribute account_number.
=> Add a method show_account_info() that prints the account number and says “PIN is private.”
=> Try to access __pin directly (observe the error).
=> Access the private attribute using name mangling to see the value.
"""
class BankAccount:
    def __init__(self, account_number, pin):
        self.account_number = account_number
        self.__pin = pin
    def show_account_info(self): 
        print(f'Account number : {self.account_number} but pin ({self.__pin}) is private')

User = BankAccount(53671257365, 6474)
User.show_account_info()
# User.__pin throws an error
print(User._BankAccount__pin)

# Exercise 3 – Protected
"""
Scenario:
A company tracks employee salary, but only child classes can access it.

Task:
=> Create an Employee class with protected attributes _name and _salary.
=> Add a protected method _show_salary() that prints the salary.
=> Create a Manager child class that accesses _salary and _show_salary() to print manager details.
=> Create a manager object and call the child method.
"""
class Worker:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    def _show_salary(self):
        print(f'Salary is : {self._salary}')

class Manager(Worker):
    def details(self):
        print(f'Manager name : {self._name}')
manage = Manager('Arshad', 90000)
print(manage._name)
print(manage._salary)
manage._show_salary()