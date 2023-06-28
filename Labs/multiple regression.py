#importing pandas
import pandas as pd
#importing data set
df=pd.read_csv('C:\\Users\\RISHI\\Desktop\\PyCodes\\Labs\\data.csv')
#making list of independent variales as x and dependent variable as y
X = df[['Weight', 'Volume']]
y = df['CO2']
#to import this sklearn pip install -U scikit-learn
from sklearn import linear_model
regr = linear_model.LinearRegression()
regr.fit(X, y)
predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2)
print(regr.coef_)
predictedCO2 = regr.predict([[3300, 1300]])
print(predictedCO2)
