"""
================================================================================
Project: Operator Overloading in Python
File: Operator_Overloading.py
Author: Shahroze
Date: 2026-01-23
================================================================================

Description:
-------------
This file demonstrates the concept of operator overloading in Python. 
It includes examples of:
1. Overloading arithmetic operators for custom classes (Point, Vector, Rectangle)
2. Overloading comparison operators (Book, Employee, BankAccount)
3. Overloading the length operator for a Playlist class
4. A mini project: BankAccount class implementing multiple operator overloads 
   (+ for deposit, - for withdrawal, > and == for balance comparison, len() for 
   transaction count)

Purpose:
---------
To illustrate how operator overloading can make custom classes more intuitive, 
readable, and aligned with Python's built-in types.

Usage:
------
Run this file in a Python 3 environment to see operator overloading in action. 
All classes have simple test cases demonstrating functionality.

Notes:
------
- Each class demonstrates a different type of operator overloading.
- Designed for learning, demonstration, and GitHub portfolio purposes.
================================================================================
"""

"""
Operator Overloading : 
                      operator overloading is a feature in python that allows developers to redefine behavior of 
                      mathematical and comparison operators for custom data types. This means that you can use the
                      standard mathematical operators (+, -, *, /) and comparison operators (<, >, ==) in your own 
                      classes. Just as you do for built-in data types (int, float, str).

                      "Operator overloading means customizing what operators like + or == do for your own classes,
                      instead of using Python’s default behavior".

Why do we need Operator Overloading ? 
                                     - Operator overloading allows you to create more intuitive and readable code.
                                     for example, consider a custom class that represents a point in 2D space. You 
                                     could define a method called 'add' to add both points together. But using the '+' 
                                     operator makes the code more concise and readable. 
"""
import os
os.system('cls')
class Point :
    def __init__(self, x, y) :
       self.x = x
       self.y = y
    
    def __add__(self, other) :
        return Point(self.x + other.x, self.y + other.y)
P1 = Point(2, 4)
P2 = Point(6, 8)
P3 = P1 + P2
print(P3.x, P3.y) # output will be 8 and 12

class Vector : 
    def __init__(self, i, j, k) :
        self.i = i
        self.j = j
        self.k = k

    def __str__(self) :
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self, x) :
        return Vector(self.i + x.i, + self.j + x.j, + self.k + x.k)
v1 = Vector(3,5,7)
print(f"v1 = ",v1)

v2 = Vector(2,4,6)
print(f"v2 = ",v2)
print(f"v1 + v2 = ", v1 + v2)
print(type(v1 + v2))

"""
Exercise 1: Equality operator == (__eq__)
Scenario : 
=> Create a class Book with:
=> title
=> author
=> price

Task :
Two books should be considered equal if:

=> their title and author are the same
(price should be ignored)
"""
class Book :
    def __init__(self, title, author, price): 
        self.title = title
        self.author = author
        self.price = price

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
book1 = Book('Sherlock Holmes', 'Canon Doyle', 2000)
book2 = Book('Sherlock Holmes', 'Canon Doyle', 1600)
print(book1 == book2)

"""
Exercise 2: Greater than operator > (__gt__)
Scenario :
=> Create a class Employee with:
=> name
=> salary
=> Task

=> Compare two employees based on salary using >.
"""
class Employee :
    def __init__(self, name, salary, task) :
        self.name = name
        self.salary = salary
        self.task = task

    def __gt__(self, other) :
        return self.salary > other.salary
    
e1 = Employee('Arjun', 60000, 'Developer')
e2 = Employee('Naila', 80000, 'HR')
print(e2 > e1)

"""
Exercise 3: Multiplication operator * (__mul__)
Scenario :
=> Create a class Rectangle with:
=> length
=> width

Task :
=> When you multiply a rectangle by a number, both dimensions should scale.
"""
class Rectangle :
    def __init__(self, length, width) :
        self.length = length
        self.width = width

    def __mul__(self, x) : 
        return Rectangle(self.length * x, self.width * x)
    
r = Rectangle(10, 15)
new_r = r * 2
print(f"New length is : ",new_r.length,'\n',"New Width is : ", new_r.width)

"""
Exercise 4: Length operator len() (__len__)
Scenario :
=> Create a class Playlist that stores:
=> a list of song names

Task : 

=> Calling len() on a playlist should return the number of songs.
"""
class Playlist :
    def __init__(self, songs) :
        self.songs = songs

    def __len__(self) :
        return len(self.songs)
    
lst = Playlist(['tere bina', 'saiyara', 'millionaire', 'Brown Rung'])
print(len(lst))

"""
Project: BankAccount Class
Objective : 
=> Create a bank account class where operators make sense:

+ → deposit money

- → withdraw money

== → compare balances

> → check which account has more money

len() → see how many transactions have occurred
"""
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def __add__(self, amount):
        # Deposit money
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        return self

    def __sub__(self, amount):
        # Withdraw money
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
        return self

    def __eq__(self, other):
        # Compare balances
        return self.balance == other.balance

    def __gt__(self, other):
        # Check which account has more money
        return self.balance > other.balance

    def __len__(self):
        # Number of transactions
        return len(self.transactions)

    def __str__(self):
        return f"{self.owner}'s account: Balance = {self.balance}"

acc1 = BankAccount("Ali", 1000)
acc2 = BankAccount("Ahmed", 1500)

# Deposit and withdraw using operators
acc1 + 500
acc2 - 300

print(acc1)          # Ali's account: Balance = 1500
print(acc2)          # Ahmed's account: Balance = 1200

# Compare balances
print(acc1 == acc2)  # False
print(acc1 > acc2)   # True

# Transactions count
print(len(acc1))     # 1
print(len(acc2))     # 1
