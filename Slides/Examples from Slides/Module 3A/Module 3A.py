#####################
# Module 3A - NumPy #
#####################
# importing NumPy library (module)
import numpy as np

# slide 5
# (create an array from list)
arr = np.array([1, 2, 3, 4])
print(arr)

# Creating NumPy arrays
# slide 8
# 1) using arange() function
arr = np.arange(10)  # arr = [0 1 2 3 4 5 6 7 8 9]
print(arr)


# slide 9 - shape property returns the dimensionality of an array
# (The array dimension is a level of array depth)
print(arr.shape)  # prints (10,)
# shape returns a sequence of values within brackets
# separated with comma. The number of values denote the
# dimensionality of the array. The value(s) denote the number
# In the above example shape returns (10,) meaning the arr
# has 1 dimesnion and 10 elements in its 1st dimension
# of elements in that dimension.

# Alternatively, use the ndim array attribute to obtain the
# dimensionality of an array as an integer value
print(arr.ndim)  # prints 1 (meaning arr is 1-D array)


# slide 10
arr = np.arange(10,16,2)  
print(arr)   # prints [10 12 14]

arr = np.arange(10,15,1)
print(arr)   # prints [10 11 12 13 14]

arr = np.arange(10,15)  # the default step is 1
print(arr)   # prints [10 11 12 13 14]


# slide 11-12
# 2) using reshape() function
arr_2D = np.arange(10).reshape(2,5)
print(arr_2D)
# step 1 - create a 1D array of 10 elements:
arr_1D = np.arange(10)
# step 2 - reshape the 1-D array arr_1D to a 2-D array arr_2D
arr_2D = arr_1D.reshape(2,5)
print(arr_2D)
'''
The output (arr_2D) is:
[[0 1 2 3 4]
 [5 6 7 8 9]]
 The number of 1-D arrays is 2 (2 1-D arrays)
 The number of elements in each of the 1-D arrays is 5 (scalars, 0-D arrays)
'''
print(arr_2D.shape)  # prints (2, 5)
print(arr_2D.ndim)   # prints 2

arr_2D = np.arange(10).reshape(5,2)
print(arr_2D)
''' The output is:
[[0 1] - 1st 1-D array, consisting of 2 0-D arrays (scalars): 0, 1
 [2 3] - 2nd 1-D array, consisting of 2 0-D arrays (scalars): 2, 3
 [4 5]
 [6 7]
 [8 9] - 5th 1-D array, consisting of 2 0-D arrays (scalars): 8, 9
]
'''


# slide 13 - 3-D arrays
arr_3D = np.arange(12).reshape(2,2,3)
print(arr_3D)
'''
The output (arr_3D) is:
[[[ 0  1  2]
  [ 3  4  5]]

 [[ 6  7  8]
  [ 9 10 11]]]


[ [ [ 0  1  2] - 1st element at 1-D
    [ 3  4  5] - 2nd element at 1-D
  ] - 1st element at 2-D

  [ [ 6  7  8]
    [ 9 10 11]
  ] - 2nd element at 2-D
]

'''
print(arr_2D.shape)  # prints (2, 5)
print(arr_2D.ndim)   # prints 2


# slide 15
arr_3D = np.arange(12).reshape(2,2,3)
print(arr_3D)
#arr_3D = arr_3D.reshape(3, 2, 1)  # throws ValueError: cannot reshape array of size 12 into shape (3,2,1)
# because 3 x 2 x 1 != 12
# to convert the above 3-D array back to 1-D array ('flatten the array'):
arr_1D = arr_3D.reshape(-1)
print(arr_1D)  # prints [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(arr_1D.ndim) # prints 1


# slide 16 - zeroes() function - creates arrays consisting of values 0
arr_1D = np.zeros((2,))  # 2 - number of elements at a specific dimension
print(arr_1D)  # prints [0. 0.]
arr_1D = np.zeros((5,))
print(arr_1D)  # prints [0. 0. 0. 0. 0.]

arr_2D = np.zeros((2,4))
print(arr_2D)

arr_3D = np.zeros((2,2,3))
print(arr_3D)

