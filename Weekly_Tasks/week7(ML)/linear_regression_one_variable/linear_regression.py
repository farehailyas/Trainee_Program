import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def compute_cost(x,y,w,b):
    total_cost = 0
    m = len(x)
    for i in range(m):
        pred = (w*x[i]) + b
        cost = (pred-y[i])**2
        total_cost += cost
    return total_cost/(2*m)

def compute_gradient(x , y , w , b):
    dw = 0 
    db = 0 
    m = len(x)
    for i in range(m):
        pred = (w*x[i] + b)
        gradient_w = (pred - y[i]) * x[i]
        gradient_b = (pred - y[i]) 
        dw+=gradient_w
        db+=gradient_b

    return dw/m , db/m

def draw_graph(iterations, cost):
    plt.figure()
    plt.plot(iterations , cost)
    plt.xlabel("iterations")
    plt.ylabel("cost")
    plt.title("Check if cost is decreasing with increasing iterations")
    plt.grid(True)
    plt.savefig("cost_vs_iterations.png")

# batch gradient descent
def gradient_descent(x , y , alpha, w , b , iterations=100):
    iteration = []
    cost_at_iteration = []
    for i in range(iterations):
        dw , db =  compute_gradient(x,y,w,b)
        w_temp = alpha * dw
        b_temp = alpha * db
        w = w - w_temp
        b = b - b_temp
    
        if i%20 == 0:
            iteration.append(i)
            cost = compute_cost(x,y,w,b)
            cost_at_iteration.append(cost)

    draw_graph(iteration , cost_at_iteration)
    return w , b

            
def define_data():
    x = np.array([1, 2, 3, 4, 5 , 6, 7, 8, 9 , 10 , 11, 12 , 13 , 14 , 15 , 16 , 17 , 18 ,  19 , 20])
    y = np.array([2 , 10, 7, 19, 12, 16 ,18 ,20 , 34 , 40 , 36, 42 , 49 , 53 , 78 , 67 , 98 , 100 , 112 , 115 ])

    # plot points on graph
    plt.scatter(x , y ,  marker = 'o' , c = 'b')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Training dataset")
    plt.savefig("train_data.png")
    return x , y 

def train_model(x , y):
    alpha = 0.01
    w = 0.0
    b = 0.0
    iterations = 100
    updated_w , updated_b = gradient_descent(x, y, alpha , w , b , iterations)
    return updated_w , updated_b

def training_graph(x , y , prediction ):
    plt.figure()
    plt.plot(x , prediction , c = 'b')
    plt.scatter(x , y ,  marker = 'o' , c = 'r')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Training dataset")
    plt.savefig("training_graph.png")

def predict_output(x , y , w , b ):
    m = len(x)
    prediction = np.zeros(m)
   
    for i in range(m):
        prediction[i] = (x[i] * w) + b 

    training_graph(x,y,prediction)
    return prediction 

    

def test_graph(x , y , prediction ):
    plt.figure()
    plt.plot(x , prediction , c = 'b')
    plt.scatter(x , y ,  marker = 'o' , c = 'r')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Training dataset")
    plt.savefig("training_graph.png")

def test_model (w , b ):
    pred = 40*w+b
    
    return pred

x , y = define_data()
updated_w , updated_b = train_model(x , y )
prediction = predict_output(x , y , updated_w , updated_b)
print(prediction)

