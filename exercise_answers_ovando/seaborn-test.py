'''
# import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# load the built-in 'titanic' data set into a data frame
df_titanic = sns.load_dataset("titanic")
print(df_titanic)

# draw the plot and include the plot title
sns.countplot(data=df_titanic, x="sex")
plt.title("Total number of passengers by gender")
plt.show()

'''

#######################
# Module 4B - Seaborn #
#######################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Question 1
# ----------
"""
Using the 'titanic' built-in Seaborn data set, create a
distribution plot to visualise the survival distribution
a) by each of the three passenger classes (first, second, third)
b) by each of the three passenger types (man, woman, child)
c) by each gender (male, female)
"""
# load the built-in 'titanic' data set into a data frame
df_titanic = sns.load_dataset('titanic')
# print the list of all the column headers of the 'titanic' data set
print(df_titanic.columns.values)


# Question 1a)
# ------------
# setting hue kwarg to class, a separate density estimate
# will be computed for each value of the variable class
#sns.displot(data=df_titanic, x='survived', hue='class', kind='kde')
# OR
sns.kdeplot(data=df_titanic, x='survived', hue='class')
plt.title('Survival distribution by passenger classes')
plt.tight_layout()
plt.show()