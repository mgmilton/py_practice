import pandas as pd
census_df = pd.read_csv('./course1_downloads/census.csv')
census_df.head()
census_df.set_index(['STNAME', 'CTYNAME'])

def answer_five():
    return census_df[(census_df['SUMLEV'] == 50)].groupby('STNAME')['COUNTY'].nunique().idxmax()




def answer_six():
    return census_df[(census_df['SUMLEV'] == 50)].groupby('STNAME')['CENSUS2010POP'].apply(
    lambda x: x.nlargest(3).sum()).nlargest(
    3).index.values.tolist()
