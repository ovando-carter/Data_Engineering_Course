#####################
# Module 3A - NumPy #
#####################

import numpy as np
import os
currentDirectoryPath = os.getcwd()


# Question 1
# ----------
def Q1():
    # a) Create a 2-D array of 100 elements: 1 – 100 with 25 rows and 4 columns
    arr_2D = np.arange(1, 101).reshape(25,4)
    print(arr_2D)

    # b) use two ways of displaying the dimensionality of the above array 
    # - using the shape property
    arr_2D.shape
    print(arr_2D.shape)
    # using the ndim property
    arr_2D.ndim
    print(arr_2D.ndim)

    # c) write the statement that returns number 77 from the above 2-D array
    # 'pedestrian' way
    arr_2D[19, 0]
    print(arr_2D[19, 0])
    # using the where() numpy function:
    row_index, col_index = np.where(arr_2D == 77)
    print("The number 77 is in row", row_index[0], "and column", col_index[0])
    print(arr_2D[row_index[0], col_index[0]])
    # OR
    indices = np.where(arr_2D == 77)
    print("The number 77 is in row", indices[0][0], "and column", indices[1][0])
    print(arr_2D[indices[0][0], indices[1][0]])

    # d) reshape the above 2-D array to a 3-D array with 10 rows and 5 columns, where each 1-D array contains 2 elements
    arr_3D = arr_2D.reshape(10, 5, 2)
    print(arr_3D)

    # e) write the statement that returns number 77 from the above 3-D array
    # 'pedestrian' way    
    arr_3D[7, 3, 0]
    print(arr_3D[7, 3, 0])
    # using the where() numpy function:
    index_1D, index_2D, index_3D = np.where(arr_3D == 77)  # indices is a tuple of 3 arrays: (array([7], dtype=int32), array([3], dtype=int32), array([0], dtype=int32))
    print("The number 77 is in position", index_1D[0], ",", index_2D[0], ",", index_3D[0])
    print(arr_3D[index_1D[0], index_2D[0], index_3D[0]])
    
    # OR
    indices = np.where(arr_3D == 77)  # indices is a tuple of 3 arrays: (array([7], dtype=int32), array([3], dtype=int32), array([0], dtype=int32))
    print("The number 77 is in position", indices[0][0], ",", indices[1][0], ",", indices[2][0])
    print(arr_3D[indices[0][0], indices[1][0], indices[2][0]])
    
    # f) reshape the above array to a 3-D array with 5 rows and 2 columns, where each 1-D array contains 10 elements
    arr_3D = arr_3D.reshape(5, 2, 10)
    print(arr_3D)

    # g) write the statement that returns number 77 from the above 3-D array
    arr_3D[3, 1, 6]
    print(arr_3D[3, 1, 6])

    # h) reshape the above array to a 3-D array with 2 rows and 10 columns, where each 1-D array contains 5 elements
    arr_3D = arr_3D.reshape(2, 10, 5)
    print(arr_3D)

    # i) write the statement that returns number 77 from the above 3-D array
    arr_3D[1, 5, 1]
    print(arr_3D[1, 5, 1])

    # j) reshape the above array to a 3-D array with 20 rows and 5 columns, where each 1-D array contains 1 element
    arr_3D = arr_3D.reshape(20, 5, 1)
    print(arr_3D)

    # k) write the statement that returns number 77 from the above 3-D array
    arr_3D[15, 1, 0]
    print(arr_3D[15, 1, 0])

    # l) flatten the last 3-D array
    arr_1D = arr_3D.reshape(-1)
    print(arr_1D)

    # m) write the statement that returns number 77 from the above 1-D array
    arr_1D[76]
    print(arr_1D[76])


# Question 2
# ----------
# Write a Python function generate_2D_arr, that accepts 2 parameters:
# - a positive integer (r), representing the number of rows
# - a positive integer (c), representing the number of columns
# The function does not return any value but instead creates and 
# prints a 2-D array of elements 0, 1, 2, ..., r*c-1 and prints
# out all rows and all columns of the array.
def generate_2D_arr(r, c):
    arr_2D = np.arange(r*c).reshape(r,c)
    print("Array:\n", arr_2D)
    print("Rows:")
    for i in range(r):
        print("Row " + str(i) + ":")
        print(arr_2D[i,:])
    print("Columns:")
    for j in range(c):
        print("Column " + str(j) + ":")
        print(arr_2D[:, j])


# Question 3
# ----------
# Write a Python function to
# a) square numbers stored in a 1-D array.
def square_arr(arr_numbers):
    return arr_numbers ** 2

# b) square root non-negative numbers stored in a 1-D array.
# Round the values to 2 decimal places.
def square_root_arr(arr_numbers):
    return np.around(arr_numbers[ arr_numbers >= 0 ] ** 0.5, decimals=2)


# Question 4
# ----------
# Write a Python function to find invalid marks stored in a 1-D array.
# The mark is invalid if it is less than 0 and if it is greater than 100.
# solution 4a:
def invalid_marks_v1(arr_marks):
    return arr_marks[ (arr_marks < 0) | (arr_marks > 100) ]

# solution 4b:
def invalid_marks_v2(arr_marks):
    return arr_marks[ np.logical_or(arr_marks < 0, arr_marks > 100) ]


# Question 5
# ----------
# Write a Python function to find valid marks stored in a 1-D array.
# The mark is valid if it is between 0 and 100.
# solution 5a:
def valid_marks_v1(arr_marks):
    return arr_marks[ (arr_marks >= 0) & (arr_marks <= 100) ]

# solution 5b:
def valid_marks_v2(arr_marks):
    return arr_marks[ np.logical_and(arr_marks >= 0, arr_marks <= 100) ]


# Question 6
# Write a Python function to find all
# a) even
# b) odd
# integers stored in a 1-D array.
# solution 6a:
def even_numbers(arr_ints):
    return arr_ints[ arr_ints % 2 == 0 ]

# solution 6b:
def odd_numbers(arr_ints):
    return arr_ints[ arr_ints % 2 == 1 ]


