import matplotlib.pyplot as plt
import random

x = [1,2,3,4,5,6,7,8]
y = [10,20,30,40,50,60,70,80]

random.shuffle(y)

# plt.plot(x,y,label='Hello')
plt.scatter(x,y)
plt.legend()
plt.show()
