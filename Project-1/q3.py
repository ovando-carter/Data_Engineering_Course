import numpy as np

#convert all elements of an original NumPy array of non-negative integers into a NumPy array of strings
#each string is of equal length
# the number of digits in the largest integer in the original array
# and is composed of the integer value padded on the left with zeros.
# needs to find out the size of the biggest number in the array, 
# add zeroes infront of the other numbers so that they all have the same number 

def pad_arr_int_to_str(arr):
    str_from_arr = arr.astype(str)  

    val = 0 
    new_arr = np.array([])

    #loop through str_from_arr to find each string
    for i in range(0, len(str_from_arr)):
        #len(str_from_arr[i]) counts the number of characters in the string
        #will only save the number of the biggest string
        if len(str_from_arr[i]) > val:
            val = len(str_from_arr[i])
        #save if value is > the last

    #subtract the len(str_from_arr[i]) from val
    for i in range(0, len(str_from_arr)):
        #add in the biggest number first to avoid added more zero infornt of it, or loosing it from the final array. 
        if len(str_from_arr[i]) == val:
            new_arr = np.append(new_arr,str_from_arr[i])
        else:
            # while loop will keep adding a 0 infront until it reaches the length of the biggest string  "len(str_from_arr[i])"
            while len(str_from_arr[i]) < val:
                str_from_arr[i] = '0' + str_from_arr[i]
                if len(str_from_arr[i])==val:
                    # appends the new strings to the array new_arr
                    new_arr = np.append(new_arr,str_from_arr[i])

    return new_arr 