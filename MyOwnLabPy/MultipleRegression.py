import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('C:\\Users\\RISHI\\Desktop\\PyCodes\\CSV\\Employee.csv')
df=df.drop('Exit Date',axis=1)

X=df.drop('Age',axis=1)
y=df['Age']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,y_train)


pred=model.predict(X_test)
print(pred)

from sklearn.metrics import mean_absolute_error
error=mean_absolute_error(pred,y_test)
print(error)
