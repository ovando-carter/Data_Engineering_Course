
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
        df_stringFileName = pd.read_csv('/Users/apple/Documents/coding/companies/FDM/FDM_training/FDM_Python_2/Project/Project-1/' + FileName)   

        
        #group by 'Academy','Percentage' and adds an index to the data
        groupData = df_stringFileName.groupby(['Academy'])['Percentage'].count().reset_index()  
        # change the name from percentage to average
        renameData = groupData.rename(columns={'Percentage': 'Total No. Exams'}) 
        
        # Query each Academy for Distinction, Merit, Pass, Fail
        distinctionResultLO = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'London' & `Percentage` >= 0.90").count()[0]
        distinctionResultG = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Glasgow' & `Percentage` >= 0.90").count()[0]
        distinctionResultAR = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Arlington' & `Percentage` >= 0.90").count()[0]
        distinctionResultAU = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Austin' & `Percentage` >= 0.90").count()[0]
        distinctionResultFF = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Frankfurt' & `Percentage` >= 0.90").count()[0]
        distinctionResultHK = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Hong Kong' & `Percentage` >= 0.90").count()[0]
        distinctionResultJ = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Johannesburg' & `Percentage` >= 0.90").count()[0]
        distinctionResultLU = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Luxembourg' & `Percentage` >= 0.90").count()[0]
        distinctionResultLE = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Leeds' & `Percentage` >= 0.90").count()[0]
        distinctionResultNY = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'New York' & `Percentage` >= 0.90").count()[0]
        distinctionResultP = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Poland' & `Percentage` >= 0.90").count()[0]
        distinctionResultS = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Singapore' & `Percentage` >= 0.90").count()[0]
        distinctionResultSD = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Sydney' & `Percentage` >= 0.90").count()[0]
        distinctionResultTR = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Toronto' & `Percentage` >= 0.90").count()[0]

        meritResultLO = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'London' & `Percentage` <= 0.90 & `Percentage` > 0.80").count()[0]
        meritResultG = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Glasgow' & `Percentage` <= 0.90 & `Percentage` > 0.80").count()[0]
        meritResultAR = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Arlington' & `Percentage` <= 0.90 & `Percentage` > 0.80").count()[0]
        meritResultAU = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Austin' & `Percentage` <= 0.90 & `Percentage` > 0.80").count()[0]
        meritResultFF = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Frankfurt' & `Percentage` <= 0.90 & `Percentage` > 0.80").count()[0]
        meritResultHK = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Hong Kong' & `Percentage` <= 0.90 & `Percentage` > 0.80").count()[0]
        meritResultJ = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Johannesburg' & `Percentage` <= 0.90 & `Percentage` > 0.80").count()[0]
        meritResultLU = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Luxembourg' & `Percentage` <= 0.90 & `Percentage` > 0.80").count()[0]
        meritResultLE = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Leeds' & `Percentage` <= 0.90 & `Percentage` > 0.80").count()[0]
        meritResultNY = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'New York' & `Percentage` <= 0.90 & `Percentage` > 0.80").count()[0]
        meritResultP = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Poland' & `Percentage` <= 0.90 & `Percentage` > 0.80").count()[0]
        meritResultS = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Singapore' & `Percentage` <= 0.90 & `Percentage` > 0.80").count()[0]
        meritResultSD = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Sydney' & `Percentage` <= 0.90 & `Percentage` > 0.80").count()[0]
        meritResultTR = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Toronto' & `Percentage` <= 0.90 & `Percentage` > 0.80").count()[0]

        passResultLO = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'London' & `Percentage` <= 0.80 & `Percentage` > 0.75").count()[0]
        passResultG = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Glasgow' & `Percentage` <= 0.80 & `Percentage` > 0.75").count()[0]
        passResultAR = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Arlington' & `Percentage` <= 0.80 & `Percentage` > 0.75").count()[0]
        passResultAU = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Austin' & `Percentage` <= 0.80 & `Percentage` > 0.75").count()[0]
        passResultFF = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Frankfurt' & `Percentage` <= 0.80 & `Percentage` > 0.75").count()[0]
        passResultHK = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Hong Kong' & `Percentage` <= 0.80 & `Percentage` > 0.75").count()[0]
        passResultJ = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Johannesburg' & `Percentage` <= 0.80 & `Percentage` > 0.75").count()[0]
        passResultLU = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Luxembourg' & `Percentage` <= 0.80 & `Percentage` > 0.75").count()[0]
        passResultLE = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Leeds' & `Percentage` <= 0.80 & `Percentage` > 0.75").count()[0]
        passResultNY = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'New York' & `Percentage` <= 0.80 & `Percentage` > 0.75").count()[0]
        passResultP = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Poland' & `Percentage` <= 0.80 & `Percentage` > 0.75").count()[0]
        passResultS = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Singapore' & `Percentage` <= 0.80 & `Percentage` > 0.75").count()[0]
        passResultSD = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Sydney' & `Percentage` <= 0.80 & `Percentage` > 0.75").count()[0]
        passResultTR = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Toronto' & `Percentage` <= 0.80 & `Percentage` > 0.75").count()[0]

        failResultLO = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'London' & `Percentage` <= 0.75").count()[0]
        failResultG = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Glasgow' & `Percentage` <= 0.75").count()[0]
        failResultAR = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Arlington' & `Percentage` <= 0.75").count()[0]
        failResultAU = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Austin' & `Percentage` <= 0.75").count()[0]
        failResultFF = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Frankfurt' & `Percentage` <= 0.75").count()[0]
        failResultHK = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Hong Kong' & `Percentage` <= 0.75").count()[0]
        failResultJ = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Johannesburg' & `Percentage` <= 0.75").count()[0]
        failResultLU = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Luxembourg' & `Percentage` <= 0.75").count()[0]
        failResultLE = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Leeds' & `Percentage` <= 0.75").count()[0]
        failResultNY = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'New York' & `Percentage` <= 0.75").count()[0]
        failResultP = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Poland' & `Percentage` <= 0.75").count()[0]
        failResultS = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Singapore' & `Percentage` <= 0.75").count()[0]
        failResultSD = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Sydney' & `Percentage` <= 0.75").count()[0]
        failResultTR = df_stringFileName[['Academy', 'Percentage']].query("`Academy` == 'Toronto' & `Percentage` <= 0.75").count()[0]
       
       # collecting all the results for each query
        distinctionResult = [distinctionResultLO, distinctionResultG, distinctionResultAR, distinctionResultAU, 
                            distinctionResultFF, distinctionResultHK, distinctionResultJ, distinctionResultLU, 
                            distinctionResultLE, distinctionResultNY, distinctionResultP, distinctionResultS, 
                            distinctionResultSD, distinctionResultTR
                            ]
        meritResult = [meritResultLO, meritResultG, meritResultAR, meritResultAU, 
                            meritResultFF, meritResultHK, meritResultJ, meritResultLU, 
                            meritResultLE, meritResultNY, meritResultP, meritResultS, 
                            meritResultSD, meritResultTR
                            ]
        passResult = [passResultLO, passResultG, passResultAR, passResultAU, 
                            passResultFF, passResultHK, passResultJ, passResultLU, 
                            passResultLE, passResultNY, passResultP, passResultS, 
                            passResultSD, passResultTR
                            ]
        failResult = [failResultLO, failResultG, failResultAR, failResultAU, 
                            failResultFF, failResultHK, failResultJ, failResultLU, 
                            failResultLE, failResultNY, failResultP, failResultS, 
                            failResultSD, failResultTR
                            ]

        # insert the tot_survived column into the DataFrame after the 'class' column
        renameData.insert(2, "Distinction", distinctionResult)
        renameData.insert(3, "Merit", meritResult)
        renameData.insert(4, "Pass", passResult)
        renameData.insert(5, "Fail", failResult)
    
        return  renameData  

    except UnicodeDecodeError:
        return 'Error reading file "' + FileName +'"'
        
    except FileNotFoundError:
        return 'The file "' + FileName +'" does not exist'
    
    
print(summary_grades_2021_UK(fileName, Academy))