# default data type is float, to change data type use dtype kwarg:
arr_3D = np.zeros((2,2,3), dtype=int)
print(arr_3D)


# slide 17 - ones() function - creates arrays consisting of values 1
arr_1D = np.ones((2,))  # 2 - number of elements at a specific dimension
print(arr_1D)  # prints [1. 1.]
arr_1D = np.ones((5,))
print(arr_1D)  # prints [1. 1. 1. 1. 1.]

arr_2D = np.ones((2,4))
print(arr_2D)

arr_3D = np.ones((2,2,3))
print(arr_3D)

# default data type is float, to change data type use dtype kwarg:
arr_3D = np.ones((2,2,3), dtype=int)
print(arr_3D)


# slide 18 - empty() function - creates arrasy with random content
# empty() can be used to initialise an array of strings:
arr_1D = np.empty((5,), dtype=str)
print(arr_1D) # prints ['' '' '' '' '']

arr_2D = np.empty((2,3), dtype=str)
print(arr_2D)

# or to initiallise an array of boolean data type
arr_2D = np.empty((2,3), dtype=bool)
print(arr_2D)

# 2. by converting a list to an array
arr = np.array([1, 2, 3])
print(arr)
# Note: list elements must be of the same data type
arr = np.array([1, 2, 3.3])
# produces [1 2 3] (converts float 3.3 to int 3)
# naming the list:
lst = [1, 2, 3]
arr = np.array(lst)
print(arr)  # prints [1 2 3] (an array)

# converting the array back to a list:
lst = arr.tolist()
print(lst)  # print [1, 2, 3] (a list)


# slide 22
# To create a two-dimensional array from lists, pass a sequence of lists and/or tuples to the array function 
arr = np.array([(1,2,3), [4,5,6]])
print(arr)
# You can define the number of dimensions by using the ndmin argument in the array function.
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
'''
[
 [
   [
     [
       [1 2 3 4]
     ]
   ]
 ]
]
'''
print(arr.shape)  # prints (1, 1, 1, 1, 4)


# slide 23
arr = np.random.random((2,2))
print(arr)
print(arr.shape)  # prints (2, 2)


# slide 24
arr = np.array([1, 2, 3, 4])
print(arr[0])  #prints 1
print(arr[1])  #prints 2
print(arr[3])  #prints 4
print(arr[-1])  #prints 4


# slide 25
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr)
print('4th element of the 1st dim:', arr[0, 3])
print('Last element of the 2nd dim:', arr[1, 4])
print('Last element of the 2nd dim:', arr[1, -1])


# slide 26
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print(arr.shape)  # prints (2, 2, 3)
print('3rd element of the 2nd dimension of the 1st dimension:', arr[0,1,2])


# slide 27 - Logical operations on arrays
a = np.array([True, True, False, False])
b = np.array([True, False, True, False])
print(np.logical_and(a, b))
print(a & b)


# slide 28
c = np.arange(5)
print(c)  # prints [0 1 2 3 4]
print(np.logical_and(c > 1, c < 4))  # prints [False False  True  True False]
print(np.logical_or(c > 1, c < 4))   # prints [ True  True  True  True  True]


# slide 29
print(c[np.logical_and(c > 1, c < 4)])  # prints [2 3]


# slide 30 - arithmetic operations on arrays
# All arithmetic operations apply to two arrays of the same
# shape, elementwise.
a = np.array([10, 10, 10])
b = np.array([5, 5, 5])
c = a + b
print(c)  # [15 15 15]

a = np.array([10, 10, 10])
b = np.array([5, 5])
#c = a + b  # ValueError: operands could not be broadcast together with shapes (3,) (2,)
#c = a * b   # ValueError: operands could not be broadcast together with shapes (3,) (2,)


# slide 31
# All arithmetic operations can be applied between arrays and scalars.
a = np.array([10, 10, 10])
b = a * 3  # [30 30 30]
c = a ** 3 # [1000 1000 1000] 
d = a % 3  # [1 1 1]
print(b, c, d)

a = np.array([7, 8, 9])
print(a < 9) # [ True  True False]


