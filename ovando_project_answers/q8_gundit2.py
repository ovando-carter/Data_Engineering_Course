import numpy as np
import os


#  returns the corresponding value in a specified row (implement the Excel HLOOKUP function with the exact match)



# the function always returns a string
# takes in data from data_set_1 and creates an array from it. 

'''
currentDirectoryPath = os.getcwd()
file_path = currentDirectoryPath + '/data_set_1.txt'
input_array = np.loadtxt(file_path, usecols=(1,2,3,4,5,6,7,8,9,10,11), delimiter='\t', dtype=str)
#file_path_2 = currentDirectoryPath + '/data_set_1_bis.txt'
#input_array_2 = np.loadtxt(file_path_2, usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22), delimiter='\t', dtype=str)

lookup_val = 'WX-534'
row_num = 5
'''

def hlookup(input_array,lookup_val,row_num):
    import numpy as np
    # check is the look up val in the list
    
    if lookup_val not in input_array[0]:
        
        # The function returns the value:
        # ‘-1’ (as string) if lookup value is not found in the first row
        return '-1'
    
    # this makes sure that it will not give a value if the person inputs a number that exceeds the number of rows
    # input_array.shape[0] will give the number of rows to be 8. If someone wanted to look up the values in a row 9 
    # they would get None because there is no row there at all. 
    elif row_num > input_array.shape[0]:
        
        # The function returns the value:
        # ‘None’ (as string) if the given row does not exist within the data set.
        return 'None'
    
    else:
        
        # the shape will give the number of entries in both directions (8,11) meaning 8 rows and 11 columns
        for i in range (input_array.shape[1]):

            # finds the value in the first row of a given NumPy array
            # we use the information on the rows and columns here to select the sepefic entry that we want.
            # in this case we care about finding the specific lookup value i.e. WX-534.
            if input_array[0][i] == lookup_val:
                index = i

                Return_val = input_array[row_num-1][index]
                
                # The function returns the string value:
                return Return_val
        
#print(hlookup(input_array,lookup_val,row_num))