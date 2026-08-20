from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from kmeans import k_means

centroids = [( 0 , 0 ) , (7 , 5) , (6,6) , (8,9)]
cluster_std = [1 , 1 , 1, 1]
X , y = make_blobs(n_samples=1000, n_features=2, centers=centroids, cluster_std=cluster_std, random_state=2)

plt.scatter (X[:,0] , X[: , 1] , c =  y)
plt.savefig("data")

# make clusters
km = k_means(n_clusters = 4 , max_iterations = 15000000)
y_means = km.fit_predict(X)
plt.figure()
plt.scatter (X[y_means == 0, 0] , X[y_means == 0, 1] , color = 'red')
plt.scatter (X[y_means == 1, 0] , X[y_means == 1, 1] , color = 'blue')
plt.scatter (X[y_means == 2, 0] , X[y_means == 2, 1] , color = 'yellow')
plt.scatter (X[y_means == 3, 0] , X[y_means == 3, 1] , color = 'green')
plt.savefig('clusters')