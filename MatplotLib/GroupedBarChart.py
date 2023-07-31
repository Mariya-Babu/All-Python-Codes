#Stacked Bar Chart Example
import matplotlib.pyplot as plt
import numpy as np

x = ['2012','2013','2014','2015','2016']

cse = [40,20,50,67,78]
ece = [56,64,72,80,74]
civil = [90,81,70,55,50]
w = 0.2

cse_start = np.arange(len(x))
ece_start = [i+w for i in cse_start]
civil_start = [i+w for i in ece_start]

# plt.bar(x,cse)
# plt.bar(x,ece)
# plt.bar(x,civil)
plt.bar(cse_start,cse,width=w)
plt.bar(ece_start,ece,width=w)
plt.bar(civil_start,civil,width=w)

# plt.xticks(x)
# plt.xticks(ticks=x)
plt.show()



