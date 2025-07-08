'''
located: /Users/apple/Documents/coding/companies/FDM/FDM_training/FDM_Python_2/Project/ovando_project_answers

'''

#q1
'''
string = input("tell me the string \n")
position = int(input("tell me the postion \n"))
newChar = input("tell me the character to what to change it to \n")

# Python code to convert string to list character-wise

def Convert(string, position, newChar):
    list1=[]
    list1[:0]=string
    list1[position] = newChar
    list2 = ''.join(list1)
    return list2

print(Convert(string, position, newChar))

'''

#trying lambda method
'''
def regular_higher_order_func(string, position, newChar, func):


regular_higher_order_func(string, position, newChar, lambda string, position, newChar: list2)
'''
'''
#method2
string = input("tell me the string \n")
position = int(input("tell me the postion \n"))
newChar = input("tell me the character to what to change it to \n")

#will preint the tring up to the position selected, then will concatnate with the new character they we select and then print of the rest of the string from that postion.
replace_ch_in_pos = (lambda string, position, newChar: string[:position] + newChar + string[position +1:])(string, position, newChar)
print(replace_ch_in_pos)
'''

'''
#Hard coded
replace_ch_in_pos1 = (lambda word, posi, char: word[:posi] + char + word[posi +1:])('ABCDE', 3, '#')
replace_ch_in_pos2 = (lambda word, posi, char: word[:posi] + char + word[posi +1:])('Trainer', 6, 'e')
replace_ch_in_pos3 = (lambda word, posi, char: word[:posi] + char + word[posi +1:])('python', 0, 'P')
replace_ch_in_pos4 = (lambda word, posi, char: word[:posi] + char + word[posi +1:])('12-11-2003-17:34:54', 10, ' ')
replace_ch_in_pos5 = (lambda word, posi, char: word[:posi] + char + word[posi +1:])('12345', 4, '0')
replace_ch_in_pos6 = (lambda word, posi, char: word[:posi] + char + word[posi +1:])('stutter', 1, 'c')
replace_ch_in_pos7 = (lambda word, posi, char: word[:posi] + char + word[posi +1:])('P', 0, '£')

print(replace_ch_in_pos1)
print(replace_ch_in_pos2)
print(replace_ch_in_pos3)
print(replace_ch_in_pos4)
print(replace_ch_in_pos5)
print(replace_ch_in_pos6)
print(replace_ch_in_pos7)
'''


'''
#q3 Numpy
import numpy as np

arr = np.array([45, 4832, 123, 987655])

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
        #add in the biggest number first 
        if len(str_from_arr[i]) == val:
            new_arr = np.append(new_arr,str_from_arr[i])
        else:
            while len(str_from_arr[i]) < val:
                str_from_arr[i] = '0'+str_from_arr[i]
                if len(str_from_arr[i])==val:
                    new_arr = np.append(new_arr,str_from_arr[i])

    return new_arr

print(pad_arr_int_to_str(arr))
'''

###############################################################################################################################


#q6.
# returns a list of strings obtained from the input list
# the input list of strings of equal length
# every string the character at the specified position is replaced with the given character
# The ordinary function solution() must consist of one return statement alone,
# • the map() built-in function OR
# • list comprehension OR
# • generator comprehension


#string = input("tell me the string \n")
#position = int(input("tell me the postion \n"))
#newChar = input("tell me the character to what to change it to \n")

stringLst = ['$153.25', '$100.50', '$199.99', '$300.00']
position = 0
newChar = '£'

'''
newList = []
for i in range(0, len(stringLst)):
    string = stringLst[i]
    if isinstance(string, str):
        newList.append(string[:position] + newChar + string[position +1:])
        #print(newString)
'''
'''
newList = [newString = string[:position] + newChar + string[position +1:]for i in range(0, len(stringLst)) string = stringLst[i] if isinstance(string, str) newList.append(string[:position] + newChar + string[position +1:])]
print(newList)
'''
'''
def solution(word , char, posi):
    return list(map(lambda x: x[:posi] + char + x[posi +1:],word))

print(solution(stringLst, newChar, position))
    
#string = stringLst[i] for i in range(0, len(stringLst))
#print(newString)
'''
'''
#will preint the tring up to the position selected, then will concatnate with the new character they we select and then print of the rest of the string from that postion.
replace_ch_in_pos = (lambda string, position, newChar: string[:position] + newChar + string[position +1:])(string, position, newChar)
print(replace_ch_in_pos)
'''
                
###############################################################################################################################

#q4 

# location: find the files for fdm_training_data_2021.csv  and exsiting_unreadable_file here: /Users/apple/Documents/coding/companies/FDM/FDM_training/FDM_Python_2/Project/Project-1


