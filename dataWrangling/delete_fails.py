import pandas as pd
from IPython.display import display
from csv import writer

df = pd.read_csv('results.csv')
df2 = pd.read_csv('typResults.csv')

df = df.replace('True', 1)
df = df.replace('False', 0)

df['accuracy'] = df['accuracy'].astype(bool)
display(df.head(10))



failed_pnums = []
'''for item in df.groupby(['id','phase']):
    if item[0][1] == 'trainPhase':
       
        if item[1].sum()['accuracy'] == 0  and item[0][0] not in failed_pnums:
            failed_pnums.append(item[0][0])


            #df = df[df['pnum'] != item[1]['pnum']]'''


for subject in df['id'].unique():
    #print(subject, df[(df['id'] == subject) & (df['phase'] == 'trainPhase')]['accuracy'][-15:])
    
    acc = df[(df['id'] == subject) & (df['phase'] == 'trainPhase')]['accuracy'][-15:].sum()
    print(subject, acc)
    if acc != 15:
        failed_pnums.append(subject)
print(failed_pnums)


for item in failed_pnums:
    #if df[item]['pnum'] in failed_pnums:
    df = df.drop(index = df[df['id'] == item].index)
    df2 = df2.drop(index = df2[df2['id'] == item].index)
    

    #print(df[df['pnum'] == item].index)


print('number of subjects who failed')
print(len(failed_pnums))

df.to_csv( "Results_metCrit.csv", index=False, encoding='utf-8-sig')
df2.to_csv( "typResults_metCrit.csv", index=False, encoding='utf-8-sig')
        





