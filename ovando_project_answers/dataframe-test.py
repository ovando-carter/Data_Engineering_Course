# import pandas as pd
import pandas as pd

# list of strings
lst = ['D', 'M', 'P', 'F', 'Unknown']

# list of int
lst2 = [0,1,1,1,10]

# Calling DataFrame constructor after zipping
# both lists, with columns specified
df_grade_total = pd.DataFrame(list(zip(lst, lst2)),
			columns =['Grade', 'Total'])
print(df)



