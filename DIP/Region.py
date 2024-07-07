import numpy as np 
import matplotlib.pyplot as plt 
image = np.ones((6,6))
image[2:4,2:4] = 6
image[4:6,3:6] = 8
image[4,5] = 9
image[3,4] = 5
plt.imshow(image)