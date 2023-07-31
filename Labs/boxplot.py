import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
data = [np.random.normal(0, 1, 100),
        np.random.normal(2, 1, 100),
        np.random.normal(1, 2, 100),
        np.random.normal(3, 2, 100)]
plt.boxplot(data)
plt.xlabel("Data Groups")
plt.ylabel("Values")
plt.title("Box Plot")
plt.show()
