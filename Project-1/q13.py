import numpy as np 

def total_yearly_loans(arr):

    # create empty lists for months and total_sales
    months = []
    total_sales = []

    # for each product (row indexed 1-7) add together the values in columns indexed 1-4 (sales from Q1-Q4)
    #arr.shape[0] means number of rows in each column - i.e. loops over each array
    for row_index in range(1, arr.shape[0]):
        row_total = 0
        # arr.shape[1] means number of entries in that row - i.e. loops through each array
        for col_index in range(1, arr.shape[1]):
            # calculates the total of loans for each month
            # adds up the values for each month and creates a row total
            row_total += int(arr[row_index][col_index])
            
            # rename the row index
            new_word = 'Tot. ' + arr[row_index][0] 
        
        months.append(new_word)
        total_sales.append(row_total)

    # create an array of arrays
    months_arr = np.array(months)
    total_sales_arr = np.array(total_sales)
    array_of_arrays = np.array([months, total_sales])
    

    np.savetxt("tot_yearly_loans.txt", array_of_arrays, fmt='%s', delimiter =';')

    # returns a 2-D array of 2 rows and 12 columns with the following headings: Tot. 
    # Loans Jan, Tot. Loans Feb, Tot. Loans Mar, ..., Tot. Loans Dec.
    return array_of_arrays




