import seaborn as sns
import matplotlib.pyplot as plt

# Line plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
sns.lineplot(x=x, y=y)
plt.show()

# Area plot (using fill_between from Matplotlib)
plt.fill_between(x, y)
plt.show()

# Histogram (using distplot from Seaborn)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sns.histplot(x)
plt.show()

# Bar chart
x = ["A", "B", "C", "D", "E"]
y = [10, 20, 30, 40, 50]
sns.barplot(x=x, y=y)
plt.show()

# Pie chart
labels = ["A", "B", "C", "D", "E"]
sizes = [10, 20, 30, 40, 50]
plt.pie(sizes, labels=labels)
plt.show()

# Box plot
x = ["A", "B", "C", "D", "E"]
y = [10, 20, 30, 40, 50]
sns.boxplot(x=x, y=y)
plt.show()

# Scatter plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
sns.scatterplot(x=x, y=y)
plt.show()

# Regression plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
sns.regplot(x=x, y=y)
plt.show()
