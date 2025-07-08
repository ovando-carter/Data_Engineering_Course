
fileName = 'fdm_training_data_2021.csv'
#fileName = 'fdm_training_data_2029.csv'
#fileName = 'existing_unreadable_file'
Academy = [ 'Arlington', 
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


def summary_grades_2021_UK(FileName, Academy):
    import pandas as pd

    try:
        '''Version 4: using groupby()'''
        # load the titanic dataset
        df_stringFileName = pd.read_csv('/Users/apple/Documents/coding/companies/FDM/FDM_training/FDM_Python_2/Project/Project-1/' + FileName)   

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
        return 'Error reading file "' + FileName +'"'
        
    except FileNotFoundError:
        return 'The file "' + FileName +'" does not exist'
    
    


print(summary_grades_2021_UK(fileName, Academy))


    