# Question 7
# ----------
# Write a Python function to test whether each element of a 1-D array is also present in a second array.
# solution 7a:
def common_arr_values_v1(arr1, arr2):
    # initialise the array storing common values
    common_values = np.array([], dtype=int)
    # find the common values:
    # for each element in the first array check if present in the second array
    for el in arr1:
        common_values = np.append(common_values, arr2[ (arr2 == el) ])
    return common_values

# solution 7b:
def common_arr_values_v2(arr1, arr2):
    # initialise the array storing common values
    common_values = np.array([], dtype=int)
    # find the common values:
    # for each element in the second array check if present in the first array
    for el in arr2:
        common_values = np.append(common_values, arr1[ (arr1 == el) ])
    return common_values

# solution 7c:
def common_arr_values_v3(arr1, arr2):
    return arr1[ np.in1d(arr1, arr2) ]

# solution 7d:
def common_arr_values_v4(arr1, arr2):
    return arr1[ np.array([el in arr2 for el in arr1]) ]


# Question 8
# ----------
# Write a Python function that accepts 3 arguments: the 2-D array of strings,
# a string containing the value looked up for in the first column, and an
# integer representing the column where the corresponding value is to be found
# (1 represents 1st column, 2 represents 2nd column etc.). The function looks
# for the lookup value in the first column of the given 2-D array and returns
# the corresponding value in the given column (implementing the Excel VLOOKUP
# function with the exact match). The function returns the value '-1' (as string)
# if lookup value is not found in the first column, and 'None' (as string) if
# the given column does not exist within the data set.
# Note that the function always returns a string: it contains either the found value,
# '-1' or 'None'. The function accepts an array but the data set is given in the
# file data_set_1, with TAB separating the data.
# solution 8a:
# using the custom-built function find_el()
def vlookup_v1(arr, lookup_val, col):
    # return None if index col does not exist within data set
    if col < 0 or col > arr.shape[-1]:
        return str(None)
    # find the row index of the lookup value in the first column
    row_index = find_el(arr[:, 0], lookup_val)
    if row_index == -1:
        return str(-1)
    # return the value from intersection of row_index
    # and col-1 (column indexes start with 0)
    return str(arr[row_index, col-1])
    
def find_el(arr, el):
    """Returns the index of element el in array arr if el exists, -1 if it doesn't."""
    for index in range(len(arr)):
        if el == arr[index]:
            return index
    return -1

# solution 8b:
# using the built-in numpy method where() instead of
# the custom-built function find_el()
def vlookup_v2(arr, lookup_val, col):
    # return None if index col does not exist within data set
    if col < 0 or col > arr.shape[-1]:
        return str(None)
    # find the row index of the lookup value in the first column
    row_index, = np.where(arr[:, 0] == lookup_val)
    # if lookup_val is not found, where returns an empty array
    if row_index.size == 0:
        # the array is empty
        return str(-1)
    # return the value from intersection of row_index
    # and col-1 (column indexes start with 0)
    # (the row_index (as an integer) can be obtained
    # through row_index[0])
    return str(arr[row_index[0], col-1])


# Question 9
# ----------
# Write a Python function that accepts 4 arguments:
# 1) the array that includes headings
# 2) the heading name where the value to be looked for will be found
# 3) the value to be looked for
# 4) the heading where the corresponding value to be returned will be found
# (implement the Excel INDEX function with 2 nested MATCH functions).
# The function returns None if the 2nd or 4th argument does not exist in the
# first row of the data set and -1 if value looked for is not found in the
# column headed by 2nd argument. The function always returns a string:
# it contains either the found value, None or -1.
# Note: The function accepts an array but the data set is given in the file data_set_1.
# solution 9:
def index_match(arr, head_look_val, lookup_val, head_ret_val):
    # find the column index of the head_look_val in the first row of the data set
    col_ind_hlv = find_el(arr[0, :], head_look_val)
    # find the column index of the head_ret_val in the first row of the data set
    col_ind_hrv = find_el(arr[0, :], head_ret_val)
    # return None if head_look_val or head_ret_val does not exist in the first row of the data set
    if col_ind_hlv < 0 or col_ind_hlv > arr.shape[-1] or \
       col_ind_hrv < 0 or col_ind_hrv > arr.shape[-1]:
        return str(None)
    # find the row index of the value looked for in the column headed by 2nd argument
    row_ind_lv = find_el(arr[:, col_ind_hlv], lookup_val)
    # return -1 if value looked for is not found in the column headed by 2nd argument
    if row_ind_lv == -1:
        return str(-1)
    # return the value from intersection of row_ind_lv and col_ind_hrv
    return str(arr[row_ind_lv, col_ind_hrv])
    

# Question 10
#------------
# A company assembled its products sale over 4 quarters of a year, stored in the flat file data_set_2.
# It wants to calculate:
# a) the total of sales for the whole year, for each product.
# The expected results is in format of 2-D array of 8 rows and 2 columns with the following headings:
# Products; Total Sales
# b) the total of sales for each quarter
# The expected results is in format of 2-D array of 2 rows and 4 columns with the following headings:
# Total Sales: Q1;Total Sales: Q2;Total Sales: Q3;Total Sales: Q4
# c) the overall total sales for that year
# The expected results is in format of one int value.
# Write a Python function for each of the three calculations. From the calling environment (the main() function),
# save the outputs of functions for questions 10a and 10b to a text file.
# Note: The sample flat file data_set_2 has 8 rows and 5 columns. The solution must work
# for any number of rows and any number of columns (to check this try data_set_2_bis).

# solution 10a:
def total_sales_per_product(arr):
    # create an empty array
    arr_totals = np.array([], dtype='str')
    # add the array headings
    arr_totals = np.concatenate((arr_totals, np.array(['Products', 'Total Sales'], dtype='str')))
    # for each product (row indexed 1-7) add together the values in columns indexed 1-4 (sales from Q1-Q4)
    for row_index in range(1, arr.shape[0]):
        row_total = 0
        for col_index in range(1, arr.shape[1]):
            row_total += int(arr[row_index][col_index])
        # add the product and its total sales
        arr_totals = np.concatenate((arr_totals, np.array([arr[row_index][0], row_total], dtype='str')))    
    # reshape the array to have the same number of rows as the original array and 2 columns
    arr_totals = arr_totals.reshape(arr.shape[0],2)       
    return arr_totals

