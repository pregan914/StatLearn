"""
Going through the labs and exercises of intro to statistical learning - 
Book by G. James, D. Witten, T. Hastie, R. Tibshirani, J. Taylor

Goes through everything from linear regression through deep learning etc. 

First file: Basic Commands, Numpy, and Graphics
"""

# Can easily add two integers
3 + 5
print('Can easily add two integers and print') 
print(3 + 5)
print('\n')

# Can do something similar with strings
'hello' + ' ' + 'world' 
# Again, it does not print so.. 
print('We can add strings and print')
print('hello' + ' ' + 'world')

# Let's say I have two vectors of numbers and I want to add them. Inutition 
# tells me I should be able to do: 
a = [3, 4, 5]
b = [4, 9, 7]

# This should add 3 + 4 and 4 + 9, etc. .. but we get
print('Here is what happens when we add two lists')
print(a + b)

# Not what we expected! Which is because these are lists and not arrays
# We're going to heavily rely on the package numpy and need to import it 
import numpy as np

x = np.array([3, 4, 5])
y = np.array([4, 9, 7])
print('Now if we add np.arrays')
print(x + y)

# Much better
# We can create a matrix via 
x = np.array([[1, 2], [3, 4]])
print('We can also print matrices')
print(x)
# How many dimensions does x have
print(x.ndim, '\n')
#%%
##########################################################
# Now let's loook at reshape
x = np.array([1, 2, 3, 4, 5, 6])
print('beginning x: \n',x)
x_reshape = x.reshape((2,3))
print('reshaped x:\n', x_reshape)

##########################################################
print('Generating random numbers with numpy')
x = np.random.normal(size = 50)
print(x)

print('Now create variable y that is x plus more random nums')
y = x + np.random.normal(loc=50,scale = 1,size = 50)
# loc is the mean, scale std, size is the number of entries
print(y)

#%%
##########################################################
# Graphics 
rng = np.random.default_rng(100)
from matplotlib.pyplot import subplots
fig, ax = subplots(figsize = (8,8))
x = rng.standard_normal(100)
y = rng.standard_normal(100)
ax.plot(x,y);

fig, ax = subplots(figsize=(8,8))
ax.scatter(x,y, marker = 'o')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title('title')

#%%
##########################################################
# Importing and working with data
import pandas as pd
Auto = pd.read_csv('Data\Auto.csv')
print(Auto)
print('What if I want to look at just horsepower')
print(Auto['horsepower'])

# They're all strings.. why? 
print(np.unique(Auto['horsepower']))

# There's a question mark in the data set causing issues! We can fix this by 
# including an argument into read_csv
Auto = pd.read_csv('Data\Auto.data', na_values = ['?'], delim_whitespace = True)
print(Auto['horsepower'].sum())

# Drop the rows with missing observations
Auto_new = Auto.dropna()
print(Auto_new.shape)

