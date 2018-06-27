import pandas as pd

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

df.head()
df.loc['Store 2']
type(df.loc['Store 2'])
df.loc['Store 1']
df.loc['Store 1', 'Cost']
df.T
df.T.loc['Cost']
df['Cost']
df.loc['Store 1']['Cost']

# to query by column name
df.loc[:,['Name', 'Cost']]


# Dataframe Indexing and Loading

costs = df['Cost']

costs += 2
costs

df = pd.read_csv('./course1_downloads/olympics.csv', index_col=0, skiprows=1)
df.head()
df.columns

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True)

df.head()


# Querying a DataFrame

df['Gold'] > 0 # returns all Countries with boolean if the country has won a gold medal

only_gold = df.where(df['Gold'] > 0)
only_gold.head()

only_gold['Gold'].count()
df['Gold'].count()
only_gold = only_gold.dropna()
only_gold.head()

only_gold = df[df['Gold'] > 0]
only_gold.head()

print(len(df[(df['Gold'] > 0) | (df['Gold.1'] > 0)]))
print(len(df[(df['Gold.1'] > 0) | (df['Gold'] == 0)]))
