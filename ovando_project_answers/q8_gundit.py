import numpy as np
import os

currentDirectoryPath = os.getcwd()
file_path = currentDirectoryPath + '\\data_set_1.txt'
input_array = np.loadtxt(file_path, usecols=(1,2,3,4,5,6,7,8,9,10,11), delimiter='\t', dtype=str)
file_path_2 = currentDirectoryPath + '\\data_set_1_bis.txt'
input_array_2 = np.loadtxt(file_path_2, usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22), delimiter='\t', dtype=str)

lookup_val = 'WX-534'
row_num = 5

def hlookup(input_array,lookup_val,row_num):
    index=0
    # the shape will give the number of entries in both directions (8,11) meaning 8 rows and 11 columns
    for i in range (input_array.shape[1]):
        # we use the information on the rows and columns here to select the sepefic entry that we want.
        # in this case we care about finding the specific lookup value i.e. WX-534.
        if input_array[0][i] == lookup_val:
            index = i
            
            if input_array.shape[1] < row_num:
                Return_val = input_array[row_num-1][index]
                return Return_val
            else:
                None
        else:
            return "-1"