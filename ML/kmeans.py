
import numpy as np


def k_means(X, k, max_iterations=1000):
    # step 1: initialize random centriod
    centriods = X[np.random.choice(len(X), k, replace=False)]
    for _ in range(max_iterations):
        # step 2: assign random cluster initially
        labels = []
        for point in X:
            distances = []
            for centriod in centriods:
                distance = np.sqrt(np.sum(point-centriod)**2)
                distances.append(distance)

            # Finding the closest clusters
            closest_cluster = np.argmin(distances)
            labels.append(closest_cluster)
        labels = np.array(labels)

        # step 3: finding means the cluster
        new_centriods = []
        for cluster in range(k):
            cluster_points = X[labels == cluster]
            centriod = np.mean(cluster_points, axis=0)
            new_centriods.append(centriod)
        new_centriods = np.array(new_centriods)

        # step 4: checking convergence
        if np.all(centriods == new_centriods):
            break
        centriods = new_centriods
    return centriods, labels


X = np.array([
    [1, 2],
    [1, 3],
    [2, 2],
    [8, 8],
    [9, 8],
    [8, 9]
])

centroids, labels = k_means(X, 2)

print("Centroids:")
print(centroids)

print("Labels:")
print(labels)
