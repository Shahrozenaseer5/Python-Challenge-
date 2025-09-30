
# set methods in python
# 1- union() and update()
# union() and update() function print all items that are present in two sets.
# union() method return a new set whereas update() method adds items into the existing set from another set
# union() : combine values of both sets but remove duplicates
s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
s1.update(s2) # it means put those values of s2 which are not present in s1
print(s1,s2) # it will print updated s1 and s2 remain same.
# s2.update(s1)
# print(s2,s1)

# 2- intersection() and intersection_update()
# intersection() and intersection_update() print values that are similar in both sets.
# intersection() method return a new set whereas intersection_update() method updates into the existing set from another set
# intersection() : put values that are same in both sets.
cities_1 = {'Tokyo', 'Madrid', 'Berlin', 'Delhi'}
cities_2 = {'Tokyo', 'Seoul', 'Kabul', 'Madrid'}
# print(cities_1.intersection(cities_2))
cities_3 = cities_1.intersection(cities_2) # we get new set through intersection() method
print(cities_3)
cities_1.intersection_update(cities_2) # we get updated version of cities_1
print(cities_1)

# 3 - Symmetric_difference() and symmetric_difference update()
# symmetric_difference() and symmetric_difference update() methods prints only those items which are 'not similar' in both sets.
cities_1 = {'Tokyo', 'Madrid', 'Berlin', 'Delhi'}
cities_2 = {'Tokyo', 'Seoul', 'Kabul', 'Madrid'}
# print(cities_1.symmetric_difference(cities_2))
cities_3 = cities_1.symmetric_difference(cities_2) # we get new set through symmetric_difference() method
print(cities_3)
cities_4 = (cities_1.symmetric_difference_update(cities_2)) # we get updated version of cities_1
print(cities_1)

# 4 - difference() and difference_update()
# difference() and difference_update() methods prints only items that are only present in the original set.
# The difference method returns a new set on the other hand differenece_update() method updates into the existing set from another set
# differenece is (A - B) in general
cities_1 = {'Tokyo', 'Madrid', 'Berlin', 'Delhi'}
cities_2 = {'Tokyo', 'Seoul', 'Kabul', 'Madrid'}
cities_3 = cities_1.difference(cities_2)
print(cities_3)  # we get new set through difference() method
cities_1.difference_update(cities_2)
print(cities_1) # we get updated version of cities_1

# Other set methods
# there are several in-built methods used for the manipulation of sets. They are explained below :

# 1 - isdisjoint()
# isdisjoint() method checks if items of given set are present in another set.
# This method returns False if if items are present, else it returns True.
cities_1 = {'Berlin', 'Delhi'}
cities_2 = {'Tokyo', 'Seoul', 'Kabul', 'Madrid'}
# print(cities_1.isdisjoint(cities_2)) check whether values of cities_1 are present in cities_2 or not. if not then return True else return False.
cities_3 = cities_1.isdisjoint(cities_2) # we get new set through isdisjoint() method
print(cities_3)

# 2 - issuperset()
# issuperset() method checks if all the items of a particular set are present in the original set.
# it returns True if all items are present, else it returns False.
cities_1 = {'Tokyo', 'Madrid', 'Berlin', 'Delhi'}
cities_2 = {'Tokyo', 'Seoul', 'Kabul', 'Madrid'}
# print(cities_1.issuperset(cities_2))
cities_3 = cities_1.issuperset(cities_2) # we get new set through issuperset() method
print(cities_3)
cities_4 = {'Tokyo', 'Madrid'}
# print(cities_4.issuperset(cities_1))
cities_5 = cities_4.issuperset(cities_1)
print(cities_5)
cities_6 = {'Tokyo', 'Madrid', 'Berlin', 'Delhi', 'Kabul', 'Seoul'}
# print(cities_6.issuperset(cities_1))
cities_7 = cities_6.issuperset(cities_1) # output will be True because cities_6 is the superset of cities_1.
print(cities_7)

# 3 - issubset()
cities_3 = cities_2.issubset(cities_1)
print(cities_3)
cities_7 = cities_4.issubset(cities_6) # output will be True because cities_4 is the subset of cities_6
print(cities_7)

# 4 - add()
# if we want to add a single item in set, use add() method
cities = {'London', 'New Zeeland', 'Zimbabwe', 'Ireland'}
cities.add('America') # America will be added in cities
print(cities)

# 5 - update()
# if we want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary)
# and use update() method to add it into the existing set
cities_1 = {'Tokyo', 'Madrid', 'Berlin', 'Delhi'}
cities_2 = {'Tokyo', 'Seoul', 'Kabul', 'Madrid'}
cities_1.update(cities_2)
print(cities_1)

# 6 - remove() / discard()
# we can use remove() or discard() methods to remove values in set.
places = {'Vietnam', 'Thailand', 'China', 'Japan', 'Tanzania', 'Afghanistan'}
places.remove("Afghanistan")
print(places)
# Note : the main difference between remove() and discard() is that, if we try to delete an item which is not present in set, 
# than remove() generate an error while discard() doesn't raise any error
city = {'India', 'Africa', 'Poland', 'Russia'}
# city.remove('Pakistan') # it will generate an error
# print(city)
city.discard('Pakistan')
print(city)

# 7 - pop()
# this method remove the last item of the set but the catch is that we don't know which item gets popped.
# Because sets are unordered. However you can access the popped item if you assign the pop() method to a variable.
city = {'India', 'Africa', 'Poland', 'Russia'}
item = city.pop()
print(item)
print(city)

# del
# del is a keyword that delete a set entirely
s = {'India', 'Africa', 'Poland', 'Russia'}
del s
# print(s) => error occur because 'del' keyword deleted 's' already

# 8- clear()
# what if we don't want to delete whole set but we just want to delete all items in set. 
# In this case, we use clear() method.
# This method clear all items in a set and print an empty set
countries = {'India', 'Africa', 'Poland', 'Russia'}
countries.clear()
print(countries)

# Check if items exists in set 
set_1 = {'Honda', 94, 45.7, False, 94, 119191}
# we use 'in' keyword to identify presence of specific item in set
if 94 in set_1:
  print('94 is present in set_1')
else :
  print('94 is not present in set_1')
