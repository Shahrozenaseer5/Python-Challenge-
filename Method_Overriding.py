"""
===============================================================================
Project       : Python OOP Exercises – Method Overriding
File Name     : Method_Overriding.py
Author        : Shahroze
Date Created  : 2026-01-13
Python Version: 3.x
Purpose       : 
    This file contains multiple exercises demonstrating the concept of 
    method overriding in Python. It includes:
        1. Shape and Circle area calculation
        2. Square perimeter overriding
        3. Animal sound overriding
        4. BankAccount and SpecialAccount interest calculation
        5. Employee and Manager bonus calculation with super()
        6. Customer and PremiumCustomer discount calculation with super()
        7. Vehicle and SportsCar max speed calculation with super()
    
    Each exercise shows how a child class can override parent methods 
    and optionally use the parent method via 'super()'.
===============================================================================
"""

"""  
Method Overriding :
                   "When a child class defines a method with the same name as a method in its parent class,
                    it can customize the behavior while optionally using the parent’s method. This process is called method overriding."
                    In this scenario, we can use same name of method in child class but we can customize it according to our needs.
"""
import os
os.system('cls')
class Shape :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        # return 3.14 * self.radius * self.radius # because circle area = πr2
        return 3.14 * super().area()
rec = Shape(44,53)
print(rec.area()) # area of rectangle

Gol = Circle(12)
print(Gol.area())

"""
Exercise 1: Square Class

=> Create a Shape class with a method perimeter() that calculates perimeter as 2*(x+y).
=> Create a Square class that inherits Shape and overrides perimeter() to calculate 4*side.
=> Test it with a square of side 10.
"""
class Shape1 :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def perimeter(self):
        return 2 * (self.x + self.y)
    
class Square(Shape1):
    def __init__(self, side):
        super().__init__(side, side)  # optional if you want to store x and y too
        self.side = side
    def perimeter(self):
        return 4 * self.side
    
s1 = Square(10)
print(s1.perimeter())

"""
Exercise 2: Animal Sounds

=> Create a class Animal with a method sound() that prints "Some generic sound".
=> Create two subclasses Dog and Cat that override sound() to print "Woof" and "Meow" respectively.
=> Create objects of each and call sound()
"""
class Animal :
    def sound(self) :
        return f"Some generic sound"
    
class Dog(Animal) : 
       def sound(self) :
        return f"Woof Woof"
       
class Cat(Animal) : 
       def sound(self) :
        return f"Meow Meow"
       
Janvar = Animal()
print(Janvar.sound())
Kutta = Dog()
print(Kutta.sound())
Billi = Cat()
print(Billi.sound())

"""
Exercise 3: Bank Interest

=> Create a class BankAccount with a method interest() that returns balance * 0.05 (5%).
=> Create a subclass SpecialAccount that overrides interest() to return balance * 0.08 (8%).
=> Test both classes with balance = 1000.
"""
class BankAccount :
    def __init__(self, balance):
        self.balance = balance

    def interest(self):
        return self.balance * 0.05 # 5%
    
class SpecialAccount(BankAccount) :
    def interest(self):
        return self.balance * 0.08 # 8%
    
SimpleAccount = BankAccount(1000)
print(SimpleAccount.interest()) # 5% interest for normal account

Special = SpecialAccount(1000)
print(Special.interest()) # 8% interest for special account

"""
Exercise: Employee Bonus

Create a class Employee with:
=> __init__(self, name, salary)
=> bonus() method that returns 10% of salary.
=> Create a subclass Manager that:
=> Overrides bonus()
=> Uses the parent’s bonus() (super) and adds an extra 5% bonus.

Test it with:
=> Regular employee with salary 1000
=> Manager with salary 2000
"""
class Employee :
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def bonus(self):
        return self.salary * 0.10
    
class Manager(Employee) :
    def bonus(self) :
        return super().bonus() + self.salary * 0.05 # 5% extra bonus
    
regular = Employee("Rohan Das", 1000)    
print(f"Bonus of regular Employee is : ",regular.bonus())

manager = Manager("Naseer", 2000)    
print(f"Bonus of Manager is : ", manager.bonus())

"""
Exercise : Online Store Discounts

=> Create a class Customer with:
=> __init__(self, name, purchase_amount)
=> discount() method that gives 5% discount on purchase_amount.

Create a subclass PremiumCustomer that:
=> Overrides discount()
=> Uses super() to get the base 5% discount and adds an extra 5% discount.

Test with:
=> Customer buying 1000 units
=> PremiumCustomer buying 1000 units
"""
class Customer :
    def __init__(self, name, purchase_amount) :
        self.name = name
        self.purchase_amount = purchase_amount

    def discount(self) :
        return self.purchase_amount * 0.05
    
class PremiumCustomer(Customer) :
    def discount(self) :
        return super().discount() + self.purchase_amount * 0.05
    
customer = Customer('Peter', 1000)
print(f"Regular customer will get discount of rupees : ", customer.discount())

premium = PremiumCustomer('Bill Gates', 1000)
print(f"Premium customers will get discount of rupees : ", premium.discount())

"""
Exercise : Vehicle Speed

Create a class Vehicle with:
=> __init__(self, speed)
=> max_speed() method returning the speed

Create a subclass SportsCar that:
=> Overrides max_speed()
=> Uses super() and adds 50 km/h extra to the parent speed

Test with:
=> Vehicle with speed 120 km/h
=> SportsCar with speed 120 km/h
"""
class Vehicle :
    def __init__(self, speed) :
        self.speed = speed 

    def max_speed(self) :
        return self.speed
    
class SportsCar(Vehicle) :
    def max_speed(self) :
        return super().max_speed() + 50 # add 50 km/h extra speed 
    
vehicle = Vehicle(120)
print(f"Regular vehicle max speed will be : ", vehicle.max_speed(), "km/h")

sports = SportsCar(120)
print(f"Sports Car max speed will be : ", sports.max_speed(), "km/h")