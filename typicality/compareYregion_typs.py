import pandas as pd
import numpy as np
from scipy.stats import sem
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols



df2 = pd.read_csv('typicality\persubj_discourageTyps_percat.csv')
df1 = pd.read_csv('typicality\persubj_encourageTyps_percat.csv')
df3 = pd.read_csv('typicality\persubj_neutralTyps_percat.csv')


##drop all the other categories from the data frame
for item in df1:
    df1 = df1.drop(index = df1[df1['category'] != 'y'].index)

for item in df2:
    df2 = df2.drop(index = df2[df2['category'] != 'y'].index)

for item in df3:
    df3 = df3.drop(index = df3[df3['category'] != 'y'].index)

#create lists to hold data
encourage_typs = []
discourage_typs = []
neutral_typs = []
#put all the data into lists
for item in df1['means']:
    encourage_typs.append(item)

for item in df2['means']:
    discourage_typs.append(item)

for item in df3['means']:
    neutral_typs.append(item)

#noramlize the data so that 0 is most typical A and 1 is most typical B
normencourage_typs= []
normdiscourage_typs=[]
normneutral_typs=[]

for item in encourage_typs:
    item = (item-0)/(13-0)
    normencourage_typs.append(item)
for item in discourage_typs:
    item = (item-0)/(13-0)
    normdiscourage_typs.append(item)

for item in neutral_typs:
    item = (item-0)/(13-0)
    normneutral_typs.append(item)


from scipy import stats
print(stats.ttest_ind(encourage_typs, discourage_typs))
print(stats.ttest_ind(encourage_typs, neutral_typs))

#get lists of the conditions
c1 = []
c2 = []
c3 = []
for item in df1['means']:
    c1.append(1)

for item in df2['means']:
    c2.append(2)

for item in df3['means']:
    c3.append(3)

#add all the lists together
condition = c1 + c2 + c3
typs = normencourage_typs + normdiscourage_typs + normneutral_typs 
#make lists into df
anova_df = pd.DataFrame({'condition': condition,'typicality':typs,})

# Ordinary Least Squares (OLS) model
model = ols('typicality ~ C(condition)', data=anova_df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

#GRAPH NOW
#get the means
c1Mean = np.mean(normencourage_typs)
c2Mean = np.mean(normdiscourage_typs)
c3Mean = np.mean(normneutral_typs)

#get standard error
c1err = sem(normencourage_typs)
c2err = sem(normdiscourage_typs)
c3err = sem(normneutral_typs)


conditions = ['encourage', 'discourage', 'neutral']
x_pos = np.arange(len(conditions))
typ = [c1Mean, c2Mean, c3Mean]
err = [c1err, c2err, c3err]

# Build the plot
fig, ax = plt.subplots()
plt.ylim(0,1)
ax.bar(x_pos, typ, yerr=err, align='center', color =['g', 'b', 'r'], alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Typicalty (0 is most typical A; 1 is most typical B)')
ax.set_xticks(x_pos)
ax.set_xticklabels(conditions)
ax.set_title('Typicality scores for the Y region')
ax.yaxis.grid(True)

# Save the figure
#plt.tight_layout()
plt.savefig('typicality\Y_regionTypBarPlot.png')

