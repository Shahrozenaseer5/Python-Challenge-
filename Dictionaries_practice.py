
# Dictionaries in python
# "Dictionary is ordered collection of data items"
# "Dictionary is a combination of key value pairs"
dict = {'Shahroze': 'Human Bieng', 
        'Spoon' : 'object',
        'Eagle' : 'Bird'}
print(dict)
# we can access value by it's key in dictionaries
print(dict['Eagle'] ,'
', dict['Spoon'])

# Example :
employee_id = {
              337 : 'Shami',
              29 : 'Katrina',
              45 : 'Aniket',
              867 : 'Maria',
              134 : 'Peter'
}
print(employee_id[29])

info = {'Name' : 'Khadija', 'age' : 34, 'city' : 'Karachi', 'Eligible' : True}
print(info)
# we can access value by two methods :
print(info['Name'])
print(info.get('Name')) 
# if we enter key which is not present in dictionary, direct access method will throw an error
# print(info['Name2'])
# but if we use .get() method, it will pass 'none' if no key is found in dictionary
print(info.get('Name2'))

# Accessing multiple keys in dictionary : .keys()
info = {'Name' : 'Khadija', 'age' : 34, 'city' : 'Karachi', 'Eligible' : True}
print(info.keys())
# we can access all values in dictionary : .values()
print(info.values())

# we can iterate all values of all keys using for loop
for key in info.keys() :
  # print(info[key])
  print(f'Value of {key} is {info[key]}') # using f-strings

# we can access all key:value pairs by using .items() method
print(info.items())
# using for loop
for key,value in info.items() :
  print(f'Key is {key} and value is {value}')
