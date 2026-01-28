"""
File Name   : multiple_inheritance.py
Author      : Shahroze
Description :
    This file demonstrates the concept of Multiple Inheritance in Python.
    It covers how a single class can inherit from multiple parent classes
    and how Python resolves method and attribute conflicts using
    Method Resolution Order (MRO).

Concepts Covered :
    - Multiple Inheritance syntax and usage
    - Method overriding in parent and child classes
    - Method Resolution Order (MRO)
    - How Python selects methods when names clash
    - Proper and improper use of super()
    - Real-world design examples using multiple inheritance

Purpose :
    This file is created for learning, practice, and portfolio demonstration.
    The examples progress from basic inheritance to real-world scenarios
    to build a clear and practical understanding of the topic.

Note :
    MRO always follows the class order defined during inheritance.
    Child class methods override parent class methods if present.

"""

"""
Multiple Inheritance :
                      We can make a single class inheriting 2 or more classes is called " multiple inheritance ".

Syntax : 
        class ChildClass(Parent1, Parent2, Parent3) :
        class body
"""
import os
os.system('cls')
class Employee :
    def __init__(self, name) :
        self.name = name

    def show(self) :
        print(f"Name is {self.name}")

class Dancer :
    def __init__(self, dance) :
        self.dance = dance

    def show(self) :
        print(f"Dance is {self.dance}")

class DancerEmployee (Employee, Dancer) :
    def __init__(self, name , dance) :
        self.dance = dance
        self.name = name

o = DancerEmployee('Rasmesh', 'Hip Hop')
print(o.name)
print(o.dance)
o.show() # If 2 methods are same in 2 parent classes, then The method of the class that is defined first will execute first.
"""
MRO is the order in which Python looks for a method or attribute when you call it on an object, especially when multiple inheritance is involved.

In simple words:

MRO tells Python which class’s method to run first when more than one class has the same method name.
"""
print(DancerEmployee.mro())

# Example 2
class Animal :
    def __init__(self, name, species) :
        self.name = name
        self.species = species

    def make_sound(self) :
        print('Sound made by the animal')
class Mamal :
    def __init__(self, name, fur_color) :
        self.name = name
        self.fur_color = fur_color

class Dog(Animal, Mamal) :
    def __init__(self, name, breed, fur_color) :
        Animal.__init__(self, name, species = 'Dog')
        Mamal.__init__(self, name, fur_color)
        self.breed = breed

    def make_sound(self) :
        print('Baw Baw !')

a = Dog('Tommy', 'Golden Retriever', 'Cream')
a.make_sound()
print(a.name)
print(a.fur_color)
print(a.breed)
print(Dog.mro())

"""
Exercise 1: Method Resolution Order in Action

Goal: Understand how Python decides which method runs.

Task:
=> Create three classes:
=> A with a method show()
=> B inheriting from A and overriding show()
=> C inheriting from A and overriding show()
=> Create a class D that inherits from both B and C
=> Call show() using an object of D
=> Print the MRO of class D

Observation :
=> Which class method runs
=> How the order in D(B, C) affects execution
"""
class A :
    def show(self) :
        print('I am A class')

class B (A) :
    def show(self) :
        print('I am B class')

class C (A) :
    def show(self) :
        print('I am C class')

class D (B, C) :
    pass

d = D()
d.show()
print(D.mro()) # mro works with class not object

"""
Exercise 2: Using super() with Multiple Inheritance

Goal: Learn how super() works with MRO.

Task:
Create classes:
=> A with a method process()
=> B(A) that uses super().process()
=> C(A) that also uses super().process()
=> D(B, C) that calls process()
=> Each class should print its class name inside process()

Observation :
=> All methods run once
=> The order follows MRO, not parent order logic
=> Why super() is powerful and safe
"""
class A :
    def process(self) :
        print('Process of A')

class B (A) :
    def process(self) :
        super().process()

class C (A) :
    def process(self) :
        super().process()

class D (B, C) :
    def process(self) :
        print('process of D')

b = B()
b.process()

c = C()
c.process()

d1 = D()
d1.process()
print(D.mro())

"""
Exercise 3: Real-World Style Design

Goal: Apply multiple inheritance logically, not just syntactically.

Scenario:
You are designing a system for devices.

Task:

Create:
=> PowerDevice class with power_on()
=> NetworkDevice class with connect()
=> SmartDevice class inheriting from both
=> Add a method in SmartDevice that uses both parent methods
=> Add at least one overlapping method name in both parents and resolve it cleanly

Observation :
=> When multiple inheritance makes sense
=> How to avoid confusion
=> How to design clean class hierarchies
"""
class PowerDevice :
    def power_on(self) :
        print('Power On ... ')

    def internet(self) :
        print('Wifi 📶')

class NetworkDevice :
    def connect(self) :
        print('Connected')

    def internet(self) :
        print('Hotspot 🌐')

class SmartDevice(PowerDevice, NetworkDevice) :
    def start(self) :
        super().power_on() # super only works inside a method
        super().connect()

    def internet(self):
        print("Smart internet enabled 📶🌐")

p1 = PowerDevice()
p1.internet()
p1.power_on()

p2 = NetworkDevice()
p2.connect()
p2.internet()

p3 = SmartDevice()
p3.connect()
p3.internet() # SmartDevice (method found here, parents not checked)
p3.power_on()
print(SmartDevice.mro())