# slide 32
# NumPy Arrays are mutable, which means that you can change
# the value of an element in the array after an array has been
# initialized
arr_1D = np.arange(10)
print(arr_1D)
arr_1D[3] = 100  # changes the 4th array element (with index 3) to 100
print(arr_1D)   # [  0   1   2 100   4   5   6   7   8   9]
# an attempt to assign a value of different data type throws an error:
#arr_1D[3] = 'string'  # throws ValueError: invalid literal for int() with base 10: 'string'


# slide 33
arr_2D = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr_2D)
arr_2D[1][3] = 100
print(arr_2D)


# slide 34
arr_3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr_3D)
arr_3D[1][0][2] = 100
print(arr_3D)


# slide 35
arr_ints = np.array([[1,2,3,4,5], [6,7,8,9,10]])
arr_strings = arr_ints.astype(str)
print(arr_strings)


# slide 36 - slicing arrays
# the result includes the start index, but excludes the end index.
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])    # [2 3 4 5]
print(arr[1:5:2])  # [2 4]


# slide 38
# slicing 2-D arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4]) # from the second array, slice elements from index 1 to 3
print(arr[0:2, 2]) # returns element with index 2 from both array elements
print(arr[0:2, 1:4]) # both array elements sliced from index 1 to index 3


# slide 39
arr_2D = np.arange(12).reshape(3,4)
print(arr_2D)
print(arr_2D[1, :]) # returns second row: [4 5 6 7]
print(arr_2D[:, 1]) # returns second column: [1 5 9]


# slide 40
# append(arr, value) – returns a copy of the array arr with
# a new element value added to it at the end; the original
# array arr remains unchanged
arr = np.array([57, 34, 42, 28, 5, 17])  
new_arr = np.append(arr, 100)
print(new_arr)  # [ 57  34  42  28   5  17 100]
print(arr)
# insert(arr, index, value) – returns a copy of the array arr
# with a new element value added to it at the position index;
# the original array arr remains unchanged
new_arr = np.insert(arr, 0, 100)  
print(new_arr)  # [100  57  34  42  28   5  17]
print(arr)


# slide 41
# concatenate((arr1, arr2, arr3, ...)) – returns a copy of two
# or more arrays passed to it, joined together; the original
# arrays passed to it remain unchanged
arr1 = np.array([57, 34, 42, 28, 5, 17])
arr2 = np.array([6, 3, 11])
new_arr = np.concatenate((arr1, arr2))
print(new_arr) # [57 34 42 28  5 17  6  3 11]
new_arr1 = np.concatenate((arr1, [100])) # adds 100 at the end of the array
new_arr2 = np.concatenate(([100], arr1)) # adds 100 at beginning of the array
print(new_arr1) # [ 57  34  42  28   5  17 100]
print(new_arr2) # [100  57  34  42  28   5  17]
# Note: the arrays must be passed to the concatenate function
# within a tuple or a list
new_arr = np.concatenate((arr1, arr2))
# (arr1, arr2) is a tuple consisting of arr1 & arr2
new_arr = np.concatenate([arr1, arr2])
# [arr1, arr2] is a list consisting of arr1 & arr2


# slide 42 - appending a column to a NumPy array
# append(arr, value, axis) function has the 3rd optional kwarg parameter:
# axis, which allows to add a new column or row at the end of a 2-D array
# and in general, append elements to array allong the specified axis.
# If axis is not given, both arr and value are flattened before use.
# Example: add a new column at the end of an existing 2-D array
arr = np.array([[1,2], [3,4], [5,6]])
print("Original 2-D array:\n", arr, sep='')
print(arr.shape)  # (3, 2)

new_col = np.array([[1],[1],[1]])
print("New column:\n", new_col, sep='')
print(new_col.shape)  # (3, 1)

arr_with_new_col = np.append(arr, [[1],[1],[1]], axis=1)  # note: axis=1, as we are adding a row
print("2-D array with a new column:\n", arr_with_new_col, sep='')
print(arr_with_new_col.shape)  # (3, 3)

