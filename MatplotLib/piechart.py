#PieChart Example 
import matplotlib.pyplot as plt

fruits = ['Orange','Apple','Mango','PineApple']
x  = [90,30,12,78]

plt.pie(x,labels=fruits, autopct="%2.0f%%",explode=[0,0,0.2,0])
plt.show()