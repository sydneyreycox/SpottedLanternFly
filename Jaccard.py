import numpy as np
from shapely.ops import unary_union
from shapely.geometry import polygon
from scipy.stats import linregress
import alphashape
import matplotlib.pyplot as plt

#The goal of this is to take the provided alpha shapes and define where the 
# ranges of trees and SLF overlap, and how those ranges change over time

#Function to intake a file path and return the lat lon data
def generateDataArray(path):
    data = []
    file = open(path,'r',encoding = 'utf-8').readlines()[1:] #Skip line 1, read through the file
    for line in file:
        lat,lon = map(float,line.split(',')[1:3]) #We're swapping lat,lon for math plotting
        data.append([lon,lat])
    return np.array(data)

#Calculate the jaccard index by basic function
def jaccard(polyA,polyB):
    return polyA.intersection(polyB).area/polyA.union(polyB).area

#Intake the tags for two of them and process it into an array of time values and jaccard values
def getValues(bugTag,treeTag):
    outputData = []
    for i in range(2015,2025):
        #Unite the multipolygon into a single polygon shape, generate alpha based on data array, a=0.95
        bugAlpha = unary_union(alphashape.alphashape(generateDataArray(
            "datefiles/"+bugTag+"DataSplit/"+bugTag+"Data_Pruned"+str(i)+".csv"),0.95)
        ).buffer(0)
        treeAlpha = unary_union(alphashape.alphashape(generateDataArray(
            "datefiles/"+treeTag+"DataSplit/"+treeTag+"Data_Pruned"+str(i)+".csv"),0.95)
        ).buffer(0)
        #Run jaccard
        jc = jaccard(bugAlpha,treeAlpha)
        #Prevent -inf values from a 0 value in jc index, ln transform to provide linearity
        if(jc>0): outputData.append([i,np.log(jc)])
    #Return in the form of np.array for ease of plotting
    outputData=np.array(outputData)
    return outputData[:,0],outputData[:,1]

#A function to intake the tags and a color, then plot all the values onto matplotlib
def plotBugTreeData(bugTag,treeTag,col):
    #Call getvalues
    xvals,yvals = getValues(bugTag,treeTag)
    #Run linear regression
    slope, intercept, r_value, p_value, std_err = linregress(xvals, yvals)
    # Predicted line
    predicted = intercept + slope * xvals
    #Plot values
    plt.plot(xvals, yvals, 'o', label="ln(Jaccard Index) "+treeTag,color=col)
    #Plot linear regression curve and add to legend
    plt.plot(xvals, predicted, '--', label=f"Linear Fit (R²={r_value**2:.3f}, Slope={slope:.3f}, 2024:{yvals[len(yvals)-1]:.3f})",color=col)
    #)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Boilerplate for generating a Linear regression plot
plt.figure(figsize=(8, 5))
#Plot all the important trees on the same graph and construct the legend
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