'''
Example from Notes of slide 42:
Multiple columns can also be appended to an existing NumPy
array. For example, to append 2 columns to the above NumPy
array, the new array must be shaped as (3, 2) – 3 rows as
the existing array has 3 rows, and 2 columns as the new
array has 2 columns:
'''
two_new_cols = np.array([[1, 2], [1, 2], [1, 2]])
print(two_new_cols)
arr_with_new_cols = np.append(arr, two_new_cols, axis=1)
print(arr_with_new_cols)


# slide 43 - appending a row to a NumPy array
# Example: add a new row at the end of an existing 2-D array
print("Original 2-D array:\n", arr, sep='')
print(arr.shape)  # (3, 2)

new_row = np.array([[7,8]])
print("New row:\n", new_row, sep='')
print(new_row.shape)  # (1, 2)

arr_with_new_row = np.append(arr, new_row, axis=0)  # note: axis=0, as we are adding a row
print("2-D array with a new row:\n", arr_with_new_row, sep='')
print(arr_with_new_row.shape)  # (4, 2)

'''
Multiple rows can also be appended to an existing NumPy
array. For example, to append 2 rows to the above NumPy
array, the new array must be shaped as (2, 2) – 2 rows
as the new array has 2 rows, and 2 columns as the existing
array has 2 columns:
'''
two_new_rows = np.array([[7, 8], [9, 10]])
print(two_new_rows)
arr_with_new_rows = np.append(arr, two_new_rows, axis=0)
arr_with_new_rows

# extra example 1: adding an new column to a 3-D array
arr = np.array([[[1,2], [3,4], [5,6]]])
print("Original 3-D array:\n", arr, sep='')
print(arr.shape)  # (1, 3, 2)

new_col = np.array([[[7], [8], [9]]])
print("New column:\n", new_col, sep='')
print(new_col.shape)  # (1, 3, 1)

arr_with_new_col = np.append(arr, new_col, axis=2)  # note: axis=2, as we are adding a column
print("3-D array with a new column:\n", arr_with_new_col, sep='')
print(arr_with_new_col.shape)  # (1, 3, 3)

# extra example 2: adding a new row to a 3-D array:
print("Original 3-D array:\n", arr, sep='')
print(arr.shape)  # (1, 3, 2)

new_row = np.array([[[7, 8]]])
print("New row:\n", new_col, sep='')
print(new_row.shape)  # (1, 1, 2)

arr_with_new_row = np.append(arr, new_row, axis=1)    # note: axis=1, as we are adding a row
print("3-D array with a new row:\n", arr_with_new_row, sep='')
print(arr_with_new_row.shape)  # (1, 4, 2)


# slide 44
# adding a new column to a 2-D array using concatenate()
arr = np.array([[1,2], [3,4], [5,6]])
print("Original 2-D array:\n", arr, sep='')
print(arr.shape)  # (3, 2)

new_col = np.array([[1],[1],[1]])
print("New column:\n", new_col, sep='')
print(new_col.shape)  # (3, 1)

arr_with_new_col = np.concatenate((arr, new_col), axis=1)
print("2-D array with a new column:\n", arr_with_new_col, sep='')
print(arr_with_new_col.shape)  # (3, 3)

# example from notes of slide 44:
# adding multiple columns to an existing array using concatenate:
arr = np.array([[1,2], [3,4], [5,6]])
two_new_cols = np.array([[1, 2], [1, 2], [1, 2]])
arr_with_new_cols = np.concatenate((arr, two_new_cols), axis=1)
print(arr_with_new_cols)


# slide 45
# adding a new row to an existing 2-D array using concatenate()
print("Original 2-D array:\n", arr, sep='')
print(arr.shape)  # (3, 2)

new_row = np.array([[7,8]])
print("New row:\n", new_row, sep='')
print(new_row.shape)  # (1, 2)

arr_with_new_row = np.concatenate((arr, new_row), axis=0)
print("2-D array with a new row:\n", arr_with_new_row, sep='')
print(arr_with_new_row.shape)  # (4, 2)

# example from notes of slide 45:
# adding multiple rows to an existing array using concatenate:
arr = np.array([[1,2], [3,4], [5,6]])
new_rows = np.array([[7,8], [9,10]])
arr_with_new_rows = np.concatenate((arr, new_rows), axis=0)
print(arr_with_new_rows)

