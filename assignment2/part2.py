import pandas as pd
census_df = pd.read_csv('./course1_downloads/census.csv')
census_df.head()
census_df.set_index(['STNAME', 'CTYNAME'])


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






def a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index)


def answer_eight():
