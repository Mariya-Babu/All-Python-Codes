"""Data Visualization.py

1)Bar chart
"""

import matplotlib.pyplot as plt

# Sample data
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
values = [25, 50, 75, 100]

# Create a bar chart
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')

# Display the chart
plt.show()

"""2)Line plot"""

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y, marker='o', linestyle='-', color='b')

# Customize the plot
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Line Plot')

# Display the plot
plt.show()

"""3) Area plot"""

import matplotlib.pyplot as plt

# Sample data
years = [2010, 2011, 2012, 2013, 2014, 2015]
variable1 = [2, 5, 8, 6, 9, 3]
variable2 = [1, 3, 2, 7, 5, 4]
variable3 = [6, 8, 7, 3, 2, 5]

# Plotting
plt.stackplot(years, variable1, variable2, variable3, labels=['Variable 1', 'Variable 2', 'Variable 3'])
plt.legend(loc='upper left')
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Area Plot')
plt.show()

"""4) histogram"""

import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30, alpha=0.5, color='steelblue')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

"""5) PIe chart

"""

import matplotlib.pyplot as plt

# Data for the pie chart
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [30, 20, 25, 15]

# Creating the pie chart
plt.pie(values, labels=categories, autopct='%1.1f%%')

# Aspect ratio to make the pie circular, if desired
plt.axis('equal')

# Adding a title
plt.title('Pie Chart Example')

# Displaying the chart
plt.show()

"""6)Boxplot

"""

import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
np.random.seed(1)
data1 = np.random.normal(loc=0, scale=1, size=100)
data2 = np.random.normal(loc=2, scale=1, size=100)
data3 = np.random.normal(loc=4, scale=1, size=100)

# Create a list of data sets
data = [data1, data2, data3]

# Create a figure and axis
fig, ax = plt.subplots()

# Create a box plot
bp = ax.boxplot(data)

# Add labels and title
ax.set_xticklabels(['Data 1', 'Data 2', 'Data 3'])
ax.set_xlabel('Data Sets')
ax.set_ylabel('Values')
ax.set_title('Box Plot Example')

"""7) Scatter plot

"""

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a scatter plot
plt.scatter(x, y)

# Customize the plot
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()

"""8) Bubble plot"""

import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.rand(50) * 100  # Random sizes for the bubbles

# Create the scatter plot with bubble sizes
plt.scatter(x, y, s=sizes, alpha=0.5)

# Set labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bubble Plot')

# Show the plot
plt.show()