# solution 10b:
def total_sales_per_quarter(arr):
    # create an empty array
    arr_totals = np.array([], dtype='str')
    # add the array headings (append the word 'Total ' to each of the existing heading)
    for col_index in range(1, arr.shape[1]):
        arr_totals = np.append(arr_totals, 'Total ' + arr[0, col_index])
    # calculate the total sales for each quarter and add it to the array
    for col_index in range(1, arr.shape[1]):
        # extract the column with index col_index (each related to a separate quarter)
        col_q = arr[:, col_index]
        # remove the column heading ('Sales: Qn', n = 1-4)
        sales_q_str = col_q[1:len(col_q)]
        # convert the values in the column from str to int
        sales_q_int = sales_q_str.astype(int)
        # add up all values in the column
        tot_quarter = sum(sales_q_int)
        # add the total sales to the array
        arr_totals = np.append(arr_totals, tot_quarter)  
    # reshape the array to 2 rows and 1 less columns than the number of
    # columns of the original array (to exclude the 'product' column) 
    arr_totals = arr_totals.reshape(2, arr.shape[1]-1)
    return arr_totals

# solution 10c:
# version 1
def total_sales_overall_V1(arr):
    # use the function produced in question 10b to find the
    # total sales per each quarter
    # (the function returns an array of 2 rows and 4 columns) 
    tot_sales_per_quarter = total_sales_per_quarter(arr)
    # convert the values in the 2nd row from str to int
    tot_sales_q_int = tot_sales_per_quarter[1, :].astype(int)
    # add up all elements in the 2nd row
    tot_sales = sum(tot_sales_q_int)
    return tot_sales

# version 2
def total_sales_overall_V2(arr):
    # use the function produced in question 10a  
    # to find the total sales per each product
    # (the function returns an array of 8 rows and 2 columns) 
    tot_sales_per_product = total_sales_per_product(arr)
    # extract the 2nd column from the array
    tot_sales_col_2 = tot_sales_per_product[:, 1]
    # remove the column heading ('Total Sales')
    tot_sales_prod_str = tot_sales_col_2[1:len(tot_sales_col_2)]
    # convert the values in the 2nd column from str to int
    tot_sales_prod_int = tot_sales_prod_str.astype(int)
    # add up all elements in the 2nd row
    tot_sales = sum(tot_sales_prod_int)
    return tot_sales


# Question 11
#------------
# A company is looking at its products sale over 4 years. It wants to calculate the
# total income from sales for each year as follows: unit price x number sold per year.
# The sample flat file data_set_3 contains the list of products with their price,
# as well as the number of sales per each product for each of the 4 years.
# Write a Python function that calculates the total income from sales per each product
# for each of the 4 years and returns the 2-D array with 8 rows and 5 columns,
# where the 1st row contains the following headings: 
# Product;Total Income: Yr1;Total Income: Yr2;Total Income: Yr3;Total Income: Yr4
# The returned array then needs to be written to a file in form of a data set from
# the calling environment - the main() function.
# Note: The sample flat file data_set_3 has 8 rows and 6 columns. The solution must work
# for any number of rows and any number of columns (to check this try data_set_3_bis).
# solution 11:
def total_income_per_product_and_year(arr):
    # create an empty array
    arr_totals = np.array([], dtype='str')
    # add the first array heading ('Product')
    arr_totals = np.append(arr_totals, arr[0, 0])
    # add the array headings (replace the word 'Sales' with 'Income'
    # and append the word 'Total ' to each of the existing heading)
    for col_index in range(2, arr.shape[1]):
        arr_totals = np.append(arr_totals, 'Total ' + arr[0, col_index].replace('Sales', 'Income'))
    # calculate the total sales for each year and add it to the array
    for row_index in range(1, arr.shape[0]):
        # extract the row with index row_index (each related to a separate product)
        row_p = arr[row_index, :]
        # extract the product code and add it to the array arr_totals
        arr_totals = np.append(arr_totals, arr[row_index, 0])
        # remove the product code ('BK...') from row_p 
        row_p_str = row_p[1:len(row_p)]
        # convert the values in the column from str to int
        row_p_int = row_p_str.astype(int)
        # multiply the unit cost with all remaining values (year sales)
        # in the row and add each to the array arr_totals
        for col_index in range(1, len(row_p_int)):
            tot_income = row_p_int[0] * row_p_int[col_index]
            # add the total income for this product and year to the array
            arr_totals = np.append(arr_totals, tot_income)  
    # reshape the array to the same number of rows as arr and one less columns than arr
    # (to exclude the 'unit price' column) 
    arr_totals = arr_totals.reshape(arr.shape[0], arr.shape[1]-1)
    return arr_totals


# Question 12
#------------
def find_region_from_country(country):
    if country in ["Angola", "Cameroon","Tanzania","South Africa"]:
        return 'Africa'
    elif country in ["India","Japan","Singapore","South Korea"]: 
        return 'Asia'
    elif country in ["France","Greece","Italy","Spain","Portugal"]: 
        return 'Europe'
    elif country == "U.S.A.": 
        return 'North America'
    elif country in ["Cuba","Mexico","Panama"]: 
        return 'Central America'
    elif country in ["Argentina","Brazil","Venezuela"]: 
        return 'South America'
    else:
        return 'ERROR: country ' + country + ' not traded with.'
    
def find_age_range_from_age(age):
    if age >= 65:
        return 'elderly'
    elif age >= 40: 
        return 'middle-aged'
    elif age >= 18: 
        return 'adult'
    else:
        return 'ERROR: age ' + age + ' not traded with.'

def calculate_age(date_of_birth):
    from datetime import datetime

    # store the current year, month & day
    current_datetime = datetime.now()
    current_year = current_datetime.year
    current_month = current_datetime.month
    current_day = current_datetime.day

    # get the year, month & day from the date_of_birth
    dob_day = int(date_of_birth[0:2])
    dob_month = int(date_of_birth[3:5])
    dob_year = int(date_of_birth[6:])

    # work out the age
    age = current_year - dob_year 
    if (current_month < dob_month) or (current_month == dob_month and current_day < dob_day):
        age -= 1
    return age

