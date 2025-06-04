from scipy.spatial import cKDTree
import numpy as np

# tree_points: array of shape (m, 2)
# slf_points: array of shape (n, 2)
def generateDataArray(path):
    data = []
    file = open(path,'r',encoding = 'utf-8').readlines()[1:] #Skip line 1, read through the file
    for line in file:
        lat,lon = map(float,line.split(',')[1:3]) #We're swapping lat,lon for math plotting
        data.append([lon,lat])
    return np.array(data)

tree_points = generateDataArray('datefiles/TOHDataSplit/TOHData_Pruned2024.csv')
tree_points2 = generateDataArray('datefiles/SMDataSplit/SMData_Pruned2024.csv')
slf_points = generateDataArray('datefiles/LFDataSplit/LFData_Pruned2024.csv')

tree_kdtree = cKDTree(tree_points)
distances, _ = tree_kdtree.query(slf_points, k=1)  # Distance from each SLF to nearest tree
mean_distance = np.mean(distances)

tree_kdtree2 = cKDTree(tree_points2)
distances2, _ = tree_kdtree2.query(slf_points, k=1)  # Distance from each SLF to nearest tree
mean_distance2 = np.mean(distances2)

import matplotlib.pyplot as plt

print(f"Observed mean distance: {mean_distance}")

plt.hist(distances, bins=30, alpha=0.7, label="DistanceTOH")
plt.axvline(mean_distance, color='red', linestyle='--', label="Observed SLF")
plt.hist(distances2, bins=30, alpha=0.7, label="DistanceSM")
plt.axvline(mean_distance2, color='black', linestyle='--', label="Observed SLF")
plt.legend()
plt.title("Monte Carlo Test: SLF Distance to Trees")
plt.xlabel("Mean distance to nearest tree")
plt.ylabel("Frequency")
plt.show()


