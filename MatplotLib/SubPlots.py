#SubPlots Exaples Practice
import matplotlib.pyplot as plt

x1 = [1,2,3,4,5,6,7]
y1 = [10,20,30,40,50,60,70]

x2 = [11,19,12,34,76,89,23]
y2 = [10,34,23,15,19,49,37]

x3 = [90,70,50,30,12,45]
y3 = [90,70,50,30,12,45]

x4 = [1,2,3,4,5,6,7,8,9]
y4 = [1,8,27,64,125,118,171,206,349]

plt.show()
plt.suptitle('Sub Classes Example')

plt.subplot(2,2,1)
plt.plot(x1,y1)
plt.show()
plt.title('Plot-1')

plt.subplot(2,2,2)
plt.plot(x2,{1,2,3,4,5,6,7})
plt.show()
plt.title('Plot-2')

plt.subplot(2,2,3)
plt.plot(x3,y3)
plt.show()
plt.title('Plot-3')

plt.subplot(2,2,4)
plt.plot(x4,y4)
plt.show()
plt.title('Plot-4')