# Version 1: with manual initialisation of dictionary of
#            dictionaries - by hard-coding region names
def number_of_sales_per_region_and_age_v1(arr):
    # find the number of rows and columns in the 2-D aray
    tpl_shape = arr.shape
    num_rows = tpl_shape[0]
    num_cols = tpl_shape[1]
    
    # find the indices of the 'Country', 'DoB' and 'Sale (£)' columns
    arr_index_country, = np.where(arr[0,:] == 'Country') 
    arr_index_dob, = np.where(arr[0,:] == 'DoB')
    arr_index_sale, = np.where(arr[0,:] == 'Sale (£)')
    index_country = arr_index_country[0]
    index_dob = arr_index_dob[0]
    index_sale = arr_index_sale[0]

    # initialise the dictionary of dictionaries
    count_sales_per_region_age_range = {}
    '''
    # Note: setting the dictionary this way would produce the same numbers for all regions
    # because the same dictionary (breakdown_age_range) is used for each age range:
    count_sales_per_age_range = {'adult': 0, 'middle-aged': 0, 'elderly': 0}
    count_sales_per_region_age_range['Africa'] = count_sales_per_age_range
    count_sales_per_region_age_range['Asia'] = count_sales_per_age_range
    count_sales_per_region_age_range['Europe'] = count_sales_per_age_range
    count_sales_per_region_age_range['North America'] = count_sales_per_age_range
    count_sales_per_region_age_range['Central America'] = count_sales_per_age_range
    count_sales_per_region_age_range['South America'] = count_sales_per_age_range
    Instead, the dictionary for each region must be defined separately:
    '''
    # manual initialisation of dictionary of dictionaries - by hard-coding region names    
    count_sales_per_region_age_range['Africa'] = {'adult': 0, 'middle-aged': 0, 'elderly': 0}
    count_sales_per_region_age_range['Asia'] = {'adult': 0, 'middle-aged': 0, 'elderly': 0}
    count_sales_per_region_age_range['Europe'] = {'adult': 0, 'middle-aged': 0, 'elderly': 0}
    count_sales_per_region_age_range['North America'] = {'adult': 0, 'middle-aged': 0, 'elderly': 0}
    count_sales_per_region_age_range['Central America'] = {'adult': 0, 'middle-aged': 0, 'elderly': 0}
    count_sales_per_region_age_range['South America'] = {'adult': 0, 'middle-aged': 0, 'elderly': 0}
    
    # increment the counter of the relevant age range
    # and region for each customer in the data set (array)
    for row_index in range(1, num_rows):
        # find the region of the country in row row_index
        region = find_region_from_country(arr[row_index, index_country].astype(str))
        # find the age from the date of birth
        age = calculate_age(arr[row_index, index_dob].astype(str))
        age_range = find_age_range_from_age(age)
        count_sales_per_region_age_range[region][age_range] += 1
        
    return count_sales_per_region_age_range


# Version 2: with automated initialisation of dictionary of dictionaries
#            - using region names returned by find_region_from_country()
def number_of_sales_per_region_and_age_v2(arr):
    # find the number of rows and columns in the 2-D aray
    tpl_shape = arr.shape
    num_rows = tpl_shape[0]
    num_cols = tpl_shape[1]
    
    # find the indices of the 'Country', 'DoB' and 'Sale (£)' columns
    arr_index_country, = np.where(arr[0,:] == 'Country') 
    arr_index_dob, = np.where(arr[0,:] == 'DoB')
    arr_index_sale, = np.where(arr[0,:] == 'Sale (£)')
    index_country = arr_index_country[0]
    index_dob = arr_index_dob[0]
    index_sale = arr_index_sale[0]

    # initialise the dictionary of dictionaries
    count_sales_per_region_age_range = {}

    # initialise the sub-dictionary
    age_ranges = ['adult', 'middle-aged', 'elderly']
    count_sales_per_age_range = {}
    for index in range(len(age_ranges)):
        count_sales_per_age_range[age_ranges[index]] = count_sales_per_age_range.get(age_ranges[index], 0)

    # increment the counter of the relevant age range
    # and region for each customer in the data set (array)
    for row_index in range(1, num_rows):
        # find the region of the country in row row_index
        region = find_region_from_country(arr[row_index, index_country].astype(str))
        # automated initialisation of dictionary - using 
        # region names returned by find_region_from_country()
        # if region doesn't exist as key in dictionary count_sales_per_region_age_range
        # it will be initialised with region:{'adult': 0, 'middle-aged': 0, 'elderly': 0};
        # otherwise get() returns the current dictionary of age ranges for that region
        # Note: a copy of the sub-dictionary must be created otherwise all countries would
        # end up using the same sub-dictionary
        count_sales_per_region_age_range[region] = count_sales_per_region_age_range.get(region, count_sales_per_age_range.copy())
        # find the age from the date of birth
        age = calculate_age(arr[row_index, index_dob].astype(str))
        age_range = find_age_range_from_age(age)
        count_sales_per_region_age_range[region][age_range] += 1
        
    return count_sales_per_region_age_range


# Question 13
# -----------
# Write a Python function that returns the last two elements
# from each Nth dimension in a N-D multidimensional array ( N >= 1).
# If the Nth dimension has less than 2 elements the function returns None.
# For example, for the 3-D array shaped as (2, 2, 3):
# [[[ 1,  2,  3], [ 4,  5,  6]],
#  [[ 7,  8,  9], [10, 11, 12]]]
# the function should return the last 2 elements of each 3rd dimension:
# [[[ 2,  3], [ 5,  6]],
#  [[ 8,  9], [11, 12]]]
# Note: The eval() function returns the result of parsing and evaluating
# the given expression represented as a string.
def last_2_col_from_last_dim(arr):
    dimension = arr.ndim
    tpl_shape = arr.shape
    # return None if the Nth dimension
    # contains less than 2 elements
    if tpl_shape[-1] < 2:
        return None
    # find the indexes of the last two 
    # elements from the Nth dimension
    ind_minus_1 = tpl_shape[-1] - 1
    ind_minus_2 = ind_minus_1 - 1
    # work out the number of colons (one for 
    # each dimension below the Nth dimension)
    other_dims = ':, ' * (dimension - 1)
    # compose the expression (any of the 3 solutions below)
    #ret_str = "arr["+ other_dims +"ind_minus_2:]"
    #ret_str = "arr["+ other_dims +"tpl_shape[-1]-2:tpl_shape[-1]]"
    ret_str = "arr[" + other_dims + "[ind_minus_2, ind_minus_1]]"
    # return the evaluated expression
    return eval(ret_str)


