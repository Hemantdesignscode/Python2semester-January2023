# Program Lab 4 Assignment 02 - CSC 1302 Lab
# Author: Hemant Kosaraju
# Email: hkosaraju2@student.gsu.edu

import time
import numpy as np
one_dimension_array = np.arange(0,100000)
list_arange = [*range(0,100000)] # THE * OPERATOR IN FRONT OF THE RANGE IS AN ARGUMENT UNPACKING OPERATOR *
Start_time = time.time()
print(f"\nTHE SUM OF ONE DIMENSION ARRAY : {one_dimension_array.sum()}")
End_time = time.time()

Start_time2 = time.time()
sum = 0
for _ in list_arange:
    sum += _
End_time2 = time.time()
print(f"\nTHE SUM OF LIST : {sum}\n")

total_time_array = End_time - Start_time
total_time_list = End_time2 - Start_time2

print(f"THIS IS THE TOTAL TIME DIFFERENCE IT TAKES TO PRINT THE ARRAY\'S SUM: {total_time_array}")
print(f"\nTHIS IS THE TOTAL TIME DIFFERENCE IT TAKES TO PRINT THE LIST\'S SUM: {total_time_list}\n")