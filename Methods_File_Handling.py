"""
File: Methods_File_Handling.py
Author: Shahroze
Purpose: Demonstrates file handling in Python
         - Reading from a file (commented section)
         - Writing to a new file
"""

import os

# Clear the terminal screen
os.system('cls')  # Use 'clear' on Linux/Mac

# ------------------ Reading from a file ------------------
# Uncomment and use if you have 'textfile.txt' with comma-separated values
# f = open('textfile.txt', 'r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     print(line)
#     if not line:
#         print(line, type(line))
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"Marks of student {i} in Math is : {m1 * 2}")
#     print(f"Marks of student {i} in English is : {m2 * 2}")
#     print(f"Marks of student {i} in SST is : {m3 * 2}")

# ------------------ Writing to a new file ------------------
f = open('newfile.txt', 'w')  # Automatically creates a file
lines = ['First Line \n', 'Second Line \n', "Third line \n"]

# Fill data in file
f.writelines(lines)

# Add a new line after each line
for line in lines:
    f.write(line + '\n')

# Successfully closes the file
f.close()

print("Data successfully written to 'newfile.txt'")
