# Short hand if else statements

# There is also a shorthand syntax for the if else statement that can be used when the condition being tested is simple and
# the code blocks to be executed are short. 

# 
a = int(input('Enter value of a : '))
b = int(input('Enter value of b : '))
print('A') if a > b else print('=') if a == b else print("B")
# This logic is equivalent to :

# if a > b:
#     print('A')
# elif a == b:
#     print('=')
# else:
#     print('B')

# it means :
# If a is greater than b, print 'A'
# Else if (elif) a equals b, print '='
# Otherwise, print 'B'

c = 9 if a > b else 0
print(c)

# Example :
# result = value_if_true if condition else value_if_false
# It is equals to :

# if condition:
#     result = value_if_true
# else:
#     result = value_if_false

# Conclusion : This syntax is best for simple if else statements especially for assigning value to a variable or with expressions.
# But it will not recommended for complex if else ladder because it affects readability.
