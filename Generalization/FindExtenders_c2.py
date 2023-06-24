import pandas as pd
from IPython.display import display


df0 = pd.read_csv('C:/Users/apers/partXpush_data/dataWrangling/c2Results.csv')


#drop trainPhase and subTestPhase
for item in df0['id']:
    df = df0.drop(index = df0[df0['phase'] != 'testPhase'].index)

#drop responses that are not the reduced category
for item in df['id']:
    df = df.drop(index = df[df['response'] != 'b'].index)

#drop categories that are not x
for item in df['id']:
    df = df.drop(index = df[df['category'] != 'x'].index)

df = df.groupby(['id', 'category'], as_index = True)['response'].describe()
#display(df.head(15))
#print(df)

df.to_csv('C:/Users/apers/partXpush_data/Generalization/c2groupby_extenders.csv')