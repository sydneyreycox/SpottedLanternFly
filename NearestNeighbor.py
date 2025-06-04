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

tree_points = generateDataArray('datefiles/SMDataSplit/SMData_Pruned2024.csv')
slf_points = generateDataArray('datefiles/LFDataSplit/LFData_Pruned2024.csv')

tree_kdtree = cKDTree(tree_points)
distances, _ = tree_kdtree.query(slf_points, k=1)  # Distance from each SLF to nearest tree

mean_distance = np.mean(distances)

from shapely.geometry import box, Point
import random

# Create bounding box

import alphashape

# Create alpha shape (concave hull) around SLF points
alpha = 0.95  # Adjust this as needed. Smaller = tighter shape
slf_shape = alphashape.alphashape(slf_points, alpha)

# Function to generate random points within the alpha shape
def generate_random_within_shape(shape, n):
    points = []
    minx, miny, maxx, maxy = shape.bounds
    while len(points) < n:
        x = random.uniform(minx, maxx)
        y = random.uniform(miny, maxy)
        if shape.contains(Point(x, y)):
            points.append([x, y])
    return np.array(points)


# Generate N random SLF points
n_sim = 100
random_distances = []

for _ in range(n_sim):
    rand_points = generate_random_within_shape(slf_shape, len(slf_points))
    rand_dists, _ = tree_kdtree.query(rand_points, k=1)
    random_distances.append(np.mean(rand_dists))
    
import matplotlib.pyplot as plt
p_value = np.mean([d <= mean_distance for d in random_distances])
print(f"p-value: {p_value:.4f}")
print(f"Observed mean distance: {mean_distance}")
print(f"Min random mean: {min(random_distances)}")
print(f"Max random mean: {max(random_distances)}")
plt.hist(random_distances, bins=30, alpha=0.7, label="Random")
plt.axvline(mean_distance, color='red', linestyle='--', label="Observed SLF")
plt.legend()
plt.title("Monte Carlo Test: SLF Distance to Trees")
plt.xlabel("Mean distance to nearest tree")
plt.ylabel("Frequency")
plt.show()

rand_points_sample = generate_random_within_shape(slf_shape, len(slf_points))

# Plot the distributions
plt.figure(figsize=(8, 8))
plt.scatter(tree_points[:, 0], tree_points[:, 1], s=1, c='green', label='Trees', alpha=0.5)
plt.scatter(slf_points[:, 0], slf_points[:, 1], s=1, c='red', label='SLF', marker='x')
plt.scatter(rand_points_sample[:, 0], rand_points_sample[:, 1], s=1, c='blue', label='Random Points', alpha=0.01)

plt.legend()
plt.title("SLF, Trees, and Sample Random Points")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.axis('equal')
plt.show()