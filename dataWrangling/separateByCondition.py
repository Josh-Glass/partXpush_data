import pandas as pd
from IPython.display import display
from csv import writer
import numpy as np

df = pd.read_csv('dataWrangling/Results_metCrit.csv')

#display(df.head(5))


#get condition 1 pnums
cond1_pnums = []
cond1_filter = np.where(df['condition']== 1, df['id'], 0)
cond1_filter_collected = np.unique(cond1_filter)

#print(cond1_filter_collected)

df_cond1_filter_collected = pd.DataFrame(cond1_filter_collected, columns = ['pnums'])
#print(df_cond1_filter_collected)
df_cond1_filter_collected = df_cond1_filter_collected.drop(index= 0)
#print(df_cond1_filter_collected)

for subjects in df_cond1_filter_collected['pnums'].unique():
    cond1_pnums.append(subjects)

print('encourage pnums:')
print(len(cond1_pnums))




#get condition 2 pnums
cond2_pnums = []
cond2_filter = np.where(df['condition']== 2, df['id'], 0)
cond2_filter_collected = np.unique(cond2_filter)

#print(cond2_filter_collected)

df_cond2_filter_collected = pd.DataFrame(cond2_filter_collected, columns = ['pnums'])
#print(df_cond2_filter_collected)
df_cond2_filter_collected = df_cond2_filter_collected.drop(index= 0)
#print(df_cond2_filter_collected)

for subjects in df_cond2_filter_collected['pnums'].unique():
    cond2_pnums.append(subjects)

print('discourage pnums')
print(len(cond2_pnums))






#get condition 3 pnums
cond3_pnums = []
cond3_filter = np.where(df['condition']== 3, df['id'], 0)
cond3_filter_collected = np.unique(cond3_filter)

#print(cond3_filter_collected)

df_cond3_filter_collected = pd.DataFrame(cond3_filter_collected, columns = ['pnums'])
#print(df_cond3_filter_collected)
df_cond3_filter_collected = df_cond3_filter_collected.drop(index= 0)
#print(df_cond3_filter_collected)

for subjects in df_cond3_filter_collected['pnums'].unique():
    cond3_pnums.append(subjects)

print('neutral pnums')
print(len(cond3_pnums))


#make a cond1_df by dropping cond2 and cond3 pnums
#this loop drops cond2_pnums
cond1_df = df
for item in cond2_pnums:
    cond1_df = cond1_df.drop(index = cond1_df[cond1_df['id'] == item].index)
    
#this loop drops cond3_pnums
for item in cond3_pnums:
    cond1_df = cond1_df.drop(index = cond1_df[cond1_df['id'] == item].index)
    
#save cond1_df as a csv    
#cond1_df.to_csv( "c1Results.csv", index=False, encoding='utf-8-sig')
        



#make a cond2_df by dropping cond1 and cond3 pnums
#this loop drops cond1_pnums
cond2_df = df
for item in cond1_pnums:
    cond2_df = cond2_df.drop(index = cond2_df[cond2_df['id'] == item].index)
    
#this loop drops cond3_pnums
for item in cond3_pnums:
    cond2_df = cond2_df.drop(index = cond2_df[cond2_df['id'] == item].index)
    
#save cond2_df as a csv    
#cond2_df.to_csv( "c2Results.csv", index=False, encoding='utf-8-sig')






#make a cond3_df by dropping cond1 and cond2 pnums
#this loop drops cond1_pnums
cond3_df = df
for item in cond1_pnums:
    cond3_df = cond3_df.drop(index = cond3_df[cond3_df['id'] == item].index)
    
#this loop drops cond2_pnums
for item in cond2_pnums:
    cond3_df = cond3_df.drop(index = cond3_df[cond3_df['id'] == item].index)
    
#save cond3_df as a csv    
#cond3_df.to_csv( "c3Results.csv", index=False, encoding='utf-8-sig')

#print(cond3_df)
