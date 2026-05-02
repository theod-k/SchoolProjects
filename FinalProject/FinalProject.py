import numpy as np
import pandas as pd
import numpy.matlib
import matplotlib.pyplot as plt

df = pd.read_csv("housing.csv")

X = df.drop("median_house_value", axis=1)
y = df["median_house_value"].values.reshape(-1, 1)

X = pd.get_dummies(X, columns=["ocean_proximity"])

for col in X.columns:
    if X[col].dtype != 'uint8':
        X[col].fillna(X[col].median(), inplace=True)

X_mean = X.mean()
X_std = X.std()
X_scaled = (X - X_mean) / X_std
X_scaled = X_scaled.values

y_mean = np.mean(y)
y_std = np.std(y)
y_scaled = (y - y_mean) / y_std

split_index = int(0.8 * len(X_scaled))
X_train, X_test = X_scaled[:split_index], X_scaled[split_index:]
y_train, y_test = y_scaled[:split_index], y_scaled[split_index:]

class LinearRegression:
    def __init__(self, lr=0.1, iters=500, reg=0.1):
        self.lr = lr
        self.iters = iters
        self.reg = reg

    def fit(self, X, y):
        m, n = X.shape
        self.theta = np.zeros((n, 1))
        self.bias = 0
        self.losses = []

        for _ in range(self.iters):
            y_pred = X @ self.theta + self.bias
            error = y_pred - y

            grad_theta = (X.T @ error) / m + self.reg * np.sign(self.theta) / m
            grad_bias = np.sum(error) / m

            self.theta -= self.lr * grad_theta
            self.bias -= self.lr * grad_bias

            loss = np.mean(error**2) / 2 + self.reg * np.sum(np.abs(self.theta)) / m
            self.losses.append(loss)

    def predict(self, X):
        return X @ self.theta + self.bias

model = LinearRegression()
model.fit(X_train, y_train)

y_pred_scaled = model.predict(X_test)
y_pred = y_pred_scaled * y_std + y_mean
y_actual = y_test * y_std + y_mean

rmse = np.sqrt(np.mean((y_pred - y_actual)**2))
# print("RMSE:", rmse)


plt.figure(figsize=(8, 5))
plt.plot(model.losses)
plt.title("Training Loss Over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df["median_house_value"], bins=50, edgecolor='black')
plt.title("Distribution of Housing Prices")
plt.xlabel("Median House Value ($)")
plt.ylabel("Count")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df["median_income"], df["median_house_value"], alpha=0.3)
plt.title("Housing Price vs. Median Income")
plt.xlabel("Median Income")
plt.ylabel("Median House Value ($)")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df["longitude"], df["latitude"], alpha=0.4,
            c=df["median_house_value"], cmap="viridis", s=20)
plt.colorbar(label="Median House Value")
plt.title("California Housing Prices by Location")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df["total_rooms"], df["median_house_value"], alpha=0.3)
plt.title("Housing Price vs. Size of House (Total Rooms)")
plt.xlabel("Total Rooms")
plt.ylabel("Median House Value ($)")
plt.grid(True)
plt.show()

np.random.seed(42)
num_predictions = 20
sample_indices = np.random.choice(len(X_test), size=num_predictions, replace=False)

X_sample = X_test[sample_indices]
y_true_sample = y_test[sample_indices]
y_pred_sample = model.predict(X_sample)

y_true_dollar = y_true_sample * y_std + y_mean
y_pred_dollar = y_pred_sample * y_std + y_mean

X_unscaled = (X_sample * X_std.values) + X_mean.values
input_columns = X.columns

print("\nPredicted vs Actual House Prices with Input Features:")
for i in range(num_predictions):
    print(f"\nSample {i+1}")
    print("-" * 40)
    print("Input Features:")
    for j in range(len(input_columns)):
        print(f"{input_columns[j]:>20}: {X_unscaled[i, j]:,.2f}")
    print(f"{'Actual Price':>20}: ${y_true_dollar[i, 0]:,.2f}")
    print(f"{'Predicted Price':>20}: ${y_pred_dollar[i, 0]:,.2f}")

indices = np.arange(num_predictions)
bar_width = 0.35

plt.figure(figsize=(12, 6))
plt.bar(indices, y_true_dollar.flatten(), bar_width, label='Actual Price', alpha=0.7)
plt.bar(indices + bar_width, y_pred_dollar.flatten(), bar_width, label='Predicted Price', alpha=0.7)

plt.xlabel('Sample Index')
plt.ylabel('House Price ($)')
plt.title('Predicted vs Actual House Prices (Random Sample)')
plt.xticks(indices + bar_width / 2, [f'Sample {i+1}' for i in indices], rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
