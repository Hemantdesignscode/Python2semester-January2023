
from matplotlib import pyplot as plt
import numpy as np

x_axis = np.linspace(-10, 10, 50)
y_axis = x_axis ** 3

plt.plot(x_axis, y_axis, lw = 10, color = "blue", ls = "--")
plt.title("Cubic Function")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.show()