# Question 14
# -----------
# Write a Python function that returns the last two elements
# from each of the highest dimension containing at least 2
# elements in a N-D multidimensional array ( N >= 1).
# For example, for the 3-D array shaped as (3, 4, 1):
# [[[ 1], [ 2], [ 3], [ 4]],
#  [[ 5], [ 6], [ 7], [ 8]],
#  [[ 9], [10], [11], [12]]]
# the function should return the last 2 elements of each 2nd dimension
# (as the 3rd dimension has only 1 element):
#  [[[ 3], [ 4]]
#   [[ 7], [ 8]]
#   [[11], [12]]]
def last_2_col_from_highest_dim(arr):
    tpl_shape = arr.shape
    index_found = False
    # find the highest dimension containing at least 2 elements
    for index in range(len(tpl_shape)-1, -1, -1):
        if tpl_shape[index] >= 2:
            index_found = True
            break
    if not index_found:
        return None
    # find the indexes of the last two elements from the  
    # highest dimension containing at least 2 elements
    ind_minus_1 = tpl_shape[index] - 1
    ind_minus_2 = ind_minus_1 - 1
    # work out the number of colons (one for each dimension
    # below the highest dimension containing at least 2 elements)
    other_dims = ''
    if index >= 1:
        other_dims = ':, ' * index
    # compose the expression (any of the 3 solutions below)
    #ret_str = "arr["+ other_dims +"ind_minus_2:]"
    #ret_str = "arr["+ other_dims +"tpl_shape[index]-2:tpl_shape[index]]"
    ret_str = "arr["+ other_dims +"[ind_minus_2, ind_minus_1]]"
    # return the evaluated expression
    return eval(ret_str)



