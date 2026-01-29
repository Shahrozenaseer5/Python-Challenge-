"""
================================================================================
Project       : Hybrid vs Hierarchical Inheritance in Python
Author        : Shahroze
Date          : 2026-01-30
Language      : Python 3.x
Purpose       : Demonstrate examples of Hierarchical and Hybrid inheritance,
                including exercises and diamond problem resolution.
                
================================================================================

Description:
------------
This script contains:
1. Explanation of Hierarchical and Hybrid Inheritance.
2. Code examples illustrating both types of inheritance.
3. Exercises for practice:
   - Hierarchical Inheritance:
     * Shape System
     * Employee Roles
   - Hybrid Inheritance:
     * Vehicle System (HybridCar example)
     * Device Access Control (SmartPhone example)
4. Demonstration of diamond problem and Method Resolution Order (MRO).

Usage:
------
Run this file directly in a Python 3 environment to see examples and outputs
for all exercises. Each section prints relevant outputs and MROs for hybrid inheritance.

Note:
-----
- Hierarchical Inheritance: One parent → multiple children (tree structure).
- Hybrid Inheritance: Combination of multiple types, often forming diamond shapes.
- Super() is used consistently to resolve method calls in hybrid inheritance.

================================================================================
"""

"""
Hybrid Vs Hierarchical Inheritance :
Hierarchical Inheritance : Hierarchical inheritance is when one parent class has multiple child classes.
it's like a tree where one base node branches into many.

Structure :
=> One parent
=> Many children
=> Children are independent of each other

Use case : Use hierarchical inheritance when different classes share common behavior but represent different specialized forms.

Hybrid Inheritance : 
                    Hybrid inheritance is a combination of two or more types of inheritance, usually involving multiple inheritance.

It mixes patterns like:
=> Single
=> Multiple
=> Hierarchical
=> Multilevel

Structure :
=> More complex
=> Can involve multiple parents
=> Often forms a diamond shape

Use case : 
Use hybrid inheritance when a class naturally belongs to multiple categories and needs behavior from all of them.

Observation : 
- Hierarchical = one → many
- Hybrid = mix of inheritance types
"""
import os
os.system('cls')
from abc import ABC, abstractmethod
# Example of Hierarchical Inheritance
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Cat(Animal):
    def meow(self):
        print("Meowing")

# Example of Hybrid Inheritance 
class Animal:
    def eat(self):
        print("Eating")

class Mammal(Animal):
    def walk(self):
        print("Walking")

class Bird(Animal):
    def fly(self):
        print("Flying")

class Bat(Mammal, Bird):
    pass

""" 1- Animal → Mammal and Bird (hierarchical)
    2- Bat inherits from both Mammal and Bird (multiple)
    => Together, this forms hybrid inheritance
"""

"""
Hierarchical Inheritance (2 Exercises)
Exercise 1: Shape System
=> Create a base class Shape with a method area().
=> Create two child classes:
=> Rectangle
=> Circle
=> Each child should implement its own version of area().

Goal: Practice one parent, multiple children.
"""
class Shape :
    def area(self) :
        raise NotImplementedError("Subclasses must implement area()") # This prevents accidental misuse of Shape.
        

class Rectangle(Shape) :
    def __init__(self, length, width) :
        self.length = length
        self.width = width
    def area(self) :
        return self.length * self.width
    
class Circle(Shape) :
    def __init__(self, r) :
        self.r = r
    def area(self) :
        return 3.14 * (self.r * self.r)
    
r = Rectangle(10, 12)
print(r.area()) # Rectangle area

c = Circle(22)
print(c.area()) # Circle area

"""
Exercise 2: Employee Roles
=> Create a base class Employee with common attributes like name and salary.
=> Create child classes:
=> Manager
=> Developer
=> Intern
=> Each child class should have a method get_role_details().

Goal: Model different roles sharing common employee data.
"""
class Employee(ABC) :
    def __init__(self, name, salary) :
        self.name = name
        self.salary = salary

    @abstractmethod
    def get_role_details(self) :
        pass

