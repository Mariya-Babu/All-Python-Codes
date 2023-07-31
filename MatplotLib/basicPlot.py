import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
# x = [1,2,3,4,5,6,7,8,9]
# y = [10,20,30,40,50,60,70,80,90]
# z = [1,2,3,4,5,6,7,8,9]


# plt.plot(x,y,z,z)
# plt.title('Sample Plotings')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.legend('Hello')
# plt.show()


data = pd.read_csv('./labs/data.csv')
df = pd.DataFrame(data)

x = df.CO2
y = df.Weight

plt.plot(x,y)
plt.xlabel('CO2')
plt.ylabel('Weight')
plt.title('CO2 vs Weight')
plt.legend('Hello')
plt.show()