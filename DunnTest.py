import scikit_posthocs as sp
import pandas as pd

def populate(path):
    file = open(path,'r',encoding = 'utf-8').read()
    num = []
    numin = [int(n) for n in file.split(',')]
    num.append(numin)
    return num

group1 = populate()
group2 = populate()
group3 = populate()
group4 = populate()
group5 = populate()
group6 = populate()
group7 = populate()
group8 = populate()

data = group1 + group2 + group3 + group4 + group5 + group6 + group7 + group8

groups = (     
['group1'] * len(group1)+
['group2'] * len(group2)+
['group3'] * len(group3)+
['group4'] * len(group4)+
['group5'] * len(group5)+
['group6'] * len(group6)+
['group7'] * len(group7)+
['group8'] * len(group8)
)


 
df = pd.DataFrame({'data': data, 'group': groups})

#dunnData = [df[n].values for n in df.columns]

dunnResult = sp.posthoc_dunn(df, val_col='data', group_col='group')

print(dunnResult)