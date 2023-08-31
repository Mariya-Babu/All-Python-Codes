# Basic Matrix operations
import numpy as np
p = np.array([[1,2],[2,1],[3,2]])
q = np.array([[4,5],[2,3],[3,1]])

a = np.add(p,q)
print(a)

b = np.subtract(p,q)
print(b)

r = np.array([[4,5],[3,4]])
c = np.dot(p,r)
print(c)
