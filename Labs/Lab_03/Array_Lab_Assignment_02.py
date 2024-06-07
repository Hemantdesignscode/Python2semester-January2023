
# Code's Author: Hemant Kosaraju, Email: hkosaraju2@student.gsu.edu 
import numpy as np

array = np.random.randint(0,100,(30,3))
print("\nTHIS IS A RANDOM ARRAY FROM 0 TO 100 WITH THE SHAPE (30,3): ")
print(f"\n{array}\n")

print("THIS IS A RANDOM ARRAY FROM 0 TO 100 AFTER CHANGING THE SHAPE TO (18,5): ")
array1 = array.reshape(18,5)
print(f"\n{array1}\n")

print("THIS IS THE INFORMATION EXTRACTED FROM THE SECOND COLUMN AND EVERYTHING AFTER IT")
sliced_array = array[:,1:]
print(f"\n{sliced_array}\n")

print("THIS IS THE INFORMATION EXTRACTED FROM THE FIFTH ROW SECOND COLUMN TO THE EIGHTH ROW SECOND COLUMN: ")
another_sliced_array = array[4:8,1:2]
print(f"\n{another_sliced_array}\n")