"""
Topic: Super Keyword in Python (Inheritance & MRO)

Author: Shahroze
Description:
This file demonstrates the use of the 'super()' keyword in Python.

Key concepts covered:
- Calling parent class methods using 'super()'
- Using 'super()' inside constructors (__init__)
- Method overriding vs method extension
- Single inheritance examples
- Multiple inheritance and Method Resolution Order (MRO)
- How 'super()' follows MRO to safely call the next method

Notes:
- 'super()' does not extract or duplicate parent methods.
- It allows a child class to cooperate with its parent class behavior.
- In multiple inheritance, 'super()' follows MRO to avoid method conflicts.

This file also includes hands-on exercises to reinforce understanding.
"""

"""
Super Keyword :  
               Super keyword is used to access the parent class. super() is useful in single and multiple inheritance, 
               and in multiple inheritance it follows MRO (Method Resolution Order) to safely call the next method.
               When a method is called, Python follows a fixed path to decide which class’s method runs first.
               "MRO defines the path, super() follows it".
               When a class inherits from a parent class, it can override or extend the methods defined in
               the parent class. Sometimes we want to use parent class methods in child class. In this case,
               "super" keyword is used. 
               super() calls parent behavior, it doesn’t take it out or duplicate it.
               super() lets a child class call methods of its parent class.
"""
import os
os.system('cls')
# super example
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()   # call parent's method
        print("Hello from Child")

Child().greet()

# we can call constructer of parent class using 'super'
class Boy :
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Adult(Boy) :
    def __init__(self, name, age, hobby):
        super().__init__(name, age) # call Parent constructor
        self.hobby = hobby

ad = Adult('Rohan Das', 30, "Chess")
print(ad.name)
print(ad.age)
print(ad.hobby)

# calling parent class method using 'super'
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        super().speak() # call speak method from parent class(Animal)
        print("Dog barks")

a1 = Dog()
a1.speak()

# 'super' example
class ParentClass :
    def parent_method(self):
        print('This is the parent method1')

class ChildClass(ParentClass):
    def parent_method(self):
        print('Hamid2')

    def child_method(self):
        print('This is the child method2')
        super().parent_method() # calls 'parent_method' of ParentClass 

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()

# another example of 'super'
class Employee :
    def __init__(self, name, id):
        self.name = name
        self.id = id
class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

Shami = Employee('Amna', 432)
Shahroze = Programmer('Sheri', 536, 'Python')

print(Shami.name)
print(Shami.id)

print(Shahroze.name)
print(Shahroze.lang)
print(Shahroze.id)

"""
Exercise 1: Extend parent behavior (basic)

Goal: Understand how super() adds to parent logic.

Task:

=> Create a class Vehicle with a method start() that prints
"Vehicle is starting".
=> Create a class Car that inherits from Vehicle.
=> Override start() in Car so that it:
=> Calls the parent start() using super()
=> Then prints "Car is ready to drive"
=> Create an object of Car and call start().

Think about:
What happens if you remove super()?
"""

class Vehicle :
    def start(self):
        print('Vehicle is starting')

class Car(Vehicle):
    def start(self):
        super().start()
        print('Car is ready to drive')

car1 = Car()
car1.start()

"""
Exercise 2: Parent constructor + child constructor

Goal: Understand why super() is used in __init__.

Task:

=> Create a class Person with name and age.
=> Create a class Employee that inherits from Person and adds salary.
=> Use super() to initialize name and age.
=> Print all attributes from an Employee object.

Think about:
What error do you get if you don’t call super().__init__()?
"""
class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

Emp1 = Employee('John', 43, 78645)
print(Emp1.name)
print(Emp1.age)
print(Emp1.salary)

"""
Exercise 3: Multiple inheritance + MRO (core concept)

Goal: Understand how super() follows MRO.

Task:

=> Create class A with method show() printing "A".
=> Create class B(A) and class C(A):
=> Each overrides show()
=> Each calls super().show() and prints its own name
=> Create class D(B, C):
=> Override show()
=> Call super().show() and print "D"
=> Call show() on D and print D.mro().

Think about:
Why does the output order look “reversed”?
"""
class A :
    def show(self):
        print('A')

class B(A):
    def show(self):
        super().show()
        print('B')

class C(A):
    def show(self):
        super().show()
        print('C')

class D(B, C):
    def show(self):
        super().show()
        print('D')

D().show()
print(D.mro())