# extra example 2: adding an new column to a 3-D array - using concatenate()
arr = np.array([[[1,2], [3,4], [5,6]]])
print("Original 3-D array:\n", arr, sep='')
print(arr.shape)  # (1, 3, 2)

new_col = np.array([[[7], [8], [9]]])
print("New column:\n", new_col, sep='')
print(new_col.shape)  # (1, 3, 1)

arr_with_new_col = np.concatenate((arr, new_col), axis=2)
print("3-D array with a new column:\n", arr_with_new_col, sep='')
print(arr_with_new_col.shape)  # (1, 3, 3)

# extra example 2: adding a new row to a 3-D array - using concatenate()
print("Original 3-D array:\n", arr, sep='')
print(arr.shape)  # (1, 3, 2)

new_row = np.array([[[7, 8]]])
print("New row:\n", new_row, sep='')
print(new_row.shape)  # (1, 1, 2)

arr_with_new_row = np.concatenate((arr, new_row), axis=1)
print("3-D array with a new row:\n", arr_with_new_row, sep='')
print(arr_with_new_row.shape)  # (1, 4, 2)


# slide 46 - insert a new column having the same values - using insert()
arr = np.array([[1,2], [3,4], [5,6]])
print("Original 2-D array:\n", arr, sep='')
print(arr.shape)  # (3, 2)

# add a new column at index 2 (as 3rd column) consisting of value 1
arr_with_new_col = np.insert(arr, 2, 1, axis=1)
print("2-D array with a new column:\n", arr_with_new_col, sep='')
print(arr_with_new_col.shape)  # (3, 3)

# examples from notes of slide 46:
# adding multiple columns to an existing array using insert:
arr = np.array([[1,2], [3,4], [5,6]])
# at the end (before the column index 2)
arr_with_new_cols = np.insert(arr, (2, 2), 1, axis=1)
print(arr_with_new_cols)
# between cols 0 and 1 (before the column index 1)
arr_with_new_cols = np.insert(arr, (1, 1), 1, axis=1)
print(arr_with_new_cols)
# at the beginning and end (before col 0 and before col 2)
arr_with_new_cols = np.insert(arr, (0, 2), 1, axis=1)
print(arr_with_new_cols)


# slide 47
# insert a new row: [7, 8] at index 3 (as 4th row)
arr_with_new_row = np.insert(arr, 3, [7,8], axis=0)
print("2-D array with a new row:\n", arr_with_new_row, sep='')
print(arr_with_new_row.shape)  # (4, 2)

# adding a new row at index 3 (as 4th row) consisting of value 1
arr_with_new_row = np.insert(arr, 3, 1, axis=0)
print("2-D array with a new row:\n", arr_with_new_row, sep='')
print(arr_with_new_row.shape)  # (4, 2)

# examples from notes of slide 47:
# adding multiple rows to an existing array using insert:
arr = np.array([[1,2], [3,4], [5,6]])
# at the end (before the row index 3)
arr_with_new_rows = np.insert(arr, (3, 3), 1, axis=0)
print(arr_with_new_rows)
# between rows 0 and 1 (before the index 1)
arr_with_new_rows = np.insert(arr, (1, 1), 1, axis=0)
print(arr_with_new_rows)
# at the beginning and end (before row 0 and before row 3)
arr_with_new_rows = np.insert(arr, (0, 3), 1, axis=0)
print(arr_with_new_rows)

# extra example 1: adding an new column to a 3-D array - using insert()
arr = np.array([[[1,2], [3,4], [5,6]]])
print("Original 3-D array:\n", arr, sep='')
print(arr.shape)  # (1, 3, 2)

arr_with_new_col = np.insert(arr, 2, 1, axis=2)
print("3-D array with a new column:\n", arr_with_new_col, sep='')
print(arr_with_new_col.shape)  # (1, 3, 3)

# extra example 2: adding a new row to a 3-D array - using insert()
print("Original 3-D array:\n", arr, sep='')
print(arr.shape)  # (1, 3, 2)

