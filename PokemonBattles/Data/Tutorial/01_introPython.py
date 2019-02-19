import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('./input/pokemon.csv')

# ========== MATPLOTLIB ==========

# Line Plot
data.Speed.plot(kind='line', color='g', label='Speed', linewidth=1, alpha=0.5, grid=True, linestyle=':')
data.Defense.plot(color='r',label='Defense', linewidth=1, alpha=0.5, grid=True, linestyle='-.')
plt.legend(loc='upper right')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Line Plot')
plt.show()

# Scatter Plot
# x = attack, y = defense
data.plot(kind='scatter', x='Attack', y='Defense', alpha=0.5, color='red')
plt.xlabel('Attack')
plt.ylabel('Defence')
plt.title('Attack Defense Scatter Plot')
plt.show()

# Histogram
# bins = number of bar in figure
data.Speed.plot(kind='hist', bins=50,figsize=(12, 12))
plt.show()

# clf() = cleans it up again you can start a fresh
# plt.clf()
# We cannot see plot due to clf()


# ========== DICTIONARY ==========

# Create dictionary and look at its keys and values
dictionary = {'spain' : 'madrid', 'usa' : 'vegas'}
print(dictionary.keys())
print(dictionary.values())

# keys have to be immutable objects like string, boolean, float, integer, or tuples
# lists are not immutable
dictionary['spain'] = "barcelona"    # update existing entry
dictionary['france'] = "paris"       # Add new entry
del dictionary['spain']              # remove entry with key 'spain'
print('france' in dictionary)        # check include or not (returns True or False)
dictionary.clear()                   # remove all entries in dict (returns {} )


# ============ PANDAS ============
data = pd.read_csv('./input/pokemon.csv')

series = data['Defense']
data_frame = data[['Defense']]  # Keeps data as single column DF

# 1. Filtering Pandas DF
high_def = data['Defense'] > 200  # Returns column of bool related to the condition
print(data[high_def])  # Prints only columns where bool is True (def > 200)

# 2. Filtering pandas with logical_and
print(data[np.logical_and(data['Defense'] > 200, data['Attack'] > 100)])  # Prints Pokemon that have def>200 and att>100

# Can also use & for filtering (same output as above):
print(data[(data['Defense']>200) & (data['Attack']>100)])



# ============= WHILE AND FOR LOOPS =============

# Looping through dictionary:
dictionary = {'spain':'madrid','france':'paris'}
for key, value in dictionary.items():
    print(key, " : ", value)
print('')

# For pandas we can achieve index and value
for index, value in data[['Attack']][0:1].iterrows():
    print(index, " : ", value)
    # Prints '0  :  Attack    49'

# ======================================================================================================================
# Link : https://www.kaggle.com/kanncaa1/data-sciencetutorial-for-beginners
# ======================================================================================================================
