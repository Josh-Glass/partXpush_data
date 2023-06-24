import pandas as pd

df1 = pd.read_csv('dataWrangling/c1typResults.csv')
df2 = pd.read_csv('dataWrangling/c2typResults.csv')
df3 = pd.read_csv('dataWrangling/c3typResults.csv')


means_df1 = df1.groupby(['category'], as_index= True)['response'].describe()
means_df1.to_csv( "C:/Users/apers/partXpush_data/typicality/encourageTyps_percat.csv", index=True, encoding='utf-8-sig')


means_df2 = df2.groupby(['category'], as_index= True)['response'].describe()
means_df2.to_csv( "C:/Users/apers/partXpush_data/typicality/discourageTyps_percat.csv", index=True, encoding='utf-8-sig')


means_df3 = df3.groupby(['category'], as_index= True)['response'].describe()
means_df3.to_csv( "C:/Users/apers/partXpush_data/typicality/neutralTyps_percat.csv", index=True, encoding='utf-8-sig')