class Manager(Employee) :
    def __init__(self, name, salary, role) :
        super().__init__(name, salary)
        self.role = role

    def get_role_details(self) :
        print(f'Name : {self.name}')
        print(f'Salary : {self.salary}')
        print(f'Role : {self.role}')

class Developer(Employee) :
    def __init__(self, name, salary, role) :
        super().__init__(name, salary)
        self.role = role

    def get_role_details(self) :
        print(f'Name : {self.name}')
        print(f'Salary : {self.salary}')
        print(f'Role : {self.role}')

class Intern(Employee) :
    def __init__(self, name, salary, role) :
        super().__init__(name, salary)
        self.role = role

    def get_role_details(self) :
        print(f'Name : {self.name}')
        print(f'Salary : {self.salary}')
        print(f'Role : {self.role}')

m = Manager('Rohan Das', 80000, 'Manager')
m.get_role_details()

d = Developer('Jackson', 70000, 'Developer')
d.get_role_details()

i = Intern('Khurram', 25000, 'Internee')
i.get_role_details()

"""
Hybrid Inheritance (2 Exercises)
Exercise 3: Vehicle System
=> Create a base class Vehicle with a method start().
=> Create two classes:
=> ElectricVehicle (inherits from Vehicle)
=> FuelVehicle (inherits from Vehicle)
=> Create a class HybridCar that inherits from both ElectricVehicle and FuelVehicle.

Goal: Combine behaviors from multiple parents.
"""
class Vehicle:
    def power_on(self):
        print("Vehicle starting...")

class ElectricVehicle(Vehicle):
    def power_on(self):
        print("Electric part powering on")
        super().power_on()

class FuelVehicle(Vehicle):
    def power_on(self):
        print("Fuel part powering on")
        super().power_on()

class HybridCar(ElectricVehicle, FuelVehicle):
    def power_on(self):
        print("Hybrid car powering on")
        super().power_on()

h = HybridCar()
h.power_on()
print(HybridCar.mro())

"""
=> HybridCar.power_on() → calls super().power_on() → goes to ElectricVehicle.power_on()
=>ElectricVehicle.power_on() → calls super().power_on() → goes to FuelVehicle.power_on()
=> FuelVehicle.power_on() → calls super().power_on() → goes to Vehicle.power_on()
=> Vehicle.power_on() → prints “Vehicle starting…”

This respects the diamond MRO perfectly, so all intermediate classes run in order.
"""

"""
Exercise 4: Device Access Control
=> Create a base class Device with a method power_on().
=> Create two child classes:
=> Camera
=> Microphone
=> Create a class SmartPhone that inherits from both Camera and Microphone.

Goal: Practice diamond-style hybrid inheritance.
"""
class Device : 
    def power_on(self) :
        print('Device is starting ..')

class Camera(Device) :
    def power_on(self) :
        print('Camera is ready to click ..')
        super().power_on()

class Microphone(Device) :
    def power_on(self) :
        print('Microphone is ready to hear ..')
        super().power_on()

class SmartPhone(Microphone, Camera) :
    def power_on(self) :
        print('Microphone and Camera enabled ..')
        super().power_on()

s = SmartPhone()
s.power_on()
print(SmartPhone.mro())

"""
How it works (MRO explained) :
=> SmartPhone.power_on() → calls super().power_on() → goes to Microphone.power_on() (because Microphone is first in the definition)
=> Microphone.power_on() → calls super().power_on() → goes to Camera.power_on()
=> Camera.power_on() → calls super().power_on() → goes to Device.power_on()`
=> Device.power_on() → prints “Device is starting ..”

✅ All classes execute once, respecting the diamond MRO.
"""

"""
Conclusion :
=> The order of parent classes in the class definition affects MRO in Python.
=> Using super() in all classes consistently allows Python to resolve the diamond safely.
=> This is the canonical way to implement hybrid inheritance in Python.
"""