def summary_grades_per_activity():
    return 

# use q4 + q11



def avg_percentage_per_activity(file_name, course_code):
    import pandas as pd

    try:
        df_string_file_Name = pd.read_csv('/Users/apple/Documents/coding/companies/FDM/FDM_training/FDM_Python_2/Project/Project-1/' + file_name)   
        #print(df_string_file_Name)

        # group by course code
        group_code = df_string_file_Name.query("`Course Code` == @course_code") 
         
        # display data
        display_data = (group_code[['Course Code', 'Activity Name','Attempt', 'Percentage']])  
        # sort by Activity Name
        sorted_data = display_data.sort_values(by='Activity Name', ascending=False) 
        #group by activity name and average percentage - get the mean of the percentage
        group_data = sorted_data.groupby(['Course Code', 'Activity Name', 'Attempt'])['Percentage'].sum() 
        # adds an index to the data
        index_data = group_data.reset_index() 
        # change the name from percentage to average

        
        '''
        # list of strings
        lst = ['D', 'M', 'P', 'F', 'Unknown']

        # list of int
        lst2 = [0,1,1,1,10]

        # Calling DataFrame constructor after zipping
        # both lists, with columns specified
        df_grade_total = pd.DataFrame(list(zip(lst, lst2)),
                    columns =['Grade', 'Total'])
    
        # attempt to connect newly made data frame to the same group by as previous.
        grade_total_group = df_grade_total.groupby(['Course Code', 'Activity Name', 'Attempt'])['Percentage'].count().reset_index
        print(grade_total_group)
        '''
        '''
        # new group for grade and total
        grade = group_code.query('`Percentage` >= @percentages')
        total = grade.query('`Percentage` >= @percentages')
        print(total)


        # for loop to look through each row:
        for i in range(data.shape[1]):
            # if statement to hlookup to find percentage column data
            if data[0][i] == 'Percentage':
            # e.g. if percentage >= 0.9: 
                # output D
            #elif percentage <0.9 and percentage >= 0.8:
                # output M
            #elif percentage <0.8 and percentage >= 0.75:
                # output P
            #elif percentage <0.75:
                # output F
        '''


        '''
        rename_data = group_code.rename(columns={'Percentage': 'Grade'}) 
        rename_data2 = group_code.rename(columns={'Percentage': 'Total'})
        '''
        return None 

    except UnicodeDecodeError:
        return 'Error reading file "' + file_name +'"'

    except FileNotFoundError:
        return 'The file "' + file_name +'" does not exist'
    

file_name = 'fdm_training_data_2021.csv'
#file_name = 'fdm_training_data_2029.csv'
#file_name = 'existing_unreadable_file'
course_code = 'L-21-FOU-02'

    
avg_percentage_per_activity(file_name, course_code)    
print()
