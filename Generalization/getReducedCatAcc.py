import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import os




def getReducedCatAcc(path, title):

    #get the test phase data
    dftest = pd.read_csv(path)
    dftest.drop(index = dftest[dftest['phase'] != 'testPhase'].index, inplace=True)
    dftest['accuracy'] = dftest['accuracy'].astype(str)
    dftest = dftest.replace('True', 1)
    dftest = dftest.replace('False', 0)

    dftesta = dftest.drop(index = dftest[dftest['category'] != 'a'].index)
    dftestb = dftest.drop(index = dftest[dftest['category'] != 'b'].index)

    

    #get the train phase data to compare
    dftrain = pd.read_csv(path)
    dftrain.drop(index = dftrain[dftrain['phase'] != 'trainPhase'].index, inplace=True)
    dftrain['accuracy'] = dftrain['accuracy'].astype(str)
    dftrain = dftrain.replace('True', 1)
    dftrain = dftrain.replace('False', 0)

    dftraina = dftrain.drop(index = dftrain[dftrain['category'] != 'a'].index)
    dftrainb = dftrain.drop(index = dftrain[dftrain['category'] != 'b'].index)

    atrainhits= []
    for subject in dftraina['id'].unique():
        atrainhits.append(np.array(dftraina['accuracy'])[-1])
    
    btrainhits= []
    for subject in dftrainb['id'].unique():
        btrainhits.append(np.array(dftrainb['accuracy'])[-1])

    print('test means')
    #print(np.mean(dftesta['accuracy']))
    print(np.mean(dftestb['accuracy']))

    print('train means')
    #print(np.mean(atrainhits))
    print(np.mean(btrainhits))
    print(stats.ttest_ind(dftestb['accuracy'],btrainhits))
    data = [np.mean(btrainhits),np.mean(dftestb['accuracy'])]
    sem = [stats.sem(btrainhits), stats.sem(dftestb['accuracy'])]
    xlabels= ['last block at train', 'test']
    xpos= np.arange(len(xlabels))
    plt.ylabel('average accuracy')
    plt.title(str(title))

    plt.bar(xlabels[0], height=data[0], yerr= sem[0], edgecolor='k', color='white', capsize=8, hatch= '//')
    plt.bar(xlabels[1], height=data[1], yerr= sem[1], edgecolor='k', color='white', capsize=8, hatch= 'oo')

    #plt.xticks(xlabels[xpos])
    plt.savefig('Generalization/'+ str(title) +'.png')
    plt.clf()
            #break
    
    




    





    group = dftest.groupby(['category', 'response'], as_index = True)['accuracy'].describe()
    #print(group)
    



conds={
    'dataWrangling/c1Results.csv': 'encourage',
    'dataWrangling/c2Results.csv': 'discourage',
    'dataWrangling/c3Results.csv': 'Neutral'


}

for key in conds:
    getReducedCatAcc(path=key, title=conds[key])









