# Program Lab 4 Assignment 01 - CSC 1302 Lab
# Author: Hemant Kosaraju
# Email: hkosaraju2@student.gsu.edu

import numpy as np
array1 = np.arange(0,25).reshape(5,5)
print(f"\nTHIS IS ARRAY 1: \n\n{array1}")
print(f"\nTHIS IS THE SUM OF ARRAY 1: {array1.sum()}")
print(f"\nTHIS IS THE ARGMIN OF ARRAY 1: {array1.argmin(axis=0)}")
print(f"\nTHIS IS THE ARGMAX OF ARRAY 1: {array1.argmax(axis=1)}")
print()