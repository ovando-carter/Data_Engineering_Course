import numpy as np
import pandas as pd
def avg_percentage_per_activity(inputFile,courseCode,attempt):
   
    try:
        input_file1 = pd.read_csv('/Users/apple/Documents/coding/companies/FDM/FDM_training/FDM_Python_2/Project/Project-1/'+ inputFile)

        
    
        coursecode = input_file1.query("`Course Code` == @courseCode") # group by course code
        coursecodeAndAttenpt = coursecode.query("`Attempt` == @attempt") # group by attemp
        newdata=(coursecodeAndAttenpt[['Course Code','Activity Name','Attempt','Percentage']]) #display new data and group code activity name attemp and percentage
        new_group_data=newdata.groupby(['Course Code','Activity Name']).mean('Percentage') # group nby activity name and average percent
        new_group_data=new_group_data.reset_index() # reset index
        
        return new_group_data
        
    except FileNotFoundError: # file not name
        print('The file “inexistent_file” does not exist')
    except UnicodeDecodeError: # when file exist but when you try to run it
        print('Error reading file "existing_unreadable_file"')
    return 



input_file = 'fdm_training_data_2021.csv'
#input_file = 'C:/Users/gandi/PYTHON/Project-1/existing_unreadable_file'
course_code1 = 'G-21-PSO-05'
attempt = 1
print(avg_percentage_per_activity(input_file,course_code1,attempt))

