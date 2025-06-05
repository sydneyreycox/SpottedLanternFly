import scikit_posthocs as sp
import pandas as pd
import numpy as np

def populate(path):
    num = list(map(float,(open(path,'r',encoding = 'utf-8').read().split(',')[1:])))
    return num

group1 = populate('nndata/nndata_AS.csv')
group2 = populate('nndata/nndata_BW.csv')
group3 = populate('nndata/nndata_RM.csv')
group4 = populate('nndata/nndata_SM.csv')
group5 = populate('nndata/nndata_TOH.csv')

data = group1 + group2 + group3 + group4 + group5

def remove_out(df, data):
    Quart1 = df[data].quantile(0.25)
    Quart2 = df[data].quantile(0.75)
    IQR = Quart2 - Quart1
    low = Quart1 - 1.5 * IQR
    up = Quart2 + 1.5 * IQR
    return df[(df[data] >= low) & (df[data] <= up)]

groups = (['AS'] * len(group1) +
          ['BW'] * len(group2) +
          ['RM'] * len(group3) +
          ['SM'] * len(group4) +
          ['TOH'] * len(group5))


 
df = pd.DataFrame({'data': data, 'group': groups})

dfNoOut = df.groupby('group').apply(lambda g: remove_out(g, 'data')).reset_index(drop=True)

dunnResult = sp.posthoc_dunn(dfNoOut, val_col='data', group_col='group', p_adjust='bonferroni')

print(dunnResult)