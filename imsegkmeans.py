import cv2
import random
import math
import numpy as np

# Computes the Euclidean distance between two pixels
def euclidean_distance(pixel1, pixel2):
    return math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(pixel1, pixel2)))

# Initializes centroids by randomly sampling k pixels from the image
# i // image.shape[1]: This expression converts the linear index i to a row index in a 2D matrix.
# i % image.shape[1]: This expression converts the same linear index i to a column index.
# Extracts the RGB values of the pixel at each index in the indices list and creates a list of centroids.
def initialize_centroids(image, k):
    indices = random.sample(range(image.shape[0] * image.shape[1]), k)
    return [image[i // image.shape[1]][i % image.shape[1]].tolist() for i in indices]

# Assigns each pixel to the nearest centroid by calculating the distance to all centroids and choosing the closest one
def assign_clusters(image, centroids):
    clusters = []
    for i in range(image.shape[0]):
        cluster_row = []
        for j in range(image.shape[1]):
            pixel = image[i][j]
            distances = [euclidean_distance(pixel, centroid) for centroid in centroids]
            cluster_index = distances.index(min(distances))
            cluster_row.append(cluster_index)
        clusters.append(cluster_row)
    return clusters

# Recomputes the centroid of each cluster by calculating the mean RGB values of the pixels in the cluster
# New centroids better represent the color distributions of the clusters
def update_centroids(image, clusters, k):
    new_centroids = [[0, 0, 0] for _ in range(k)]
    counts = [0] * k
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            cluster_index = clusters[i][j]
            counts[cluster_index] += 1
            new_centroids[cluster_index] = [new_centroids[cluster_index][c] + image[i][j][c] for c in range(3)]
    for index in range(k):
        if counts[index] > 0:
            new_centroids[index] = [int(new_centroids[index][c] / counts[index]) for c in range(3)]
    return new_centroids

# Sets the initial centroids, iteratively assigns clusters and updates centroids.
# Stops after the specified number of iterations or when the centroids no longer change.
def kmeans_segmentation(image, k, max_iterations=15):
    centroids = initialize_centroids(image, k)
    for _ in range(max_iterations):
        clusters = assign_clusters(image, centroids)
        new_centroids = update_centroids(image, clusters, k)
        if all(new_centroids[i] == centroids[i] for i in range(k)):
            break
        centroids = new_centroids
    return clusters, centroids

###########################################################################
"""
def show(image, clusters, k):
    # Assigns different colors to each cluster for visual labeling
    colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(k)]
    labeled_image = np.zeros_like(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            cluster_index = clusters[i][j]
            labeled_image[i][j] = colors[cluster_index]

    return labeled_image

# Load the image
image = cv2.imread('/Users/dilaraturkalp/Desktop/cmpe362hw/dog.png')
#new_size = (int(image.shape[1] * 0.3), int(image.shape[0] * 0.3))
#image = cv2.resize(image, new_size)

# Apply K-means segmentation
k = 2 
clusters, centroids = kmeans_segmentation(image, k)

labeled_image = show(image, clusters, k)

# Visualize the labeled image
cv2.imshow('Segmented Image', labeled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
