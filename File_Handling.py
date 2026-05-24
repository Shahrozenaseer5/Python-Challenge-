"""
====================================================================
File Name      : file_handling.py
Author         : Shahroze
Description    : Demonstrates fundamental concepts of file handling in Python, 
                 including reading, writing, appending, and using context managers.
Created On     : 8 November 2025
Version        : 1.0
====================================================================

Notes:
- Python provides built-in functions to handle file operations easily.
- Modes like 'r', 'w', and 'a' define how the file is accessed.
- Always close files or use 'with' for automatic cleanup.
====================================================================
"""

# -------------------------------------------------------------
# Import Section
# -------------------------------------------------------------
import os

# Clear the console (for Windows)
os.system('cls')

# -------------------------------------------------------------
# READING A FILE
# -------------------------------------------------------------
# Example:
# f = open('myfile.txt', 'r')
# text = f.read()
# print(text)
# f.close()


# -------------------------------------------------------------
# WRITING TO A FILE
# -------------------------------------------------------------
# Example:
# f = open('myfile2.txt', 'w')
# f.write('Now we are in myfile2.txt')
# f.close()
"""
Keep in mind:
Writing to a file will overwrite its contents.
If we want to append instead of overwriting, we can open it in append mode.
"""

# Example of Append Mode:
# f = open('myfile2.txt', 'a')
# f.write('Hi ! my friend')
# f.close()
# It will append the same text every time we run our code.


# -------------------------------------------------------------
# CLOSING A FILE
# -------------------------------------------------------------
# It is important to close a file after you are done with it.
# This releases resources and allows other programs to access it.
# Example:
# f = open('myfile.txt', 'rb')  # Opening a binary file in read mode


# -------------------------------------------------------------
# PRACTICAL EXAMPLE
# -------------------------------------------------------------
f = open('myfile.txt', 'r')
f.read()
f.close()


# -------------------------------------------------------------
# THE 'with' STATEMENT
# -------------------------------------------------------------
# The 'with' statement automatically closes the file after use.
# No need to call close() manually.

with open('myfile2.txt', 'a') as f:
    f.write("I am inside 'with' statement")


# -------------------------------------------------------------
# FILE MODES SUMMARY
# -------------------------------------------------------------
"""
Modes in file handling:

r  : Read mode (default). Opens file for reading. Error if file doesn’t exist.
w  : Write mode. Opens file for writing and creates a new file if it doesn’t exist.
a  : Append mode. Opens file for appending and creates a new file if it doesn’t exist.
x  : Create mode. Creates a file and raises an error if it already exists.
t  : Text mode (default). Handles text files. (e.g., 'rt' or 'wt')
b  : Binary mode. Used for binary files such as images, PDFs, etc.

Default mode is 'r' (equivalent to 'rt').
"""
