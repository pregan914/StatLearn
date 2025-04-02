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

#%%
# b) When we load in college we see the name for the first column is Unnamed:0
# We don't really want pandas to treat this as data but lets try and rename it 

college2 = pd.read_csv('Data\College.csv', index_col = 0)
print(college2)
college3 = college.rename({'Unnamed: 0': 'College'}, axis = 1)
print(college3)
college3 = college3.set_index('College')
print(college3)

college = college3

#%%
# c) Use the describe() method of to produce a numerical summary of the 
# variables in the data set

breakdown = college.describe()
print(breakdown)
# Breakdown gives interestin ginformation for each variable in the data

#%%
# d) Use the pd.plotting.scatter_matrix() function to produce a scatterplot 
# matrix of the first columns [Top10perc, Apps, Enroll]. Recall that you can 
# reference a list C of columns of a data frame A using A[C]
pd.plotting.scatter_matrix(college[['Top10perc','Apps','Enroll']])

#%%
# e) Use the boxplot() method of college to produce side-by-side boxplots of 
# Outstate versus Private
college.Private = pd.Series(college.Private, dtype = 'category')
fig, ax = plt.subplots(figsize = (8,8))
college.boxplot('Outstate', by = 'Private', ax=ax)

#%%
# f) Create a new qualitative variable called Elite, by binning the Top10perc
# variable into two groups based on whether or not the proportion of students
# coming from the top 10% of their high school classes exceeds 50%
# temp10perc = np.array([college.Top10perc]) / 100
college['Elite'] = pd.cut(college['Top10perc'], [0, 50, 100], labels = ['No', 'Yes'])

# Use the value_counts() method of colelge ['Elite'] to see how many elite
# universites there are. Finally, use the boxplot() method again to produce 
# side-by-side boxplots of Outstate versus Elite. 

numElite = college['Elite'].value_counts(); 
print('Number of elites is: ', numElite)


college.Elite = pd.Series(college.Elite, dtype = 'category')
fig, ax = plt.subplots(figsize = (8,8))
college.boxplot('Outstate', by = 'Elite', ax = ax)

#%%
# g) Use the plot.hist() method of college to produce some histograms with 
# different numbers of bins for a few of the quantitative variables. The 
# command plt.subplots(2,2) may be useful: it will divide the plot window into
# four regions so that four plots can be made simultaneously. By changing the 
# arguments you can divide the screen up in other combinations. 

fig, axes = plt.subplots(2,2)
axes[0,0].hist(college['Outstate'])
axes[0,1].hist(college['Top10perc'])
axes[1,0].hist(college['Apps'])
axes[1,1].hist(college['Enroll'])

