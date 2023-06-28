import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Generate some random data
np.random.seed(0)
X = np.linspace(-5, 5, 100).reshape(-1, 1)
#The variable X contains an array of values ranging from -5 to 5
#(inclusive) with 100 evenly spaced points.
#It is reshaped to a column vector using .reshape(-1, 1
y = 2 * X**3 - 3 * X**2 + np.random.normal(0, 10, size=X.shape)

# Perform polynomial feature transformation
degree = 3  # Set the degree of the polynomial
poly_features = PolynomialFeatures(degree=degree)
X_poly = poly_features.fit_transform(X)

# Train the polynomial regression model
model = LinearRegression()
model.fit(X_poly, y)

# Make predictions
y_pred = model.predict(X_poly)

# Calculate error metrics
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

# Print error metrics
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("Mean Absolute Error:", mae)
print("R-squared Score:", r2)

# Plot the original data and the polynomial regression curve
plt.scatter(X, y, color='red', label='Original Data')
plt.plot(X, y_pred, color='blue', label='Polynomial Regression')
plt.title("Polynomial Regression")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

