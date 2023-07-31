#Stacked Bar Chart Example
import matplotlib.pyplot as plt

x = ['2012','2013','2014','2015','2016']

cse = [40,20,50,67,78]
ece = [56,64,72,80,74]
civil = [90,81,70,55,50]
civil_start = [cse[i] + ece[i] for i in range(len(x))]

plt.bar(x,cse,bottom=0)
plt.bar(x,ece,bottom=cse)
plt.bar(x,civil,bottom=civil_start)
plt.show()
