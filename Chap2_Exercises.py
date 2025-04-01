# -*- coding: utf-8 -*-
"""
Chapter 2 exercises in Inrtoduction to Statistical Learning with Python

Going through and analyzing data with pandas etc. 

By: Pat Regan
"""
#%% First exercise deals with the college data set in the Data folder
# a) Use pd.read.csv() function to read the data in python. Call the loaded
# data college. Make sure that you have the directory set to the correct 
# location for the data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
college = pd.read_csv('Data\College.csv')

print(college)
