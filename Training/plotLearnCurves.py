import pandas as pd
import numpy as np
from scipy.stats import sem
import matplotlib.pyplot as plt



#make all of the dataframes that I'll need now
##these ones are to get the available data on mean hits
df1 = pd.read_csv('Training/c1Train_perSubj.csv')
df2 = pd.read_csv('Training/c2Train_perSubj.csv')
df3 = pd.read_csv('Training/c3Train_perSubj.csv')

e_df1 = pd.read_csv('Training/c1Train_perSubj.csv')
e_df2 = pd.read_csv('Training/c2Train_perSubj.csv')
e_df3 = pd.read_csv('Training/c3Train_perSubj.csv')

#these ones are to get the list of pnums that extended the reduced category
ext1 = pd.read_csv('Generalization/subc1groupby_extenders.csv')
ext2 = pd.read_csv('Generalization/subc2groupby_extenders.csv')
ext3 = pd.read_csv('Generalization/subc3groupby_extenders.csv')


#put all the extenders into lists so that I can use them to manipulate the data frames
extenders_1 = []
extenders_2 = []
extenders_3 = []
#fill the lists with the extenders here
##encourage cond (c1)
for item in ext1['id']:
    ext1 = ext1.drop(index = ext1[ext1['count'] < 6].index) ##getting rid of anybody who endorsed less than 6 items as the reduced cat

for subject in ext1['id']:
    extenders_1.append(subject)##append the subjects to the list



##discourage cond (c2)
for item in ext2['id']:
    ext2 = ext2.drop(index = ext2[ext2['count'] < 6].index) ##getting rid of anybody who endorsed less than 6 items as the reduced cat

for subject in ext2['id']:
    extenders_2.append(subject)##append the subjects to the list



##neutral cond (c3)
for item in ext3['id']:
    ext3 = ext3.drop(index = ext3[ext3['count'] < 6].index) ##getting rid of anybody who endorsed less than 6 items as the reduced cat

for subject in ext3['id']:
    extenders_3.append(subject)##append the subjects to the list


#make lists to hold all the data in
#here's the lists for non extenders
###cond 1
c1Block1 = []
c1Block2 = []
c1Block3 = []
c1Block4 = []
c1Block5 = []
c1Block6 = []
c1Block7 = []
c1Block8 = []
c1Block9 = []
c1Block10 = []
###cond2
c2Block1 = []
c2Block2 = []
c2Block3 = []
c2Block4 = []
c2Block5 = []
c2Block6 = []
c2Block7 = []
c2Block8 = []
c2Block9 = []
c2Block10 = []
###cond 3
c3Block1 = []
c3Block2 = []
c3Block3 = []
c3Block4 = []
c3Block5 = []
c3Block6 = []
c3Block7 = []
c3Block8 = []
c3Block9 = []
c3Block10 = []
##Here's the lists for the extenders
###cond 1
e_c1Block1 = []
e_c1Block2 = []
e_c1Block3 = []
e_c1Block4 = []
e_c1Block5 = []
e_c1Block6 = []
e_c1Block7 = []
e_c1Block8 = []
e_c1Block9 = []
e_c1Block10 = []
###cond 2
e_c2Block1 = []
e_c2Block2 = []
e_c2Block3 = []
e_c2Block4 = []
e_c2Block5 = []
e_c2Block6 = []
e_c2Block7 = []
e_c2Block8 = []
e_c2Block9 = []
e_c2Block10 = []
###cond 3
e_c3Block1 = []
e_c3Block2 = []
e_c3Block3 = []
e_c3Block4 = []
e_c3Block5 = []
e_c3Block6 = []
e_c3Block7 = []
e_c3Block8 = []
e_c3Block9 = []
e_c3Block10 = []




#drop the extenders from the non extenders data frame
for item in extenders_1:
    df1 = df1.drop(index = df1[df1['id'] == item].index)

for item in extenders_2:
    df2 = df2.drop(index = df2[df2['id'] == item].index)

for item in extenders_3:
    df3 = df3.drop(index = df3[df3['id'] == item].index)


#now put all the non extenders into lists so I can drop them form the extenders dataframes
##create lists to put them in
non_e1 = []
non_e2 = []
non_e3 = []
###now add pnums to these lists
for subject in df1['id']:
    non_e1.append(subject)##append the subjects to the list
for subject in df2['id']:
    non_e2.append(subject)##append the subjects to the list
for subject in df3['id']:
    non_e3.append(subject)##append the subjects to the list

#Now drop all the nonextenders form the extenders dataframes
for item in non_e1:
    e_df1 = e_df1.drop(index = e_df1[e_df1['id'] == item].index)

for item in non_e2:
    e_df2 = e_df2.drop(index = e_df2[e_df2['id'] == item].index)

for item in non_e3:
   e_df3 = e_df3.drop(index = e_df3[e_df3['id'] == item].index)




############################################################################################################################################
############################################################################################################################################
#Now adding available block data to appropriate lists

##start with non-extenders
###condition 1
#Block 1
for i, row in df1.iterrows():
    if row.block == 1:
        c1Block1.append(row.means)
#Block 2
for i, row in df1.iterrows():
    if row.block == 2:
        c1Block2.append(row.means)
#Block 3
for i, row in df1.iterrows():
    if row.block == 3:
        c1Block3.append(row.means)
#Block 4
for i, row in df1.iterrows():
    if row.block == 4:
        c1Block4.append(row.means)
#Block 5
for i, row in df1.iterrows():
    if row.block == 5:
        c1Block5.append(row.means)
#Block 6
for i, row in df1.iterrows():
    if row.block == 6:
        c1Block6.append(row.means)
