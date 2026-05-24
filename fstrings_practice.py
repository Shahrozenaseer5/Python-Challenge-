
 # f-strings in python
letter = "Hi ! my name is {} and I am from {}"
name = 'Shahroze'
country = 'Pakistan'
print(letter.format(name, country))
# The .format() method in Python is a string method used for formatting and embedding values within a string. 

# if i put country first and then name, we get wrong output
# print(letter.format(country,name))

# but we have a solution for this problem :
letter = 'Hi ! my name is {1} and I am from {0}' # here '0' show country and '1' shows name.
print(letter.format(country, name))

# using only 2 numbers after point(.) :
price = 49.099999
txt = "For only {price:.2f} dollars" # '.2f' is a format specifier that tells Python how to format the number 'price'
print(txt.format(price = 49.099999)) # it will print value upto 2 decimal places after point(.)

# Now we use latest method for string formating which is known as f-strings
print(f'My name is {name} and I am from {country}.', '
') # We can use f-strings to insert variables directly into a string
# if i want to print as it is : 
print(f'My name is {{name}} and I am from {{country}}.', '
')
# I put 2 more curly braces in string.

# we can use .3f in f-strings like this :
price2 = 78.099999
print(f'For only {price2:.3f}') # '.3f' is a format specifier that tells Python how to format the number 'price2'
# . (The period): This indicates that you're about to specify precision for a floating-point number.
# 3: This specifies the precision, meaning the number should be displayed with exactly 3 digits after the decimal point.
# f: This specifies the type, indicating that the value should be treated as a floating-point number (a number with a decimal point).
# it will print value upto 3 decimal places after point(.)

# even if we need a single variable as a string, we can do so
print(f"{555*767}")
print(type(f"{555*767}")) 

# Expression evaluation using f-strings :
x = 12
y = 18
print(f"Sum of {x} and {y} is equal to {x+y}")

price3 = 15.35
quantity = 79
print(f'Total pirce = {price3*quantity}')

# f strings for debugging :
# F-strings are also useful for debugging. You can add an equals sign = after a variable to automatically include
# the variable name and its value in the output, which is useful for quick debugging print statements.
message = "Hello, world!"
print(f"{message=}")
# Output: message='Hello, world!'

# When you use f"{variable=}", Python does two things:
# It gets the name of the variable (e.g., message).
# It gets the value of the variable (e.g., "Hello, world!").
# It then combines them into a string formatted as variable_name='value'.
# For example, print(f"{message=}") is a cleaner, more modern alternative to writing print(f"message='{message}'").

# Formating options : decimal precision
pi = 3.1415926535
print(f"Pi to two decimal places: {pi:.2f}")
# Output: Pi to two decimal places: 3.14

# Formatting options : Padding and alignment : Pad and align text or numbers within a specified width.
number = 43556
print(f'Padded number : {number : 10}') # value of number will be print after 10 whitespaces.

# Formatting options : Thousands separators : Add commas for large numbers.
populationOfPakistan = 255219554
print(f'Current population of Pakistan is : {populationOfPakistan:,}')
