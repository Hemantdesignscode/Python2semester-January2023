
import pandas as pd
import numpy as np

list_1 = [1,2,3,4,5]
arr = np.array([6,7,8,9,10])
dict_1 = {
    "f": 11,
    "g": 12,
    "h": 13,
    "i": 14,
    "j": 15
}

s1 = pd.Series(list_1, name = "panda lab5")
s2 = pd.Series(arr, index = ["a","b","c","d","e"])
s3 = pd.Series(dict_1)

print(f"\nTHE LIST WITH THE NAME CHANGE ∨ \n{s1}\n")
print(f"THE ARRAY WITH THE INDEX CHANGED TO ALPHABETS ∨ \n{s2}\n")
print(f"THE DICTIONARY WITH NO CHANGE ∨ \n{s3}\n")