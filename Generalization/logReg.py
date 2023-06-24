import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
from statsmodels.formula.api import ols
import scipy.stats as stats
import numpy as np
from scipy.stats import sem
import matplotlib.pyplot as plt


subdf1 = pd.read_csv('C:/Users/apers/partXpush_data/dataWrangling/c1Results.csv')
subdf2 = pd.read_csv('C:/Users/apers/partXpush_data/dataWrangling/c2Results.csv')
subdf3 = pd.read_csv('C:/Users/apers/partXpush_data/dataWrangling/c3Results.csv')

df1 = pd.read_csv('C:/Users/apers/partXpush_data/dataWrangling/c1Results.csv')
df2 = pd.read_csv('C:/Users/apers/partXpush_data/dataWrangling/c2Results.csv')
df3 = pd.read_csv('C:/Users/apers/partXpush_data/dataWrangling/c3Results.csv')


c1Ext = pd.read_csv('C:/Users/apers/partXpush_data/Generalization/c1groupby_extenders.csv')
c2Ext = pd.read_csv('C:/Users/apers/partXpush_data/Generalization/c2groupby_extenders.csv')
c3Ext = pd.read_csv('C:/Users/apers/partXpush_data/Generalization/c3groupby_extenders.csv')

subc1Ext = pd.read_csv('C:/Users/apers/partXpush_data/Generalization/subc1groupby_extenders.csv')
subc2Ext = pd.read_csv('C:/Users/apers/partXpush_data/Generalization/subc2groupby_extenders.csv')
subc3Ext = pd.read_csv('C:/Users/apers/partXpush_data/Generalization/subc3groupby_extenders.csv')


#create empy lists to fill with extender pnums later
subc1 = []
subc2 = []
subc3 = []
c1 = []
c2 = []
c3 = []

#fill the lists with the extenders here
##encourage cond (c1)
for item in subc1Ext['id']:
    subc1Ext = subc1Ext.drop(index = subc1Ext[subc1Ext['count'] < 6].index) ##getting rid of anybody who endorsed less than 6 items as the reduced cat

for subject in subc1Ext['id']:
    subc1.append(subject)##append the subjects to the list



##discourage cond (c2)
for item in subc2Ext['id']:
    subc2Ext = subc2Ext.drop(index = subc2Ext[subc2Ext['count'] < 6].index) ##getting rid of anybody who endorsed less than 6 items as the reduced cat

for subject in subc2Ext['id']:
    subc2.append(subject)##append the subjects to the list



##neutral cond (c3)
for item in subc3Ext['id']:
    subc3Ext = subc3Ext.drop(index = subc3Ext[subc3Ext['count'] < 6].index) ##getting rid of anybody who endorsed less than 6 items as the reduced cat

for subject in subc3Ext['id']:
    subc3.append(subject)##append the subjects to the list





###that was the subtest phase extenders now do the same thing with the test phase extenders
#####subtest is what matters, but might as well check what's going on in the test phase as well

##encourage cond (c1)
for item in c1Ext['id']:
    c1Ext = c1Ext.drop(index = c1Ext[c1Ext['count'] < 6].index) ##getting rid of anybody who endorsed less than 6 items as the reduced cat

for subject in c1Ext['id']:
    c1.append(subject)##append the subjects to the list




##discourage cond (c2)
for item in c2Ext['id']:
    c2Ext = c2Ext.drop(index = c2Ext[c2Ext['count'] < 6].index) ##getting rid of anybody who endorsed less than 6 items as the reduced cat

for subject in c2Ext['id']:
    c2.append(subject)##append the subjects to the list



##neutral cond (c3)
for item in c3Ext['id']:
    c3Ext = c3Ext.drop(index = c3Ext[c3Ext['count'] < 6].index) ##getting rid of anybody who endorsed less than 6 items as the reduced cat

for subject in c3Ext['id']:
    c3.append(subject)##append the subjects to the list



#make lists to store the DVs in (1 if they extended 0 if they didnt)
##heres the subtest extender lists
subc1DV = []
subc2DV = []
subc3DV = []

#heres the test phase extender lists
c1DV = []
c2DV = []
c3DV = []


#make list for the IVs (these will be the same for subtest and test phase, so theres only one set of these)
c1IV = []
c2IV = []
c3IV = []




###dummy code subjects for the condition that they were (THIS IS THE IV)
######for each subject if they belong to the condition they are a 1 if not they are a 0
##########add the dummy coded value to the list for that condition
#get IV dummy code for cond 1
for i in df1['id'].unique():
    c1IV.append(1)

for i in df2['id'].unique():
    c1IV.append(0)

for i in df3['id'].unique():
    c1IV.append(0)


#get IV dummy code for cond 2
for i in df1['id'].unique():
    c2IV.append(0)

for i in df2['id'].unique():
    c2IV.append(1)

for i in df3['id'].unique():
    c2IV.append(0)



#get IV dummy code for cond 3
for i in df1['id'].unique():
    c3IV.append(0)

for i in df2['id'].unique():
    c3IV.append(0)

