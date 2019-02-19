import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

country = ["Spain", "France"]
population = ["11", "12"]
list_label = ["country", "population"]
list_col = [country, population]
zipped = list(zip(list_label, list_col))
data_dict = dict(zipped)
df = pd.DataFrame(data_dict)  # Dataframe with columns 'country' and 'population' containing above entries

df["capital"] = ["madrid", "paris"]  # adds new column to dataframe

df["income"] = 0  # broadcasts entire column


# ============== VISUAL EXPLORATORY DATA ANALYSIS ==============

data = pd.read_csv('./input/pokemon.csv')

data1 = data.loc[:, ['Attack', 'Defense', 'Speed']]  # all data points with Attack, Defense, and Speed columns
data1.plot()
data1.plot(subplots=True)
plt.show()

data1.plot(kind="scatter", x="Attack", y="Defense")
plt.show()

# Histogram
data1.plot(kind="hist", y="Defense", bins=50, range=(0, 250), density=True)  # 50 bins ranging from 0 to 250
plt.show()

# histogram subplot with cumulative and non-cumulative
fig, axes = plt.subplots(nrows=2, ncols=1)
data1.plot(kind='hist', y='Defense', bins=50, range=(0, 250), density=True, ax=axes[0])
data1.plot(kind='hist', y='Defense', bins=50, range=(0, 250), density=True, ax=axes[1], cumulative=True)
plt.show()
plt.savefig("04-cumulativeHist.png")


# ============== STATISTICAL EXPLORATORY DATA ANALYSIS ==============

data.describe()  # outputs std, mean, count, quartile values, min, max


# ============== INDEXING PANDAS TIME SERIES ==============

time_list = ["1992-03-08", "1992-04-12"]
print(type(time_list[1]))  # Date is currently string
datetime_object = pd.to_datetime(time_list)  # Converts string to datetime object

# close warning
import warnings
warnings.filterwarnings("ignore")

data2 = data.head()
date_list = ["1992-01-10", "1992-02-10", "1992-03-10", "1993-03-15", "1993-03-16"]
datetime_object = pd.to_datetime(date_list)
data2["date"] = datetime_object  # Adding fates to dataframe
data2 = data2.set_index("date")  # Turning dates into index (rather than integer values)

# Now can select according to date index
print(data2.loc["1993-03-16"])  # Prints Charmander info
print(data2.loc["1992-03-10":"1993-03-16"])  # Prints various rows corresponding to date range


# ============== RESAMPLING PANDAS TIME SERIES ==============
# Downsampling: reducing date time rows to slower frequency (from daily to weekly)
# Upsampling: increase date time rows to faster frequency (daily to hourly)
# Interpolate: Interpolate values according to different values (linear, time, or index)
# "A" = year, "M" = month

data2.resample("A").mean()  # Resamples into yearly buckets

data2.resample("M").mean()  # Resamples into monthly buckets (lot of NAN because not all months are included)

data2.resample("M").first().interpolate("linear")  # fills in NAN values with interpolations from first value

data2.resample("M").mean().interpolate("linear")  # interpolates from mean


# ============== MANIPULATING DATA FRAMES WITH PANDAS ==============
data = data.set_index("#")  # Sets pokemon number as data index
data["HP"][1]  # can index using square brackets
data.HP[1]  # using column attribute and row label
data.loc[1, ["HP"]]  # using loc accessor
data[["HP", "Attack"]]  # selecting only some columns


# ============== SLICING DATA FRAME ==============
data.loc[1:10, "HP":"Defense"]
data.loc[10:1:-1, "HP":"Defense"]  # Reverse slicing
data.loc[1:10, "Speed":]  # From speed to end


# ============== FILTERING DATA FRAMES ==============
boolean = data.HP > 200
data[boolean]  # Returns only Pokemon with HP > 200

# Combining filters
first_filter = data.HP > 150
second_filter = data.Speed > 35
data[first_filter & second_filter]  # Returns output that satisfies both filters
data.HP[data.Speed < 15]  # Returns HP of Pokemon whose speed is > 15


# ============== TRANSFORMING DATA ==============
def div(n):
    return n/2


data.HP.apply(div)  # Divides all HP by 2

data.HP.apply(lambda n: n/2)
# ======================================================================================================================
# Link : https://www.kaggle.com/kanncaa1/data-sciencetutorial-for-beginners
# ======================================================================================================================

data["total_power"] = data.Attack + data.Defense


# ============== INDEX OBJECTS AND LABELED DATA ==============
print(data.index.name)
data.index.name = "index_name"

data3 = data.copy()
data3.index = range(100, 900, 1)  # Start index from 100 rather than 0


# ============== HIERARCHICAL INDEXING ==============
data1 = data.set_index(["Type 1", "Type 2"])  # Sorts by first type and then by second


# ============== PIVOTING DATA FRAMES
dic = {"treatment":["A", "A", "B", "B"], "gender": ["F", "M", "F", "M"], "response": [10, 45, 5, 9],
       "age": [15, 4, 72, 65]}
df = pd.DataFrame(dic)
df.pivot(index="treatment",columns = "gender",values="response")  # Can change index and group other columns


# ============== STACKING AND UNSTACKING DATAFRAME ==============
df1 = df.set_index(["treatment", "gender"])
df1.unstack(level=0)  # Treatment becomes a column sub-category
df1.unstack(level=1)  # Gender becomes a column sub-category


# ============== MELTING DATA FRAMES ==============
pd.melt(df, id_vars="treatment", value_vars=["age", "response"])  # treats treatment as ID and groups vars under col


# ============== CATEGORICALS AND GROUPBY ==============
df.groupby("treatment").mean()  # mean is an aggregation method (take means of other features according to treatment)
df.groupby("treatment")[["age", "response"]].min()  # can choose multiple features
