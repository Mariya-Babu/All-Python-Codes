import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("C:\\Users\\G.Ajay kumar\\Desktop\\ds_salaries.csv")
df=pd.DataFrame(df)
data=df.loc[0:6]
print(df.loc[0:6])
"""
#line plots
x=np.arange(len(df))
y=df["salary_in_usd"]

plt.plot(x, c='r',lw='10')
plt.xlabel("points")
plt.ylabel("salaries")
plt.title("line plots")
plt.show()
"""
"""#area plots
x=[1,2,3,4,5,6,7]
y1=data["salary_in_usd"]
plt.fill_between(x, y1, color='blue', alpha=0.3, label='A')
plt.show()


#histograms
data=data["salary_in_usd"]
plt.hist(data,bins=7,edgecolor='r')
plt.xlabel("persons")
plt.ylabel("salaries")
plt.title("salaries between intervals")
plt.show()"""

#bar graphs
x=['data scientist','machine learning','artificial intelligence']
y=[175000,125000,200000]
plt.bar(x,y,width=0.2)
plt.xlabel("engineers")
plt.ylabel("salaries")
plt.show()

#pie charts
x=['data scientist','machine learning','artificial intelligence']
y=[175000,125000,200000]
m=[0,0.1,0]
plt.pie(y,labels=x,explode=m,autopct="%1.1f%%")#1.1f%%
plt.show()


#scatter plots
import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()
