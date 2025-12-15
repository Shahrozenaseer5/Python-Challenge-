"""
===============================================================================
Project: Getters and Setters Examples in Python
Author : Shahroze
Date   : 2025-12-16
Purpose: 
    This Python file demonstrates the concept of getters and setters using
    four practical examples. It shows how to encapsulate internal data 
    while allowing controlled access and updates.

    1. Person / MyClass Example - Basic getter and setter
    2. Temperature Converter - Celsius to Fahrenheit conversion
    3. BankAccount - Balance validation with setter
    4. Rectangle - Area property with indirect update of width
    5. Employee - Salary and tax calculation with reverse logic

Concepts Covered:
    - @property decorator
    - Getter methods to read data safely
    - Setter methods to update data with validation or transformation
    - Encapsulation and controlled access to class attributes
===============================================================================
"""

# Getters and Setters
"""
Getters : 
         A Getter is a small method that lets you safely read the value of a variable inside a class.
=> A getter is a function that returns the value of an attribute, but with control.
 Instead of allowing direct access, you pass the value through a method.
=> A getter is a controlled way to read a variable so you can protect it and apply extra logic before giving its value.
=> Getters in python are methods that are used to access the values of an object's properties. 
They are used to return value of a specific property and are typically defined using @property decorator.

Setters :
         It is important to note that the getters do not take any parameters and we can't set the values using getter method.
         For this purpose, we need setter method which can be added by decorating method with :
                           @property_name.setter
""" 
import os
os.system('cls')
class person :
    def __init__(self, age) :
        self._age = age  # constructor sets the value
    
    @property 
    def age(self):
        return self._age # getter reads the value
    
p = person(30) # p is an object
print(p.age)
# Example 
class MyClass :
    def __init__(self, value) : # it's a constructor
        self._value = value
    
    def show(self):
        print(f"Value is {self._value}") # it's a method
    @property
    def ten_value(self):
        return 10 * self._value # now it became a getter
    
    @ten_value.setter 
    def ten_value (self, new_value) : # it's a setter
        self._value = new_value / 10
    
obj = MyClass(20)
obj.ten_value = 76
print(obj.ten_value)
obj.show()

# Exercise 1: Temperature Converter (easy)
"""
Create a class Temperature.

Requirements:

=> Constructor takes temperature in Celsius and stores it internally.
=> Create a getter fahrenheit that returns the temperature in Fahrenheit.
=> Create a setter fahrenheit that updates the Celsius value when Fahrenheit is assigned.

Hint for formula (no code):

Fahrenheit = (C × 9/5) + 32
"""
class Temperature :
  def __init__(self, celsius) :
      self._celsius = celsius

  @property
  def fahrenheit(self) :
  # getter converts celsius to fahrenheit    
      return (self._celsius * 9/5) + 32
  
  @fahrenheit.setter
  # setter converts fahrenheit back to celsius
  def fahrenheit(self, f):
     self._celsius = (f-32) * 5/9

body_temperature = Temperature(22)
# Constructor runs → _celsius = 22

print(body_temperature._celsius)     # internal value
print(body_temperature.fahrenheit)   # calls getter
# Getter runs → converts 22°C → 71.6°F

body_temperature.fahrenheit = 98.6   # calls setter
# Setter runs → converts 98.6°F → 37°C (approx)
print(body_temperature._celsius)     # updated celsius
# Internal value updated correctly

# Exercise 2: Bank Account (validation with setter)
"""
Create a class BankAccount.

Requirements :
=> Constructor takes balance
=> Store balance internally as _balance
=> Getter balance
=> Returns current balance
=> Setter balance
=> If new balance is negative, do not update it
 Print a message like: "Balance cannot be negative"
=> If valid, update _balance
Test cases to try

=> Create account with 10,000
=> Print balance
=> Try setting balance to -500
=> Set balance to 15,000 and print again
"""
class BankAccount :
    def __init__(self, balance):
        self._balance = balance
    @property 
    def balance(self) : # getter
        return self._balance
    @balance.setter 
    def balance(self, new_balance) :
        if new_balance < 0 :
            print('Balance cannot be negative')
        else : 
            self._balance = new_balance
            print(f"You have balance of {new_balance}, Go ahead !")

# Test cases :
a = BankAccount(10000)
print(a.balance)
a.balance = -500
a.balance = 15000
print(a.balance)

# Exercise 3: Rectangle (area as a property)
"""
Create a class Rectangle.

Requirements :

=> Constructor takes width and height
=> Store them as _width and _height
=> Getter area 
=> Returns width × height
=> Setter area

=> When area is assigned, update only width
=> Height must remain unchanged
=> Assume height is never zero

Test cases to try :
=> Rectangle(10, 5)
=> Print area
=> Set area to 200
=> Print width and area again
"""
class Rectangle :
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        area = self._width * self._height
        return area
    @area.setter
    def area(self, new_area) :
        # update width only, height remains unchanged
        self._width = new_area / self._height

b = Rectangle(10, 5)
print(b.area)
b.area = 200
print(b._width)      # 40.0
print(b._height)     # 5
print(f'Area of rectangle is {b.area} and width is {b._width}')

# Exercise 4: Employee Salary (getter + setter with business logic)
"""
Goal :
=> Practice two-way logic using a property:
=> Getter calculates a derived value
=> Setter reverses that logic and updates internal state

Requirements : 
=> Create a class Employee.
=> Constructor
   Takes basic_salary
=> Store it internally as _basic_salary
=> Getter: net_salary
=> If _basic_salary ≤ 100000 → deduct 10% tax
=> If _basic_salary > 100000 → deduct 20% tax
=> Return the net salary
=> Setter: net_salary

When net salary is assigned:
=> Recalculate and store the correct basic salary
=> Reverse the tax logic properly
"""
class Employee :
    def __init__(self, basic_salary):
        self._basic_salary = basic_salary
    
    @property
    def net_salary(self) :
        if self._basic_salary < 100000 or self._basic_salary == 100000 :
            # tex amount = salary * 0.10 (0.9 is representing 10% deduction)
            return self._basic_salary * 0.9
        elif self._basic_salary > 100000 :
            return self._basic_salary * 0.8 # (0.8 is representing 10% deduction)
    
    @net_salary.setter
    def net_salary(self, new_net_salary):
           # reverse calculation to find basic salary
           if new_net_salary <= 90000:          # corresponds to <=100k basic
            self._basic_salary = new_net_salary / 0.9
           else:
            self._basic_salary = new_net_salary / 0.8

# Test cases
Shahroze = Employee(90000)
print(f'Salary of Shahroze after tax will be : {Shahroze.net_salary}')

Hira = Employee(135000)
print(f'Salary of Hira after tax will be : {Hira.net_salary}')

Alexa = Employee(254000)
print(f'Salary of Alexa after tax will be : {Alexa.net_salary}')

John = Employee(495000)
print(f'Salary of John after tax will be : {John.net_salary}')