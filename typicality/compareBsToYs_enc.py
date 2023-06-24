import pandas as pd
import numpy as np
from scipy.stats import sem
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols



df_B = pd.read_csv('typicality\persubj_encourageTyps_percat.csv')
df_Y = pd.read_csv('typicality\persubj_encourageTyps_percat.csv')


##drop all the other categories from the data frame
for item in df_B:
    df_B = df_B.drop(index = df_B[df_B['category'] != 'b'].index)

for item in df_Y:
    df_Y = df_Y.drop(index = df_Y[df_Y['category'] != 'y'].index)



#create lists to hold data
B_typs = []
Y_typs = []

#put all the data into lists
for item in df_B['means']:
    B_typs.append(item)

for item in df_Y['means']:
    Y_typs.append(item)


#noramlize the data so that 0 is most typical A and 1 is most typical B
normB_typs= []
normY_typs=[]


for item in B_typs:
    item = (item-0)/(13-0)
    normB_typs.append(item)
for item in Y_typs:
    item = (item-0)/(13-0)
    normY_typs.append(item)




from scipy import stats
print(stats.ttest_ind(B_typs, Y_typs))




#GRAPH NOW
#get the means
c1Mean = np.mean(normB_typs)
c2Mean = np.mean(normY_typs)

#get standard error
c1err = sem(normB_typs)
c2err = sem(normY_typs)


conditions = ['Trained B items', 'No-feedback Y items']
x_pos = np.arange(len(conditions))
typ = [c1Mean, c2Mean]
err = [c1err, c2err]

# Build the plot
fig, ax = plt.subplots()
plt.ylim(0,1)
ax.bar(x_pos, typ, yerr=err, align='center', color =['g', 'b', 'r'], alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Typicalty (0 is most typical A; 1 is most typical B)')
ax.set_xticks(x_pos)
ax.set_xticklabels(conditions)
ax.set_title('Encourage: typicality for trained items vs. extreme valued test items')
ax.yaxis.grid(True)
plt.axhline(y = 0.5, color = 'r', linestyle = '-')

# Save the figure
#plt.tight_layout()
plt.savefig('typicality\YvsBTypBarPlot_enc.png')

