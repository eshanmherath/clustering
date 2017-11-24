from scipy.cluster.hierarchy import fclusterdata


# a custom function that just computes Euclidean distance
def my_custom_distance_function(p1, p2):
    diff = (p1[0] - p2[0]) + (p1[1] - p2[1])
    distance = abs(diff)
    return distance

X = [[1, 1], [10, 10], [9, 9], [2, 2]]

clusters = fclusterdata(X, 1.0, metric=my_custom_distance_function)

print(clusters)
