import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [1, 3, 2, 4, 3]
y2 = [2, 4, 1, 3, 2]
y3 = [3, 1, 4, 2, 5]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the area
ax.fill_between(x, y1, color='blue', alpha=0.3, label='A')
ax.fill_between(x, y1, y2, color='green', alpha=0.3, label='B')
ax.fill_between(x, y2, y3, color='orange', alpha=0.3, label='C')

# Customize the plot
ax.set_title('Area Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()

# Display the plot
plt.show()
