from scipy.stats import kruskal
import seaborn as sns
import matplotlib.pyplot as plt
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

plot = sns.boxplot(x = 'group', y = 'value', data = dfNoOut,showfliers = False)#data has a lot of outliers, maybe we should look into a different visualization method.

plot.set_xticklabels(['TOH', 'RM', 'BW', 'SM', 'AS'])

group_positions = {'TOH': 0, 'RM': 1, 'BW': 2, 'SM': 3, 'AS': 4} 

boxes = plot.artists
whiskers = plot.lines

whiskers = plot.lines
top_whiskers = [whiskers[i].get_ydata()[1] for i in range(1, len(whiskers), 2)]
plot.set_ylim(top=max(top_whiskers) + 0.1)

def comp(startg, endg, pval, height):
    upStart = whiskers[2*group_positions[startg] + 1].get_ydata()[1]
    upAS = whiskers[2*group_positions[endg] + 1].get_ydata()[1]

    y = max(upStart, upAS) + 0.1  # add a little space above whisker
    h = height # height of bracket
    col = 'k' 

    start = group_positions[startg]
    end = group_positions[endg]

    plot.plot([start, start, end, end], [y, y+h, y+h, y], lw=1.5, c=col)

    plot.text((start+end)*.5, y+h, "p <" + pval, ha='center', va='bottom', color=col)

comp('TOH', 'AS', '10^-308', 0.05)
comp('RM', 'AS', '10^-308', 0.04)
comp('BW', 'AS', '10^-308', 0.055)
comp('SM', 'AS', '4.66 * 10^-198', 0.04)

plt.title("Kruskal-Wallis Test")
plt.xlabel("Tree")
plt.ylabel("Distance")
plt.tight_layout()
plt.show()