def main():
    # testing Question 1
    print('\n\n----------Question 1----------\n')
    Q1()


    # testing Question 2
    print('\n\n----------Question 2----------\n')
    rows = 4
    columns = 5
    generate_2D_arr(rows, columns)


    # testing Question 3
    print('\n\n----------Question 3----------\n')
    array = np.array([3, 13.5, -5, 0, 1, -12, -10.25, -1, 4])
    arr = square_arr(array)
    print("Squared array:", arr)
    arr = square_root_arr(array)
    print("Square rooted array:", arr)


    # testing Question 4
    print('\n\n----------Question 4----------\n')
    array = np.array([52, 13, -5, 0, 101, 150, 99, 1])
    arr = invalid_marks_v1(array)
    print("Invalid marks (V1):", arr)
    arr = invalid_marks_v2(array)
    print("Invalid marks (V2):", arr)
    

    # testing Question 5
    print('\n\n----------Question 5----------\n')
    array = np.array([52, 13, -5, 0, 101, 150, 99, 1])
    arr = valid_marks_v1(array)
    print("Valid marks (V1):", arr)
    arr = valid_marks_v2(array)
    print("Valid marks (V2):", arr)


    # testing Question 6
    print('\n\n----------Question 6----------\n')
    array = np.array([52, 13, -5, 0, 101, 150, -22, 99, 1, 2])
    arr = even_numbers(array)
    print("Even numbers:", arr)
    arr = odd_numbers(array)
    print("Odd numbers:", arr)


    # testing Question 7
    print('\n\n----------Question 7----------\n')
    array1 = np.array([30, -10, 0, 20, 50])
    array2 = np.array([0, 20, -10])
    arr = common_arr_values_v1(array1, array2)
    print("Common values (V1) - case when arr1 is longer:", arr)
    array1 = np.array([0, 20, -10])
    array2 = np.array([30, -10, 0, 20, 50])
    arr = common_arr_values_v1(array1, array2)
    print("Common values (V1) - case when arr2 is longer:", arr)
    
    array1 = np.array([30, -10, 0, 20, 50])
    array2 = np.array([0, 20, -10])
    arr = common_arr_values_v2(array1, array2)
    print("Common values (V2) - case when arr1 is longer:", arr)
    array1 = np.array([0, 20, -10])
    array2 = np.array([30, -10, 0, 20, 50])
    arr = common_arr_values_v2(array1, array2)
    print("Common values (V2) - case when arr2 is longer:", arr)

    array1 = np.array([30, -10, 0, 20, 50])
    array2 = np.array([0, 20, -10])
    arr = common_arr_values_v3(array1, array2)
    print("Common values (V3) - case when arr1 is longer:", arr)
    array1 = np.array([0, 20, -10])
    array2 = np.array([30, -10, 0, 20, 50])
    arr = common_arr_values_v3(array1, array2)
    print("Common values (V3) - case when arr2 is longer:", arr)

    array1 = np.array([30, -10, 0, 20, 50])
    array2 = np.array([0, 20, -10])
    arr = common_arr_values_v4(array1, array2)
    print("Common values (V4) - case when arr1 is longer:", arr)
    array1 = np.array([0, 20, -10])
    array2 = np.array([30, -10, 0, 20, 50])
    arr = common_arr_values_v4(array1, array2)
    print("Common values (V4) - case when arr2 is longer:", arr)


    # testing Question 8
    print('\n\n----------Question 8----------\n')
    # import the whole data set as str data type skipping the first row (with headings)
    file_path = currentDirectoryPath + '\\data_set_1.txt'
    array = np.loadtxt(file_path, skiprows=1, delimiter='\t', dtype=str)
    print(array)
    prod_code = 'WX-534'
    column = 5
    print("vlookup (V1):")
    q2_sale = vlookup_v1(array, prod_code, column)
    print("The Q2 sale for product " + prod_code + " is: " + q2_sale)
    prod_code = 'UW-698'
    column = 8
    fy_sale = vlookup_v1(array, prod_code, column)
    print("The full year sale for product " + prod_code + " is: " + fy_sale)
    prod_code = 'UW-698'
    column = 9
    inexisting_col = vlookup_v1(array, prod_code, column)
    print("Col 9 and product " + prod_code + " returns: " + inexisting_col + " (no column 9)")
    prod_code = 'XY-123'
    column = 5
    inexisting_prod = vlookup_v1(array, prod_code, column)
    print("The Q1 sale for product " + prod_code + " returns: " + inexisting_prod + " (no product 'XY-123')")
    prod_code = 'LJ-328'
    column = 2
    serial_no = vlookup_v1(array, prod_code, column)
    print("The serial no. for product " + prod_code + " is: " + serial_no)
    print("vlookup (V2):")
    prod_code = 'WX-534'
    column = 5
    q2_sale = vlookup_v2(array, prod_code, column)
    print("The Q2 sale for product " + prod_code + " is: " + q2_sale)
    prod_code = 'UW-698'
    column = 8
    fy_sale = vlookup_v2(array, prod_code, column)
    print("The full year sale for product " + prod_code + " is: " + fy_sale)
    prod_code = 'UW-698'
    column = 9
    inexisting_col = vlookup_v2(array, prod_code, column)
    print("Col 9 and product " + prod_code + " returns: " + inexisting_col + " (no column 9)")
    prod_code = 'XY-123'
    column = 5
    inexisting_prod = vlookup_v2(array, prod_code, column)
    print("The Q1 sale for product " + prod_code + " returns: " + inexisting_prod + " (no product 'XY-123')")
    prod_code = 'LJ-328'
    column = 2
    serial_no = vlookup_v2(array, prod_code, column)
    print("The serial no. for product " + prod_code + " is: " + serial_no)


    # testing Question 9
    print('\n\n----------Question 9----------\n')
    # import the whole data set as str data type
    file_path = currentDirectoryPath + '\\data_set_1.txt'
    array = np.loadtxt(file_path, delimiter='\t', dtype=str)   
    prod_code = 'WX-534'
    q2_sale = index_match(array, 'Product', prod_code, 'Q2')
    print("The Q2 sale for product " + prod_code + " is: " + q2_sale)
    prod_code = 'UW-698'
    fy_sale = index_match(array, 'Product', prod_code, 'FY')
    print("The full year sale for product " + prod_code + " is: " + fy_sale)
    prod_code = 'XY-123'
    inexisting_prod = index_match(array, 'Product', prod_code, 'Q1')
    print("The Q1 sale for product " + prod_code + " returns: " + inexisting_prod + " (no product 'XY-123')")
    prod_code = 'LJ-328'
    serial_no = index_match(array, 'Product', prod_code, 'Serial no.')
    print("The serial no. for product " + prod_code + " is: " + serial_no)
    manager = 'SY'
    q3_sale = index_match(array, 'Manager', manager, 'Q3')
    print("The number of sales made by the manager " + manager + " in Q3 is: " + q3_sale)
    inexisting_r_h = index_match(array, 'Manager', manager, 'Q5')
    print("The number of sales made by the manager " + manager + " in Q5 is: " + inexisting_r_h + " (no heading 'Q5')")
    serial_no = '108709'
    manager = index_match(array, 'Serial no.', serial_no, 'Manager')
    print("The manager for serial no. " + serial_no + " is: " + manager)
    inexisting_l_h = index_match(array, 'Seller', manager, 'Q4')
    print("The number of sales made by the seller " + manager + " in Q4 is: " + inexisting_l_h + " (no heading 'Seller')")
    fy_sale = '2807'
    product = index_match(array, 'FY', fy_sale, 'Product')
    print("The product who made full year sale of " + fy_sale + " is: " + product)


    # testing Question 10
    print('\n\n----------Question 10----------\n')
    # Question 10a - testing with data_set_2.txt
    # import the whole data set as str data type
    file_path = currentDirectoryPath + '\\data_set_2.txt'
    input_arr = np.loadtxt(file_path, delimiter=';', dtype=str)   
    print(input_arr)
    tot_sales_per_product = total_sales_per_product(input_arr)
    print(tot_sales_per_product)
    # save the output array to the file
    np.savetxt('tot_sales_per_product.txt', tot_sales_per_product, fmt='%s', delimiter=';')

    # Question 10b - testing with data_set_2.txt
    tot_sales_per_quarter = total_sales_per_quarter(input_arr)
    print(tot_sales_per_quarter)
    # save the output array to the file
    np.savetxt('tot_sales_per_quarter.txt', tot_sales_per_quarter, fmt='%s', delimiter=';')

    # Question 10c - testing with data_set_2.txt
    tot_sales_overall = total_sales_overall_V1(input_arr)
    print("Total overall annual sales (V1):", tot_sales_overall)
    tot_sales_overall = total_sales_overall_V2(input_arr)
    print("Total overall annual sales (V2):", tot_sales_overall)

    # Question 10a - testing with data_set_2_bis.txt
    # import the whole data set as str data type
    file_path = currentDirectoryPath + '\\data_set_2_bis.txt'
    input_arr = np.loadtxt(file_path, delimiter=';', dtype=str)   
    print(input_arr)
    tot_sales_per_product = total_sales_per_product(input_arr)
    print(tot_sales_per_product)
    # save the output array to the file
    np.savetxt('tot_sales_per_product_bis.txt', tot_sales_per_product, fmt='%s', delimiter=';')

    # Question 10b - testing with data_set_2_bis.txt
    tot_sales_per_quarter = total_sales_per_quarter(input_arr)
    print(tot_sales_per_quarter)
    # save the output array to the file
    np.savetxt('tot_sales_per_quarter_bis.txt', tot_sales_per_quarter, fmt='%s', delimiter=';')

    # Question 10c - testing with data_set_2_bis.txt
    tot_sales_overall = total_sales_overall_V1(input_arr)
    print("Total overall 3-annual sales (V1):", tot_sales_overall)
    tot_sales_overall = total_sales_overall_V2(input_arr)
    print("Total overall 3-annual sales (V2):", tot_sales_overall)


    # testing Question 11
    print('\n\n----------Question 11----------\n')
    # import the whole data set as str data type
    file_path = currentDirectoryPath + '\\data_set_3.txt'
    input_array = np.loadtxt(file_path, delimiter=';', dtype=str)   
    print(input_array)
    tot_income_per_product_and_year = total_income_per_product_and_year(input_array)
    print("Total income per product and year:", tot_income_per_product_and_year)
    np.savetxt('tot_income_per_product_and_year.txt', tot_income_per_product_and_year, fmt='%s', delimiter=';')
    
    # import the whole data set as str data type
    file_path = currentDirectoryPath + '\\data_set_3_bis.txt'
    input_array = np.loadtxt(file_path, delimiter=';', dtype=str)   
    print(input_array)
    tot_income_per_product_and_year = total_income_per_product_and_year(input_array)
    print("Total income per product and year:", tot_income_per_product_and_year)
    np.savetxt('tot_income_per_product_and_year_bis.txt', tot_income_per_product_and_year, fmt='%s', delimiter=';')


    # testing Question 12
    print('\n\n----------Question 12---------\n')
    file_path = currentDirectoryPath + '\\sales.csv'
    # load the whole data set from the input file and store it in an array
    arr = np.loadtxt(file_path, delimiter=',', dtype=str)
    # find the number of sales for each type on customer and payment type
    # using the first version:
    print(number_of_sales_per_region_and_age_v1(arr))
    # using the second version:
    print(number_of_sales_per_region_and_age_v2(arr))
    '''
    Note:
    The 2nd version: number_of_sales_per_region_and_age_v1() returns
    a dictionary with regions ordered in alphabetical order (as this
    is the order in which the dictionary was manually initialised).
    The 2nd version: number_of_sales_per_region_and_age_v2() returns
    a dictionary with a different order of regions (inferred from the data set).
    They are equivalent, as dictionaries are unordered data structures (the
    order of key:value pairs doesn't matter; what matters is the key:value association).
    Assuming that the dictionary returned by number_of_sales_per_region_and_age_v1()
    is named dict_v1, and the dictionary returned by number_of_sales_per_region_and_age_v2()
    is named dict_v2, then the expression dict_v1 == dict_v2 returns True!
    Try it yourself in Python shell by comparing the two solutions 
    with the '==' comparison operator.
    '''
    
    
    # testing Questions 13 & 14
    print('\n\n----------Questions 13 & 14----------\n')
    # 2-D array of 1 element
    arr_1_1 = np.arange(5, 6).reshape(1, 1)
    print("Q13: Last 2 elem. in (1,1) shape:\n", last_2_col_from_last_dim(arr_1_1))
    print("Q14: Last 2 elem. in (1,1) shape:\n", last_2_col_from_highest_dim(arr_1_1))
    # 2-D array of 6 elements 
    arr_3_2 = np.arange(6).reshape(3, 2)
    print("Q13: Last 2 elem. in (3,2) shape:\n", last_2_col_from_last_dim(arr_3_2))
    print("Q14: Last 2 elem. in (3,2) shape:\n", last_2_col_from_highest_dim(arr_3_2))
    arr_6_1 = np.arange(6).reshape(6, 1)
    print("Q13: Last 2 elem. in (6,1) shape:\n", last_2_col_from_last_dim(arr_6_1))
    print("Q14: Last 2 elem. in (6,1) shape:\n", last_2_col_from_highest_dim(arr_6_1))
    # 3-D array of 1 element (x1)
    arr_1_1_1 = np.arange(5, 6).reshape(1, 1, 1)
    print("Q13: Last 2 elem. in (1,1,1) shape:\n", last_2_col_from_last_dim(arr_1_1_1))
    print("Q14: Last 2 elem. in (1,1,1) shape:\n", last_2_col_from_highest_dim(arr_1_1_1))
    # 3-D array of 6 elements 5 (x1)
    arr_2_3_1 = np.arange(6).reshape(2, 3, 1)
    print("Q13: Last 2 elem. in (2,3,1) shape:\n", last_2_col_from_last_dim(arr_2_3_1))
    print("Q14: Last 2 elem. in (2,3,1) shape:\n", last_2_col_from_highest_dim(arr_2_3_1))
    # 1-D array of 12 elements (x1)
    arr_12 = np.arange(1, 13)
    print("Q13: Last 2 elem. in (12,) shape:\n", last_2_col_from_last_dim(arr_12))
    print("Q14: Last 2 elem. in (12,) shape:\n", last_2_col_from_highest_dim(arr_12))
    # 2-D arrays of 12 elements (x6)
    arr_1_12 = arr_12.reshape(1, 12)
    print("Q13: Last 2 elem. in (1, 12) shape:\n", last_2_col_from_last_dim(arr_1_12))
    print("Q14: Last 2 elem. in (1, 12) shape:\n", last_2_col_from_highest_dim(arr_1_12))
    arr_12_1 = arr_12.reshape(12, 1)
    print("Q13: Last 2 elem. in (12, 1) shape:\n", last_2_col_from_last_dim(arr_12_1))
    print("Q14: Last 2 elem. in (12, 1) shape:\n", last_2_col_from_highest_dim(arr_12_1))
    arr_2_6 = arr_12.reshape(2, 6)
    print("Q13: Last 2 elem. in (2, 6) shape:\n", last_2_col_from_last_dim(arr_2_6))
    print("Q14: Last 2 elem. in (2, 6) shape:\n", last_2_col_from_highest_dim(arr_2_6))
    arr_6_2 = arr_12.reshape(6, 2)
    print("Q13: Last 2 elem. in (6, 2) shape:\n", last_2_col_from_last_dim(arr_6_2))
    print("Q14: Last 2 elem. in (6, 2) shape:\n", last_2_col_from_highest_dim(arr_6_2))
    arr_3_4 = arr_12.reshape(3, 4)
    print("Q13: Last 2 elem. in (3, 4) shape:\n", last_2_col_from_last_dim(arr_3_4))
    print("Q14: Last 2 elem. in (3, 4) shape:\n", last_2_col_from_highest_dim(arr_3_4))
    arr_4_3 = arr_12.reshape(4, 3)
    print("Q13: Last 2 elem. in (4, 4) shape:\n", last_2_col_from_last_dim(arr_4_3))
    print("Q14: Last 2 elem. in (3, 4) shape:\n", last_2_col_from_highest_dim(arr_3_4))
    # 3-D arrays of 12 elements (x18)
    arr_2_2_3 = arr_12.reshape(2, 2, 3)
    print("Q13: Last 2 elem. in (2, 2, 3) shape:\n", last_2_col_from_last_dim(arr_2_2_3))
    print("Q14: Last 2 elem. in (2, 2, 3) shape:\n", last_2_col_from_highest_dim(arr_2_2_3))
    arr_2_3_2 = arr_12.reshape(2, 3, 2)
    print("Q13: Last 2 elem. in (2, 3, 2) shape:\n", last_2_col_from_last_dim(arr_2_3_2))
    print("Q14: Last 2 elem. in (2, 3, 2) shape:\n", last_2_col_from_highest_dim(arr_2_3_2))
    arr_3_2_2 = arr_12.reshape(3, 2, 2)
    print("Q13: Last 2 elem. in (3, 2, 2) shape:\n", last_2_col_from_last_dim(arr_3_2_2))
    print("Q14: Last 2 elem. in (3, 2, 2) shape:\n", last_2_col_from_highest_dim(arr_3_2_2))
    arr_1_3_4 = arr_12.reshape(1, 3, 4)
    print("Q13: Last 2 elem. in (1, 3, 4) shape:\n", last_2_col_from_last_dim(arr_1_3_4))
    print("Q14: Last 2 elem. in (1, 3, 4) shape:\n", last_2_col_from_highest_dim(arr_1_3_4))
    arr_3_1_4 = arr_12.reshape(3, 1, 4)
    print("Q13: Last 2 elem. in (3, 1, 4) shape:\n", last_2_col_from_last_dim(arr_3_1_4))
    print("Q14: Last 2 elem. in (3, 1, 4) shape:\n", last_2_col_from_highest_dim(arr_3_1_4))
    arr_3_4_1 = arr_12.reshape(3, 4, 1)
    print("Q13: Last 2 elem. in (3, 4, 1) shape:\n", last_2_col_from_last_dim(arr_3_4_1))
    print("Q14: Last 2 elem. in (3, 4, 1) shape:\n", last_2_col_from_highest_dim(arr_3_4_1))
    arr_1_4_3 = arr_12.reshape(1, 4, 3)
    print("Q13: Last 2 elem. in (1, 4, 3) shape:\n", last_2_col_from_last_dim(arr_1_4_3))
    print("Q14: Last 2 elem. in (1, 4, 3) shape:\n", last_2_col_from_highest_dim(arr_1_4_3))
    arr_4_3_1 = arr_12.reshape(4, 3, 1)
    print("Q13: Last 2 elem. in (4, 3, 1) shape:\n", last_2_col_from_last_dim(arr_4_3_1))
    print("Q14: Last 2 elem. in (4, 3, 1) shape:\n", last_2_col_from_highest_dim(arr_4_3_1))
    arr_4_1_3 = arr_12.reshape(4, 1, 3)
    print("Q13: Last 2 elem. in (4, 1, 3) shape:\n", last_2_col_from_last_dim(arr_4_1_3))
    print("Q14: Last 2 elem. in (4, 1, 3) shape:\n", last_2_col_from_highest_dim(arr_4_1_3))
    # 4-D arrays of 12 elements (x40)
    arr_6_2_1_1 = arr_12.reshape(6,2,1,1)
    print("Q13: Last 2 elem. in (6,2,1,1) shape:\n", last_2_col_from_last_dim(arr_6_2_1_1))
    print("Q14: Last 2 elem. in (6,2,1,1) shape:\n", last_2_col_from_highest_dim(arr_6_2_1_1))
    # 6-D arrays of 12 elements (x126)
    arr_2_2_3_1_1_1 = arr_12.reshape(2,2,3,1,1,1)
    print("Q13: Last 2 elem. in (2,2,3,1,1,1) shape:\n", last_2_col_from_last_dim(arr_2_2_3_1_1_1))
    print("Q14: Last 2 elem. in (2,2,3,1,1,1) shape:\n", last_2_col_from_highest_dim(arr_2_2_3_1_1_1))
    # 12-D arrays of 12 elements (x342)
    arr_1_1_1_1_12_1_1_1_1_1_1_1 = arr_12.reshape(1,1,1,1,12,1,1,1,1,1,1,1)
    print("Q13: Last 2 elem. in (1,1,1,1,12,1,1,1,1,1,1,1) shape:\n", last_2_col_from_last_dim(arr_1_1_1_1_12_1_1_1_1_1_1_1))
    print("Q14: Last 2 elem. in (1,1,1,1,12,1,1,1,1,1,1,1) shape:\n", last_2_col_from_highest_dim(arr_1_1_1_1_12_1_1_1_1_1_1_1))
    arr_12_1_1_1_1_1_1_1_1_1_1_1 = arr_12.reshape(12,1,1,1,1,1,1,1,1,1,1,1)
    print("Q13: Last 2 elem. in (12,1,1,1,1,1,1,1,1,1,1,1) shape:\n", last_2_col_from_last_dim(arr_12_1_1_1_1_1_1_1_1_1_1_1))
    print("Q14: Last 2 elem. in (12,1,1,1,1,1,1,1,1,1,1,1) shape:\n", last_2_col_from_highest_dim(arr_12_1_1_1_1_1_1_1_1_1_1_1))
    arr_1_3_2_2_1_1_1_1_1_1_1_1 = arr_12.reshape(1,3,2,2,1,1,1,1,1,1,1,1)
    print("Q13: Last 2 elem. in (1,3,2,2,1,1,1,1,1,1,1,1) shape:\n", last_2_col_from_last_dim(arr_1_3_2_2_1_1_1_1_1_1_1_1))
    print("Q14: Last 2 elem. in (1,3,2,2,1,1,1,1,1,1,1,1) shape:\n", last_2_col_from_highest_dim(arr_1_3_2_2_1_1_1_1_1_1_1_1))

    
main()
