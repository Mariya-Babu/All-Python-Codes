import matplotlib.pyplot as plt
import random
# x = [1,2,3,4,5]
x = ['A','B','C','D','E']
y = [10,20,34,41,59]
c = ['Black','Red','blue','yellow','green']

random.shuffle(y)
# plt.plot(x,y)
plt.bar(x,y,color=c)
plt.show()