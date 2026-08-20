from prepare_data import preprocess_data
import numpy as np
import matplotlib.pyplot as plt

def compute_cost(X_train , Y_train , w , b) :
    m = X_train.shape[0]
    err = (X_train @ w + b) - Y_train
    return (err @ err) / (2 * m)

def calculate_gradient(X_train , Y_train , w , b):
    # m is no of rows , n is no of columns
    m = X_train.shape[0]
    err = (X_train @ w + b) - Y_train     
    dw = (X_train.T @ err) / m
    db = err.mean()
    return dw, db

   
def gradient_descent(X_train , Y_train , w , b , alpha , iterations , tol = 1e-6):
    print("training started")
    cost_history = []
    prev_cost = float('inf')
    m = X_train.shape[0]
    for i in range (iterations):
        dw , db = calculate_gradient(X_train , Y_train , w , b)
        w = w - alpha * dw
        b = b - alpha * db
        cost = compute_cost(X_train , Y_train ,  w, b)
        cost_history.append(cost)
        if i % 100 == 0:
            print(f"iteration {i}, cost {cost}")
        if abs(prev_cost - cost) < tol:
            print(f"stopping at iteration {i}")
            print("training ended")
            break
        prev_cost = cost
    print("training ended")
      # plot cost vs iterations
    plt.figure(figsize=(8, 5))
    plt.plot(cost_history)
    plt.xlabel("iteration")
    plt.ylabel("cost")
    plt.title("cost vs iterations (gradient descent)")
    plt.savefig("graphs/multi_cost_vs_iterations_1000_iterations")
    plt.close()
    return w , b 

def train_model(X_train , Y_train):
    # initialize parameters
    n = X_train.shape[1]
    b = 0.0
    w = np.zeros(n)
  
    iterations = 1000
    alpha = 0.01
    # run gradient descent 
    w_final, b_final = gradient_descent(X_train, Y_train, w, b , alpha, iterations)
    return w_final, b_final

def prediction(X_train , Y_train , w_final , b_final , n_samples = 40):
    preds = X_train[:n_samples] @ w_final + b_final
    actuals = Y_train[:n_samples]

    x = range(n_samples)
    plt.figure(figsize=(12, 6))
    plt.plot(x, actuals, 'o-', label="actual price")
    plt.plot(x, preds,   'x--', label="predicted price")
    plt.xlabel("sample")
    plt.ylabel("price")
    plt.title("predicted vs actual (first 40 samples)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("graphs/multi_predicted_vs_actual_1000_iterations")
    plt.close()


def evaluate(X, Y, w, b):
    """Compute regression metrics on (X, Y) and return them as a dict."""
    preds = X @ w + b
    errors = preds - Y

    rmse = np.sqrt(np.mean(errors ** 2))
    mae = np.mean(np.abs(errors))

    ss_res = np.sum(errors ** 2)
    ss_tot = np.sum((Y - Y.mean()) ** 2)
    r2 = 1 - ss_res / ss_tot

    return {
        "rmse": rmse,
        "mae": mae,
        "r2": r2,
    }


def print_metrics_table(metrics_by_label):
    """Print a train-vs-test comparison table from {label: metrics_dict}."""
    labels = list(metrics_by_label)

    rows = [
        ("RMSE", "rmse", "{:>15,.2f}"),
        ("MAE",  "mae",  "{:>15,.2f}"),
        ("R2",   "r2",   "{:>15.9f}"),
    ]

    header = f"{'metric':>18}" + "".join(f"{lbl:>15}" for lbl in labels)
    print("\n" + header)
    print("-" * len(header))
    for name, key, fmt in rows:
        line = f"{name:>18}" + "".join(fmt.format(metrics_by_label[lbl][key]) for lbl in labels)
        print(line)

if __name__ == "__main__":
    X_train , X_test, Y_train , Y_test = preprocess_data()

    X_train = X_train.to_numpy(dtype=float)
    X_test  = X_test.to_numpy(dtype=float)
    Y_train = Y_train.to_numpy(dtype=float)
    Y_test  = Y_test.to_numpy(dtype=float)

    w_final, b_final = train_model(X_train , Y_train)
    prediction (X_train , Y_train , w_final, b_final)

    # evaluate on the training set so test_model.py can show train vs test side by side
    train_metrics = evaluate(X_train, Y_train, w_final, b_final)

    # save the trained model + test data + train metrics so test_model.py can load
    # everything without retraining
    np.savez(
        "model.npz",
        w=w_final, b=b_final,
        X_test=X_test, Y_test=Y_test,
        train_rmse=train_metrics["rmse"],
        train_mae=train_metrics["mae"],
        train_mape=train_metrics["mape"],
        train_r2=train_metrics["r2"],
        train_within_pct=train_metrics["within_pct"],
        tolerance=train_metrics["tolerance"],
    )
    print("model saved to model.npz")