#Block 7
for i, row in df1.iterrows():
    if row.block == 7:
        c1Block7.append(row.means)
#Block 8
for i, row in df1.iterrows():
    if row.block == 8:
        c1Block8.append(row.means)
#Block 9
for i, row in df1.iterrows():
    if row.block == 9:
        c1Block9.append(row.means)
#Block 10
for i, row in df1.iterrows():
    if row.block == 10:
        c1Block10.append(row.means)




###condition 2


for i, row in df2.iterrows():
    if row.block == 1:
        c2Block1.append(row.means)
#Block 2
for i, row in df2.iterrows():
    if row.block == 2:
        c2Block2.append(row.means)
#Block 3
for i, row in df2.iterrows():
    if row.block == 3:
        c2Block3.append(row.means)
#Block 4
for i, row in df2.iterrows():
    if row.block == 4:
        c2Block4.append(row.means)
#Block 5
for i, row in df2.iterrows():
    if row.block == 5:
        c2Block5.append(row.means)
#Block 6
for i, row in df2.iterrows():
    if row.block == 6:
        c2Block6.append(row.means)
#Block 7
for i, row in df2.iterrows():
    if row.block == 7:
        c2Block7.append(row.means)
#Block 8
for i, row in df2.iterrows():
    if row.block == 8:
        c2Block8.append(row.means)
#Block 9
for i, row in df2.iterrows():
    if row.block == 9:
        c2Block9.append(row.means)
#Block 10
for i, row in df2.iterrows():
    if row.block == 10:
        c2Block10.append(row.means)




###condition 3

for i, row in df3.iterrows():
    if row.block == 1:
        c3Block1.append(row.means)
#Block 2
for i, row in df3.iterrows():
    if row.block == 2:
        c3Block2.append(row.means)
#Block 3
for i, row in df3.iterrows():
    if row.block == 3:
        c3Block3.append(row.means)
#Block 4
for i, row in df3.iterrows():
    if row.block == 4:
        c3Block4.append(row.means)
#Block 5
for i, row in df3.iterrows():
    if row.block == 5:
        c3Block5.append(row.means)
#Block 6
for i, row in df3.iterrows():
    if row.block == 6:
        c3Block6.append(row.means)
#Block 7
for i, row in df3.iterrows():
    if row.block == 7:
        c3Block7.append(row.means)
#Block 8
for i, row in df3.iterrows():
    if row.block == 8:
        c3Block8.append(row.means)
#Block 9
for i, row in df3.iterrows():
    if row.block == 9:
        c3Block9.append(row.means)
#Block 10
for i, row in df3.iterrows():
    if row.block == 10:
        c3Block10.append(row.means)





###########################################################################################################################################################
##Now do the extenders

###condition 1

for i, row in e_df1.iterrows():
    if row.block == 1:
        e_c1Block1.append(row.means)
#Block 2
for i, row in e_df1.iterrows():
    if row.block == 2:
        e_c1Block2.append(row.means)
#Block 3
for i, row in e_df1.iterrows():
    if row.block == 3:
        e_c1Block3.append(row.means)
#Block 4
for i, row in e_df1.iterrows():
    if row.block == 4:
        e_c1Block4.append(row.means)
#Block 5
for i, row in e_df1.iterrows():
    if row.block == 5:
        e_c1Block5.append(row.means)
#Block 6
for i, row in e_df1.iterrows():
    if row.block == 6:
        e_c1Block6.append(row.means)
#Block 7
for i, row in e_df1.iterrows():
    if row.block == 7:
        e_c1Block7.append(row.means)
#Block 8
for i, row in e_df1.iterrows():
    if row.block == 8:
        e_c1Block8.append(row.means)
#Block 9
for i, row in e_df1.iterrows():
    if row.block == 9:
        e_c1Block9.append(row.means)
#Block 10
for i, row in e_df1.iterrows():
    if row.block == 10:
        e_c1Block10.append(row.means)




###condition 2

for i, row in e_df2.iterrows():
    if row.block == 1:
        e_c2Block1.append(row.means)
#Block 2
for i, row in e_df2.iterrows():
    if row.block == 2:
        e_c2Block2.append(row.means)
#Block 3
for i, row in e_df2.iterrows():
    if row.block == 3:
        e_c2Block3.append(row.means)
#Block 4
for i, row in e_df2.iterrows():
    if row.block == 4:
        e_c2Block4.append(row.means)
#Block 5
for i, row in e_df2.iterrows():
    if row.block == 5:
        e_c2Block5.append(row.means)
#Block 6
for i, row in e_df2.iterrows():
    if row.block == 6:
        e_c2Block6.append(row.means)
#Block 7
for i, row in e_df2.iterrows():
    if row.block == 7:
        e_c2Block7.append(row.means)
#Block 8
for i, row in e_df2.iterrows():
    if row.block == 8:
        e_c2Block8.append(row.means)
#Block 9
for i, row in e_df2.iterrows():
    if row.block == 9:
        e_c2Block9.append(row.means)
#Block 10
for i, row in e_df2.iterrows():
    if row.block == 10:
        e_c2Block10.append(row.means)



###condition 2
for i, row in e_df3.iterrows():
    if row.block == 1:
        e_c3Block1.append(row.means)
#Block 2
for i, row in e_df3.iterrows():
    if row.block == 2:
        e_c3Block2.append(row.means)
#Block 3
for i, row in e_df3.iterrows():
    if row.block == 3:
        e_c3Block3.append(row.means)
#Block 4
for i, row in e_df3.iterrows():
    if row.block == 4:
        e_c3Block4.append(row.means)
