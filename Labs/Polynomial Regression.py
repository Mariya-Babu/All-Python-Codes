#!/usr/bin/env python
# coding: utf-8

# # Polynomial Regression

# ## Importing Libraries

# In[29]:


import pandas as pd
import numpy as np



# In[30]:


df = pd.read_csv('C:\\Users\\RISHI\\Desktop\\PyCodes\\Labs\\data.csv')


# In[31]:


df


# ## Analysing the Dataset

# In[32]:


df.describe()


# In[34]:


X=df.iloc[:,1:2].values  


# In[36]:


y=df.iloc[:,2].values   


# In[37]:


X


# In[38]:


y


# ## Linear Regression with degree 1

# In[39]:


from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(X,y)


# ## Linear Regression with degree 2

# In[40]:


from sklearn.preprocessing import PolynomialFeatures
poly_reg2=PolynomialFeatures(degree=2)
X_poly=poly_reg2.fit_transform(X)
lin_reg_2=LinearRegression()
lin_reg_2.fit(X_poly,y)


# ## Linear Regression with degree 3

# In[41]:


poly_reg3=PolynomialFeatures(degree=3)
X_poly3=poly_reg3.fit_transform(X)
lin_reg_3=LinearRegression()
lin_reg_3.fit(X_poly3,y)


# # Plotting the Graph between Salary and Position Level

# In[42]:


plt.scatter(X,y,color='red')
plt.plot(X,lin_reg.predict(X),color='blue')
plt.title('Truth Or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


# In[43]:


plt.scatter(X,y,color='red')
plt.plot(X,lin_reg_2.predict(poly_reg2.fit_transform(X)),color='blue')
plt.plot(X,lin_reg_3.predict(poly_reg3.fit_transform(X)),color='green')
plt.title('Truth Or Bluff (Polynomial Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


# In[44]:


X_grid=np.arange(min(X),max(X),0.1) # This will give us a vector.We will have to convert this into a matrix 
X_grid=X_grid.reshape((len(X_grid),1))
plt.scatter(X,y,color='red')
plt.plot(X_grid,lin_reg_3.predict(poly_reg3.fit_transform(X_grid)),color='blue')
#plt.plot(X,lin_reg_3.predict(poly_reg3.fit_transform(X)),color='green')
plt.title('Truth Or Bluff (Polynomial Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


# In[45]:


lin_reg.predict([[6.5]])


# In[46]:


lin_reg_2.predict(poly_reg2.fit_transform([[6.5]]))


# In[47]:


lin_reg_3.predict(poly_reg3.fit_transform([[6.5]]))

