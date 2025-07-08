


def summary_grades_2021_UK(file_name, academy):

    import numpy as np
    import pandas as pd
    
    try:
        # why did he do this if statement? 
        if bool(academy) == False:

            df_string_file_name = pd.read_csv(file_name)

            newdata=(df_string_file_name[['Academy','Percentage']])

            newdatafilter=newdata.query("`Academy` == @academy")

            # slice the data frame horizontally (extract rows for each grade)
            # This section will filter out each grade - Distinction, Merit, Pass, Fail
            dis_renameata_F = newdatafilter.query("`Percentage` <0.75")
            dis_renameata_P = newdatafilter.query("Percentage >= 0.75 and Percentage<0.80")
            dis_renameata_M = newdatafilter.query("`Percentage` >= 0.80 & `Percentage`<0.90")
            dis_renameata_D = newdatafilter.query ("`Percentage` >= 0.90")

            # I need to group by index again so I can connect this with the dis_renameata
            fai_groupby = dis_renameata_F.groupby(['Academy'])['Percentage'].count().reset_index()
            pas_groupby = dis_renameata_P.groupby(['Academy'])['Percentage'].count().reset_index()
            mer_groupby = dis_renameata_M.groupby(['Academy'])['Percentage'].count().reset_index()
            dis_groupby = dis_renameata_D.groupby(['Academy'])['Percentage'].count().reset_index()
            
            tot_groupby = newdatafilter.groupby(['Academy'])['Percentage'].count().reset_index()

            # change the name of each grade
            fai_rename = fai_groupby.rename(columns={'Percentage': 'Fail'})
            pas_rename = pas_groupby.rename(columns={'Percentage': 'Pass'})
            mer_rename = mer_groupby.rename(columns={'Percentage': 'Merit'})
            dis_rename = dis_groupby.rename(columns={'Percentage': 'Distinction'})
            
            # change the name from percentage to average
            tot_rename = tot_groupby.rename(columns={'Percentage': 'Total No. Exams'})

            # merge the data frames together
            merge_D = pd.merge(tot_rename, dis_rename)
            merge_DM = pd.merge(merge_D, mer_rename)
            merge_DMP = pd.merge(merge_DM, pas_rename)
            merge_DMPF = pd.merge(merge_DMP, fai_rename)

            merge_DMPFSort = merge_DMPF[['Academy','Total No. Exams','Distinction','Merit','Pass','Fail']].sort_values(by='Total No. Exams', ascending=False )
            
            # sort the academies
            merge_DMPFSortreset = merge_DMPFSort.reset_index(drop=True)
            
            return merge_DMPFSortreset
            
        else:
            row_order = pd.Series(academy, name='Academy') ### Create order of data 
            row_order1 = pd.DataFrame(row_order, columns=['Academy'])
            

            df_string_file_name = pd.read_csv(file_name)
            newdata=(df_string_file_name[['Academy','Percentage']])
            newdatafilter=newdata.query("`Academy` == @academy")
            dis_renameata_F = newdatafilter.query("`Percentage` <0.75")     #### Filter data for fail, pass, meric
            dis_renameata_P = newdatafilter.query("Percentage >= 0.75 and Percentage<0.80")
            dis_renameata_M = newdatafilter.query("`Percentage` >= 0.80 & `Percentage`<0.90")
            dis_renameata_D = newdatafilter.query ("`Percentage` >= 0.90")
            
            fai_groupby = dis_renameata_F.groupby(['Academy'])['Percentage'].count().reset_index()  ### group by count
            pas_groupby = dis_renameata_P.groupby(['Academy'])['Percentage'].count().reset_index()
            mer_groupby = dis_renameata_M.groupby(['Academy'])['Percentage'].count().reset_index()
            dis_groupby = dis_renameata_D.groupby(['Academy'])['Percentage'].count().reset_index()
            tot_groupby = newdatafilter.groupby(['Academy'])['Percentage'].count().reset_index() ### group by totol of exam
            
            
            fai_rename = fai_groupby.rename(columns={'Percentage': 'Fail'}) ## rename 
            pas_rename = pas_groupby.rename(columns={'Percentage': 'Pass'})
            mer_rename = mer_groupby.rename(columns={'Percentage': 'Merit'})
            dis_rename = dis_groupby.rename(columns={'Percentage': 'Distinction'})
            tot_rename = tot_groupby.rename(columns={'Percentage': 'Total No. Exams'})
            
            
            
            merge_ = pd.merge(row_order1,tot_rename)  ## merge everything together
            merge_D = pd.merge(merge_, dis_rename)
            merge_DM = pd.merge(merge_D, mer_rename)
            merge_DMP = pd.merge(merge_DM, pas_rename)
            merge_DMPF = pd.merge(merge_DMP, fai_rename)
            merge_DMPFSortreset = merge_DMPF.reset_index(drop=True)
            
            return merge_DMPFSortreset

            
            
    except FileNotFoundError: # file not name
        return 'The file "inexistent_file" does not exist'
        
    except UnicodeDecodeError: # when file exist but when you try to run it
        return 'Error reading file "existing_unreadable_file"'
    



