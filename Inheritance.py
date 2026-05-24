"""
===========================================================
Title       : Python OOP – Inheritance & Polymorphism
Author      : Shahroze
Description :
    This file demonstrates core Object-Oriented Programming
    concepts in Python with practical, step-by-step examples.

    Covered topics:
    - Single Inheritance
    - Multi-Level Inheritance
    - Method Overriding
    - Polymorphism
    - Real-world class hierarchy design

    Each section includes:
    - Clear problem scenarios
    - Clean class structures
    - Proper parent-child relationships
    - Reusable and maintainable methods

Purpose :
    This file is part of my Python learning journey and serves
    as a long-term portfolio reference on GitHub. The focus is
    on building strong fundamentals that scale to real-world
    projects and future ML applications.

Last Updated : 2025
===========================================================
"""

# Inheritance in Python
# Inheritance means you can create a new class from an existing class, without rewriting the same code again.
"""
'Think of it as a “parent → child” relationship'
When a class derives from another class, The child class will inherit all the public and protected properties and methods
from parent class. Child class can have it's own properties and methods, that's why it is called 'inheritance'.

Python inheritance syntax :
                           classs ParentClass :
                             body of Parent class
                           class ChildClass(ParentClass) :
                             body of Child class

How inheritance helps in real projects ?
In real Python projects, inheritance helps you:

=> Build clean base classes
=> Avoid duplicate logic
=> Scale your project easily
=> Change behavior without breaking existing code
=> Write reusable, professional-grade code

Example you will see a lot later:

=> BaseModel → User, Product, Order
=> BaseException → Custom exceptions
=> Dataset → ImageDataset, TextDataset (ML projects)
=> Logger → FileLogger, DBLogger
"""
import os
os.system('cls')
# Example 1
class Employee : # Parent Class (Employee)
    def __init__ (self, name, salary) : # constructor
        self._name = name
        self._salary = salary
    def details(self) : # method
        print(f'{self._name} gets {self._salary} from company each month')
class Manager(Employee) : # Child Class (Manager)
    def moreDetails(self) : # method
        print(f'{self._name} is a manager and gets {self._salary} from company each month')

a1 = Employee('Shahroze', 70000)
a1.details()
a2 = Manager("Martin", 90000)
a2.moreDetails()

# Example 2 
class Worker :
    def __init__(self, name, id, department):
        self._name = name
        self._id = id
        self._department = department
    def info(self):
        print(f'The name of Employee : {self._id} is {self._name} and works in {self._department} department')

class Programmer(Worker):  
    def showLanguage(self) :
        print("Our default language will be python")

class DataScientist(Programmer) :
    def allInfo(self):
        print('We have done basics and now we are moving forward')

e1 = Worker("Rabia", 213, 'Accounts')
e1.info()
e2 = Worker("Fazil", 196, 'Marketing')
e2.info()
e3 = Worker("Huma", 309, 'Operations')
e3.info()
e4 = Worker("Suraiya", 44, 'IT')
e4.info()
# we can't apply child class methods on parent class but all methods of parent class will execute in child class 
e5 = Programmer("Bilal", 233, 'Human Resources (HR)')
e5.info()
e5.showLanguage()
# That's why showLanguage method can't apply on Worker class(Parent Class) but info and showLanguage both methods execute in
# Programmer class(Child class)

d1 = DataScientist('Rohan Das', 420, 'Data Science')
# here DataScientist class have properties and methods of both Programmer and Worker class.
d1.info()
d1.showLanguage()
d1.allInfo()

# Exercise 1: Single Inheritance (warm-up)
"""
Scenario:
A company has general employees and some of them are interns.

Requirements:

=> Create a class Employee
=> Attributes: name, salary
=> Method: show_details() → prints name and salary
=> Create a child class Intern
=> Extra attribute: duration (months)
=> Method: show_intern_details() → prints intern duration along with inherited details

Rules:

=> Do not rewrite employee logic inside Intern
=> Call parent methods where needed
=> Create at least 2 objects (1 Employee, 1 Intern)
"""
class Employee1 :
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    def show_details(self):
        print(f'{self._name} gets {self._salary} every month')

