import os 
# os.listdir() is used to list all files and folders inside a given directory.

"""Syntax
os.listdir(path='.')
"""
# Example (for alphabetical sorting and numerical sorting) :
import os

# Let's pretend we got this list from os.listdir("data")
folders = ['Lesson1', 'Lesson10', 'Lesson2', 'Lesson25', 'Lesson3']

print("Before sorting:")
print(folders)

# Sort normally (alphabetical)
alphabetical = sorted(folders)
print("\nAfter normal alphabetical sort:")
print(alphabetical)

# Sort by numeric part
folders.sort(key=lambda x: int(x.replace("Lesson", "")))
print("\nAfter numeric sort:")
print(folders)
print("-- Example ended --","\n")

folders = os.listdir("data")
folders.sort(key=lambda x: int(x.replace("Lesson", "")))
"""
What it means ?

You’re sorting the list folders, but instead of using normal alphabetical order, you’re telling Python how to compare items using a custom key.

Step-by-step explanation :

folders.sort(...) :
Sorts the list in place (doesn’t create a new list).
By default, it sorts alphabetically.

But with key=..., you can control the sorting logic.

key=lambda x: ...
lambda creates a small anonymous function.
For each item x in the list (like 'Lesson25'), this function runs and returns a value used for sorting.

x.replace("Lesson", "") :
Removes the word "Lesson" from the string.
Example: "Lesson25" becomes "25".

int(...) : 
Converts that "25" string into a number 25.

So when sorting, Python is comparing numbers (1, 2, 3, ..., 100) instead of strings ("Lesson1", "Lesson10", etc.).
That’s why "Lesson10" correctly comes after "Lesson9", not before it.

It tells Python:
“When sorting folder names like Lesson1, Lesson2, ..., Lesson100, ignore the word ‘Lesson’ and sort based on the numeric part.”
"""
# print(folders)
# it will list all files and folders inside data directory.

# we can list all folders properly inside data, by using for loop :
for folder in folders:
    print(folder)
# we can check each folder by writing : 
    print(os.listdir(f"data/{folder}"))
# it will search all files in folder
# we can see our current directory :
print(os.getcwd())
# we can change our directory by writing : 
os.chdir("/Users")
print(os.getcwd())