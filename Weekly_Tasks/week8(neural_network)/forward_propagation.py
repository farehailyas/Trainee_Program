import numpy as np

def sigmoid(z):
    den = 1 + np.exp(-z)
    return 1/den

def dense_layer(a_in , W , b):
    units = W.shape[1]
    a_out = np.zeros(units)
    for j in range (units):
        w = W[: , j]
        z = np.dot(w, a_in) + b[j]
        a_out[j] = sigmoid (z)

    return a_out

def sequential(X, W1 , W2 , b1 , b2):
    a1 = dense_layer(X,W1,b1)
    a2 = dense_layer(a1,W2, b2)
    return a2

def dense_layer_with_vectorization(a_in , W , b):
    z = np.matmul(a_in , W)+b
    a_out = sigmoid(z)
    return a_out