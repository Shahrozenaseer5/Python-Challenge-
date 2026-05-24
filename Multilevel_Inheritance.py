"""
File Name   : multilevel_inheritance.py
Author      : Shahroze
Description :
    This file demonstrates the concept of Multilevel Inheritance in Python.
    Multilevel inheritance occurs when a class is derived from a child class,
    which itself inherits from another parent class. This creates a hierarchical
    chain of inheritance, allowing the most derived class to access attributes 
    and methods from all its ancestor classes.

Contents :
    - Hierarchical class examples (Animal → Dog → GoldenRetriever)
    - Constructor chaining with super() and direct parent calls
    - Method overriding in multilevel inheritance
    - Exercises demonstrating:
        1. Basic method inheritance (Person → Employee → Manager)
        2. Method overriding (Vehicle → Car → ElectricCar)
        3. Using super() in multilevel constructors (Animal1 → Mammal → Dog1)

Purpose :
    This file is intended for learning, practice, and portfolio demonstration.
    It highlights how Python resolves method and constructor calls in a 
    multilevel inheritance hierarchy and demonstrates professional coding patterns.

Key Concepts :
    - Accessing parent and grandparent class methods
    - Constructor chaining using __init__ and super()
    - Method Resolution Order (MRO) in multilevel inheritance
    - Method overriding and how child methods can extend or modify behavior

"""

"""
Multilevel Inheritance:
                       In Python, multilevel inheritance occurs when a class is derived from a child class,
                       which itself inherits from another parent class. This creates a hierarchical chain of inheritance,
                       allowing the most derived class to access attributes and methods from all its ancestor classes.

Syntax : 
        class BaseClass :
        (BaseClass code)
        class DerivedClass1(BaseClass) :
        (First-level derived class code)
        (DerivedClass1 code)
        class DerivedClass2(DerivedClass1) :
        (Second-level derived class code)
        (DerivedClass2 code)
"""
import os 
os.system('cls')
class Animal :
    def __init__(self, name, species) :
        self.name = name
        self.species = species

    def show_details(self) :
        print(f'Name : {self.name}')
        print(f'Species : {self.species}')

class Dog(Animal) :
    def __init__(self, name, breed) :
        Animal.__init__(self, name, species = 'Dog')
        self.breed = breed

    def show_details(self) :
        Animal.show_details(self) 
        print(f'Breed : {self.breed}')

class GoldenRetriever(Dog) :
    def __init__(self, name, color) :
        Dog.__init__(self, name, breed = 'GoldenRetriever')  
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(f'Color : {self.color}')

o = GoldenRetriever('Jack', 'Brown')
o.show_details()

print("Dog Class (Inherited from Animal class) :")
d = Dog('Tommy', 'German Sheferd')
d.show_details()

print("Animal Class (Parent class) :")
a = Animal('Bill', 'Siberian Husky')
a.show_details()

"""
Note : 
      When we call show_details of animal class, it will only show 2 things : name and species because in Animal class,
      show_details only have 2 things to print (name and species).
      But when call show_details of Dog class, it prints 3 things : name, species and breed because when we call show_details in
      Dog class, firstly it goes straight to the animal class's show_detail method and print : name and species. Then it come 
      back and print breed. That's why it prints name, species and breed.
      In case of GoldenRetriever class, it goes to show_details of Dog class. When it comes in Dog class, it will move directly in Animal 
      class's show_detail method and print name and species. Then come back in Dog class show_details method and print : breed. Lastly it 
      print it's own show_details method and print : color. So finally we saw 4 things in GoldenRetriever's show_details, which
      are : name, species, breed and color.
"""

"""
Exercise 1: Basic Method Inheritance

Goal: Understand simple multilevel inheritance.

Task:
=> Create three classes:
=> Person with attribute name and method show_name()
=> Employee(Person) with attribute salary and method show_salary()
=> Manager(Employee) with attribute department and method show_department()
=> Create a Manager object and call all three methods.

Observation :

The derived class can access methods from all ancestor classes.
"""
class Person :
    def __init__(self, name) :
        self.name = name

    def show_name(self) :
        print (f'Name : {self.name}')

class Employee(Person) :
    def __init__(self, name, salary) :
        Person.__init__(self, name)
        self.salary = salary

    def show_salary(self) :
        print (f'Salary : {self.salary}')

class Manager(Employee) :
    def __init__(self, name, salary, department) :
        Employee.__init__(self, name, salary)
        self.department = department

    def show_department(self) :
        print(f'Department : {self.department}')

m = Manager('Amana', 400000 , 'Accounts')
m.show_name()
m.show_salary()
m.show_department()

"""
Exercise 2: Method Overriding in Multilevel Inheritance

Goal: Learn how method overriding works.

Task:
=> Create three classes:
=> Vehicle with method move() printing "Vehicle is moving"
=> Car(Vehicle) overriding move() to print "Car is moving"
=> ElectricCar(Car) overriding move() to print "Electric Car is moving silently"
=> Create an ElectricCar object and call move().

Observation :

=> Python follows the child → parent → grandparent order
=> The most derived class method executes first
"""
class Vehicle :
    def move(self) :
        print('Vehicle is moving')

class Car(Vehicle) :
    def move(self) :
        super().move()  # call Vehicle.move()
        print('Car is moving')

class ElectricCar(Car) :
    def move(self) :
        super().move()  # call Car.move()
        print('Electric Car is moving silently')

e = ElectricCar()
e.move()

"""
Exercise 3: Using super() in Multilevel Inheritance

Goal: Learn how super() works in a multilevel chain.

Task:
=> Create three classes:
=> Animal with __init__ that prints "Animal created"
=> Mammal(Animal) with __init__ that calls super().__init__() and prints "Mammal created"
=> Dog(Mammal) with __init__ that calls super().__init__() and prints "Dog created"
=> Create a Dog object

Observation :
=> Each __init__ in the hierarchy runs
=> The order follows Method Resolution Order (MRO)
"""
class Animal1 : 
    def __init__(self, name) :
        self.name = name 

    def output(self) :
        print(f'Animal created : {self.name}')

class Mammal(Animal1) :
    def __init__(self, name) :
        super().__init__(name) # Call Animal1.__init__
        print('Mamal created')
    def show(self) :
        print(f'Mamal : {self.name}')

class Dog1(Mammal) :
    def __init__(self, name) :
        super().__init__(name)  # Call Mammal.__init__
        print('Dog created')
    def showcase(self) :
        print(f'Dog : {self.name}')

d1 = Dog1('Jerry')
d1.output()
d1.show()
d1.showcase()