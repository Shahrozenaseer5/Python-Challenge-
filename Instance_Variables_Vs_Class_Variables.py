"""
================================================================================
Project Name:   Instance vs Class Variables Practice
Author:         Shahroze
Date:           2025-12-30
Description:    
    This Python file demonstrates the difference between instance variables
    and class variables using practical examples. It includes:

        - Employee class example
        - Car class example with class and instance variables
        - Library class example showing proper use of instance variables
        - Exercises for practicing variable behavior in OOP

Key Concepts:
    - Instance variables: unique to each object
    - Class variables: shared among all objects of a class
    - Shadowing class variables with instance variables
    - Proper design to avoid shared mutable state
================================================================================
"""

# Instance Variables VS Class Variables
"""
Why OOP?
=> Maps real world entities 
=> Logical grouping of variables & functions 
Instance Variable: 
=> Associated with an instance. Not with a class. 

Class Variable: 
=> Associated with class, not with an instance. 
Shared among all instances 
                       Employee.companyName 
What is the difference b/w them in Python? 
Class Variables:
=> Defined at the class level and shared among all instances of a class. 
=> Defined outside of any method. 
=> Usually used to store information that is common to all instances of a class, such as constants or 
a counter for the number of objects of a class that have been created. 

Instance Variables:
=> Defined at the instance level and are unique to each instance of a class. 
=> Defined inside methods using the self keyword. 
=> Used to store data that varies from one instance to another. 
"""
import os 
os.system('cls')

class Employee:
    companyName = 'Samsung' # class variable
    no_Of_Employees = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.05
        Employee.no_Of_Employees += 1

    def showDetails(self):
        print(f'Employee name is {self.name} and raise amount in {Employee.no_Of_Employees} sized "{self.companyName}" will be : {self.raise_amount}')

emp1 = Employee('Rehan')
# Employee.showDetails(emp1)
emp1.raise_amount = 0.4 # we make new instance variable (raise_amount) for emp1 which is 0.4
emp1.companyName = 'Apple Pakistan' # here we make an new instance variable 
emp1.showDetails()
Employee.companyName = 'Google' # we change class variable for all instances
print(Employee.companyName)
emp2 = Employee('Jenie')
emp2.companyName = 'Nestle'
emp2.showDetails()
emp3 = Employee('Yash')
emp3.showDetails()
emp4 = Employee('Manpreet')
emp4.showDetails()

# Exercise 1
class Car:
    company_name = "Suzuki"
    total_cars = 0

    def __init__(self, model, price):
        self.model = model
        self.price = price
        Car.total_cars +=1

    def CarDetails(self):
        print(f'{self.company_name} have created {self.model} in just {self.price} and total cars are : {Car.total_cars}')

car1 = Car('Suzuki alto', 3300000)
car1.company_name = 'Honda' # we have created a new instance variable "company_name"
car1.CarDetails()
Car.company_name = "Hyundai" # we have updated company_name in Car class for all instances
car2 = Car('IONIQ 6', 4500000)
car2.CarDetails()
car3 = Car('Elantra', 5500000)
car3.CarDetails()

# Exercise 2
class Library:
    def __init__(self, book):
        self.book = book
        self.books = []
        self.books.append(book)

lib1 = Library("Python")
lib2 = Library("ML")

print(lib1.books)
print(lib2.books)

