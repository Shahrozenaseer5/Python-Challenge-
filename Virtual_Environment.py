# A virtual environment is a tool used to isolate specific python environments on a single machine. 
# Allowing you to work on multiple projects with different dependencies and packages without conflicts.
# This can be useful when working on projects that have conflicting package versions or packages that are not compatible with each other.

# create a virtual environment in python :
# => python -m venv myenv

# activate virtual environment :
# => myenv\Scriptsctivate OR myenv\Scriptsctivate.ps1 (if we are in power shell)

# Once the virtual environment is activated, any packages that you install using pip will be installed in the virtual environment.
# Rather than in the global python environment.
# This allows you to have a separate set of packages for each project, without affecting the packages installed in global environment.

# to deactivate virtual environment :
# => deactivate

# "requirments.txt" file :
# In addition to creating and activating a virtual environment, it can be useful to create a requirments.txt file
# that list the packages and their versions that your project depends on. 
# This file can be used to easily install all the required packages in a new environment.

# To create a requirment.txt file, we can use pip freeze command, which outputs a list of installed packages and their versions. 
# => pip freeze > requirments.txt 

# To install the packages installed in requirments.txt, you can use pip install command with the -r flag :
# => pip install -r requirments.txt

import pandas as pd
print(pd.__version__)

import numpy as np
print(np.__version__)

import tensorflow as tf
print(tf.__version__)

import pygame as pg
print(pg.__version__)

import lxml 
print(lxml.__version__)

import openpyxl as op
print(op.__version__)