#Block 5
for i, row in e_df3.iterrows():
    if row.block == 5:
        e_c3Block5.append(row.means)
#Block 6
for i, row in e_df3.iterrows():
    if row.block == 6:
        e_c3Block6.append(row.means)
#Block 7
for i, row in e_df3.iterrows():
    if row.block == 7:
        e_c3Block7.append(row.means)
#Block 8
for i, row in e_df3.iterrows():
    if row.block == 8:
        e_c3Block8.append(row.means)
#Block 9
for i, row in e_df3.iterrows():
    if row.block == 9:
        e_c3Block9.append(row.means)
#Block 10
for i, row in e_df3.iterrows():
    if row.block == 10:
        e_c3Block10.append(row.means)

##################################################################################################################################################

#get the sample sizes for each condition for extenders and non-extenders
n_c1 = len(non_e1)
n_c2 = len(non_e2)
n_c3 = len(non_e3)

n_ec1 = len(extenders_1)
n_ec2 = len(extenders_2)
n_ec3 = len(extenders_3)

crit = 1

#####################################################################################################################################################
#####################################################################################################################################################


#now fix the lists (i.e. add data for those subjects who met crit early)

##Start with Non-extenders
###condition 1

#Block 1
count_b1c1 = 0
for i in c1Block1:
    count_b1c1 += 1 # count how many data entries we have
missing_b1c1 = n_c1 - count_b1c1 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b1c1 != 0:
    c1Block1.append(crit)
    missing_b1c1 -= 1
#Block 2
count_b2c1 = 0
for i in c1Block2:
    count_b2c1 += 1 # count how many data entries we have
missing_b2c1 = n_c1 - count_b2c1 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b2c1 != 0:
    c1Block2.append(crit)
    missing_b2c1 -= 1
#Block 3
count_b3c1 = 0
for i in c1Block3:
    count_b3c1 += 1 # count how many data entries we have
missing_b3c1 = n_c1 - count_b3c1 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b3c1 != 0:
    c1Block3.append(crit)
    missing_b3c1 -= 1
#Block 4
count_b4c1 = 0
for i in c1Block4:
    count_b4c1 += 1 # count how many data entries we have
missing_b4c1 = n_c1 - count_b4c1 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b4c1 != 0:
    c1Block4.append(crit)
    missing_b4c1 -= 1
#Block 5
count_b5c1 = 0
for i in c1Block5:
    count_b5c1 += 1 # count how many data entries we have
missing_b5c1 = n_c1 - count_b5c1 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b5c1 != 0:
    c1Block5.append(crit)
    missing_b5c1 -= 1
#Block 6
count_b6c1 = 0
for i in c1Block6:
    count_b6c1 += 1 # count how many data entries we have
missing_b6c1 = n_c1 - count_b6c1 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b6c1 != 0:
    c1Block6.append(crit)
    missing_b6c1 -= 1
#Block 7
count_b7c1 = 0
for i in c1Block7:
    count_b7c1 += 1 # count how many data entries we have
missing_b7c1 = n_c1 - count_b7c1 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b7c1 != 0:
    c1Block7.append(crit)
    missing_b7c1 -= 1
#Block 8
count_b8c1 = 0
for i in c1Block8:
    count_b8c1 += 1 # count how many data entries we have
missing_b8c1 = n_c1 - count_b8c1 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b8c1 != 0:
    c1Block8.append(crit)
    missing_b8c1 -= 1
#Block 9
count_b9c1 = 0
for i in c1Block9:
    count_b9c1 += 1 # count how many data entries we have
missing_b9c1 = n_c1 - count_b9c1 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b9c1 != 0:
    c1Block9.append(crit)
    missing_b9c1 -= 1
#Block 10
count_b10c1 = 0
for i in c1Block10:
    count_b10c1 += 1 # count how many data entries we have
missing_b10c1 = n_c1 - count_b10c1 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b10c1 != 0:
    c1Block10.append(crit)
    missing_b10c1 -= 1



###condition 2
#Block 1
count_b1c2 = 0
for i in c2Block1:
    count_b1c2 += 1 # count how many data entries we have
missing_b1c2 = n_c2 - count_b1c2 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b1c2 != 0:
    c2Block1.append(crit)
    missing_b1c2 -= 1
#Block 2
count_b2c2 = 0
for i in c2Block2:
    count_b2c2 += 1 # count how many data entries we have
missing_b2c2 = n_c2 - count_b2c2 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b2c2 != 0:
    c2Block2.append(crit)
    missing_b2c2 -= 1
#Block 3
count_b3c2 = 0
for i in c2Block3:
    count_b3c2 += 1 # count how many data entries we have
missing_b3c2 = n_c2 - count_b3c2 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b3c2 != 0:
    c2Block3.append(crit)
    missing_b3c2 -= 1
#Block 4
count_b4c2 = 0
for i in c2Block4:
    count_b4c2 += 1 # count how many data entries we have
missing_b4c2 = n_c2 - count_b4c2 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b4c2 != 0:
    c2Block4.append(crit)
    missing_b4c2 -= 1
#Block 5
count_b5c2 = 0
for i in c2Block5:
    count_b5c2 += 1 # count how many data entries we have
missing_b5c2 = n_c2 - count_b5c2 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b5c2 != 0:
    c2Block5.append(crit)
    missing_b5c2 -= 1
#Block 6
count_b6c2 = 0
for i in c2Block6:
    count_b6c2 += 1 # count how many data entries we have
missing_b6c2 = n_c2 - count_b6c2 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b6c2 != 0:
    c2Block6.append(crit)
    missing_b6c2 -= 1
