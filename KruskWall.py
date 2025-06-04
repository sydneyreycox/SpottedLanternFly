from scipy.stats import kruskal

def populate(path):
    file = open(path,'r',encoding = 'utf-8').read()
    num = []
    numin = [int(n) for n in file.split(',')]
    num.append(numin)
    return numin
        
group1 = [populate()]
group2 = [populate()]
group3 = [populate()]
group4 = [populate()]
group5 = [populate()]
group6 = [populate()]
group7 = [populate()]
group8 = [populate()]

statistic, pvalue = kruskal(group1, group2, group3, group4, group5, group6, group7, group8)

print(statistic)
print(pvalue)