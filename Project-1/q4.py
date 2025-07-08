def avg_percentage_per_activity(file_name, course_code, attempt):
    # import pands inside the function to make it portable. 
    import pandas as pd

    try:
        # impord the data
        df_string_file_Name = pd.read_csv('/Users/apple/Documents/coding/companies/FDM/FDM_training/FDM_Python_2/Project/Project-1/' + file_name)   

        # group by course code
        group_code = df_string_file_Name.query("`Course Code` == @course_code") 
        #group by attemp
        group_code_and_attempt = group_code.query("`Attempt` == @attempt") 
        # display data
        display_data = (group_code_and_attempt[['Course Code', 'Activity Name','Attempt', 'Percentage']])  
        # sort by Activity Name
        sorted_data = display_data.sort_values(by='Activity Name', ascending=False) 
        #group by activity name and average percentage - get the mean of the percentage
        group_data = sorted_data.groupby(['Course Code', 'Activity Name', 'Attempt'])['Percentage'].mean() 
        # adds an index to the data
        index_data = group_data.reset_index() 
        # change the name from percentage to average
        rename_data = index_data.rename(columns={'Percentage': 'Average'}) 

        return rename_data  

    except UnicodeDecodeError:
        return 'Error reading file "' + file_name +'"'

    except FileNotFoundError:
        return 'The file "' + file_name +'" does not exist'
    
   