#Block 7
count_b7c2 = 0
for i in c2Block7:
    count_b7c2 += 1 # count how many data entries we have
missing_b7c2 = n_c2 - count_b7c2 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b7c2 != 0:
    c2Block7.append(crit)
    missing_b7c2 -= 1
#Block 8
count_b8c2 = 0
for i in c2Block8:
    count_b8c2 += 1 # count how many data entries we have
missing_b8c2 = n_c2 - count_b8c2 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b8c2 != 0:
    c2Block8.append(crit)
    missing_b8c2 -= 1
#Block 9
count_b9c2 = 0
for i in c2Block9:
    count_b9c2 += 1 # count how many data entries we have
missing_b9c2 = n_c2 - count_b9c2 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b9c2 != 0:
    c2Block9.append(crit)
    missing_b9c2 -= 1
#Block 10
count_b10c2 = 0
for i in c2Block10:
    count_b10c2 += 1 # count how many data entries we have
missing_b10c2 = n_c2 - count_b10c2 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b10c2 != 0:
    c2Block10.append(crit)
    missing_b10c2 -= 1







###condition 3
#Block 1
count_b1c3 = 0
for i in c3Block1:
    count_b1c3 += 1 # count how many data entries we have
missing_b1c3 = n_c3 - count_b1c3 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b1c3 != 0:
    c3Block1.append(crit)
    missing_b1c3 -= 1
#Block 2
count_b2c3 = 0
for i in c3Block2:
    count_b2c3 += 1 # count how many data entries we have
missing_b2c3 = n_c3 - count_b2c3 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b2c3 != 0:
    c3Block2.append(crit)
    missing_b2c3 -= 1
#Block 3
count_b3c3 = 0
for i in c3Block3:
    count_b3c3 += 1 # count how many data entries we have
missing_b3c3 = n_c3 - count_b3c3 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b3c3 != 0:
    c3Block3.append(crit)
    missing_b3c3 -= 1
#Block 4
count_b4c3 = 0
for i in c3Block4:
    count_b4c3 += 1 # count how many data entries we have
missing_b4c3 = n_c3 - count_b4c3 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b4c3 != 0:
    c3Block4.append(crit)
    missing_b4c3 -= 1
#Block 5
count_b5c3 = 0
for i in c3Block5:
    count_b5c3 += 1 # count how many data entries we have
missing_b5c3 = n_c3 - count_b5c3 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b5c3 != 0:
    c3Block5.append(crit)
    missing_b5c3 -= 1
#Block 6
count_b6c3 = 0
for i in c3Block6:
    count_b6c3 += 1 # count how many data entries we have
missing_b6c3 = n_c3 - count_b6c3 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b6c3 != 0:
    c3Block6.append(crit)
    missing_b6c3 -= 1
#Block 7
count_b7c3 = 0
for i in c3Block7:
    count_b7c3 += 1 # count how many data entries we have
missing_b7c3 = n_c3 - count_b7c3 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b7c3 != 0:
    c3Block7.append(crit)
    missing_b7c3 -= 1
#Block 8
count_b8c3 = 0
for i in c3Block8:
    count_b8c3 += 1 # count how many data entries we have
missing_b8c3 = n_c3 - count_b8c3 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b8c3 != 0:
    c3Block8.append(crit)
    missing_b8c3 -= 1
#Block 9
count_b9c3 = 0
for i in c3Block9:
    count_b9c3 += 1 # count how many data entries we have
missing_b9c3 = n_c3 - count_b9c3 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b9c3 != 0:
    c3Block9.append(crit)
    missing_b9c3 -= 1
#Block 10
count_b10c3 = 0
for i in c3Block10:
    count_b10c3 += 1 # count how many data entries we have
missing_b10c3 = n_c3 - count_b10c3 #calculate how many are missing by substracting the number we have from the number we should have
while missing_b10c3 != 0:
    c3Block10.append(crit)
    missing_b10c3 -= 1


#####################################################################################################################################################################
#now fix the extenders lists

###condition 1

#Block 1
e_count_b1c1 = 0
for i in e_c1Block1:
    e_count_b1c1 += 1 # e_count how many data entries we have
e_missing_b1c1 = n_ec1 - e_count_b1c1 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b1c1 != 0:
    e_c1Block1.append(crit)
    e_missing_b1c1 -= 1
#Block 2
e_count_b2c1 = 0
for i in e_c1Block2:
    e_count_b2c1 += 1 # e_count how many data entries we have
e_missing_b2c1 = n_ec1 - e_count_b2c1 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b2c1 != 0:
    e_c1Block2.append(crit)
    e_missing_b2c1 -= 1
#Block 3
e_count_b3c1 = 0
for i in e_c1Block3:
    e_count_b3c1 += 1 # e_count how many data entries we have
e_missing_b3c1 = n_ec1 - e_count_b3c1 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b3c1 != 0:
    e_c1Block3.append(crit)
    e_missing_b3c1 -= 1
#Block 4
e_count_b4c1 = 0
for i in e_c1Block4:
    e_count_b4c1 += 1 # e_count how many data entries we have
e_missing_b4c1 = n_ec1 - e_count_b4c1 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b4c1 != 0:
    e_c1Block4.append(crit)
    e_missing_b4c1 -= 1
#Block 5
e_count_b5c1 = 0
for i in e_c1Block5:
    e_count_b5c1 += 1 # e_count how many data entries we have
e_missing_b5c1 = n_ec1 - e_count_b5c1 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b5c1 != 0:
    e_c1Block5.append(crit)
    e_missing_b5c1 -= 1
