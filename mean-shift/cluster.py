import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.cluster import MeanShift
from sklearn.datasets.samples_generator import make_blobs
from mpl_toolkits.mplot3d import Axes3D  # needed

# create sample data
centers = [[-7, -7, -7], [0, 0, 0], [7, 7, 7]]
X, _ = make_blobs(n_samples=250, centers=centers, cluster_std=1.5)

# create and fit to model
ms = MeanShift()
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

print("Estimated number of cluster centers : " + str(len(np.unique(labels))))
print("Estimated cluster centers")
print(cluster_centers)

# assuming number of clusters doesn't exceed 20
colors = 5 * ['r', 'g', 'b', 'y']

style.use("ggplot")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(X)):
    ax.scatter(X[i][0], X[i][1], X[i][2], c=colors[labels[i]], marker='o')

ax.scatter(cluster_centers[:, 0], cluster_centers[:, 1], cluster_centers[:, 2],
           marker="o", color='k', s=5, linewidths=5, zorder=10)

plt.show()
