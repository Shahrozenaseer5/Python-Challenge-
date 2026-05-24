import os

# now if we want to rename all 100 folders, we will write :
for i in range (1,101):
# rename() syntax : os.rename(sourc, destination) or os.rename('old_name.txt', 'new_name.txt')
    # os.rename(f"data/day{i}", f"data/Lesson {i}")
# it will rename all folder names from day1 to Lesson1 etc
    os.rename(f"data/Lesson{i}", f"data/Lesson {i}")
# this will create a space between Lesson and #