#Block 6
e_count_b6c1 = 0
for i in e_c1Block6:
    e_count_b6c1 += 1 # e_count how many data entries we have
e_missing_b6c1 = n_ec1 - e_count_b6c1 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b6c1 != 0:
    e_c1Block6.append(crit)
    e_missing_b6c1 -= 1
#Block 7
e_count_b7c1 = 0
for i in e_c1Block7:
    e_count_b7c1 += 1 # e_count how many data entries we have
e_missing_b7c1 = n_ec1 - e_count_b7c1 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b7c1 != 0:
    e_c1Block7.append(crit)
    e_missing_b7c1 -= 1
#Block 8
e_count_b8c1 = 0
for i in e_c1Block8:
    e_count_b8c1 += 1 # e_count how many data entries we have
e_missing_b8c1 = n_ec1 - e_count_b8c1 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b8c1 != 0:
    e_c1Block8.append(crit)
    e_missing_b8c1 -= 1
#Block 9
e_count_b9c1 = 0
for i in e_c1Block9:
    e_count_b9c1 += 1 # e_count how many data entries we have
e_missing_b9c1 = n_ec1 - e_count_b9c1 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b9c1 != 0:
    e_c1Block9.append(crit)
    e_missing_b9c1 -= 1
#Block 10
e_count_b10c1 = 0
for i in e_c1Block10:
    e_count_b10c1 += 1 # e_count how many data entries we have
e_missing_b10c1 = n_ec1 - e_count_b10c1 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b10c1 != 0:
    e_c1Block10.append(crit)
    e_missing_b10c1 -= 1



###condition 2
#Block 1
e_count_b1c2 = 0
for i in e_c2Block1:
    e_count_b1c2 += 1 # e_count how many data entries we have
e_missing_b1c2 = n_ec2 - e_count_b1c2 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b1c2 != 0:
    e_c2Block1.append(crit)
    e_missing_b1c2 -= 1
#Block 2
e_count_b2c2 = 0
for i in e_c2Block2:
    e_count_b2c2 += 1 # e_count how many data entries we have
e_missing_b2c2 = n_ec2 - e_count_b2c2 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b2c2 != 0:
    e_c2Block2.append(crit)
    e_missing_b2c2 -= 1
#Block 3
e_count_b3c2 = 0
for i in e_c2Block3:
    e_count_b3c2 += 1 # e_count how many data entries we have
e_missing_b3c2 = n_ec2 - e_count_b3c2 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b3c2 != 0:
    e_c2Block3.append(crit)
    e_missing_b3c2 -= 1
#Block 4
e_count_b4c2 = 0
for i in e_c2Block4:
    e_count_b4c2 += 1 # e_count how many data entries we have
e_missing_b4c2 = n_ec2 - e_count_b4c2 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b4c2 != 0:
    e_c2Block4.append(crit)
    e_missing_b4c2 -= 1
#Block 5
e_count_b5c2 = 0
for i in e_c2Block5:
    e_count_b5c2 += 1 # e_count how many data entries we have
e_missing_b5c2 = n_ec2 - e_count_b5c2 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b5c2 != 0:
    e_c2Block5.append(crit)
    e_missing_b5c2 -= 1
#Block 6
e_count_b6c2 = 0
for i in e_c2Block6:
    e_count_b6c2 += 1 # e_count how many data entries we have
e_missing_b6c2 = n_ec2 - e_count_b6c2 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b6c2 != 0:
    e_c2Block6.append(crit)
    e_missing_b6c2 -= 1
#Block 7
e_count_b7c2 = 0
for i in e_c2Block7:
    e_count_b7c2 += 1 # e_count how many data entries we have
e_missing_b7c2 = n_ec2 - e_count_b7c2 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b7c2 != 0:
    e_c2Block7.append(crit)
    e_missing_b7c2 -= 1
#Block 8
e_count_b8c2 = 0
for i in e_c2Block8:
    e_count_b8c2 += 1 # e_count how many data entries we have
e_missing_b8c2 = n_ec2 - e_count_b8c2 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b8c2 != 0:
    e_c2Block8.append(crit)
    e_missing_b8c2 -= 1
#Block 9
e_count_b9c2 = 0
for i in e_c2Block9:
    e_count_b9c2 += 1 # e_count how many data entries we have
e_missing_b9c2 = n_ec2 - e_count_b9c2 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b9c2 != 0:
    e_c2Block9.append(crit)
    e_missing_b9c2 -= 1
#Block 10
e_count_b10c2 = 0
for i in e_c2Block10:
    e_count_b10c2 += 1 # e_count how many data entries we have
e_missing_b10c2 = n_ec2 - e_count_b10c2 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b10c2 != 0:
    e_c2Block10.append(crit)
    e_missing_b10c2 -= 1







###condition 3
#Block 1
e_count_b1c3 = 0
for i in e_c3Block1:
    e_count_b1c3 += 1 # e_count how many data entries we have
e_missing_b1c3 = n_ec3 - e_count_b1c3 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b1c3 != 0:
    e_c3Block1.append(crit)
    e_missing_b1c3 -= 1
#Block 2
e_count_b2c3 = 0
for i in e_c3Block2:
    e_count_b2c3 += 1 # e_count how many data entries we have
e_missing_b2c3 = n_ec3 - e_count_b2c3 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b2c3 != 0:
    e_c3Block2.append(crit)
    e_missing_b2c3 -= 1
#Block 3
e_count_b3c3 = 0
for i in e_c3Block3:
    e_count_b3c3 += 1 # e_count how many data entries we have
