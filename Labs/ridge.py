import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Generate some random data
np.random.seed(0)
X = np.random.rand(100, 1)
#The variable X is a 2D array with shape (100, 1) containing
#random values generated from a uniform distribution between 0 and 1.
y = 2 * X + 0.5 * np.random.randn(100, 1)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Ridge Regression model
alpha = 0.1  # Regularization strength
ridge_model = Ridge(alpha=alpha)
ridge_model.fit(X_train, y_train)

# Make predictions
y_pred = ridge_model.predict(X_test)

# Calculate error metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print error metrics
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("Mean Absolute Error:", mae)
print("R-squared Score:", r2)

# Plot the data and the ridge regression line
plt.scatter(X, y, color='red', label='Data')
plt.plot(X_test, y_pred, color='blue', linewidth=2, label='Ridge Regression')
plt.title("Ridge Regression")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()
