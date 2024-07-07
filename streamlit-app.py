import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Sine Wave Plot')

# Sidebar widget for adjusting frequency
frequency = st.sidebar.slider('Frequency', 1, 10, 5)

# Generate data
x = np.linspace(0, 10, 100)
y = np.sin(frequency * x)

# Plot
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Sin(x)')
st.pyplot(plt)
