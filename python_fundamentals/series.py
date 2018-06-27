import pandas as pd
animals = ['Tiger', 'Bear', 'Moose']
pd.Series(animals)

numbers = [1, 2, 3]
pd.Series(numbers)

animals = ['Tiger', 'Bear', None]
pd.Series(numbers)

numbers = [1, 2, None]
pd.Series(numbers)

import numpy as np
np.nan == None

np.nan == np.nan

np.isnan(np.nan)

sports = {'Archery': 'Bhutan',
         'Golf': 'Scotland',
         'Sumo': 'Japan',
         'Taekwondo': 'South Korea'}
s = pd.Series(sports)
print(s)
print(s.index)

s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
print(s)
print(s.index)

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
print(s)

# Querying a Series

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s

s.iloc[3] # returns South Korea

s.loc['Golf'] # returns Scotland

s[3] #returns South Korea

s['Golf'] # returns Scotland
