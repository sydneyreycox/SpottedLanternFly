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

def getValues(bugTag,treeTag):
    outputData = []
    for i in range(2015,2025):
        bugAlpha = unary_union(alphashape.alphashape(generateDataArray(
            "datefiles/"+bugTag+"DataSplit/"+bugTag+"Data_Pruned"+str(i)+".csv"),0.95)
        ).buffer(0)
        treeAlpha = unary_union(alphashape.alphashape(generateDataArray(
            "datefiles/"+treeTag+"DataSplit/"+treeTag+"Data_Pruned"+str(i)+".csv"),0.95)
        ).buffer(0)
        jc = jaccard(bugAlpha,treeAlpha)
        if(jc>0): outputData.append([i,np.log(jc)])
    outputData=np.array(outputData)
    return outputData[:,0],outputData[:,1]


    
def plotBugTreeData(bugTag,treeTag,col):
    xvals,yvals = getValues(bugTag,treeTag)
    slope, intercept, r_value, p_value, std_err = linregress(xvals, yvals)
    # Predicted line
    predicted = intercept + slope * xvals
    plt.plot(xvals, yvals, 'o', label="ln(Jaccard Index) "+treeTag,color=col)
    plt.plot(xvals, predicted, '--', label=f"Linear Fit (R²={r_value**2:.3f}, Slope={slope:.3f}, 2024:{yvals[len(yvals)-1]:.3f})",color=col)
    #)

plt.figure(figsize=(8, 5))
plotBugTreeData('LF','TOH','blue')
plotBugTreeData('LF','AS','orange')
plotBugTreeData('LF','BW','green')
plotBugTreeData('LF','SM','purple')
plotBugTreeData('LF','RM','red')
plt.title("Jaccard Index Over Time with Linear Fit")
plt.xlabel("Year")
plt.ylabel("ln(Jaccard Index)")
plt.legend(fontsize='8')
plt.grid(True)
plt.show()

