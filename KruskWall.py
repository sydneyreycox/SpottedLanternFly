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
groups = (['AS'] * len(group1) +
          ['BW'] * len(group2) +
          ['RM'] * len(group3) +
          ['SM'] * len(group4) +
          ['TOH'] * len(group5))

df = pd.DataFrame({'value': data, 'group': groups})

statistic, pvalue = kruskal(group1, group2, group3, group4, group5)

print(f'Kruskal-Wallis Test\nH = {statistic:.3f}, p = {pvalue:.15e}') #p-value is so small is is not registered through python(practically zero)/
                                                                    #it is too small for python to register, must to Dunn's test

sns.boxplot(x = 'group', y = 'value', data = df, showfliers = False)#data has a lot of outliers, maybe we should look into a different visualization method.
plt.title("Kruskal-Wallis Test")
plt.xlabel("Tree")
plt.ylabel("Placeholder")
plt.tight_layout()
plt.show()