import numpy as np
from shapely.ops import unary_union
from shapely.geometry import polygon
from scipy.stats import linregress
import alphashape
import matplotlib.pyplot as plt

def generateDataArray(path):
    data = []
    file = open(path,'r',encoding = 'utf-8').readlines()[1:] #Skip line 1, read through the file
    for line in file:
        lat,lon = map(float,line.split(',')[1:3]) #We're swapping lat,lon for math plotting
        data.append([lon,lat])
    return np.array(data)

def jaccard(polyA,polyB):
    return polyA.intersection(polyB).area/polyA.union(polyB).area

bugTag = 'LF'
treeTag = 'AS'
outputData = []
for i in range(2015,2025):
    bugAlpha = unary_union(alphashape.alphashape(generateDataArray(
        "datefiles/"+bugTag+"DataSplit/"+bugTag+"Data_Pruned"+str(i)+".csv"),0.95)
    ).buffer(0)
    treeAlpha = unary_union(alphashape.alphashape(generateDataArray(
        "datefiles/"+treeTag+"DataSplit/"+treeTag+"Data_Pruned"+str(i)+".csv"),0.95)
    ).buffer(0)
    jc = jaccard(bugAlpha,treeAlpha)
    if(jc>0): outputData.append([i,np.log10(jc)])
outputData=np.array(outputData)
time_stamps = outputData[:,0]
jaccard_values = outputData[:,1]



slope, intercept, r_value, p_value, std_err = linregress(time_stamps, jaccard_values)

# Predicted line
predicted = intercept + slope * time_stamps

print(r_value,p_value)
plt.figure(figsize=(8, 5))
plt.plot(time_stamps, jaccard_values, 'o', label="Jaccard Index")
plt.plot(time_stamps, predicted, 'r--', label=f"Linear Fit (R²={r_value**2:.3f})")
plt.title("Jaccard Index Over Time with Linear Fit")
plt.xlabel("Year")
plt.ylabel("Jaccard Index")
plt.legend()
plt.grid(True)
plt.show()

