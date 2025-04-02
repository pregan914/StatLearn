# -*- coding: utf-8 -*-
"""
Chapter 2 exercises in Inrtoduction to Statistical Learning with Python

Going through and analyzing data with pandas etc. 
Focus on the Auto data set
By: Pat Regan
"""
#%%
# This first part will use the Auto data. We'll start by loading in and 
# removing entries that have no data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Auto = pd.read_csv("Data\Auto.csv")
Auto = pd.read_csv("Data\Auto.data", na_values = ['?'], delim_whitespace = True)
Auto = Auto.dropna() 

#%%
# a) Which of the predictors are quantitative, and which are qualitative? 
# 
# Mpg, Displacement, horsepower, weight, acceleration and year are quantitative
# while cylinders and origin are qualitative. 

#%%
# b) What is the range of each quantitative predictor? You can answer using min
# and max of numpy 

df_auto = pd