e_missing_b3c3 = n_ec3 - e_count_b3c3 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b3c3 != 0:
    e_c3Block3.append(crit)
    e_missing_b3c3 -= 1
#Block 4
e_count_b4c3 = 0
for i in e_c3Block4:
    e_count_b4c3 += 1 # e_count how many data entries we have
e_missing_b4c3 = n_ec3 - e_count_b4c3 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b4c3 != 0:
    e_c3Block4.append(crit)
    e_missing_b4c3 -= 1
#Block 5
e_count_b5c3 = 0
for i in e_c3Block5:
    e_count_b5c3 += 1 # e_count how many data entries we have
e_missing_b5c3 = n_ec3 - e_count_b5c3 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b5c3 != 0:
    e_c3Block5.append(crit)
    e_missing_b5c3 -= 1
#Block 6
e_count_b6c3 = 0
for i in e_c3Block6:
    e_count_b6c3 += 1 # e_count how many data entries we have
e_missing_b6c3 = n_ec3 - e_count_b6c3 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b6c3 != 0:
    e_c3Block6.append(crit)
    e_missing_b6c3 -= 1
#Block 7
e_count_b7c3 = 0
for i in e_c3Block7:
    e_count_b7c3 += 1 # e_count how many data entries we have
e_missing_b7c3 = n_ec3 - e_count_b7c3 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b7c3 != 0:
    e_c3Block7.append(crit)
    e_missing_b7c3 -= 1
#Block 8
e_count_b8c3 = 0
for i in e_c3Block8:
    e_count_b8c3 += 1 # e_count how many data entries we have
e_missing_b8c3 = n_ec3 - e_count_b8c3 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b8c3 != 0:
    e_c3Block8.append(crit)
    e_missing_b8c3 -= 1
#Block 9
e_count_b9c3 = 0
for i in e_c3Block9:
    e_count_b9c3 += 1 # e_count how many data entries we have
e_missing_b9c3 = n_ec3 - e_count_b9c3 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b9c3 != 0:
    e_c3Block9.append(crit)
    e_missing_b9c3 -= 1
#Block 10
e_count_b10c3 = 0
for i in e_c3Block10:
    e_count_b10c3 += 1 # e_count how many data entries we have
e_missing_b10c3 = n_ec3 - e_count_b10c3 #calculate how many are e_missing by substracting the number we have from the number we should have
while e_missing_b10c3 != 0:
    e_c3Block10.append(crit)
    e_missing_b10c3 -= 1



####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

#get means and standard errors for all the blocks and conditions for extenders and non extenders

##start with the non extenders
###condition 1
#Block 1
Mean_c1Block1 = np.mean(c1Block1) #get the mean
err_c1Block1 = sem(c1Block1) #get the standard error
#Block 2
Mean_c1Block2 = np.mean(c1Block2) #get the mean
err_c1Block2 = sem(c1Block2) #get the standard error
#Block 3
Mean_c1Block3 = np.mean(c1Block3) #get the mean
err_c1Block3 = sem(c1Block3) #get the standard error
#Block 4
Mean_c1Block4 = np.mean(c1Block4) #get the mean
err_c1Block4 = sem(c1Block4) #get the standard error
#Block 5
Mean_c1Block5 = np.mean(c1Block5) #get the mean
err_c1Block5 = sem(c1Block5) #get the standard error
#Block 1
Mean_c1Block6 = np.mean(c1Block6) #get the mean
err_c1Block6 = sem(c1Block6) #get the standard error
#Block 7
Mean_c1Block7 = np.mean(c1Block7) #get the mean
err_c1Block7 = sem(c1Block7) #get the standard error
#Block 8
Mean_c1Block8 = np.mean(c1Block8) #get the mean
err_c1Block8 = sem(c1Block8) #get the standard error
#Block 9
Mean_c1Block9 = np.mean(c1Block9) #get the mean
err_c1Block9 = sem(c1Block9) #get the standard error
#Block 10
Mean_c1Block10 = np.mean(c1Block10) #get the mean
err_c1Block10 = sem(c1Block10) #get the standard error



###Condition 2
#Block 1
Mean_c2Block1 = np.mean(c2Block1) #get the mean
err_c2Block1 = sem(c2Block1) #get the standard error
#Block 2
Mean_c2Block2 = np.mean(c2Block2) #get the mean
err_c2Block2 = sem(c2Block2) #get the standard error
#Block 3
Mean_c2Block3 = np.mean(c2Block3) #get the mean
err_c2Block3 = sem(c2Block3) #get the standard error
#Block 4
Mean_c2Block4 = np.mean(c2Block4) #get the mean
err_c2Block4 = sem(c2Block4) #get the standard error
#Block 5
Mean_c2Block5 = np.mean(c2Block5) #get the mean
err_c2Block5 = sem(c2Block5) #get the standard error
#Block 1
Mean_c2Block6 = np.mean(c2Block6) #get the mean
err_c2Block6 = sem(c2Block6) #get the standard error
#Block 7
Mean_c2Block7 = np.mean(c2Block7) #get the mean
err_c2Block7 = sem(c2Block7) #get the standard error
#Block 8
Mean_c2Block8 = np.mean(c2Block8) #get the mean
err_c2Block8 = sem(c2Block8) #get the standard error
#Block 9
Mean_c2Block9 = np.mean(c2Block9) #get the mean
err_c2Block9 = sem(c2Block9) #get the standard error
#Block 10
Mean_c2Block10 = np.mean(c2Block10) #get the mean
err_c2Block10 = sem(c2Block10) #get the standard error



