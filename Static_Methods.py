"""
========================================================================
Project       : Static Methods Practice in Python
Author        : Shahroze
Date          : 2025-12-23
Purpose : 
         This script demonstrates the use of static methods in Python
         through multiple exercises:
           1. Math utilities (static add method)
           2. User validation (is_valid_username)
           3. Library book ID validation (is_valid_book_id)
           4. Calculator safe division (safe_divide)
Notes :
    - Static methods are used when functionality logically belongs
      to a class but does not require instance (self) or class (cls) data.
    - Exercises show usage of static methods in realistic scenarios.
========================================================================
"""

"""
Static Methods :
                A static method is a method that belongs to a class, but does not depend on the instance (self) or the class (cls).
Key points:
=> No self
=> No cls
=> Behaves like a normal function
=> Lives inside a class only for logical grouping

Example:

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

Usage:
      MathUtils.add(3, 4)   # 7

Why do we need static methods?
Answer:
       When a function conceptually belongs to a class, but doesn’t need class or instance data.
"""

# Static Methods
import os 
os.system('cls')
class Math :
    def __init__(self, num):
        self.num = num
    
    def add_to_num(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a,b):
        return a + b
    
a = Math(67)
print(a.num)
a.add_to_num(89)
print(a.num)
print(Math.add(44, 77)) # we can use exact class name to access static method

# Exercise 1: User validation
"""
=> Create a User class.
=> Add a static method is_valid_username(username) that:

=> Returns True if username is a string
=> Length is at least 4 characters
=> Contains no spaces
=> Test it using the class name.
"""
class User:
    @staticmethod
    def is_valid_username(username):
        return (isinstance(username, str) 
                and len(username) >= 4 
                and " " not in username)
    
print(User.is_valid_username("Shami")) # True 
print(User.is_valid_username("Shami AB")) # False because string contain spaces
print(User.is_valid_username("Sam")) # False because string length is less than 4

# Exercise 2: Library utility
"""
=> Create a Library class.
=> Add a static method is_valid_book_id(book_id) that:
=> Accepts a book ID like "BK-1023"
=> Returns True only if it starts with "BK-" and the remaining part is numeric
=> Do not use any instance variables.
"""
class Library:
    @staticmethod
    def is_valid_book_id(book_id):
        return (
               isinstance(book_id, str)
               and book_id.startswith("BK-")
               and book_id[3 : ].isdigit()
               and " " not in book_id
               )
        
print('Checking Results of book_id .. ')
print(Library.is_valid_book_id("bk-3302")) # False because bk is in small letters
print(Library.is_valid_book_id("BK-3302"))

# Exercise 3: Calculator helper
"""
=> Create a Calculator class.
=> Add a static method safe_divide(a, b) that:
=> Returns the division result if b is not zero
=> Returns "Division not allowed" if b is zero
=> Call the method directly using the class name.
"""
class Calculator:
    @staticmethod
    def safe_divide(a, b):
        if b != 0 :
            return a / b
        else :
            return 'Division not allowed'
        
print(Calculator.safe_divide(22, 0)) 
print(Calculator.safe_divide(100000, 25))