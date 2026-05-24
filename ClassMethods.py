"""
File        : ClassMethods.py
Topic       : Python Class Methods
Author      : Shahroze
Description :
    This file demonstrates the concept of Python class methods, their purpose,
    and practical use cases. It covers:
    
    - Difference between class methods and instance methods
    - Updating shared class-level state using class methods
    - Using class methods as alternative constructors (factory pattern)
    - Tracking shared data using class variables and class methods

    The file also includes hands-on exercises to reinforce concepts through
    real-world style examples.

Concepts Covered :
    - @classmethod decorator
    - cls vs self
    - Class variables vs instance variables
    - Alternative constructors
    - Shared state management

Usage :
    Run this file directly to observe outputs of each example and exercise.
"""

"""
Class Methods :
               In python, classes are a way to define custom data types that can store data and define functions that
               can manipulate that data. One type of function that can be defined within a class is called a "method". 

What are Python Class Methods : 
                               A class method is a type of method that is bound to the class and not the instance of the 
                               class. It operates on the class as a whole, rather than a specific instance of class.
                               Class methods are defined using the @classmethod decorator, followed by a function definition.
                               First argument of the function is always 'cls' which represents the class itself.

Why use Python Class Methods ?
                               Class methods are useful in several situations. For example, you might want to create a factory 
                               method that creates instances of your class in a specific way. You could define a class method, 
                               that creates the instance and returns it to the caller. Another common use case is to provide 
                               alternative constructors for your class. This can be useful if you want to create instances of your class 
                               in multiple ways, but still have consistent interface for doing so.

Syntax : 
          class Example :
             @classmethods
             def factory_method(cls, argument_1, argument_2):
                return cls(argument_1, argument_2)
"""

# Class Methods
import os
os.system('cls')
class Employee:
    company = "Apple"
    
    def show(self):
        print(f"Name is : {self.name} and Company is : {self.company}")
     
    @classmethod
    def ChangeCompany(cls, newCompany): 
        cls.company = newCompany

a1 = Employee()
a1.name = "Sham"
a1.show()
a1.ChangeCompany("Tesla")
a1.show()
print(Employee.company)

"""
Exercise 1: Global Setting Changer

Goal: Understand how a class method updates shared state.

=> Create a 'User' class with:
=> class variable platform = "Web"
=> instance variable username
=> instance method show() → prints username and platform
=> class method change_platform(cls, new_platform)

Task:
=> Create two users.
=> Show both users.
=> Change platform using one object.
=> Show both users again.

👉 Expected insight: changing via one instance affects all
"""
class User :
    platform = "Web"
    
    def __init__(self, username):
        self.username  = username
    def show(self):
        print(f"username is : {self.username} and platform is : {self.platform}")
    
    @classmethod
    def change_platform(cls, new_platform):
        cls.platform = new_platform

user1 = User("Nickolus")
user1.show()
# user1.show(input("Enter username : "))
user2 = User("Marina")
user2.show()

User.change_platform("app")
# Now platform has changed permanently by using class method "change_platform"
user1.show()
user2.show()
"""
Mental rule to remember :

=> If data belongs to everyone → class variable + class method
=> If data belongs to one object → instance variable + instance method
"""

"""
Exercise 2: Alternative Constructor (Important one)

Goal: Rock-solid understanding of cls and factory pattern.

=> Create a Student class with:
=> name
=> marks

Create a class method:
@classmethod
def from_string(cls, data):
    # data = "Ali-85"

Task:

=> Separate the string.
=> Create and return a Student object.

Use it like:
             s1 = Student.from_string("Ali-85")

=> Print student details.

👉 This is the most common real-world use of class methods.
"""
class Student :
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    @classmethod
    def from_string(cls, data):
        parts = data.split('-')
        name = parts[0]
        marks = int(parts[1])
        return cls(name, marks)

s1 = Student('Danial', 77)
s1 = Student.from_string("Danial-77")
print(s1.name)
print(s1.marks)

"""
Exercise 3: Object Counter
Goal : 
      Understand how class variables track shared state and how class methods expose that state safely.

Task :

=> Create a Car class that keeps track of how many car objects have been created.

Requirements :

=> A class variable total_cars
=> Every time a Car object is created, the counter increases
=> A class method to return total cars

Call the class method using:

=> the class name
=> an object
"""
class Car:
    total_cars = 0

    def __init__(self, brand):
        self.brand = brand
        # increase total_cars here
        Car.total_cars += 1 

    @classmethod
    def get_total_cars(cls):
        # return total_cars
       return cls.total_cars
    
c1 = Car("Toyota")
c2 = Car("Honda")
c3 = Car("BMW")

print(Car.get_total_cars())
print(c1.get_total_cars())

"""
Final mental model :

=> Class variable → shared memory
=> Instance creation → updates shared memory
=> Class method → controlled access to shared memory
"""