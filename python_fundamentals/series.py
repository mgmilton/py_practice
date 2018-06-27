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

s[0] #This won't call s.iloc[0] as one might expect, it generates an error instead

s = pd.Series([100.00, 120.00, 101.00, 3.00])
s

total = 0
for item in s:
    total += item
print(total)

#using vectorization

total = np.sum(s)
print(total)


#this creates a big series of random numbers
s = pd.Series(np.random.randint(0,1000,10000))
s.head()
len(s)

summary = 0
for item in s:
    summary+=item

summary = np.sum(s)

s+=2
s.head()

for label, value in s.iteritems():
    s.set_value(label, value+2)
print(s.head())

s = pd.Series(np.random.randint(0,1000,10000))
for label, value in s.iteritems():
    s.loc[label] = value +2

#faster with vectorization
s = pd.Series(np.random.randint(0,1000,10000))
s+=2

original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'],
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)

print(original_sports)
print(cricket_loving_countries)
print(all_countries)
print(all_countries.loc['Cricket'])
