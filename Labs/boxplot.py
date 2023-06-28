import numpy as np
import matplotlib.pyplot as plt

# Generate some random data
np.random.seed(0)
data = [np.random.normal(0, 1, 100),
        np.random.normal(2, 1, 100),
        np.random.normal(1, 2, 100),
        np.random.normal(3, 2, 100)]
#np.random.normal(2, 1, 100): This generates an array of 100
#random numbers drawn from a normal distribution with a mean of 2
#and a standard deviation of 1. It represents the second group of data

# Create the box plot
plt.boxplot(data)

# Add labels and title
plt.xlabel("Data Groups")
plt.ylabel("Values")
plt.title("Box Plot")

# Show the plot
plt.show()
