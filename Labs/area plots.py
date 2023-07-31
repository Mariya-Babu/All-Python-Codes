import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [1, 3, 2, 4, 3]
y2 = [2, 4, 1, 3, 2]
y3 = [3, 1, 4, 2, 5]
fig, ax = plt.subplots()
ax.fill_between(x, y1, color='blue', alpha=0.3, label='A')
ax.fill_between(x, y1, y2, color='green', alpha=0.3, label='B')
ax.fill_between(x, y2, y3, color='orange', alpha=0.3, label='C')
ax.set_title('Area Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()
plt.show()
