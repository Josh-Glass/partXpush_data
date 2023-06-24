import pandas as pd



df = pd.read_csv('dataWrangling/c3typResults.csv')
#df = df.drop(index = df[df['category'] != 'y'].index)

group = df.groupby(['stimId'], as_index = True)['response'].describe()
print(group)

