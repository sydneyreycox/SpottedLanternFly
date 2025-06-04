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
slf_points = generateDataArray('datefiles/LFDataSplit/LFData_Pruned2024.csv')

tree_kdtree = cKDTree(tree_points)
distances, _ = tree_kdtree.query(slf_points, k=1)  # Distance from each SLF to nearest tree

mean_distance = np.mean(distances)

from shapely.geometry import box, Point
import random

# Create bounding box
minx, miny = np.min(slf_points, axis=0)
maxx, maxy = np.max(slf_points, axis=0)

# Generate N random SLF points
n_sim = 1000
random_distances = []

for _ in range(n_sim):
    rand_points = np.array([
        [random.uniform(minx, maxx), random.uniform(miny, maxy)]
        for _ in range(len(slf_points))
    ])
    rand_dists, _ = tree_kdtree.query(rand_points, k=1)
    random_distances.append(np.mean(rand_dists))
    
import matplotlib.pyplot as plt
p_value = np.mean([d <= mean_distance for d in random_distances])
print(f"p-value: {p_value:.20f}")
plt.hist(random_distances, bins=30, alpha=0.7, label="Random")
plt.axvline(mean_distance, color='red', linestyle='--', label="Observed SLF")
plt.legend()
plt.title("Monte Carlo Test: SLF Distance to Trees")
plt.xlabel("Mean distance to nearest tree")
plt.ylabel("Frequency")
plt.show()