class Intern(Employee1):
    def __init__(self,name, salary, duration):
        Employee1.__init__(self, name, salary) # initializes parent attributes name and salary
        self._duration = duration

    def show_intern_details(self):
        self.show_details()
        print(f'This internee works for {self._duration}')

employee = Employee1('Pooja', 50000)
employee.show_details()
# intern1 = Intern('3.5 months')
intern1 = Intern('Ali', 20000, '3.5 months')
intern1.show_intern_details()

# Exercise 2: Multi-Level Inheritance
"""
Scenario : 

A tech company has workers, developers, and ML engineers.
Each level adds something new, but keeps what came before.

Class structure (follow this exactly)
1. Worker

Attributes:
=> name
=> department

Method:

=> basic_info()
=> Prints the worker’s name and department

2. Developer (inherits from Worker)

Extra attribute:

=> language

Method:

=> dev_info()
=> Prints the programming language
=> Also shows basic worker info

3. MLEngineer (inherits from Developer)

Extra attribute:

=> model_type

Method:

=> ml_info()
=> Prints model type
=> Also shows developer and worker info

Rules :
=> Each child class must initialize its parent properly
=> Do not duplicate code
=> Use parent methods instead of rewriting logic
=> Test with one object of each class
"""
class Old_Worker :
    def __init__(self, name, department):
        self._name = name
        self._department = department
    def basic_info(self):
        print(f'{self._name} works in {self._department} department')

class Developer(Old_Worker):
    def __init__(self, name, department, language):
        Old_Worker.__init__(self, name, department) # initializes parent attributes name and department
        self._language = language
    def dev_info(self):
        print(f'Developer working on {self._language} language')
        self.basic_info() # reuse parent method

class MLEngineer(Developer):
    def __init__(self, name, department, language, model_type):
        Developer.__init__(self, name, department, language)
        self._model_type = model_type
    def ml_info(self):
        print(f'model type : {self._model_type}')
        self.dev_info() # reuse developer method

obj1 = Old_Worker('Shumaila', 'Health Care')
obj1.basic_info()
obj2 = Developer('Shubham', 'IT', 'Python')
obj2.dev_info()
obj3 = MLEngineer('Daniel', 'IT', 'Python', 'Text to Image Generator')
obj3.ml_info()

# Exercise 3: Method Overriding & Polymorphism
"""
Scenario :

Different roles in a company calculate bonuses differently. 
You will use the same method name in parent and child classes, but return different results depending on the class.

Class structure :
1. Employee
=> Attribute: salary
Method: calculate_bonus() → returns 10% of salary

2. Manager (inherits Employee)
=> Override calculate_bonus() → returns 20% of salary

3. Developer (inherits Employee)
=> Override calculate_bonus() → returns 15% of salary

Rules :
=> Use method overriding instead of creating new method names
=> Create at least 1 object of each class and call calculate_bonus()
=> Print a clear statement showing the class and bonus amount
"""
class Old_Employee :
    def __init__(self, salary):
        self._salary = salary
    def calculate_bonus(self):
        return self._salary * 0.10
    
class Old_Manager(Old_Employee):
    def calculate_bonus(self):
        return self._salary * 0.20
    
class Old_Developer(Old_Employee):
    def calculate_bonus(self):
        return self._salary * 0.15
    
L = Old_Employee(75000)
print(f'Old Employee bonus : {L.calculate_bonus()}')

M = Old_Manager(95000)
print(f'Old Manager bonus : {M.calculate_bonus()}')

N = Old_Developer(187000)
print(f'Old Developer bonus : {N.calculate_bonus()}')
"""
Types of inheritance :

1- Single Inheritance
2- Multiple Inheritance
3- Multi-Level Inheritance
4- Hierarchical Inheritance
5- Hybrid Inheritance
"""