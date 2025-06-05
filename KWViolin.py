from scipy.stats import kruskal
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

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

groups = (['TOH'] * len(group5) +
          ['RM'] * len(group3) +
          ['BW'] * len(group2) +
          ['SM'] * len(group4) +
          ['AS'] * len(group1) )

df = pd.DataFrame({'value': data, 'group': groups})

dfNoOut = df.groupby('group').apply(lambda g: remove_out(g, 'value')).reset_index(drop=True)

cleanData = [group['value'].values for n, group in dfNoOut.groupby('group')]

statistic, pvalue = kruskal(*cleanData)

print(f'Kruskal-Wallis Test\nH = {statistic:.3f}, p = {pvalue:.15e}') #p-value is so small is is not registered through python(practically zero)/
                                                                    #it is too small for python to register, must to Dunn's test

plot = sns.violinplot(x = 'group', y = 'value', data = dfNoOut)#data has a lot of outliers, maybe we should look into a different visualization method.
plot.set_xticklabels(['TOH', 'RM', 'BW', 'SM', 'AS'])
plt.title("Distance of SLF to Trees")
plt.xlabel("Tree")
plt.ylabel("Distance")
plt.tight_layout()
plt.show()