for i in df3['id'].unique():
    c3IV.append(1)






##make new dfs that have all the extenders removed, so they are not duplicates
###here I'm doing it for the sub test phase
for item in subc1:
    subdf1 = subdf1.drop(index = subdf1[subdf1['id'] == item].index)

for item in subc2:
    subdf2 = subdf2.drop(index = subdf2[subdf2['id'] == item].index)

for item in subc3:
    subdf3 = subdf3.drop(index = subdf3[subdf3['id'] == item].index)



#get dvs for cond 1
for i in subc1:
    subc1DV.append(1)

for i in subdf1['id'].unique():
    subc1DV.append(0)





#get dvs for cond 2
for i in subc2:
    subc2DV.append(1)

for i in subdf2['id'].unique():
    subc2DV.append(0)



#get dvs for cond 3
for i in subc3:
    subc3DV.append(1)

for i in subdf3['id'].unique():
    subc3DV.append(0)



subextended = subc1DV + subc2DV + subc3DV
#print(extended)
#print(len(subextended))

###do the same thing for the test phase

for item in c1:
    df1 = df1.drop(index = df1[df1['id'] == item].index)

for item in c2:
    df2 = df2.drop(index = df2[df2['id'] == item].index)

for item in c3:
    df3 = df3.drop(index = df3[df3['id'] == item].index)



#get dvs for cond 1
for i in c1:
    c1DV.append(1)

for i in df1['id'].unique():
    c1DV.append(0)





#get dvs for cond 2
for i in c2:
    c2DV.append(1)

for i in df2['id'].unique():
    c2DV.append(0)



#get dvs for cond 3
for i in c3:
    c3DV.append(1)

for i in df3['id'].unique():
    c3DV.append(0)



extended = c1DV + c2DV + c3DV




#make a df for the subtest data
sublogReg_df = pd.DataFrame({'extended': subextended,'encourage':c1IV,  'discourage': c2IV, 'neutral': c3IV,})

#do a logistic regression on the subtest data
sublogmodel = smf.logit('extended ~ encourage + discourage + neutral', data=sublogReg_df).fit()

print(sublogmodel.summary())


##Now do the same thing fo rthe tes phase data
logReg_df = pd.DataFrame({'extended': extended,'encourage':c1IV,  'discourage': c2IV, 'neutral': c3IV,})
logmodel = smf.logit('extended ~ encourage + discourage + neutral', data=logReg_df).fit()
print(logmodel.summary())






'''
olsmodel = ols('extended ~ encourage  + discourage + neutral', data=logReg_df).fit()
anovaTable = sm.stats.anova_lm(olsmodel, typ=1)

print(anovaTable)

print(stats.ttest_ind(c1DV, c2DV))
print(stats.ttest_ind(c1DV, c3DV))
print(stats.ttest_ind(c2DV, c3DV))

'''


#get means and standard errors for the DV in the subtest phase for all conditions



subc1DV_mean = np.mean(subc1DV)
subc1DV_err = sem(subc1DV)


subc2DV_mean = np.mean(subc2DV)
subc2DV_err = sem(subc2DV)


subc3DV_mean = np.mean(subc3DV)
subc3DV_err = sem(subc3DV)



conditions = ['encourage', 'neutral', 'discourage']
x_pos = np.arange(len(conditions))
subaccuracy = [subc1DV_mean, subc3DV_mean, subc2DV_mean]
suberror = [subc1DV_err, subc3DV_err, subc2DV_err]

# Build the plot
fig, ax = plt.subplots()
plt.ylim(0,1)
ax.bar(x_pos, subaccuracy, yerr=suberror, align='center', color =['g', 'b', 'r'], alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('proportion of subjects who were extenders')
ax.set_xticks(x_pos)
ax.set_xticklabels(conditions)
ax.set_title('Extension of the reduced category during generalization')
ax.yaxis.grid(True)

# Save the figure
#plt.tight_layout()
plt.savefig('C:/Users/apers/partXpush_data/Generalization/subExtendersBarPlot.png')












##Now do the same thing for the DV in the test phase

c1DV_mean = np.mean(c1DV)
c1DV_err = sem(c1DV)


c2DV_mean = np.mean(c2DV)
c2DV_err = sem(c2DV)


c3DV_mean = np.mean(c3DV)
c3DV_err = sem(c3DV)



conditions = ['encourage', 'neutral', 'discourage']
x_pos = np.arange(len(conditions))
accuracy = [c1DV_mean, c3DV_mean, c2DV_mean]
error = [c1DV_err, c3DV_err, c2DV_err]

# Build the plot
fig, ax = plt.subplots()
plt.ylim(0,1)
ax.bar(x_pos, accuracy, yerr=error, align='center', color =['g', 'b', 'r'], alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('proportion of subjects who were extenders')
ax.set_xticks(x_pos)
ax.set_xticklabels(conditions)
ax.set_title('Extension of the reduced category during generalization')
ax.yaxis.grid(True)

# Save the figure
#plt.tight_layout()
plt.savefig('C:/Users/apers/partXpush_data/Generalization/ExtendersBarPlot.png')

