import matplotlib.pyplot as plt
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [20, 35, 30, 15]
fig, ax = plt.subplots()
ax.bar(categories, values)
ax.set_title('Bar Chart')
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
plt.show()
