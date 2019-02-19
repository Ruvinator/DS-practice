import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('./input/pokemon.csv')
data.head()  # Outputs first X rows
data.tail()  # Outputs last X rows
data.columns  # Outputs columns in data
data.shape  # Outputs number of rows and columns in table
data.info()  # Gives data type, number of samples (rows), number of features (columns), feature types, memory usage


# ============== EXPLORATORY DATA ANALYSIS ==============
# Outliers are smaller than Q1 (25%) and larger than Q3 (75%), where Q3 - Q1 = Inner Quartile Range

# Frequency of primary okemon types:
print(data['Type 1'].value_counts(dropna=False))

# Finding descriptions of columns (min/max, mean, std, count):
data.describe()


# ============== VISUAL EXPLORATORY DATA ANALYSIS ==============

# Attack of regular vs. legendary:
data.boxplot(column='Attack', by='Legendary')


# ============== TIDY DATA ==============
# Data is tidied with melt, see example below.

# Create new data from Pokemon data to explain melt more easily
data_new = data.head()  # Only take first 5 rows

# id_vars: we do not want to melt
# value_vars: want to melt
melted = pd.melt(frame=data_new, id_vars='Name', value_vars=['Attack', 'Defense'])

# Combines Attack and Defense in a single column. Table also contains Name and value (of Attack and Defense)


# ============== PIVOTING DATA ==============
# This is the reverse of melting
melted.pivot(index='Name', columns='variable', values='value')


# ============== CONCATENATING DATA ==============
data1 = data.head()
data2 = data.tail()
conc_data_row = pd.concat([data1, data2], axis=0, ignore_index=True)

# Can concatenate dataframes with different columns into one dataframe with multiple columns
data1 = data['Attack'].head()
data2 = data['Defense'].head()
conc_data_col = pd.concat([data1, data2], axis=1)  # Axis = 1 adds dataframe columns


# ============== DATA TYPES ==============
# There are 5 basic data types: object(string), boolean, integer, float, and categorical.
# Category can make dataframe smaller in memory and can be used for analysis (esp. sklearn)
data.dtypes
data['Type 1'] = data['Type 1'].astype('category')
data['Speed'] = data['Speed'].astype(float)
data.dtypes


# ============== MISSING DATA AND TESTING WITH ASSERT ==============
# If we encounter missing data, we can:
#   leave it
#   drop it with dropna()
#   fill missing value with fillna()
#   fill missing value with test statistic like mean
# Assert is a check that can be turned on or off when program testing is done

data['Type 2'].value_counts(dropna=False)  # Results in 386 NAN values (secondary type)
data1 = data
data1['Type2'].dropna(inplace=True)  # Do not assign it to new variable (automatically assign to data)

# Check with assert statement
assert 1 == 1  # Returns nothing because it is true
assert data['Type 2'].notnull().all()  # Returns nothing because nan values were dropped
data['Type 2'].fillna('empty', inplace=True)
assert data['Type 2'].notnull().all()  # Returns nothing because nan values were filled with empty


# ======================================================================================================================
# Link : https://www.kaggle.com/kanncaa1/data-sciencetutorial-for-beginners
# ======================================================================================================================
