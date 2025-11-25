# ============================================
#  Title: OOP (Object Oriented Programming) Notes & Examples
#  Author: Shahroze
#  Description: This file contains handwritten notes, examples,
#               and basic demonstrations of OOP concepts in Python,
#               including classes, objects, encapsulation,
#               inheritance, and polymorphism.
#  Date: 2025-11-25
#  Purpose: For learning, revision, and GitHub portfolio.
# ============================================

# == OOP (Object Oriented Programing) in python ==
"""
In programing languages, there are 2 approaches to write code :
1 - Procedural Programing.
2 - Object Oriented Programing.

=> OOP is used to map real world entities. So that programer can easily understand the program. 

=> Basic idea of OOP in python is to use classes and objects to represent real world concepts and entities.

=> Class is a blueprint or template for creating objects. It defines the properties and methods that an object of that class will have.
properties are the data or state of an object, and methods are the actions or behaviors that an object can perform.

=> An object is an instance of a class and it contains it's own data and methods. 
For example, you can create a class called "Person" that has properties such as name and age, and methods such as speak() and walk().
Each instance of the person class would be a unique object with it's own name and age. But they would all have the same methods to 
speak and walk. 

=> One of the key feaures of OOP in python is 'encapsulation'. Which means that the internal state of an object is hidden and can only be
accessed or modified through the object's methods. This helps to protect the object's data and prevent it from being modified in 
unexpected ways.

=> Inheritance : This is the key feature of OOP. Which allows new classes to be created that inherit the properties and methods of an 
existing class. This allows for code reuse and makes it easy to create new classes that have similar functionality to existing classes.
In below RailwayForm example, we can make another class "VIP RailwayForm" from class "RailwayForm" which will be surved to VIPs only.
Let assume we have a phone, we apply some methods and make it a 'drone'. It's inheritance.
If we have a cycle, we installed an engine, now it's become a bike. and if we installed 2 more wheels, it will become a car. 
These are all examples of inheritance.

=> Polymorphism : it is also supported in python. Which means that objects of different classes can be treated as if they were objects of a 
common class. This allows for greater flexibility in code and makes it easier to write code that can work with multiple types of objects.

Summary : OOP in python allows developers to model real-world concepts and entities using classes and objects, encapsulate data, 
reuse code through inheritance and write more flexible code through polymorphism.
"""
import os
os.system('cls')
def hello():
    print('Hi ! it\'s me.')
hello()

sales_1 = 7000 
profit_1 = 2500
ad_1 = 1350
# Khaleeq.sales

sales_2 = 9000 
profit_2 = 3500
ad_2 = 2000
# Saira.sales

sales_3 = 5000 
profit_3 = 1500
ad_3 = 1000
# Memona.sales

sales_4 = 9500 
profit_4 = 4500
ad_4 = 1900
# shahroze.sales

"""
In the above scenario, we have made 4 variables in which information of business owners is saved. 
But it's not suitable in the long run. In place we prefer to make a universal template by which we can just add details and get result 
according to different business owners by using OOP.
We use OOP to perform a specific operatons on an entity which is convenient and can easily moderate.

Scenario 2 : Let's assume we have to make a game in which a whole city will be the enemy and we have only 1 super hero.
In this case, we can either create variable for each enemy or we can make a template by which we can analyze health, weapons etc of
our enemies. This approach is more convenient and maintainable.

Example 3 : Let suppose we have to see passenger record, we can make a template / blue-print for this purpose and 
all entities will be made by using this blue-print.

RailwayForm --> Class [Blueprint / Template]
Saim --> Saim ki info wala form --> Object [entity]
Joseph --> Joseph ki info wala form --> Object [entity]
Sophia --> Sophia ki info wala form --> Object [entity]
we can change name also by using class methods :
Sophia.changeName('Maria')
"""