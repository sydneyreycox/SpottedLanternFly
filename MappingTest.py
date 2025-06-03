import alphashape
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as feet

#Mapping file, to generate the various maps

#A quick function processing our data in NPArray, and converted from math form of lat,lon to geographic lon,lat format
def generateDataArray(path):
    data = []
    file = open(path,'r',encoding = 'utf-8').readlines()[1:]
    for line in file:
        lat,lon = map(float,line.split(',')[1:3])
        data.append([lon,lat])
    return np.array(data)

#Quick wrapper method to make the code a bit simpler when plotting AlphaShapes    
def plotAlphaShape(data,alphaval, shape_opac,point_opac, graph, innerCol, outerCol):
    alphaShape = alphashape.alphashape(data,alphaval)
    
    
    
    graph.add_feature(
        feet.ShapelyFeature([alphaShape],crs=ccrs.PlateCarree(),
        facecolor=innerCol,edgecolor=outerCol,alpha=shape_opac)
    )
    plt.scatter(*data.T, color=outerCol,s=1,alpha = point_opac)  # Plot points
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
  
TOHdata = generateDataArray("datefiles/TOHDataSplit/TOHData_Pruned2024.csv")
LFdata = generateDataArray("datefiles/LFDataSplit/LFData_Pruned2024.csv")

#Boilerplate for generating our map in matplotlib
fig,ax = plt.subplots(subplot_kw={'projection':ccrs.PlateCarree()})
ax.coastlines()
ax.add_feature(feet.BORDERS)
ax.add_feature(feet.LAND, edgecolor ='black')

plotAlphaShape(TOHdata,0.25,0.25,0.5,ax,'lightcoral','red')
plotAlphaShape(LFdata,0.25,0.40,0.25,ax,'skyblue','blue')

ax.set_extent([-130,-60,20,60],crs=ccrs.PlateCarree())
#ax.set_extent([-180,180,90,-90],crs=ccrs.PlateCarree())
plt.show()