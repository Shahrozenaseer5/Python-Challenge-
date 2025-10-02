
# Methods on dictionaries
# .update() Method
# .update() method updates the value of the key provided to it if the item already exists in the dictionary,
# else it creates a new key value pair.
info = {'name' : 'Aditi', 'age' : 29, 'eligible' : True}
# now if we need to update age from 29 to 30, and we need to add a new key value pair of DOB, we use .update() method
info.update({'age' : 30, 'DOB' : 2001})
# it will upadte age value and add a new key value pair of {'DOB' : 2001}
print(info)

# Example : update employee id and employee performance
employee_id1 = {
              337 : 69, # performance of employee id 337 is 69% out of 100%
              29 : 56,
              45 : 90,
              867 : 46,
              134 : 78
}
employee_id2 = {
              339 : 89, # performance of employee id 339 is 89% out of 100%
              100 : 66,
              111 : 50,
              224 : 82,
              234 : 62
}
# let's assume employee_id1 is our senior manager and employee_id2 is junior manager
# employee_id1 tells employee_id2 to give all data of employees to me and i will add and update it to my record.
# for this purpose we will use .update() method
employee_id1.update(employee_id2)
print(employee_id1) # we get new record of all employees

# Removing items from dictionary :
# there are few methods to clear items from the dictionary

# .clear()
# .clear() method removes all the items from the dictionary
info = {'name' : 'Aditi', 'age' : 29, 'eligible' : True}
info.clear() # it will remove all items from dictionary
print(info)  # it will return an empty dictionary
# if we want to make empty dictionary, we simple write :
empt = {}
print(empt) # it will also print an empty dictionary

# .pop()
# .pop() method removes the item with the provided key and returns the value
# basically, we can remove an item of our choice through .pop() method
info = {'name' : 'Aditi', 'age' : 29, 'eligible' : True}
info.pop('eligible') # it will remove 'eligible' key value pair from dictionary
print(info)

# .popitem()
# if we want to remove last key value pair from the dictionary, we use .pop() method
info = {'name' : 'Aditi', 'age' : 29, 'eligible' : True}
info.popitem() # it will remove last key value pair ('eligible' : True) from dictionary
print(info)

# del keyword
# we can also use del keyword to remove a dictionary item
info = {'name' : 'Aditi', 'age' : 29, 'eligible' : True}
del info['eligible'] # we can remove a specific item from dictionary by passing it to dictionary with del keyword
print(info)
# if key is specified, del keyword will remove all dictionary items
del info
# print(info) it will throw an error because del keyword already deleted info dictionary

# we can always see latest documentation of confusing topic by searching like "python dictionary documentation"
# Link of "python dictionary documentation" : https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
{x: x**2 for x in (2, 4, 6)}

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
dict(sape=4139, guido=4127, jack=4098)

# Looping Techniques
# When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.
for i in reversed(range(1, 10, 2)): # 1 is starting index, 10 is ending index and jump index is 2 which means jump by 2 in reverse.
    print(i)

# To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket): # sorted by first alphabet of a,b,c..z
    print(i)

# Using set() on a sequence eliminates duplicate elements. The use of sorted() in combination with set() 
# over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)): # we get sorted and unique items
    print(f)
