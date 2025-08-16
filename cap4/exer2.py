import numpy as np

arr1 = np.arange(0, 51, 2)
arr2 = np.arange(100, 49, -2)

arr_concatenated = np.concatenate((arr1, arr2))

arr_sorted = np.sort(arr_concatenated)

print(arr_sorted)