import matplotlib.pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [30, 15, 45, 10]
colors = ['blue', 'green', 'orange', 'red']
explode = (0, 0.1, 0, 0)  # Explode the second slice

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the pie chart
ax.pie(values, labels=categories, colors=colors, explode=explode, autopct='%1.1f%%')

# Customize the plot
ax.set_title('Pie Chart')

# Display the plot
plt.show()
