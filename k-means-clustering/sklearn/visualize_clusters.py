import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.cluster import KMeans

X = [[1.0, 1.0], [7.0, 9.0], [9.5, 8.0], [1.5, 2.0], [1.4, 1.7], [10, 10], [9.0, 8.0], [2.0, 1.8]]

kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)
print()

style.use("ggplot")

colors = ["g.", "r."]

for i in range(len(X)):
    print("training example :", X[i], "\tcentroid label:", labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)

plt.show()
