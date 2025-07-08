# should be london leads glasgo, but mine is the opposete. may need to do reverse index?

# An empty list should return an empty DataFrame?


def summary_grades_2021_UK(file_name, academies):
    import pandas as pd

    try:

        # load the dataset
        df_stringFileName = pd.read_csv('/Users/apple/Documents/coding/companies/FDM/FDM_training/FDM_Python_2/Project/Project-1/' + file_name)   

        academyfilter = df_stringFileName.query("`Academy` == @academies")

        #group by 'Academy','Percentage' and adds an index to the data
        groupData = academyfilter.groupby(['Academy'])['Percentage'].count().reset_index()  
                
        # change the name from percentage to average - check

        renameData = groupData.rename(columns={'Percentage': 'Total No. Exams'}) 

        # slice the data frame horizontally (extract rows for each grade)
        # This section will filter out each grade - Distinction, Merit, Pass, Fail
        renameData_D = df_stringFileName.query(' `Percentage` >= 0.90')
        renameData_M = df_stringFileName.query('`Percentage` < 0.90 & `Percentage` >= 0.80')
        renameData_P = df_stringFileName.query('`Percentage` < 0.80 & `Percentage` >= 0.75')
        renameData_F = df_stringFileName.query('`Percentage` < 0.75')
                
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


        row_order=pd.Series(academies, name='Academy') ### Create order of data 
        row_order1=pd.DataFrame(row_order, columns=['Academy'])

        # merge the data frames together
        merge_D = pd.merge(renameData, dis_rename)
        merge_DM = pd.merge(merge_D, mer_rename)
        merge_DMP = pd.merge(merge_DM, pas_rename)
        merge_DMPF = pd.merge(merge_DMP, fai_rename)
        DMPF_reorder = pd.merge(merge_DMPF, row_order1)

        # reverse index
        #merge_DMPF_rev = merge_DMPF[::-1].reset_index(drop = True) # works for london, lees, glasgow

        return DMPF_reorder        
                
    except UnicodeDecodeError:
        return 'Error reading file "' + file_name +'"'
            
    except FileNotFoundError:
        return 'The file "' + file_name +'" does not exist'        
    
    

# dataset that works
file_name = 'fdm_training_data_2021.csv'

# test for file that dose not exsist
#fileName = 'fdm_training_data_2029.csv'

# test for unreadable file
#fileName = 'existing_unreadable_file'

academies = ['Frankfurt', 'Poland', 'Luxembourg']
'''
academies = [ 'Arlington', 
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
'''

print(summary_grades_2021_UK(file_name, academies))





    