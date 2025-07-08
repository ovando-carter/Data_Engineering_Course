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

lst_from_arr = array_1d.tolist()

print('list from array: ', lst_from_arr)

arrayShape = array_2d.shape

print(arrayShape)

selectElement = array_2d[0][3]

print(selectElement)

index = np.where(array_1d == 4)

print(index)