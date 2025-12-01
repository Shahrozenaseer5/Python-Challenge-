"""
File: constructors.py
Author: Shahroze
Description: Demonstration of Python constructors (default and parameterized),
object creation, and basic class usage. Prepared for GitHub upload.
"""
# Constructors
import os
os.system('cls')
"""
Constructor : A constructor is a special method in class used to craete and initialize an object of a class.
There are different kinds of constructor. Constructor is invoked automatically when an object of a class is created.

A constructor is a unique function that gets called automatically when an object is created of a class.
The main purpose of a constructor is to initialize or assign values to the data members of the class. 
It cannot return any value other than 'None'.

Syntax : def __init__ (self) :
         (initialization)

init is one of the reversed functions in python. In OOP, it is known as 'constructor'.
We can also create constructor by defining the function name with same class name.

Syntax :
        class ABC :
           def ABC(self) :
         (initialization)  

There are 2 types of constructors :
1- Default constructors
2- Parameterized constructors

Parameterized constructors :
                            When constructor accepts arguments along with self, it is known as Parameterized constructors.
                            These arguments can be used inside the class to assign values to the data members.

                            class details :
                               def __init__(self, animal, group)
                                 self.animal = animal
                                 self.group = group

                            obj_1 = details('Crab', 'Crustaceans')
                            print(obj_1.animal, 'belongs to the', obj_1.group, 'group.')

Default constructors : 
                      When constructor doesn't accept any arguments from object and
                      has only 1 argument, "self" in the constructor, it is known as Default constructor.

                      class details :
                         def __init__(self) :
                            print('Animal Crab belongs to Crustaceans group.')
                      obj1.details()
"""
# Creating class person
class person :
    # def __init__(self) :  it is known as 'Default constructor'
    #   print("Hi ! I am inside constructor") 
      
    def __init__(self, name, occ) : # Parameterized constructor
       print("Hi ! I am inside constructor")
       self.name = name
       self.occ = occ

# We define a method
    def info(self) :
     print(f"{self.name} is a {self.occ}.")

# We will create an object
a = person('Ahsan', 'Engineer')
b = person('Maria', 'Fashion Designer')
# c = person(1,2,3) 
# Error : person.__init__() takes 3 positional arguments but 4 were given because self is automatically passes c as first parameter

a.info() # it takes Ahsan as name and Engineer as occ
b.info() # it takes Maria as name and Fashion Designer as occ

# So whenever we create an object, constructor will automatically called.

