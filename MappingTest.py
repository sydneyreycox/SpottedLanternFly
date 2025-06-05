import alphashape
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col
import cartopy.crs as ccrs
import cartopy.feature as feet

#Mapping file, to generate the various maps

#A quick function processing our data in NPArray, and converted from math form of lat,lon to geographic lon,lat format
def generateDataArray(path):
    data = []
    file = open(path,'r',encoding = 'utf-8').readlines()[1:] #Skip line 1, read through the file
    for line in file:
        lat,lon = map(float,line.split(',')[1:3]) #We're swapping lat,lon for math plotting
        data.append([lon,lat])
    return np.array(data)

#Quick wrapper method to make the code a bit simpler when plotting AlphaShapes    
def plotAlphaShape(graph,data,alphaval, innerCol, outerCol, pointCol): #Colors should be supplied in rgba format
    alphaShape = alphashape.alphashape(data,alphaval)
    graph.add_feature(
        feet.ShapelyFeature([alphaShape],crs=ccrs.PlateCarree(),
        facecolor=innerCol,edgecolor=outerCol),
        rasterized=True  # Critical for alpha blending
    )
    plt.scatter(*data.T, color=pointCol,s=1)  # Plot points
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
  
TOHdata = generateDataArray("datefiles/SMDataSplit/SMData_Pruned2024.csv")
LFdata = generateDataArray("datefiles/LFDataSplit/LFData_Pruned2024.csv")

#Boilerplate for generating our map in matplotlib
fig,ax = plt.subplots(subplot_kw={'projection':ccrs.PlateCarree()}) #Render Map Object and projection
ax.coastlines() #We need coastlines
ax.add_feature(feet.BORDERS) #International Borders, shows our data in US
ax.add_feature(feet.LAND, edgecolor ='black') #Draw the land seperately

plotAlphaShape(ax,TOHdata,0.95,col.to_rgba('red',0.20),col.to_rgba('red',0.50),col.to_rgba('red',0.5)) #TOH Plot
plotAlphaShape(ax,LFdata,0.95,col.to_rgba('blue',0.20),col.to_rgba('blue',0.50),col.to_rgba('blue',0.1)) #LF Plot

#North America Range
ax.set_extent([-130,-60,20,60],crs=ccrs.PlateCarree())
#ax.set_extent([-180,180,90,-90],crs=ccrs.PlateCarree())

#Produce Gridlines and lables for ease of use
gl = ax.gridlines(
    crs=ccrs.PlateCarree(),
    draw_labels=True,      # Enable labels
    linewidth=0.5,         # Gridline width
    color='gray',          # Gridline color
    alpha=0.3,            # Gridline transparency
    linestyle='--'        # Dashed lines
)
plt.show()