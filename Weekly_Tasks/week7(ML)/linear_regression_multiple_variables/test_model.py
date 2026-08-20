from train_model import evaluate, print_metrics_table
import numpy as np
import matplotlib.pyplot as plt

# load the saved model + test data + train metrics (no retraining)
data = np.load("model.npz")
w_final = data["w"]
b_final = data["b"]
X_test = data["X_test"]
Y_test = data["Y_test"]

# train metrics were computed and saved during training
train_metrics = {
    "rmse": float(data["train_rmse"]),
    "mae": float(data["train_mae"]),
    "r2": float(data["train_r2"]),
}


def print_samples(X, Y, w, b, n_samples=20):
    preds = X[:n_samples] @ w + b
    actuals = Y[:n_samples]

    print(f"\n{'sample':>8}{'actual':>15}{'predicted':>15}{'difference':>15}")
    for i in range(n_samples):
        diff = actuals[i] - preds[i]
        print(f"{i:>8}{actuals[i]:>15,.2f}{preds[i]:>15,.2f}{diff:>15,.2f}")


def test_prediction(X, Y, w, b, n_samples=40):
    preds = X[:n_samples] @ w + b
    actuals = Y[:n_samples]

    x = range(n_samples)
    plt.figure(figsize=(12, 6))
    plt.plot(x, actuals, 'o-', label="actual price")
    plt.plot(x, preds, 'x--', label="predicted price")
    plt.xlabel("sample")
    plt.ylabel("price")
    plt.title("predicted vs actual - TEST (first 40 samples)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("graphs/test_predicted_vs_actual")
    plt.close()


# validate the trained model on unseen test data and compare against training
test_metrics = evaluate(X_test, Y_test, w_final, b_final)
print_metrics_table({"train": train_metrics, "test": test_metrics})

test_prediction(X_test, Y_test, w_final, b_final)
print_samples(X_test, Y_test, w_final, b_final, n_samples=20)
