import pandas as pd
#get hit descriuptives per stim for trainining phase 1


df1 = pd.read_csv('C:/Users/apers/partXpush_data/dataWrangling/c1Results.csv')
df2 = pd.read_csv('C:/Users/apers/partXpush_data/dataWrangling/c2Results.csv')
df3 = pd.read_csv('C:/Users/apers/partXpush_data/dataWrangling/c3Results.csv')


#get cond 1 training phase means

df1['accuracy'] = df1['accuracy'].astype(str)
df1 = df1.replace('True', 1)
df1 = df1.replace('False', 0)
df1 = df1.drop(index = df1[df1['phase'] == 'subTestPhase'].index)
df1 = df1.drop(index = df1[df1['phase']== 'testPhase'].index)

means_df1 = df1.groupby(['block', 'id'], as_index= True)['accuracy'].describe()

#print(means_df1)

means_df1.to_csv( "C:/Users/apers/partXpush_data/Training/c1Train_perSubj.csv", index=True, encoding='utf-8-sig')


#get cond 2 training phase means

df2['accuracy'] = df2['accuracy'].astype(str)
df2 = df2.replace('True', 1)
df2 = df2.replace('False', 0)
df2 = df2.drop(index = df2[df2['phase'] == 'subTestPhase'].index)
df2 = df2.drop(index = df2[df2['phase']== 'testPhase'].index)

means_df2 = df2.groupby(['block', 'id'], as_index= True)['accuracy'].describe()

#print(means_df2)

means_df2.to_csv( "C:/Users/apers/partXpush_data/Training/c2Train_perSubj.csv", index=True, encoding='utf-8-sig')


#get cond 3 training phase means

df3['accuracy'] = df3['accuracy'].astype(str)
df3 = df3.replace('True', 1)
df3 = df3.replace('False', 0)
df3 = df3.drop(index = df3[df3['phase'] == 'subTestPhase'].index)
df3 = df3.drop(index = df3[df3['phase']== 'testPhase'].index)

means_df3 = df3.groupby(['block', 'id'], as_index= True)['accuracy'].describe()

#print(means_df3)

means_df3.to_csv( "C:/Users/apers/partXpush_data/Training/c3Train_perSubj.csv", index=True, encoding='utf-8-sig')