arr_with_new_row = np.insert(arr, 3, 1, axis=1)
print("3-D array with a new row:\n", arr_with_new_row, sep='')
print(arr_with_new_row.shape)  # (1, 4, 2)


# slide 48 - delete() function
arr = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(arr)
# remove the column with index 2 (3rd column)
arr_without_column_2 = np.delete(arr, 2, 1)
print(arr_without_column_2)


# slide 49
# remove the row with index 1 (2nd row)
arr_without_row_1 = np.delete(arr, 1, 0)
print(arr_without_row_1)

# When axis is not set, the array is flattened 
# and the elements with specified indices are removed
arr_with_deleted_elements = np.delete(arr, [1,3,5])  # removes 2, 4, & 6
print(arr_with_deleted_elements)   # [ 1  3  5  7  8  9 10 11 12]


# slide 50
# Elements can be removed from arrays by matching value(s)
# or based on condition(s)
arr = np.array([3, 4, 5, 6, 7, 8, 5, 9, 4, 2, 5, 7])
print(arr) # [3 4 5 6 7 8 5 9 4 2 5 7]
arr_without_5 = arr[arr != 5]  # keeps all array elements satisfying the condition 
print(arr_without_5) # [3 4 6 7 8 9 4 2 7]
print(arr) # [3 4 5 6 7 8 5 9 4 2 5 7]


# slide 51
arr = np.array([3, 4, 5, 6, 7, 8, 5, 9, 4, 2, 5, 7])
arr_and = arr[ (arr >= 5) & (arr <= 8) ]     
print(arr)  # [5 6 7 8 5 5 7]
arr_or = arr[ (arr >= 5) | (arr <= 8) ]
arr_or = arr[ np.logical_or((arr >= 5), (arr <= 8)) ]
print(arr_or)  # [3 4 5 6 7 8 5 9 4 2 5 7]


# slide 52
# removing array elements
arr = np.array([3, 4, 5, 6, 7, 8, 5, 9, 4, 2, 5, 7])
arr_del = np.delete(arr, np.argwhere(arr == 5))
print(arr_del) # [3 4 6 7 8 9 4 2 7]
print(arr)     # [3 4 5 6 7 8 5 9 4 2 5 7]

# Question: how would you use np.delete() and np.argwhere()
# functions to remove all occurrences of elements between 5
# and 8?
arr_del = np.delete(arr, np.argwhere(np.logical_and((arr >= 5), (arr <= 8))))
print(arr_del)  # [3 4 9 4 2]
arr_del = np.delete(arr, np.argwhere(( (arr >= 5) & (arr <= 8) )))
print(arr_del)  # [3 4 9 4 2]


# slide 53
# To find the index(es) of an array element use the np.where()
# numpy function: np.where(array == element)
arr_1D = np.arange(10, 19)
print(arr_1D)  # [10 11 12 13 14 15 16 17 18]
index, = np.where(arr_1D == 16)
print(index)  # [6]
# to get the index as an int, use subscript operator with index 0
print(index[0])  # 6

index = np.where(arr_1D == 16)
print(index)  # prints a tuple: (array([6], dtype=int32),)
print(index[0])  # [6]
print(index[0][0]) # 6

# If the element does not exist in the array, the array
# returned by the where() function will be empty
index, = np.where(arr_1D == 19)
print(index)  # []

arr = np.array([2, 5, 7, 3, 8, 4, 5, 9, 5])
index, = np.where(arr == 5)
print(index) # [1 6 8]


# slide 54
arr_2D = arr_1D.reshape(3,3)
print(arr_2D)
row_index, col_index = np.where(arr_2D == 16)
print(row_index, col_index)  # [2] [0]
print(row_index[0], col_index[0])  # 2 0


# slide 55
a = np.array([1, 2, 3, 4, 5])
a_sum = np.sum(a)
print(a_sum) # prints 15
a_prod = np.prod(a)
print(a_prod) # prints 120


# slide 58 - example from notes section
arr = np.array([2, 7, 3, 5, 5, 2, 8, 1, 7, 2])
unique_elements, counts_elements = np.unique(arr, return_counts=True)
print('unique_elements:', unique_elements)  # array of unique elements: [1 2 3 5 7 8]
print('counts_elements:', counts_elements)  # array of frequencies of each element: [1 3 1 2 2 1]


