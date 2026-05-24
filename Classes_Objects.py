"""
File: Classes_Objects.py
Author: Shahroze
Description:
    Demonstration of Python classes and objects.
    Shows how to define class attributes, instance methods,
    create multiple objects, and override default attributes.
    Includes an explanation of the self parameter and how
    methods access the current instance.
"""

# Classes and Objects in Python
"""
Class is a blueprint or template for creating objects. Providing initial values for state (member variables or attributes),
and implementations of behavior (member functions or methods). User defined objects are created using 'class' keyword.
We can think class as a placeholder
"""
import os 
os.system('cls')
# Creating a class :
# We can create class using "class" keyword
class details :
    name = 'Akriti'
    age = 28
# Creating method inside class :
    def desc(self) :
      print(f"My name is {self.name} and my age is {self.age}")

# We have creared 2 properties and 1 method here.

# Creating an object : 
# Object is the instance of the class used to access the properties of the class. Now lets create an object of the class.
obj_1 = details() 
# print(obj_1.name) # Akriti will be printed
obj_1.desc()
# person class
class person :
    name = 'Amna'
    age = 33
    occupation = 'Singer'
    Car = 'Lamborgini'
    Networth = 22200000
# 5 properties are added
    def info(self) : # Method
      print(f"{self.name} is a {self.occupation}")
""" Self parameter is a reference to the current instance of the class and is used to access variables that belongs to the class.
It must be provided as the extra parameter inside the method definition.

Self ka matlab wo object jis k liye ye method call kiya ja raha hy
"""
# 1 method
# So here we use 5 properties and 1 method(info). We may have 10 properties and 50 methods dapending upon the scenario.
# All methods remain inside the class.

# Creating object 'a' :
a = person()
b = person()
c = person()
# We can make many objects and methods as we needed using the same class.
# We can change name by writing a.name = "Zulqarnain". We can change any attribute in class for every single object.
a.name = "Zulqarnain"
a.occupation = "CEO"

b.name = "Nabeel"
b.occupation = "Chef in Canada"
# print(a.name, '=>',a.occupation)
# if we doesn't change anything, default info will be printed.
a.info()
b.info()
c.info() # Here we get default values of class 'Person' because we haven't change anything in c.