# find the average percentate per activity in the Activity Name column

# need try statement
'''
Try:
Except:
    # if it exsists but unreadable
    # use exsiting_unreadable_file  
Else:
    # return “inexistent_file” does not exist
Final: 
    #return Error reading file "existing_unreadable_file".
'''
#  In case the input file is not found, the following message should be returned (not displayed): The file return “inexistent_file” does not exist

# In case the input file is found, but is not readable, the following message should be returned (not displayed): return Error reading file "existing_unreadable_file".

'''
#fileName = 'fdm_training_data_2021.csv'
#fileName = 'fdm_training_data_2029.csv'
fileName = 'existing_unreadable_file'
courseCode = 'L-21-FOU-02'
Attempt = 2



def avg_percentage_per_activity(FileName, courseCode, Attempt):
    import pandas as pd

    
    
    try:
        df_stringFileName = pd.read_csv('/Users/apple/Documents/coding/companies/FDM/FDM_training/FDM_Python_2/Project/Project-1/' + FileName)   

        # group by course code
        groupCode = df_stringFileName.query("`Course Code` == @courseCode") 
        #group by attemp
        groupCodeAndAttempt = groupCode.query("`Attempt` == @Attempt") 
        # display data
        displayData = (groupCodeAndAttempt[['Course Code', 'Activity Name','Attempt', 'Percentage']])  
        # sort by Activity Name
        sortedData = displayData.sort_values(by='Activity Name', ascending=False) 
        #group by activity name and average percentage
        groupData = sortedData.groupby(['Course Code', 'Activity Name', 'Attempt'])['Percentage'].mean() 
        # adds an index to the data
        indexData = groupData.reset_index() 
        # change the name from percentage to average
        renameData = indexData.rename(columns={'Percentage': 'Average'}) 

        return renameData  

    except UnicodeDecodeError:
        return 'Error reading file "' + FileName +'"'
    except FileNotFoundError:
        return 'The file "' + FileName +'" does not exist'
    

    
    

print(avg_percentage_per_activity(fileName, courseCode, Attempt))
'''
###############################################################################################################################

'''
import numpy as np
import os

# NB: I am running my code on a mac, so the file path needed to be changed in the test for it to work. 
# file_path = currentDirectoryPath + '\\data_set_1.txt' change to file_path = currentDirectoryPath + '/data_set_1.txt' 



currentDirectoryPath = os.getcwd()
file_path = currentDirectoryPath + '/data_set_1.txt'
input_array = np.loadtxt(file_path, usecols=(1,2,3,4,5,6,7,8,9,10,11), delimiter='\t', dtype=str)
#file_path_2 = currentDirectoryPath + '/data_set_1_bis.txt'
#input_array_2 = np.loadtxt(file_path_2, usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22), delimiter='\t', dtype=str)

lookup_val = 'WX-534'
row_num = 5


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

        # returns the corresponding value in a specified row (implement the Excel HLOOKUP function with the exact match)
        # the shape will give the number of entries in both directions (8,11) meaning 8 rows and 11 columns
        for i in range (input_array.shape[1]):

            # finds the value in the first row of a given NumPy array
            # we use the information on the rows and columns here to select the sepefic entry that we want.
            # in this case we care about finding the specific lookup value i.e. WX-534.
            if input_array[0][i] == lookup_val:
                index = i

                Return_val = input_array[row_num-1][index]
                
                # the function always returns a string value
                return str(Return_val)
        
print(hlookup(input_array,lookup_val,row_num))
'''
###############################################################################################################################
'''
# q9. 


file_name = 'fdm_training_data_2021.csv'
#fileName = 'fdm_training_data_2029.csv'
#fileName = 'existing_unreadable_file'
academy = [ 'Arlington', 
            'Austin', 
            'Frankfurt', 
            'Glasgow', 
            'Hong Kong', 
            'Johannesburg', 
            'Leeds', 
            'London', 
            'Luxembourg', 
            'New York',
            'Poland',
            'Singapore',
            'Sydney',
            'Toronto']


def summary_grades_2021_UK(file_name, academy):
    import pandas as pd

    try:
        '''Version 4: using groupby()'''
        # load the titanic dataset
        df_stringFileName = pd.read_csv('/Users/apple/Documents/coding/companies/FDM/FDM_training/FDM_Python_2/Project/Project-1/' + file_name)   

        #group by 'Academy','Percentage' and adds an index to the data
        groupData = df_stringFileName.groupby(['Academy'])['Percentage'].count().reset_index()  
        
        # change the name from percentage to average
        renameData = groupData.rename(columns={'Percentage': 'Total No. Exams'}) 
        
        # slice the data frame horizontally (extract rows for each grade)
        # This section will filter out each grade - Distinction, Merit, Pass, Fail
        renameData_D = df_stringFileName.query('`Percentage` >= 0.90')
        renameData_M = df_stringFileName.query('`Percentage` <= 0.90 & `Percentage` > 0.80')
        renameData_P = df_stringFileName.query('`Percentage` <= 0.80 & `Percentage` > 0.75')
        renameData_F = df_stringFileName.query('`Percentage` <= 0.75')
        
        # I need to group by index again so I can connect this with the renameData
        dis_groupby = renameData_D.groupby(['Academy'])['Percentage'].count().reset_index()
        mer_groupby = renameData_M.groupby(['Academy'])['Percentage'].count().reset_index()
        pas_groupby = renameData_P.groupby(['Academy'])['Percentage'].count().reset_index()
        fai_groupby = renameData_F.groupby(['Academy'])['Percentage'].count().reset_index()

        # change the name of each grade
        dis_rename = dis_groupby.rename(columns={'Percentage': 'Distinction'})
        mer_rename = mer_groupby.rename(columns={'Percentage': 'Merit'})
        pas_rename = pas_groupby.rename(columns={'Percentage': 'Pass'})
        fai_rename = fai_groupby.rename(columns={'Percentage': 'Fail'})
        
        # merge the data frames together
        merge_D = pd.merge(renameData, dis_rename)
        merge_DM = pd.merge(merge_D, mer_rename)
        merge_DMP = pd.merge(merge_DM, pas_rename)
        merge_DMPF = pd.merge(merge_DMP, fai_rename)
        
        return merge_DMPF
        

    except UnicodeDecodeError:
        return 'Error reading file "' + file_name +'"'
        
    except FileNotFoundError:
        return 'The file "' + file_name +'" does not exist'
    
    


print(summary_grades_2021_UK(file_name, academy))
'''

    

