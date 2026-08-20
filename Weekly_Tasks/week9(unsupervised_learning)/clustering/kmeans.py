import random
import numpy as np


class k_means:
    def __init__(self , n_clusters , max_iterations):
        self.n_clusters = n_clusters
        self.max_iterations = max_iterations
        self.centroids = None

    def fit_predict(self , X):

        # select centroid
        rand_index = random.sample(range(0, X.shape[0]) , self.n_clusters)
        self.centroids = X[rand_index]

        for i in range(self.max_iterations):
            # assign cluster
            cluster_group = self.assign_clusters(X)

            # move centroid 
            old_centroids = self.centroids
            self.centroids = self.move_centroids(X,cluster_group)

            # check finish
            if (old_centroids == self.centroids ).all():
                break
        return cluster_group
    
    def assign_clusters(self , X):
        cluster_group = []
        distance = []
        for row in X:
            for centroid in self.centroids:
                distance.append(np.sqrt(np.dot( row - centroid , row - centroid)))
            min_dist = min (distance)
            ind_pos = distance.index(min_dist)
            cluster_group.append(ind_pos)
            distance.clear()


        return np.array(cluster_group)
    
   
    def move_centroids(self , X , cluster_group):
        new_centroids = []
        cluster_type = np.unique(cluster_group)
        for type in cluster_type:
            new_centroids.append(X[cluster_group == type].mean(axis = 0))
        return np.array(new_centroids)
    
        