###Condition 3
#Block 1
Mean_c3Block1 = np.mean(c3Block1) #get the mean
err_c3Block1 = sem(c3Block1) #get the standard error
#Block 2
Mean_c3Block2 = np.mean(c3Block2) #get the mean
err_c3Block2 = sem(c3Block2) #get the standard error
#Block 3
Mean_c3Block3 = np.mean(c3Block3) #get the mean
err_c3Block3 = sem(c3Block3) #get the standard error
#Block 4
Mean_c3Block4 = np.mean(c3Block4) #get the mean
err_c3Block4 = sem(c3Block4) #get the standard error
#Block 5
Mean_c3Block5 = np.mean(c3Block5) #get the mean
err_c3Block5 = sem(c3Block5) #get the standard error
#Block 1
Mean_c3Block6 = np.mean(c3Block6) #get the mean
err_c3Block6 = sem(c3Block6) #get the standard error
#Block 7
Mean_c3Block7 = np.mean(c3Block7) #get the mean
err_c3Block7 = sem(c3Block7) #get the standard error
#Block 8
Mean_c3Block8 = np.mean(c3Block8) #get the mean
err_c3Block8 = sem(c3Block8) #get the standard error
#Block 9
Mean_c3Block9 = np.mean(c3Block9) #get the mean
err_c3Block9 = sem(c3Block9) #get the standard error
#Block 10
Mean_c3Block10 = np.mean(c3Block10) #get the mean
err_c3Block10 = sem(c3Block10) #get the standard error

###########################################################################################################################################################
#Now do it for the extenders
###condition 1
#Block 1
Mean_e_c1Block1 = np.mean(e_c1Block1) #get the mean
err_e_c1Block1 = sem(e_c1Block1) #get the standard error
#Block 2
Mean_e_c1Block2 = np.mean(e_c1Block2) #get the mean
err_e_c1Block2 = sem(e_c1Block2) #get the standard error
#Block 3
Mean_e_c1Block3 = np.mean(e_c1Block3) #get the mean
err_e_c1Block3 = sem(e_c1Block3) #get the standard error
#Block 4
Mean_e_c1Block4 = np.mean(e_c1Block4) #get the mean
err_e_c1Block4 = sem(e_c1Block4) #get the standard error
#Block 5
Mean_e_c1Block5 = np.mean(e_c1Block5) #get the mean
err_e_c1Block5 = sem(e_c1Block5) #get the standard error
#Block 1
Mean_e_c1Block6 = np.mean(e_c1Block6) #get the mean
err_e_c1Block6 = sem(e_c1Block6) #get the standard error
#Block 7
Mean_e_c1Block7 = np.mean(e_c1Block7) #get the mean
err_e_c1Block7 = sem(e_c1Block7) #get the standard error
#Block 8
Mean_e_c1Block8 = np.mean(e_c1Block8) #get the mean
err_e_c1Block8 = sem(e_c1Block8) #get the standard error
#Block 9
Mean_e_c1Block9 = np.mean(e_c1Block9) #get the mean
err_e_c1Block9 = sem(e_c1Block9) #get the standard error
#Block 10
Mean_e_c1Block10 = np.mean(e_c1Block10) #get the mean
err_e_c1Block10 = sem(e_c1Block10) #get the standard error



###Condition 2
#Block 1
Mean_e_c2Block1 = np.mean(e_c2Block1) #get the mean
err_e_c2Block1 = sem(e_c2Block1) #get the standard error
#Block 2
Mean_e_c2Block2 = np.mean(e_c2Block2) #get the mean
err_e_c2Block2 = sem(e_c2Block2) #get the standard error
#Block 3
Mean_e_c2Block3 = np.mean(e_c2Block3) #get the mean
err_e_c2Block3 = sem(e_c2Block3) #get the standard error
#Block 4
Mean_e_c2Block4 = np.mean(e_c2Block4) #get the mean
err_e_c2Block4 = sem(e_c2Block4) #get the standard error
#Block 5
Mean_e_c2Block5 = np.mean(e_c2Block5) #get the mean
err_e_c2Block5 = sem(e_c2Block5) #get the standard error
#Block 1
Mean_e_c2Block6 = np.mean(e_c2Block6) #get the mean
err_e_c2Block6 = sem(e_c2Block6) #get the standard error
#Block 7
Mean_e_c2Block7 = np.mean(e_c2Block7) #get the mean
err_e_c2Block7 = sem(e_c2Block7) #get the standard error
#Block 8
Mean_e_c2Block8 = np.mean(e_c2Block8) #get the mean
err_e_c2Block8 = sem(e_c2Block8) #get the standard error
#Block 9
Mean_e_c2Block9 = np.mean(e_c2Block9) #get the mean
err_e_c2Block9 = sem(e_c2Block9) #get the standard error
#Block 10
Mean_e_c2Block10 = np.mean(e_c2Block10) #get the mean
err_e_c2Block10 = sem(e_c2Block10) #get the standard error



