import numpy as np

arr1 = np.ones(8)
arr2 = np.random.randint(1, 10, 8)

soma_arr = arr1 + arr2

soma = soma_arr.sum()

if(soma >= 40):
    soma_arr.reshape(4, 2)
else:
    soma_arr.reshape(2, 4)