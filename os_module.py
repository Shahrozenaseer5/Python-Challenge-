""" 
=> os module in python is a built-in library that provides functions for interacting with the operating systen.
=> it allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system
    and running system commands.
"""
# here are some common tasks, we can perform with os module :
"""
reading and writing files, os module provides functions for opening, reading and writing files.

✅ The full os module (Python 3.12+) has over 130+ functions,
    but about 40–50 are common and cross-platform — the rest are system-specific or low-level.
"""
# if we want to open file for reading, we can use open method :
import os
os.system('cls')
print('Hi, my friend')
# to make a new directory / folder, we write :
if (not os.path.exists("data")): 
  os.mkdir('Data')
# it will automatically create a new folder whose name is 'data'.

# now if we want to make more folders inide our data folder, let suppose we want to create 100 folders for 100 days of code,  we write :
for i in range(1,101) :
  os.mkdir(f"data/day{i}")
# it will create 100 folders from day 1 to day 100
print(os.getcwd())