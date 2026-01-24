"""
===========================================================================
Author       : Shahroze
Date         : 24-Jan-2026
Description  : Demonstration of Single Inheritance in Python

This script illustrates:
1. Single inheritance using the Animal class as a parent class.
2. Implementation of a Dog class inheriting from Animal, with method overriding.
3. A quick quiz implementation of a Cat class inheriting from Animal,
   with additional methods specific to the Cat class.

Note:
- The second 'animal' class (lowercase) is created solely for experiment/quiz
  purposes, to demonstrate subclassing and method overriding without modifying
  the first Animal class. In practice, only one properly named base class
  should be used.

===========================================================================
"""


""" Single Inheritance : In single inheritance, child class simply get the prpperties and methods of parent class by
                         writing the parent class inside the small brackets like Employee(Company).
"""
import os
os.system('cls')
class Animal :
    def __init__(self, name, species) :
        self.name = name 
        self.species = species

    def make_sound(self) :
        print('Sound made by the animal')

class Dog(Animal) :
    def __init__(self, name, breed) :
        Animal.__init__(self, name, species = "Dog")
        self.breed = breed

    def make_sound(self) :
        print('Bow Bow !!')

A1 = Animal('Zibbi', 'Grevy’s Zebra')
A1.make_sound()

D1 = Dog('Blizzard', 'Siberian Husky')
D1.make_sound()

"""
Quick Quiz : Implement a cat class by using the animal class. Add some methods specific to cat class.
"""

class animal :
    def __init__(self, name, age, color) :
        self.name = name
        self.age = age
        self.color = color

    def sleep_hours(self) : 
        print('Default sleeping time of animals: 4–20 hours per day, depending on species.')

    def eat(self) :
        print('Diet differ according to the animal species')

    def make_sound(self) :
        print('Animal\'s sound ...')

class Cat(animal) :
    def __init__(self, name, food) :
        animal.__init__(self, name, '1.5 years', 'Brownish Black')
        self.food = food

    def make_sound(self):
        print('Meow Meow ..')

    def sleep_hours(self) :
        print('8 hours a day')

    def eat(self) :
        print('Cat food. 3 times a day')

a1 = animal('Nini', '6 months', 'brown')
a1.sleep_hours()
a1.eat()
a1.make_sound()

c1 = Cat('Luna', 'Cat Food')
c1.sleep_hours()
c1.eat()
c1.make_sound()