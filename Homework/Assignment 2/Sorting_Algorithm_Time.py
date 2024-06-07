
import numpy as np 
import time
import sys

sys.setrecursionlimit(10000000)

arr = np.random.randint(0, 10000000, 10000)

arr1 = np.copy(arr)
arr2 = np.copy(arr)
arr3 = np.copy(arr)
arr4 = list(np.copy(arr))

def BubbleSort(arr1):
    n = len(arr1)

    if n <= 1:
        return arr1
    
    for _ in range (n):
        for j in range (n-_-1):
            if arr1[j] > arr1[j+1]:

                (arr1[j],arr1[j+1]) = (arr1[j+1],arr1[j])
    return arr1

Starttime = time.time()
BubbleSort(arr1)
Endtime = time.time()

print("\nThe Sorted Array for Bubble Sort is {}\n".format(BubbleSort(arr1)))
print("The Running Time For Bubble Sort is {}\n".format(Endtime - Starttime))

def InsertSort(arr2):
    n = len(arr2)

    if n <= 1:
        return arr2
    
    for _ in range (1,n):
        j=_
        target = arr2[_]

        while j>0 and target < arr2 [j-1]:
            arr2[j] = arr2[j-1]
            j = j-1
        
        arr2[j] = target 
    return arr2

Starttime2 = time.time()
InsertSort(arr2)
Endtime2 = time.time()

print("The Sorted Array for Insertion Sort is {}\n".format(InsertSort(arr2)))
print("The Running Time For Insertion Sort is {}\n".format(Endtime2 - Starttime2))

def quick_sort(arr3):
    less = []
    pivotList = []
    more = []

    if len(arr3) <= 1:
        return arr3
    
    else:

        pivot = arr3[0]
        for _ in arr3:
            
            if _ < pivot:
                less.append(_)

            elif _ > pivot:
                more.append(_)

            else:
                pivotList.append(_)

        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivotList + more

Starttime3 = time.time()
print("The Sorted Array for Quick Sort is {}".format(quick_sort(arr3)))
Endtime3 = time.time()

print("\nThe Running Time For Quick Sort is {}\n".format(Endtime3 - Starttime3))

def MergeSort(arr4):
    def merge(left, right):
        result = []
        _ = j = 0
        while _ < len(left) and j < len(right):
            if left[_] <= right[j]:
                result.append(left[_])
                _ += 1
            else:
                result.append(right[j])
                j += 1
        result = result + left[_:] + right[j:]
        return result
    if len(arr4) <= 1:
        return arr4
    mid = len(arr4) // 2
    left = MergeSort(arr4[:mid])
    right = MergeSort(arr4[mid:])
    return merge(left, right)

Starttime4 = time.time()
print("The Sorted Array for Merge Sort is {}".format(MergeSort(arr4)))
Endtime4 = time.time()

print("\nThe Running Time For Merge Sort is {}\n".format(Endtime4 - Starttime4))