###############################################################################################################################

'''
# 10

import matplotlib.pyplot as plt
import numpy as np

# ported from 9
#from q9 import *


# Matplotlib Example: Grouped Bar Plot
no_grades = 4

# convert dataframe into array 
#select rows called london, leeds and glasgow .iloc[,7]


xG = summary_grades_2021_UK(file_name, academy).loc[3].to_numpy()
glasgow = xG[2:6]

xLe = summary_grades_2021_UK(file_name, academy).loc[6].to_numpy()
leeds = xLe[2:6]

xLo = summary_grades_2021_UK(file_name, academy).loc[7].to_numpy()
london = xLo[2:6]

# creating plot
fig, ax = plt.subplots()
index = np.arange(no_grades)
bar_width = 0.3

# x position is the index, y position is the data from the array in the first case london, bar width is defined above at 0.3
london_bars = ax.bar(index, london, bar_width, color = 'blue', label='london')
leeds_bars = ax.bar(index + bar_width, leeds, bar_width, color='orange', label='leeds')
glasgow_bars = ax.bar(index + (2 * bar_width), glasgow, bar_width, color='green', label='glasgow')

ax.set_facecolor('white') # sets the background colour of the plot

ax.set_xlabel('Grade') # sets the x-axis label 
ax.set_ylabel('Number of exams') # sets the y-axis label 
ax.set_title('Number of exams by grades in UK Academies') # sets the plot title

ax.set_xticks(index + bar_width) # places the ticks right between the male and leeds bars
ax.set_xticklabels(('Distinction', 'Merit', 'Pass', 'Fail'))

ax.bar_label(london_bars, padding=3)   # add values as labels to london bars
ax.bar_label(leeds_bars, padding=3) # add values as labels to leeds bars
ax.bar_label(glasgow_bars, padding=3) # add values as labels to leeds bars

ax.legend()

fig.tight_layout()

plt.show()
#plt.savefig('grouped_bar_plot.png')
'''

# q11

# The higher order function can be defined as an ordinary or lambda function 
def solution(strings, char, posi):

    def ordinary_higher(strings, char, posi, func):
        # passed lambda function for q1 as an argument to the higher 
        # order function, or returned from a higher order function
        new_list = [str(func(word, char, posi)) for word in strings]

        return new_list
    
    replace_ch_in_pos = ordinary_higher(strings, char, posi, lambda word, char, posi: word[:posi] + char + word[posi +1:])

    return replace_ch_in_pos

  
strings = ['$153.25', '$100.50', '$199.99', '$300.00']
char = '£'
posi = 0


print(solution(strings, char, posi))

