import pandas as pd
census_df = pd.read_csv('./course1_downloads/census.csv')
census_df.head()


#Question 5

# Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)
#
# This function should return a single string value.

def answer_five():
    return census_df[(census_df['SUMLEV'] == 50)].groupby('STNAME')['COUNTY'].nunique().idxmax()


# Question 6
# Only looking at the three most populous counties for each state, what are the three most populous states (in order of highest population to lowest population)? Use CENSUS2010POP.
#
# This function should return a list of string values.

def answer_six():
    return census_df[(census_df['SUMLEV'] == 50)].groupby('STNAME')['CENSUS2010POP'].apply(
    lambda x: x.nlargest(3).sum()).nlargest(
    3).index.values.tolist()



# Question 7
# Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
#
# e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.
#
# This function should return a single string value.

def answer_seven():
