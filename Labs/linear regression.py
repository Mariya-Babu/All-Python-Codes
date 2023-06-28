import pandas as pd
df=pd.read_csv("C:\\Users\\RISHI\\Desktop\\PyCodes\\Labs\\data.csv")
df.head()
data_=df.loc[:,['Weight','CO2']]
print(data_.head(10))
#showing the data in matplotlib
#to use we need to first install matplotlib
import matplotlib.pyplot as plt
df.plot(x='Weight',y='CO2',style='o')
plt.xlabel('Weight')
plt.ylabel('CO2')
plt.show()
#dividing the variables into dependent and independent
X=pd.DataFrame(df['Weight'])
y=pd.DataFrame(df['CO2'])
#Split the data into train and test sets
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1)
#knowing the shapes of the test and train
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

#train the algorithm
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)
#retriving the intercept
print(regressor.intercept_)
#retriving the slope
print(regressor.coef_)
#predecting the test results
y_pred = regressor.predict(X_test)
y_test
print(y_pred)
print(y_test)
#evaluting the algorithm
from sklearn import metrics
import numpy as np
print('Mean Absolute Error:',metrics.mean_absolute_error(y_test,y_pred))
print('Mean Squared Error:',metrics.mean_squared_error(y_test,y_pred))
print('Root Mean Squared Error:',np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

#plot for the train set
plt.scatter(X_train, y_train, color='red') # plotting the observation line

plt.plot(X_train, regressor.predict(X_train), color='blue') # plotting the regression line

plt.title("Weight vs CO2 (Training set)") # stating the title of the graph

plt.xlabel("Weight") # adding the name of x-axis
plt.ylabel("CO2") # adding the name of y-axis
plt.show() # specifies end of graph


#plot for the test set
 
plt.scatter(X_test, y_test, color='red') 
plt.plot(X_train, regressor.predict(X_train), color='blue') # plotting the regression line
plt.title("Weight vs CO2 (Testing set)")
 
plt.xlabel("Weight") 
plt.ylabel("CO2") 
plt.show() 
