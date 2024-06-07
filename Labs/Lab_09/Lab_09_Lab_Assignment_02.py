
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataframe_reading = pd.read_csv("C:\\Users\\Heman\\Documents\\Computer Science 1302\\DataFrame_March_20.csv")

dataframe_reading.plot(x = "Age", y = "Score", color = "Red", ls = "--")

plt.show()