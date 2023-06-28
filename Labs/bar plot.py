import matplotlib.pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [20, 35, 30, 15]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the bar chart
ax.bar(categories, values)

# Customize the plot
ax.set_title('Bar Chart')
ax.set_xlabel('Categories')
ax.set_ylabel('Values')

# Display the plot
plt.show()
