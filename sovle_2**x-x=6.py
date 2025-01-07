
#############################
#Solve 2**x + x = 6
#############################
# 2**x=6-x
# y1 = y2

#y1=2**x
#y2=6-x


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)
y1 = 2 ** x

plt.plot(x, y1)
plt.title('y1 = 2^x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()



x = np.linspace(-10, 10, 400)
y2 = 6 - x

plt.plot(x, y2)
plt.title('y2 = 6 - x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.show()


#plotting both lines at the same time

x = np.linspace(0, 5, 50)
y1 = 2 ** x
y2 = 6 - x

plt.plot(x, y1, label='y = 2^x')
plt.plot(x, y2, label='y = 6 - x')
plt.title('Plot of y = 2^x and y = 6 - x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend()
plt.show()