###Condition 3
#Block 1
Mean_e_c3Block1 = np.mean(e_c3Block1) #get the mean
err_e_c3Block1 = sem(e_c3Block1) #get the standard error
#Block 2
Mean_e_c3Block2 = np.mean(e_c3Block2) #get the mean
err_e_c3Block2 = sem(e_c3Block2) #get the standard error
#Block 3
Mean_e_c3Block3 = np.mean(e_c3Block3) #get the mean
err_e_c3Block3 = sem(e_c3Block3) #get the standard error
#Block 4
Mean_e_c3Block4 = np.mean(e_c3Block4) #get the mean
err_e_c3Block4 = sem(e_c3Block4) #get the standard error
#Block 5
Mean_e_c3Block5 = np.mean(e_c3Block5) #get the mean
err_e_c3Block5 = sem(e_c3Block5) #get the standard error
#Block 1
Mean_e_c3Block6 = np.mean(e_c3Block6) #get the mean
err_e_c3Block6 = sem(e_c3Block6) #get the standard error
#Block 7
Mean_e_c3Block7 = np.mean(e_c3Block7) #get the mean
err_e_c3Block7 = sem(e_c3Block7) #get the standard error
#Block 8
Mean_e_c3Block8 = np.mean(e_c3Block8) #get the mean
err_e_c3Block8 = sem(e_c3Block8) #get the standard error
#Block 9
Mean_e_c3Block9 = np.mean(e_c3Block9) #get the mean
err_e_c3Block9 = sem(e_c3Block9) #get the standard error
#Block 10
Mean_e_c3Block10 = np.mean(e_c3Block10) #get the mean
err_e_c3Block10 = sem(e_c3Block10) #get the standard error


###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################
#################################                  GRAPH  NOW                   ##########################################################
###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################



block_data = [1,2,3,4,5,6,7,8,9,10]

#non extenders final data
c1data = [
    Mean_c1Block1,
    Mean_c1Block2,
    Mean_c1Block3,
    Mean_c1Block4,
    Mean_c1Block5,
    Mean_c1Block6,
    Mean_c1Block7,
    Mean_c1Block8,
    Mean_c1Block9,
    Mean_c1Block10,
    ]
c1err = [
    err_c1Block1,
    err_c1Block2,
    err_c1Block3,
    err_c1Block4,
    err_c1Block5,
    err_c1Block6,
    err_c1Block7,
    err_c1Block8,
    err_c1Block9,
    err_c1Block10,
    ]
c2data = [
    Mean_c2Block1,
    Mean_c2Block2,
    Mean_c2Block3,
    Mean_c2Block4,
    Mean_c2Block5,
    Mean_c2Block6,
    Mean_c2Block7,
    Mean_c2Block8,
    Mean_c2Block9,
    Mean_c2Block10,
    ]
c2err = [
    err_c2Block1,
    err_c2Block2,
    err_c2Block3,
    err_c2Block4,
    err_c2Block5,
    err_c2Block6,
    err_c2Block7,
    err_c2Block8,
    err_c2Block9,
    err_c2Block10,
    ]
c3data = [
    Mean_c3Block1,
    Mean_c3Block2,
    Mean_c3Block3,
    Mean_c3Block4,
    Mean_c3Block5,
    Mean_c3Block6,
    Mean_c3Block7,
    Mean_c3Block8,
    Mean_c3Block9,
    Mean_c3Block10,
    ]
c3err = [
    err_c3Block1,
    err_c3Block2,
    err_c3Block3,
    err_c3Block4,
    err_c3Block5,
    err_c3Block6,
    err_c3Block7,
    err_c3Block8,
    err_c3Block9,
    err_c3Block10,
    ]

#extenders final data
e_c1data = [
    Mean_e_c1Block1,
    Mean_e_c1Block2,
    Mean_e_c1Block3,
    Mean_e_c1Block4,
    Mean_e_c1Block5,
    Mean_e_c1Block6,
    Mean_e_c1Block7,
    Mean_e_c1Block8,
    Mean_e_c1Block9,
    Mean_e_c1Block10,
    ]
e_c1err = [
    err_e_c1Block1,
    err_e_c1Block2,
    err_e_c1Block3,
    err_e_c1Block4,
    err_e_c1Block5,
    err_e_c1Block6,
    err_e_c1Block7,
    err_e_c1Block8,
    err_e_c1Block9,
    err_e_c1Block10,
    ]
e_c2data = [
    Mean_e_c2Block1,
    Mean_e_c2Block2,
    Mean_e_c2Block3,
    Mean_e_c2Block4,
    Mean_e_c2Block5,
    Mean_e_c2Block6,
    Mean_e_c2Block7,
    Mean_e_c2Block8,
    Mean_e_c2Block9,
    Mean_e_c2Block10,
    ]
e_c2err = [
    err_e_c2Block1,
    err_e_c2Block2,
    err_e_c2Block3,
    err_e_c2Block4,
    err_e_c2Block5,
    err_e_c2Block6,
    err_e_c2Block7,
    err_e_c2Block8,
    err_e_c2Block9,
    err_e_c2Block10,
    ]
e_c3data = [
    Mean_e_c3Block1,
    Mean_e_c3Block2,
    Mean_e_c3Block3,
    Mean_e_c3Block4,
    Mean_e_c3Block5,
    Mean_e_c3Block6,
    Mean_e_c3Block7,
    Mean_e_c3Block8,
    Mean_e_c3Block9,
    Mean_e_c3Block10,
    ]
e_c3err = [
    err_e_c3Block1,
    err_e_c3Block2,
    err_e_c3Block3,
    err_e_c3Block4,
    err_e_c3Block5,
    err_e_c3Block6,
    err_e_c3Block7,
    err_e_c3Block8,
    err_e_c3Block9,
    err_e_c3Block10,
    ]


plt.errorbar(block_data, c2data, yerr= c2err, color = 'k', label = 'non_extenders', marker= 'o', markersize= 10)
plt.errorbar(block_data, e_c2data, yerr= e_c2err, color= 'r', label = 'extenders', marker= 's', markersize= 10)



plt.ylim(0.2,1.05)
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.65, top=0.85)
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.xlabel("Training Block")
plt.ylabel("Proportioin Correct")
plt.title("Learning curve: discourage condition ")
plt.savefig('Training/LearnCurve_discourage')