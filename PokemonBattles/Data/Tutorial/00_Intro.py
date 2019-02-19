import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("./input/pokemon.csv")
data.info()

# correlation map
f, ax = plt.subplots(figsize=(18, 18))
sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt='.1f', ax=ax)
plt.show()

data.head(10)  # prints first 10 rows
print(data.columns)  # outputs columns in dataframe

# ======================================================================================================================
# Link : https://www.kaggle.com/kanncaa1/data-sciencetutorial-for-beginners
# ======================================================================================================================
