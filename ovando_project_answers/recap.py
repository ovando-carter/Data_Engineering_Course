import numpy as np

arr = np.array([1,2,3,4])

print(arr)

arr1 = np.array(range(10))

print(arr1)

# a quicker way to do the same thing
arr2 = np.arange(10)

print(arr2)

array_1d = np.arange(10)

array_2d = array_1d.reshape(2,5)

print(array_2d)