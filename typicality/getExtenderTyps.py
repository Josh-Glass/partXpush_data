import pandas as pd


df1 = pd.read_csv('dataWrangling/c1typResults.csv')
df2 = pd.read_csv('dataWrangling/c2typResults.csv')
df3 = pd.read_csv('dataWrangling/c3typResults.csv')


subc1 = [
    11214, 
    #11263
]
subc2 = [
    #11189,
    #11211,
    11268,
    11272,
    11278,
    11284
]
subc3 = [
    11221,
    11240,
    11293,
    11318,
    11308
    ]

means_df1 = df1.groupby(['id','category'], as_index= True)['response'].describe()
means_df1.to_csv( "C:/Users/apers/partXpush_data/typicality/persubj_encourageTyps_percat.csv", index=True, encoding='utf-8-sig')


means_df2 = df2.groupby(['id','category'], as_index= True)['response'].describe()
means_df2.to_csv( "C:/Users/apers/partXpush_data/typicality/persubj_discourageTyps_percat.csv", index=True, encoding='utf-8-sig')


means_df3 = df3.groupby(['id','category'], as_index= True)['response'].describe()
means_df3.to_csv( "C:/Users/apers/partXpush_data/typicality/persubj_neutralTyps_percat.csv", index=True, encoding='utf-8-sig')


