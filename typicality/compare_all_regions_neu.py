import pandas as pd
import numpy as np
from scipy.stats import sem
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols



df_a = pd.read_csv('typicality\persubj_neutralTyps_percat.csv')
df_b = pd.read_csv('typicality\persubj_neutralTyps_percat.csv')
df_w = pd.read_csv('typicality\persubj_neutralTyps_percat.csv')
df_x = pd.read_csv('typicality\persubj_neutralTyps_percat.csv')
df_y = pd.read_csv('typicality\persubj_neutralTyps_percat.csv')
df_z = pd.read_csv('typicality\persubj_neutralTyps_percat.csv')


##drop all the other categories from the data frame
for item in df_a:
    df_a = df_a.drop(index = df_a[df_a['category'] != 'a'].index)

for item in df_b:
    df_b = df_b.drop(index = df_b[df_b['category'] != 'b'].index)

for item in df_w:
    df_w = df_w.drop(index = df_w[df_w['category'] != 'w'].index)
for item in df_x:
    df_x = df_x.drop(index = df_x[df_x['category'] != 'x'].index)
for item in df_y:
    df_y = df_y.drop(index = df_y[df_y['category'] != 'y'].index)
for item in df_w:
    df_w = df_w.drop(index = df_w[df_w['category'] != 'w'].index)
    
#create lists to hold data
a_typs = []
b_typs = []
w_typs = []
x_typs = []
y_typs = []
z_typs = []

#put all the data into lists
for item in df_a['means']:
    a_typs.append(item)

for item in df_b['means']:
    b_typs.append(item)

for item in df_w['means']:
    w_typs.append(item)

for item in df_x['means']:
    x_typs.append(item)

for item in df_y['means']:
    y_typs.append(item)

for item in df_z['means']:
    z_typs.append(item)

#noramlize the data so that 0 is most typical A and 1 is most typical B
norma_typs= []
normb_typs=[]
normw_typs=[]
normx_typs = []
normy_typs = []
normz_typs = []
for item in a_typs:
    item = (item-0)/(13-0)
    norma_typs.append(item)

for item in b_typs:
    item = (item-0)/(13-0)
    normb_typs.append(item)

for item in w_typs:
    item = (item-0)/(13-0)
    normw_typs.append(item)

for item in x_typs:
    item = (item-0)/(13-0)
    normx_typs.append(item)

for item in y_typs:
    item = (item-0)/(13-0)
    normy_typs.append(item)

for item in z_typs:
    item = (item-0)/(13-0)
    normz_typs.append(item)





from scipy import stats
print(stats.ttest_ind(a_typs, b_typs))
print(stats.ttest_ind(a_typs, w_typs))

#get lists of the conditions
a = []
b = []
w = []
x = []
y = []
z = []


for item in df_a['means']:
    a.append('a')

for item in df_b['means']:
    b.append('b')

for item in df_w['means']:
    w.append('w')

for item in df_x['means']:
    x.append('x')

for item in df_y['means']:
    y.append('y')

for item in df_z['means']:
    z.append('z')

#add all the lists together
region = a + b + w + x + y + z
typs = norma_typs + normb_typs + normw_typs + normx_typs + normy_typs + normz_typs 
#make lists into df
anova_df = pd.DataFrame({'region': region,'typicality':typs})

# Ordinary Least Squares (OLS) model
model = ols('typicality ~ C(region)', data=anova_df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

#GRAPH NOW
#get the means
c1Mean = np.mean(norma_typs)
c2Mean = np.mean(normb_typs)
c3Mean = np.mean(normw_typs)
c4Mean = np.mean(normx_typs)
c5Mean = np.mean(normy_typs)
c6Mean = np.mean(normz_typs)


#get standard error
c1err = sem(norma_typs)
c2err = sem(normb_typs)
c3err = sem(normw_typs)
c4err = sem(normx_typs)
c5err = sem(normy_typs)
c6err = sem(normz_typs)


regions = ['A', 'B', 'W', 'X', 'Y', 'Z']
x_pos = np.arange(len(regions))
typ = [c1Mean, c2Mean, c3Mean, c4Mean, c5Mean, c6Mean]
err = [c1err, c2err, c3err, c4err, c5err, c6err]

# Build the plot
fig, ax = plt.subplots()
plt.ylim(0,1)
ax.bar(x_pos, typ, yerr=err, align='center', color =['g', 'b', 'r'], alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Typicalty (0 is most typical A; 1 is most typical B)')
ax.set_xticks(x_pos)
ax.set_xticklabels(regions)
ax.set_title('Neutral: Typicality scores per region')
ax.yaxis.grid(True)

# Save the figure
#plt.tight_layout()
plt.savefig('typicality/per_Region_Typ_neu.png')

