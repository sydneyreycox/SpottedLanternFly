from scipy.spatial import cKDTree
import numpy as np
import matplotlib.pyplot as plt

# tree_points: array of shape (m, 2)
# slf_points: array of shape (n, 2)
def generateDataArray(path):
    data = []
    file = open(path,'r',encoding = 'utf-8').readlines()[1:] #Skip line 1, read through the file
    for line in file:
        lat,lon = map(float,line.split(',')[1:3]) #We're swapping lat,lon for math plotting
        data.append([lon,lat])
    return np.array(data)

#Make a cKD, calculate the SLF distance to the closest tree 
def distanceArray(slf_points, tree_points):
    distances, _ = cKDTree(tree_points).query(slf_points, k=1)  # Distance from each SLF to nearest tree
    return distances

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TREE_TAGS =["AS","BW","RM","SM","TOH"]

slf_data=generateDataArray("datafiles/LFData_Pruned.csv")

#Itterate through the tree tags and make the files of their distances for use in KruskWall
for tag in TREE_TAGS:
    out = open("nndata/nndata_"+tag+'.csv','w+',encoding='utf-8')
    dist = distanceArray(slf_data,generateDataArray("datafiles/"+tag+"Data_Pruned.csv"))
    out.write("nn_distance_val,"+str(dist[0]))
    for val in dist[1:]:
        out.write(","+str(val))
    

#Histogram here for viewing data, not utilizing currently
'''
mean_distance = np.mean(distances)

print(f"Observed mean distance: {mean_distance}")

plt.hist(distances, bins=30, alpha=0.7, label="DistanceRM")
plt.axvline(mean_distance, color='red', linestyle='--', label="Observed SLF/RM")
plt.hist(distances2, bins=30, alpha=0.7, label="DistanceAS")
plt.axvline(mean_distance2, color='black', linestyle='--', label="Observed SLF/AS")
plt.legend()
plt.title("Distance Measures: SLF Distance to Trees")
plt.xlabel("Mean distance to nearest tree")
plt.ylabel("Frequency")
plt.show()
'''