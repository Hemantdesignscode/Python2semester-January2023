
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure()

axes1 = fig.add_axes([1,0,1,1])
axes2 = fig.add_axes([0,0,1,1])

x = np.linspace(-50, 50, 10)
x_squared = x ** 2
x_cubed = x ** 3

axes1 = fig.add_subplot(1, 2, 1)
axes1.plot(x, x_squared, marker = "s",label = "y = x{}".format(chr(178)))
axes1.legend(loc = "upper left") 
plt.xlabel("x-axis")
plt.ylabel("y-axis")
axes2 = fig.add_subplot(1, 2, 2)
axes2.plot(x, x_cubed, color = "k", marker = "o",label = "y = x{}".format(chr(179)))
axes2.legend(loc = "upper left") 
plt.xlabel("second x-axis")
plt.ylabel("second y-axis")

plt.suptitle("Lab_Assignment_01")


fig, axes2 = plt.subplots(2)
axes2[0].plot(x, x_squared, color = "red", marker = ",",label = "y = x{}".format(chr(178)))
axes2[0].legend(loc = "upper left")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
axes2[1].plot(x, x_cubed, color = "m", marker = ">",label = "y = x{}".format(chr(179)))
axes2[1].legend(loc = "upper left")
plt.xlabel("second x-axis")
plt.ylabel("second y-axis")

plt.suptitle("Lab_Assignment_01")

plt.show()