# slide 60 - working with files containing data to be stored in arrays
import os
current_directory_path = os.getcwd()
# setting the file path (folder + filename)
file_path = current_directory_path + '\data_ints.txt'
# OR (if the file is in the same folder with the Python script): 
file_name = 'data_ints.txt'
# OR (using the normcase function from the os.path module): 
file_path = os.path.normcase(file_path)
print(file_path)
file_path = current_directory_path + '/data_ints.txt'
file_path = os.path.normcase(file_path)
print(file_path)

# Example 1: importing the whole file into numpy array
arr = np.loadtxt(file_path, dtype=int)  # default data type is float
print(arr)
# Example 2: importing multiple columns of text file into NumPy array
arr = np.loadtxt(file_path, usecols=1, dtype=int)  # import only column with index 1
print(arr)  # [60 86 92]
arr = np.loadtxt(file_path, usecols=(1,2,3), dtype=int)  # import only columns with index 1, 2 & 3
print(arr)


# slide 61
# Example 3:
file_path = current_directory_path + '\data_ints_with_headings.txt'
arr = np.loadtxt(file_path, skiprows=1, dtype=int)  # skips 1st row (indexed as 0)
print(arr)
# additional example:
# skip the first two rows (indexed as 0 and 1):
arr = np.loadtxt(file_path, skiprows=2, dtype=int) 
print(arr)
'''
With usecols, the numbers represent indices
(usecols=0 means use the column with index 0 etc.)
Multiple column indices can be specified within a tuple or a list.
With skiprows, the number represents the order number of rows, counting form 1.
(skiprows=1 means skip the 1st row – indexed 0),
(skiprows=2 means skip the 1st and 2nd row – indexed 0 and 1), etc.
Multiple row indices cannot be specified.
'''

# slide 62
# Example 4:
# importing only the first column of the text file into NumPy
# array and skipping the first row (with headings).
arr = np.loadtxt(file_path, skiprows=1, usecols=0, dtype=int)
print(arr)  # [28 40 48]


# slide 63
# importing data of different data type from file into NumPy array
# Method 1: import all data in string format
file_path = current_directory_path + '\data_strings_floats_ints.txt'
arr = np.loadtxt(file_path, delimiter='\t', dtype=str)
print(arr)
# Note: the default delimiter is space; to change the delimiter
# use the delimiter key argument (in this example set to tab)


# slide 64
# Method 2: pass a comma-separated datatype string specifying
# the data type of each column (in order of their existence) to
# the dtype parameter
file_path = current_directory_path + '\data_strings_floats_ints.txt'
arr = np.loadtxt(file_path, delimiter='\t', dtype='U6,f,i')
print(arr)


# slide 65
# Method 3: Specify dtype=str as the array data type
# (because arrays as a whole can have only 1 data type)
# Then use the converters key argument to convert values to
# correct data type within each string array element.
file_path = current_directory_path + '\data_strings_floats_ints.txt'
arr = np.loadtxt(file_path, delimiter='\t', dtype=str, \
                 converters={0: lambda bs: bs.decode(), 1: float, 2: int})
print(arr)


# slides 66-67
# Example 8: importing data of different data type when there
# are missing values
file_path = current_directory_path + '\data_mixed_with_missing_values.txt'
arr = np.loadtxt(file_path, delimiter='\t', dtype=str, \
                 converters={0: lambda bs: bs.decode() or '', \
                             1: lambda s: float(s.strip() or 0.0), \
                             2: lambda s: int(s.strip() or 0)})
print(arr)


# slides 69-70
arr = np.arange(10).reshape(5, 2)
print(arr)
# by default, numerical data are stored as float with 18 decimals
np.savetxt('output_file.txt', arr)
# use the fmt kwarg to save nuerical data in a different format
# fmt uses the format string as used with the print statement
# to format output values: %[flags][width][.precision]type 
np.savetxt('output_file.txt', arr, fmt='%d', delimiter=';')







