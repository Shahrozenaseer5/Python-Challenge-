"""
================================================================================
Project     : Clear the Clutter
File        : Ex7_ClearTheClutter.py
Author      : Shahroze
Created on  : 2026-1-1
Description : 
    This script clears clutter inside a folder by renaming all files according to 
    their file types. PNG images, PDFs, EXEs, etc. are renamed sequentially based 
    on their extensions, e.g., 1.png, 2.png, 1.pdf, 2.pdf, etc.
    
    The script demonstrates the use of the os module for:
    - Listing directory contents
    - Checking file types
    - Renaming files systematically
    - Preserving original file extensions
    
Usage :
    1. Set the 'folder_path' variable to the target folder.
    2. Run the script.
    3. Files in the folder will be renamed by type in numerical order.
    
Note :
    - Recommended to test on a dummy folder before running on important data.
    - Commented sections show ideas for converting images to .png format.
================================================================================
"""

"""
Write a program to clear the clutter inside a folder in your computer. 
You should use os module to rename all the png images from 1.png all the way till n.png,
where n is the number of png files in that folder. Do the same for other file formats. For example :
image.png  -->  1.png
file.png  -->  2.png
this.png  -->  3.png
design.png  -->  4.png
name.png  -->  5.png
"""
import os
os.system('cls')
# if (not os.path.exists("Programing")):
#     os.mkdir("Programing") => it will create a new folder whose name will be 'Programing'

# folder_path = r"c:\Users\dell\Downloads\Stock Photos"

# count = 1

# for file in sorted(os.listdir(folder_path)):
#     if file.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
#         old_path = os.path.join(folder_path, file)
#         extension = os.path.splitext(file)[1]
#         new_name = f"{count}.png"
#         new_path = os.path.join(folder_path, new_name)

#         os.rename(old_path, new_path)
#         count += 1

print('After renaming everything in dummy folder :')
folder_path = r"C:\Users\dell\Downloads\dummy_data"

for item in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, item)):
        print(item, "->", os.path.splitext(item)[1])

counters = {}

for file in sorted(os.listdir(folder_path)):
    old_path = os.path.join(folder_path, file)

    if os.path.isfile(old_path):
        ext = os.path.splitext(file)[1]

        if ext:
            counters.setdefault(ext, 0)
            counters[ext] += 1

            new_name = f"{counters[ext]}{ext}"
            new_path = os.path.join(folder_path, new_name)

            os.rename(old_path, new_path)

print('Clutter cleared successfully.')