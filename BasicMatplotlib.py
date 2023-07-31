# import matplotlib.plot as plt
from matplotlib import pyplot as plt
x = [1,2,3,4,5,6,7]

y = [9,12,15,67,45,90,34]

plt.xlabel('Cars')
plt.ylabel('Costs')
plt.legend('Cars and their prices!')
plt.title('Line Plot\'s ' )

plt.plot(x,y)
plt.show()
