import pandas as pd
import pandas_profiling
import matplotlib.pyplot as plt

combats_data = pd.read_csv("./input/combats.csv")
pokemon_data = pd.read_csv("./input/pokemon.csv")
tests_data = pd.read_csv("./input/tests.csv")

# Creates summary of dataframe
combats_profile = pandas_profiling.ProfileReport(combats_data)
combats_profile.to_file("combat_profile.html")

# Showing correlation of combat data (nothing useful)
plt.matshow(combats_data.corr())
plt.xticks(range(len(combats_data.columns)), combats_data.columns)
plt.yticks(range(len(combats_data.columns)), combats_data.columns)
plt.colorbar()


