import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\Users\\RISHI\\Desktop\\PyCodes\\Labs\\dataset.csv")
df=df.head(10)
print(df)
print(df.columns)
print(df.isnull().sum())#to clean the data
print(df.describe())
x=df.drop('Salary',axis=1)#these are features ,except salary all the columns are there in x
y=df['Salary']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,y_train)
pred=model.predict(X_test)
print(pred)
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
mse = mean_squared_error(y_test, pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, pred)
r2 = r2_score(y_test, pred)
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("Mean Absolute Error:", mae)
print("R-squared Score:", r2)
import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.show()
plt.scatter(X_train, y_train, color='red') # plotting the observation line
plt.plot(X_train, model.predict(X_train), color='blue') # plotting the regression line
plt.title("salary vs experience (Training set)") # stating the title of the graph
plt.xlabel("years of experience") # adding the name of x-axis
plt.ylabel("salary") # adding the name of y-axis
plt.show() # specifies end of graph
plt.scatter(X_test, y_test, color='red') 
plt.plot(X_train, model.predict(X_train), color='blue') # plotting the regression line
plt.title("salary vs experience (Testing set)")
plt.xlabel("years of experience") 
plt.ylabel("salary")
plt.show()