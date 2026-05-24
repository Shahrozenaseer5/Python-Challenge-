# Raising Custom Errors
# In python we can raise custom errors by using 'raise' keyword.
a = int(input('Enter value between 2 and 9 : '))
if a<2 or a>9 :
  raise ValueError ('Value must between 2 and 9 :(')

# Example :
salary = int(input('Enter salary : '))
if not 2000 < salary < 5000 : # it is a chained comparison in python

# means:
# “If salary is NOT between 2000 and 5000, run this block.”

  raise ValueError('Salary must be between 2000 and 5000')

# Defining custom exceptions

# syntax :

# class CustomError(Exception) :
  #code....
# try :
#  code...
# except CustomError :
#  code...

# This is useful because sometimes we might want to do something when a particular exception is raised. 
# For example, sending an error report to admin, calling an api etc.

# if user enters "quit" then no error will be raised otherwise raise error
# lst = ['5','6','7','8','9', 'quit']
# b = input('Enter value between 5 and 9 : ')
# if b not in lst :
#   raise ValueError('Value must between 5 and 9 or you can quit')

# Method # 2 : if we want to keep integers :

c = input('Enter value : ')
if c == 'quit' :
  print('Exiting...')
else :
  c = int(c)
  num = [5,6,7,8,9]
  if c not in num :
    raise ValueError ('Number is not between the given range :(')
  else :
    print('You are on the right track :)')
