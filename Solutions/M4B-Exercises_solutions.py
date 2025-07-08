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



# Question 1b)
# ------------
# setting hue kwarg to who, a separate density estimate
# will be computed for each value of the variable who
#sns.displot(data=df_titanic, x='survived', hue='who', kind='kde')
# OR
sns.kdeplot(data=df_titanic, x='survived', hue='who')
plt.title('Survival distribution by passenger types')
plt.tight_layout()
plt.show()


# Question 1c)
# setting hue kwarg to sex, a separate density estimate
# will be computed for each value of the variable sex
#sns.displot(data=df_titanic, x='survived', hue='sex', kind='kde')
# OR
sns.kdeplot(data=df_titanic, x='survived', hue='sex')
plt.title('Survival distribution by passenger gender')
plt.tight_layout()
plt.show()



# Question 2
# ----------
'''
Bundle the three plots created in question 1 together into one multi-plot
(grid of subplots) with one row and tree columns.
'''
fig, ax = plt.subplots(1, 3, figsize=(10, 5))
# note: grid of subplots can't be created using figure-level plots (such as displot)
# grids of plots can be created using axes-level functions (here kdeplot)
sns.kdeplot(data=df_titanic, x='survived', ax=ax[0], hue='class')
sns.kdeplot(data=df_titanic, x='survived', ax=ax[1], hue='who')
sns.kdeplot(data=df_titanic, x='survived', ax=ax[2], hue='sex')
# alternative way of changing the size of figure to 10X5
#fig.set_figwidth(10)
#fig.set_figheight(5)
plt.suptitle("Survival distribution - multiplot figure")
plt.show()



# Question 3
# ----------
"""
Using the 'titanic' Seaborn built-in dataset, illustrate the number of male and female
passengers on the Titanic split by class using:
a) countplot() function, including the numbers on top of each bar
b) count plot through catplot() function, including the numbers in the centre of each bar
c) barplot() function, including the numbers on top of each bar
d) bar plot through catplot() function, including the numbers in the centre of each bar
e) multiple bar plot, where each subplot relates to a different gender value. Include
   the numbers in the centre of each bar. Use the 'bar' value for kwarg kind.
f) multiple bar plot, where each subplot relates to a different gender value. Include
   the numbers in the centre of each bar. Use the 'count' value for kwarg kind.
"""
# Question 3a)
# ------------
# create a count plot
# store the matplotlib Axes object returned by axes-level function countplot()
ax = sns.countplot(data=df_titanic, x='sex', hue='class')
# iterate through containers (groups), identified by hue kwarg
for container in ax.containers:
    # include numbers on top of the bars
    ax.bar_label(container, label_type='edge')
# set the title and display the plot
plt.title("Number of passengers by gender split by class\nusing countplot()")
plt.show() 


# Question 3b)
# ------------
# store the FaceGrid object returned by figure-level function catplot()
fg = sns.catplot(data=df_titanic, x='sex', hue='class', kind='count', legend=False)
# store the matplotlib Axes subplot objects returned by FacetGrid.facet_axis()
# here axis are present in row 0 and column 0 (since there are no subplots)
ax = fg.facet_axis(0, 0)
# iterate through containers (groups), identified by hue kwarg
for container in ax.containers:
    # include numbers in the centre of the bars
    ax.bar_label(container, label_type='center')
# set the title, legend, adjust the layout and display the plot
plt.title("Number of passengers by gender split by class\nusing catplot() with kind='count'")
plt.legend(title='class', loc="upper right")
plt.tight_layout()
plt.show() 


# Question 3c) - VERSION 1: solution using query() Pandas function
# ------------
# calculate the number of male/female passengers within first/second/third class 
# (note that the variable 'class' cannot be used as it is a Python keyword)
female_first_count = df_titanic[['sex', 'pclass']].query('sex=="female" and pclass==1').count()
female_second_count = df_titanic[['sex', 'pclass']].query('sex=="female" and pclass==2').count()
female_third_count = df_titanic[['sex', 'pclass']].query('sex=="female" and pclass==3').count()
male_first_count = df_titanic[['sex', 'pclass']].query('sex=="male" and pclass==1').count()
male_second_count = df_titanic[['sex', 'pclass']].query('sex=="male" and pclass==2').count()
male_third_count = df_titanic[['sex', 'pclass']].query('sex=="male" and pclass==3').count()
# create the data frame with these calculated values
df_totals_calc = pd.DataFrame({
   'gender': ['male', 'male', 'male', 'female', 'female', 'female'],
   'class': ['First', 'Second', 'Third', 'First', 'Second', 'Third'],
   'count': [male_first_count[0], male_second_count[0], male_third_count[0], female_first_count[0], female_second_count[0], female_third_count[0]]
})
# construct the plot
ax = sns.barplot(data=df_totals_calc, x='gender', y='count', hue='class')
# include numbers on top of the bars
#ax.bar_label(ax.containers[0], label_type='edge')  # values for 'First' class bars
#ax.bar_label(ax.containers[1], label_type='edge')  # values for 'Second' class bars
#ax.bar_label(ax.containers[2], label_type='edge')  # values for 'Third' class bars
# OR
# iterate through containers (groups), identified by hue kwarg
for container in ax.containers:
    ax.bar_label(container, label_type='edge')  # values for bars of each class
# set the title, adjust the layout and display the plot
plt.title("Number of passengers by gender split by class\nusing barplot() with query()")
plt.tight_layout()
plt.show() 


# Question 3c) - VERSION 2: solution using groupby() Pandas function, with 'female' bars shown before 'male'
# ------------
# calculate the number of male/female passengers within first/second/third class 
df_totals = df_titanic.groupby(['sex', 'class'])['survived'].count().reset_index()
print(df_totals)
# draw the plot
ax = sns.barplot(data=df_totals, x='sex', y='survived',hue='class')
# include numbers in the centre of the bars
for container in ax.containers:
    ax.bar_label(container, label_type='edge')  # values for bars of each class
plt.title("Number of passengers by gender split by class\nusing barplot() with groupby() - female bars shown first")
plt.tight_layout()
plt.show()


# Question 3c) - VERSION 3: solution using groupby() Pandas function, with sort_values() to show 'male' bars before 'female'
# ------------
# calculate the number of male/female passengers within first/second/third class 
df_totals = df_titanic.groupby(['sex', 'class'])['survived'].count().reset_index().sort_values(by='sex', ascending=False)
print(df_totals)
# draw the plot
ax = sns.barplot(data=df_totals, x='sex', y='survived',hue='class')
# include numbers in the centre of the bars
for container in ax.containers:
    ax.bar_label(container, label_type='edge')  # values for bars of each class
plt.title("Number of passengers by gender split by class\nusing barplot() with groupby() & sort_values()")
plt.tight_layout()
plt.show()


# Question 3c) - VERSION 4: solution using groupby() Pandas function, with Categorical() to show 'male' bars before 'female'
# ------------
# calculate the number of male/female passengers within first/second/third class 
df_totals = df_titanic.groupby(['sex', 'class'])['survived'].count().reset_index()
print(df_totals)
# change the order of the sex values to display 'male' bars before 'female'
df_totals.sex = pd.Categorical(df_totals.sex, categories=['male', 'female'])
# readjust the index to a new sequential index that will correspond to the
# sex values sorted according to the new given order ('male' before 'female')
df_totals = df_totals.groupby(['sex', 'class'])['survived'].sum().reset_index()
# draw the plot
ax = sns.barplot(data=df_totals, x='sex', y='survived',hue='class')
# include numbers in the centre of the bars
for container in ax.containers:
    ax.bar_label(container, label_type='edge')  # values for bars of each class
plt.title("Number of passengers by gender split by class\nusing barplot() with groupby() & Categorical()")
plt.tight_layout()
plt.show()


# Question 3d)
# ------------
# store the FaceGrid object returned by figure-level function catplot()
fg = sns.catplot(data=df_totals_calc, x='gender', y='count', hue='class', kind='bar', legend=False)
# store the matplotlib Axes subplot objects returned by FacetGrid.facet_axis()
# here axis are present in row 0 and column 0 (since there are no subplots)
ax = fg.facet_axis(0, 0)
# iterate through containers (groups), identified by hue kwarg
for container in ax.containers:
    # include numbers in the centre of the bars
    ax.bar_label(container, label_type='center')
plt.title("Number of passengers by gender split by class\nusing catplot() with kind='bar'")
plt.tight_layout()
plt.legend(title='class', loc='upper right')
plt.show() 


# Question 3e)
# ------------
# create a multiple plot showing the number of passengers in each class
# plot the dependency between 'class' and 'count'
# data variables against the data variable 'gender' of the dataset
fg = sns.catplot(data=df_totals_calc, x='class', y='count', col='gender', kind='bar')
# iterate through axes (subplots)
for ax in fg.axes.ravel():
    # iterate through containers (groups)
    for container in ax.containers:
        # include numbers in the centre of the bars
        ax.bar_label(container, label_type='center')
plt.suptitle("Number of passengers by class for each facet of gender\nusing catplot() with kind='bar' and col='gender'")
plt.tight_layout()
plt.show()


# Question 3f)
# ------------
# store the FaceGrid object returned by figure-level function catplot()
# Note: hue adds an additional layer of nesting to the bars. Setting the kwarg dodge to False
# prevents bars from shifting along the categorical axis, and restores their initial width.
fg = sns.catplot(data=df_titanic, x='class', hue='class', col='sex', kind='count', dodge=False)
# iterate through axes (subplots), identified by col kwarg
for ax in fg.axes.ravel():
    # iterate through containers (groups) of each subplot, identified by hue kwarg
    for container in ax.containers:
        # include numbers in the centre of the bars
        ax.bar_label(container, label_type='center')
plt.suptitle("Number of passengers by class for each facet of gender\nusing catplot() with kind='count' and col='gender'")
plt.tight_layout()
plt.show() 



# Question 4
# ----------
'''
Using the 'titanic' Seaborn built-in dataset, illustrate
the average age per class of the titanic passengers
a) using the barplot() function
b) using the catplot() function
Include the numbers at the centre of bars.
'''
# Question 4a)
# ------------
ax = sns.barplot(data=df_titanic, x="class", y="age", ci=None)
# iterate through axes (subplots)
for container in ax.containers:
    # include numbers in the centre of the bars
    ax.bar_label(container, label_type='center')
# Note: since there is no value set for kwarg hue, there is no need
# for the inner loop (to iterate through groups within each subplot).
# We can therefore replace the above nested loop with the following
# statement to include numbers in the centre of the bars:
#ax.bar_label(ax.containers[0], label_type='center')  # values for the average age bars
plt.title('Average age of passengers by class\nusing barplot()')
plt.xlabel('Class')
plt.ylabel('Average Age')
plt.show()


# Question 4b)
# ------------
fg = sns.catplot(data=df_titanic, x='class', y='age', kind='bar', ci=None)
# iterate through axes (subplots)
for ax in fg.axes.ravel():
    # iterate through containers (groups)
    for container in ax.containers:
        # include numbers in the centre of the bars
        ax.bar_label(container, label_type='center')
# Note: since there is no value set for kwarg col, there is no need for the outer loop
# (to iterate through subplots), and since there is no value set for kwarg hue,
# there is no need for the inner loop (to iterate through groups within each subplot).
# We can therefore replace the above nested loop with the following statement
# to include numbers in the centre of the bars:
#fg.ax.bar_label(ax.containers[0], label_type='center')  # values for the average age bars
plt.title('Average age of passengers by class\nusing catplot()')
plt.tight_layout()
plt.show() 



# Question 5
# ----------
'''
Using the 'titanic' Seaborn built-in dataset, illustrate
the average age per gender of the titanic passengers
a) using the barplot() function
b) using the catplot() function
Include the numbers at the centre of bars.
'''
# Question 5a)
# ------------
ax = sns.barplot(data=df_titanic, x="sex", y="age", ci=None)
# iterate through axes (subplots)
for container in ax.containers:
    # include numbers in the centre of the bars
    ax.bar_label(container, label_type='center')
# Note: since there is no value set for kwarg hue, there is no need
# for the inner loop (to iterate through groups within each subplot).
# We can therefore replace the above nested loop with the following 
# statement to include numbers in the centre of the bars
#ax.bar_label(ax.containers[0], label_type='center')  # values for the average age bars
plt.title('Average age of passengers by gender\nusing barplot()')
plt.xlabel('Class')
plt.ylabel('Average Age')
plt.show()


# Question 5b)
# ------------
fg = sns.catplot(data=df_titanic, x='sex', y='age', kind='bar', ci=None)
# iterate through axes (subplots)
for ax in fg.axes.ravel():
    # iterate through containers (groups)
    for container in ax.containers:
        # include numbers in the centre of the bars
        ax.bar_label(container, label_type='center')
# Note: since there is no value set for kwarg col, there is no need for the outer loop
# (to iterate through subplots), and since there is no value set for kwarg hue,
# there is no need for the inner loop (to iterate through groups within each subplot).
# We can therefore replace the above nested loop with the following statement
# to include numbers in the centre of the bars
#fg.ax.bar_label(ax.containers[0], label_type='center')  # values for the average age bars
plt.title('Average age of passengers by gender\nusing catplot()')
plt.tight_layout()
plt.show() 



# Question 6
# ----------
'''
Using the 'titanic' Seaborn built-in dataset, illustrate the
average age per gender split by class of the titanic passengers
a) using the barplot() function
b) using the catplot() function
Include the numbers at the centre of bars and ensure the legend is shown
in the top right corner.
'''
# Question 6a)
# ------------
ax = sns.barplot(data=df_titanic, x="sex", y="age", hue='class', ci=None)
# include numbers in the centre of the bars
for container in ax.containers:
    # include numbers in the centre of the bars
    ax.bar_label(container, label_type='center')
# Note: since there is no value set for kwarg col, there is no need for the outer loop
# (to iterate through subplots), but since there is a value set for kwarg hue,
# we need for the inner loop (to iterate through groups - here classes, within each subplot).
# We could therefore replace the above loop with the following statements:
'''
ax.bar_label(ax.containers[0], label_type='center')  # values for the First class bars
ax.bar_label(ax.containers[1], label_type='center')  # values for the Second class bars
ax.bar_label(ax.containers[2], label_type='center')  # values for the Third class bars
'''
plt.title('Average age of passengers by gender split by class\nusing barplot()')
plt.xlabel('Class')
plt.ylabel('Average Age')
plt.show()


# Question 6b)
# ------------
fg = sns.catplot(data=df_titanic, x='sex', y='age', hue='class', kind='bar', ci=None, legend=False)
# iterate through axes (subplots)
for container in ax.containers:
    # include numbers in the centre of the bars
    fg.ax.bar_label(container, label_type='center')
# OR
'''
fg.ax.bar_label(ax.containers[0], label_type='center')  # values for the First class bars
fg.ax.bar_label(ax.containers[1], label_type='center')  # values for the Second class bars
fg.ax.bar_label(ax.containers[2], label_type='center')  # values for the Third class bars
'''
plt.title('Average age of passengers by gender split by class\nusing catplot()')
plt.legend(title='class:', loc="upper right")
plt.tight_layout()
plt.show() 



# Question 7
# ----------
'''
Using the 'titanic' Seaborn built-in dataset, illustrate
a) the number of passengers per class split by the type of person (man, woman, child)
   Use the 'ocean' colour palette and display values on top of the bars in purple colour.
b) the survival rate of passengers per class split by type of person.
   Use the 'inferno' colour palette and display values in the centre of the bars in white colour.
'''
# Question 7a)
# ------------
# create the plot using the 'ocean' palette
ax = sns.countplot(data=df_titanic, x='class', hue='who', palette='ocean')
# for multi-group bar plots (with 'hue'), iterate the multiple bar containers:
for container in ax.containers:
    # include numbers on top of the bars in purple colour
    ax.bar_label(container, label_type='edge', color='purple')
plt.title("Number of passengers per class split by type of person")
plt.show()


# Question 7b)
# ------------
# create the plot using the 'inferno' palette
ax = sns.barplot(data=df_titanic, x='who', y='survived', hue='class', palette='inferno', ci=None)
# iterate through containers
for container in ax.containers:
    # include numbers in the centre of the bars in white colour
    ax.bar_label(container, fmt='%.3f', label_type='center', color='white')
plt.title("Survival rate for type of person split by class")
plt.show()



# Question 8
# ----------
"""
Using the 'titanic' Seaborn built-in dataset, illustrate the
number of passengers by class split by each age group,
for each facet of survival, following the sinking of the titanic
a) creating a new data frame using queries, consisting of the following columns:
   class, age_range, survived and a column listing the number of passengers for
   each (class, age_range, survived) combination
b) creating and populating a new column within the existing data frame
   step 1: define a function that will populate the new column 'age_range'
   step 2: create a new column in the titanic data frame  and populate it
   passing the custom-made set_age_range() function to the apply() method
Categorise the age using the following categories:
<18
18-25
26-34
35-44
45-54
55-64
65+
Include numbers of top of the bars.
"""
# Note: this question poses two problems:
# 1) we need to work out the age range for each age in df_titanic
# 2) we need to figure out what plotting function to use, as not all will be suitable
# Solutions to each problem:
# 1) There are two ways of working out the age range for each age:
#    a) creating a new data frame using queries, 'pedestrian way'. The new data frame will
#       consist of just the columns that we need: class, age_range, survived and a column
#       listing the number of passengers for each (class, age_range, survived) combination.
#    b) creating and populating a new column within the existing data frame to show the age
#       range for each age in df_titanic - using the apply() Pandas method and passing to it
#       a custom function that determines the age range for an age passed to it as parameter
# 2) Once we work out the number of passengers in each age group, we need to fix
#    the class, age_range and survived. This will result in a unique value for each
#    (class, age_range, survived) combination. Using countplot (or catplot with kind='count')
#    would just count these values, hence returning value 1 for each (class, age_range, survived)
#    combination, ruling it out as an option. barplot() on the other hand would calculate the average
#    value for each (class, age_range, survived) combination, but we need the total number
#    of survived passengers for each (class, age_range) combination, and the total number
#    of non-survived passengers for each (class, age_range) combination, ruling out
#    barplot() as well. The only way to produce this plot is to use catplot() with kind='bar'
#    and by setting col kwarg to 'survived', resulting in two subplots, the first showing the number 
#    of survived passengers for each (class, age_range) combination and the second showing the number 
#    of non-survived passengers for each (class, age_range) combination.
#    Although kind='bar' calculates the mean value, within each subplot it efectively displays
#    the values of p_count (the new column storing the number of passengers within each age range),
#    as values in (class, age_range) are fixed. Within each subplot (one for survivors, the other for
#    non-survivors), it will add up values for each different (class, age_range) combination - which are
#    unique, and therefore dividing each number in column p_count by 1).

# Question 8a) (creating a new data frame using queries, 'pedestrian way')
# -----------
# create data series, storing the total number of survivors
# calculate the number of survived passengers from each age group by class
# (note that the variable 'class' cannot be used as it is a Python keyword)
# calculating values for every age group of the survived passengers from the 1st class
survived_1st_unknown = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==1 and age.isnull()').count()
survived_1st_lt18 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==1 and age<18').count()
survived_1st_18to25 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==1 and age>=18 and age<=25').count()
survived_1st_26to34 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==1 and age>=26 and age<=34').count()
survived_1st_35to44 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==1 and age>=35 and age<=44').count()
survived_1st_45to54 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==1 and age>=45 and age<=54').count()
survived_1st_55to64 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==1 and age>=55 and age<=64').count()
survived_1st_gte65 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==1 and age>=65').count()
print('survived_1st_unknown', survived_1st_unknown[0])
print('survived_1st_lt18', survived_1st_lt18[0])
print('survived_1st_18to25', survived_1st_18to25[0])
print('survived_1st_26to34', survived_1st_26to34[0])
print('survived_1st_35to44', survived_1st_35to44[0])
print('survived_1st_45to54', survived_1st_45to54[0])
print('survived_1st_55to64', survived_1st_55to64[0])
print('survived_1st_gte65', survived_1st_gte65[0])
# calculating values for every age group of the survived passengers from the 2nd class
survived_2nd_unknown = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==2 and age.isnull()').count()
survived_2nd_lt18 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==2 and age<18').count()
survived_2nd_18to25 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==2 and age>=18 and age<=25').count()
survived_2nd_26to34 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==2 and age>=26 and age<=34').count()
survived_2nd_35to44 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==2 and age>=35 and age<=44').count()
survived_2nd_45to54 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==2 and age>=45 and age<=54').count()
survived_2nd_55to64 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==2 and age>=55 and age<=64').count()
survived_2nd_gte65 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==2 and age>=65').count()
print('survived_2nd_unknown', survived_2nd_unknown[0])
print('survived_2nd_lt18', survived_2nd_lt18[0])
print('survived_2nd_18to25', survived_2nd_18to25[0])
print('survived_2nd_26to34', survived_2nd_26to34[0])
print('survived_2nd_35to44', survived_2nd_35to44[0])
print('survived_2nd_45to54', survived_2nd_45to54[0])
print('survived_2nd_55to64', survived_2nd_55to64[0])
print('survived_2nd_gte65', survived_2nd_gte65[0])
# calculating values for every age group of the survived passengers from the 3rd class
survived_3rd_unknown = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==3 and age.isnull()').count()
survived_3rd_lt18 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==3 and age<18').count()
survived_3rd_18to25 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==3 and age>=18 and age<=25').count()
survived_3rd_26to34 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==3 and age>=26 and age<=34').count()
survived_3rd_35to44 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==3 and age>=35 and age<=44').count()
survived_3rd_45to54 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==3 and age>=45 and age<=54').count()
survived_3rd_55to64 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==3 and age>=55 and age<=64').count()
survived_3rd_gte65 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==3 and age>=65').count()
print('survived_3rd_unknown', survived_3rd_unknown[0])
print('survived_3rd_lt18', survived_3rd_lt18[0])
print('survived_3rd_18to25', survived_3rd_18to25[0])
print('survived_3rd_26to34', survived_3rd_26to34[0])
print('survived_3rd_35to44', survived_3rd_35to44[0])
print('survived_3rd_45to54', survived_3rd_45to54[0])
print('survived_3rd_55to64', survived_3rd_55to64[0])
print('survived_3rd_gte65', survived_3rd_gte65[0])

# calculating values for every age group of the non-survived passengers from the 1st class
not_survived_1st_unknown = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==1 and age.isnull()').count()
not_survived_1st_lt18 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==1 and age<18').count()
not_survived_1st_18to25 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==1 and age>=18 and age<26').count()
not_survived_1st_26to34 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==1 and age>=26 and age<35').count()
not_survived_1st_35to44 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==1 and age>=35 and age<45').count()
not_survived_1st_45to54 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==1 and age>=45 and age<55').count()
not_survived_1st_55to64 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==1 and age>=55 and age<65').count()
not_survived_1st_gte65 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==1 and age>=65').count()
print('not_survived_1st_unknown', not_survived_1st_unknown[0])
print('not_survived_1st_lt18', not_survived_1st_lt18[0])
print('not_survived_1st_18to25', not_survived_1st_18to25[0])
print('not_survived_1st_26to34', not_survived_1st_26to34[0])
print('not_survived_1st_35to44', not_survived_1st_35to44[0])
print('not_survived_1st_45to54', not_survived_1st_45to54[0])
print('not_survived_1st_55to64', not_survived_1st_55to64[0])
print('not_survived_1st_gte65', not_survived_1st_gte65[0])
# calculating values for every age group of the non-survived passengers from the 2nd class
not_survived_2nd_unknown = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==2 and age.isnull()').count()
not_survived_2nd_lt18 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==2 and age<18').count()
not_survived_2nd_18to25 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==2 and age>=18 and age<26').count()
not_survived_2nd_26to34 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==2 and age>=26 and age<35').count()
not_survived_2nd_35to44 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==2 and age>=35 and age<45').count()
not_survived_2nd_45to54 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==2 and age>=45 and age<55').count()
not_survived_2nd_55to64 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==2 and age>=55 and age<65').count()
not_survived_2nd_gte65 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==2 and age>=65').count()
print('not_survived_2nd_unknown', not_survived_2nd_unknown[0])
print('not_survived_2nd_lt18', not_survived_2nd_lt18[0])
print('not_survived_2nd_18to25', not_survived_2nd_18to25[0])
print('not_survived_2nd_26to34', not_survived_2nd_26to34[0])
print('not_survived_2nd_35to44', not_survived_2nd_35to44[0])
print('not_survived_2nd_45to54', not_survived_2nd_45to54[0])
print('not_survived_2nd_55to64', not_survived_2nd_55to64[0])
print('not_survived_2nd_gte65', not_survived_2nd_gte65[0])
# calculating values for every age group of the non-survived passengers from the 3rd class
not_survived_3rd_unknown = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==3 and age.isnull()').count()
not_survived_3rd_lt18 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==3 and age<18').count()
not_survived_3rd_18to25 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==3 and age>=18 and age<26').count()
not_survived_3rd_26to34 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==3 and age>=26 and age<35').count()
not_survived_3rd_35to44 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==3 and age>=35 and age<45').count()
not_survived_3rd_45to54 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==3 and age>=45 and age<55').count()
not_survived_3rd_55to64 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==3 and age>=55 and age<65').count()
not_survived_3rd_gte65 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==3 and age>=65').count()
print('not_survived_3rd_unknown', not_survived_3rd_unknown[0])
print('not_survived_3rd_lt18', not_survived_3rd_lt18[0])
print('not_survived_3rd_18to25', not_survived_3rd_18to25[0])
print('not_survived_3rd_26to34', not_survived_3rd_26to34[0])
print('not_survived_3rd_35to44', not_survived_3rd_35to44[0])
print('not_survived_3rd_45to54', not_survived_3rd_45to54[0])
print('not_survived_3rd_55to64', not_survived_3rd_55to64[0])
print('not_survived_3rd_gte65', not_survived_3rd_gte65[0])

# create the data frame with these calculated values
df_totals = pd.DataFrame({
   'p_survived': [1, 1, 1, 1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1, 1, 1, 1,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0],
   'p_class': ['First', 'First', 'First', 'First', 'First', 'First', 'First', 'First',
               'Second', 'Second', 'Second', 'Second', 'Second', 'Second', 'Second', 'Second',
               'Third', 'Third', 'Third', 'Third', 'Third', 'Third', 'Third', 'Third',
               'First', 'First', 'First', 'First', 'First', 'First', 'First', 'First',
               'Second', 'Second', 'Second', 'Second', 'Second', 'Second', 'Second', 'Second',
               'Third', 'Third', 'Third', 'Third', 'Third', 'Third', 'Third', 'Third'],
   'p_age_range': ['unknown', '<18', '18-25', '26-34', '35-44', '45-54', '55-64', '>=65',
                   'unknown', '<18', '18-25', '26-34', '35-44', '45-54', '55-64', '>=65',
                   'unknown', '<18', '18-25', '26-34', '35-44', '45-54', '55-64', '>=65',
                   'unknown', '<18', '18-25', '26-34', '35-44', '45-54', '55-64', '>=65',
                   'unknown', '<18', '18-25', '26-34', '35-44', '45-54', '55-64', '>=65',
                   'unknown', '<18', '18-25', '26-34', '35-44', '45-54', '55-64', '>=65'],
   'p_count': [survived_1st_unknown[0], survived_1st_lt18[0], survived_1st_18to25[0], survived_1st_26to34[0], 
               survived_1st_35to44[0], survived_1st_45to54[0], survived_1st_55to64[0], survived_1st_gte65[0],
               survived_2nd_unknown[0], survived_2nd_lt18[0], survived_2nd_18to25[0], survived_2nd_26to34[0], 
               survived_2nd_35to44[0], survived_2nd_45to54[0], survived_2nd_55to64[0], survived_2nd_gte65[0],
               survived_3rd_unknown[0], survived_3rd_lt18[0], survived_3rd_18to25[0], survived_3rd_26to34[0], 
               survived_3rd_35to44[0], survived_3rd_45to54[0], survived_3rd_55to64[0], survived_3rd_gte65[0],
               not_survived_1st_unknown[0], not_survived_1st_lt18[0], not_survived_1st_18to25[0], not_survived_1st_26to34[0], 
               not_survived_1st_35to44[0], not_survived_1st_45to54[0], not_survived_1st_55to64[0], not_survived_1st_gte65[0],
               not_survived_2nd_unknown[0], not_survived_2nd_lt18[0], not_survived_2nd_18to25[0], not_survived_2nd_26to34[0], 
               not_survived_2nd_35to44[0], not_survived_2nd_45to54[0], not_survived_2nd_55to64[0], not_survived_2nd_gte65[0],             
               not_survived_3rd_unknown[0], not_survived_3rd_lt18[0], not_survived_3rd_18to25[0], not_survived_3rd_26to34[0], 
               not_survived_3rd_35to44[0], not_survived_3rd_45to54[0], not_survived_3rd_55to64[0], not_survived_3rd_gte65[0]             
              ]
})
print(df_totals)
# construct the plot
# store the FaceGrid object returned by figure-level function (e.g. catplot)
fg = sns.catplot(data=df_totals, x='p_class', y='p_count', hue='p_age_range', col='p_survived', kind='bar')
# Note: after fixing the p_class, p_age_range and p_survived, the values on all rows are unique
# (values in p_count are not being considered as the mean is calculated for these values).
# Therefore, although barplot() calculates the mean value, it efectively displays the values of p_count
# as values in all other columns are fixed (it divides each number in column p_count by 1).
# Another way of achieveing the same outcome is to include the estimator kwarg with the value np.sum:
#fg = sns.catplot(data=df_totals, x='p_class', y='p_count', hue='p_age_range', col='p_survived', kind='bar', estimator=np.sum)
# iterate through axes (subplots), identified by col kwarg
for ax in fg.axes.ravel():
    # iterate through containers (groups) of each subplot, identified by hue kwarg
    for container in ax.containers:
        # include numbers on top of the bars
        ax.bar_label(container, label_type='edge')
plt.suptitle("Number of passengers by class split by age group, for each facet of survival\nusing catplot() with kind='bar' and col='survived'\n(Version 1)")
plt.tight_layout()
plt.show() 


# Question 8b) (creating and populating a new column within the existing data frame)
# -----------
# step 1: define a function that will populate the new column 'age_range'
def set_age_range(age):
    if age >= 65:
        return '65+'
    elif age >=55:
        return '55-64'
    elif age >=45:
        return '45-54'
    elif age >= 35:
        return '35-44'
    elif age >= 26:
        return '26-34'
    elif age >= 18:
        return '18-25'
    elif age >= 0:
        return '0-18'
    else:
        # NaN value
        return 'unknown'

# step 2: create a new column in the df_titanic data frame
# and populate it passing the custom made set_age_range() function
# to the apply() method. Then use the catplot() function with
# kind='count' to count the number of rows for each (class, age_range)
# combination with col kwarg set to 'survived' to create two plots
# (one for survived passengers and another for passengers who did not survive).
df_titanic['age_range'] = df_titanic['age'].apply(set_age_range)
# create a dataframe with age_range values sorted in custom order:
# 'unknown','0-18','18-25','26-34','35-44','45-54','55-64','65+'
df_titanic.age_range = pd.Categorical(df_titanic.age_range, categories=['unknown','0-18','18-25','26-34','35-44','45-54','55-64','65+'])
# readjust the index to a new sequential index that will correspond to
# age_range sex values sorted according to the new given order
df_titanic = df_titanic.reset_index()
# construct the plot
# store the FaceGrid object returned by figure-level function (e.g. catplot)
fg = sns.catplot(data=df_titanic, x='pclass', hue='age_range', col='survived', kind='count')
#fg = sns.catplot(data=df_titanic, x='pclass', hue='age_range', col='survived', kind='count', estimator=np.sum)
# iterate through axes (subplots), identified by col kwarg
for ax in fg.axes.ravel():
    # iterate through containers (groups) of each subplot, identified by hue kwarg
    for container in ax.containers:
        # include numbers on top of the bars
        ax.bar_label(container, label_type='edge')
plt.suptitle("Number of passengers by class split by age group, for each facet of survival\nusing catplot() with kind='count' and col='survived'\n(Version 2)")
plt.tight_layout()
plt.show() 



# Question 9
# ----------
'''
Using the new data frame created in question 8a, illustrate the average
number between survived and deaths per class across all age ranges,
including the numbers on top of each bar.
'''
# The category following 'For each' (class), goes on the x-axis and is the only one that is fixed.
# The number of rows with different values for each class is therefore 2 x 8
# (2 values for survived; 8 values for the age ranges).
# Therefore, barplot() here calculates the mean value by adding up values for the same class
# for survived=1 and for survived=0, and dividing the obtained total by 16.
# e.g. survived for first class = 136; deaths for first class = 80;
# the mean value between survived and deaths in 1st class across all age ranges: (136 + 80) / 16 = 13.5
# the mean value between survived and deaths in 2nd class across all age ranges: (87 + 97) / 16 = 11.5
# the mean value between survived and deaths in 3rd class across all age ranges: (119 + 372) / 16 = 30.6875
ax = sns.barplot(data=df_totals, x='p_class', y='p_count', ci=None)
# include numbers at the top of the bars
for container in ax.containers:
    # include numbers on top of the bars
    ax.bar_label(container, label_type='edge')
'''
# OR
ax.bar_label(ax.containers[0], label_type='edge')  # values for the bars of variable p_class
'''
plt.title("Average number between survivors & deaths per class")
plt.tight_layout()
plt.show() 



# Question 10
# -----------
'''
Using the new data frame created in question 8a, illustrate the average
number between survived and non-survived passengers per class,
split by age range, including the numbers on top of each bar.
Reflect on the data in the data frame created in task 8a to figure out
how to resolve the task.
'''
# The category following 'For each' (class), goes on the x-axis.
# Because we need to find the average number for each range as well,
# in this case 2 variables are fixed: class and age_range. This means that the
# number of rows with different values for each p_class and p_age_range is 2:
# one for survived (1), the other for died (0). 
# The the new df_totals data frame includes a column: p_count, containing the
# number of survivals for each (class, age_range) pair. Applying barplot() to
# such dataset causes calculating the average number of survivals for each
# (class, age_range) pair: for example, the value of p_count for the number of people
# with unknown age of the first class that survived is 14; the value of p_count for
# the number of people of unknown age of the first class that died is 16.
# Therefore, barplot() here calculates the mean value by adding up values for the same
# age range and class for survived=1 and for survived=0, and dividing the obtained
# total by 2. For example:
# the mean value between unknown age of survived and dead for second class is (14 + 16) / 2 = 15
# the mean value between unknown age of survived and dead for second class is (4 + 7) / 2 = 5.5
# the mean value between unknown age of survived and dead for third class is (34 + 102) / 2 = 68
# and so on...
# Version 1 - using catplot() with kind='bar'
fg = sns.catplot(data=df_totals, x='p_class', y='p_count', hue='p_age_range', kind='bar', height=6, aspect=1.8, ci=None)
# iterate through containers (groups) of each subplot, identified by hue kwarg
for container in fg.ax.containers:
    # include numbers on top of the bars
    fg.ax.bar_label(container, fmt='%.2f', label_type='edge')
plt.title("Average between the number of survived and non-survived\npassengers per class split by age range\nusing catplot() with kind='bar'")
plt.tight_layout()
plt.show()
# Version 2 - using barplot()
# change the size of the plot
# (style=None removes the darkgrid, as style='darkgrid' by default; width=14, height=7)
sns.set(style=None, rc={"figure.figsize":(14, 7)})
ax = sns.barplot(data=df_totals, x='p_class', y='p_count', hue='p_age_range', ci=None)
# iterate through containers (groups) of each subplot, identified by hue kwarg
for container in ax.containers:
    # include numbers on top of the bars
    ax.bar_label(container,label_type='edge')
'''
# OR (since there are 8 values of the categorical variable p_age_range assigned to the 'hue' kwarg)
ax.bar_label(ax.containers[0], label_type='edge')  # values for 'unknown' bars
ax.bar_label(ax.containers[1], label_type='edge')  # values for '<18' bars
ax.bar_label(ax.containers[2], label_type='edge')  # values for '18-25' bars
ax.bar_label(ax.containers[3], label_type='edge')  # values for '26-34' bars
ax.bar_label(ax.containers[4], label_type='edge')  # values for '35-44' bars
ax.bar_label(ax.containers[5], label_type='edge')  # values for '45-54' bars
ax.bar_label(ax.containers[6], label_type='edge')  # values for '55-64' bars
ax.bar_label(ax.containers[7], label_type='edge')  # values for '65+' bars
'''
plt.title("Average between the number of survived and non-survived\npassengers per class split by age range\nusing barplot()")
plt.tight_layout()
plt.show() 



# Question 11
# -----------
'''
Using the expanded titanic data frame created in question 8b, illustrate the passengers'
survival rate per class, split by age range, including the numbers on top of each bar.
Reflect on the data in the expanded titanic data frame to figure out how
to resolve the task.
'''
# In this case the same 2 variables are fixed: class and age_range.
# The extended titanic dataset includes an additional column: age_range, containing the
# age range each person's age falls within. Applying barplot() to such dataset causes
# calculating the average number of survivals for each (class, age_range) pair: for example
# in case of unknown age, the number of survived passengers with unknown age of for first class
# is 14; the number of non-survived passengers with unknown age of for first class is 16.
# barplot() adds all survived values up and devides them with the number of observations:
# (14 x 1 + 16 x 0) / (14 + 16) = 14/30 = 0.47
# the survival rate for unknown age from second class is (4 x 1 + 7 x 0) / (4 + 7) = 0.36
# the survival rate for unknown age from third class is (34 x 1 + 102 x 0) / (34 + 102) = 0.25
# and so on...
# Version 1 - using catplot() with kind='bar'
fg = sns.catplot(data=df_titanic, x='class', y='survived', hue='age_range', kind='bar', height=6, aspect=1.8, legend=False, ci=None)
# iterate through containers (groups) of each subplot, identified by hue kwarg
for container in fg.ax.containers:
    # include numbers on top of the bars
    fg.ax.bar_label(container, fmt='%.2f', label_type='edge')
plt.title("Survival rate per class split by age range\nusing catplot() with kind='bar'")
plt.legend(title='age_range', loc='upper right')
plt.tight_layout()
plt.show()
# Version 2 - using barplot()
# change the size of the plot
# (style=None removes the darkgrid, as style='darkgrid' by default; width=14, height=7)
sns.set(style=None, rc={"figure.figsize":(14, 7)})
ax = sns.barplot(data=df_titanic, x='class', y='survived', hue='age_range', ci=None)
# iterate through containers (groups) of each subplot, identified by hue kwarg
for container in ax.containers:
    # include numbers on top of the bars
    ax.bar_label(container, fmt='%.2f', label_type='edge')
plt.title("Survival rate per class split by age range\nsplit by age range\nusing barplot()")
plt.show()



# Question 12
# -----------
'''
Using the 'titanic' Seaborn built-in dataset, create a scatter plot to show the dependency:
a) between 'age' and 'fare' variables
b) between 'age' and 'fare' variables against the data variable 'sex'
c) between 'age' and 'fare' variables against the data variable 'who' (type of person)
   representing each type of person with a different size of data points.
d) same as in task 10c) but show each size with a different colour
e) same as in task 10c) but instead of the size, use a different shape
   for data points of each type of person.
f) same as in task 10c) but create a multiple plot consisting of two subplots,
   each showing values for each facet of the genders: male, female
'''
# Question 12a)
# ------------
# create the scatter plot (3 ways):
sns.scatterplot(data=df_titanic, x='age', y='fare')
plt.title("Dependency between age and fare\nusing scatterplot()")
plt.show()
# OR
sns.relplot(data=df_titanic, x='age', y='fare', kind='scatter')
plt.title("Dependency between age and fare\nusing relplot() with kind='scatter'")
plt.tight_layout()
plt.show()
# OR (since kind='scatter' is the default value for the relplot() kind kwarg)
sns.relplot(data=df_titanic, x='age', y='fare')
plt.title("Dependency between age and fare\nusing relplot() without kind='scatter'")
plt.tight_layout()
plt.show()


# Question 12b)
# ------------
# create the scatter plot (3 ways):
sns.scatterplot(data=df_titanic, x='age', y='fare', hue='sex')
plt.title("Dependency between age and fare split by gender\nusing scatterplot()")
plt.show()
# OR
sns.relplot(data=df_titanic, x='age', y='fare', hue='sex', kind='scatter')
plt.title("Dependency between age and fare split by gender\nusing relplot() with kind='scatter'")
plt.tight_layout()
plt.show()
# OR (since kind='scatter' is the default value for the relplot() kind kwarg)
sns.relplot(data=df_titanic, x='age', y='fare', hue='sex')
plt.title("Dependency between age and fare split by gender\nusing relplot() without kind='scatter'")
plt.tight_layout()
plt.show()


# Question 12c)
# ------------
# create the scatter plot
sns.scatterplot(data=df_titanic, x='age', y='fare', size='who')
plt.title("Dependency between age and fare split by type of person\nusing scatterplot() with size='who'")
plt.show()
# OR
sns.relplot(data=df_titanic, x='age', y='fare', size='who', kind='scatter')
plt.title("Dependency between age and fare split by type of person\nusing relplot() with kind='scatter' and size='who'")
plt.tight_layout()
plt.show()
# OR (since kind='scatter' is the default value for the relplot() kind kwarg)
sns.relplot(data=df_titanic, x='age', y='fare', size='who')
plt.title("Dependency between age and fare split by type of person\nusing relplot() without kind='scatter' & with size='who'")
plt.tight_layout()
plt.show()


# Question 12d)
# ------------
# create the scatter plot
sns.scatterplot(data=df_titanic, x='age', y='fare', hue='who', size='who')
plt.title("Dependency between age and fare split by type of person\nusing scatterplot() with size='who'")
plt.show()
# OR
sns.relplot(data=df_titanic, x='age', y='fare', hue='who', size='who', kind='scatter')
plt.title("Dependency between age and fare split by type of person\nusing relplot() with kind='scatter' & size='who'")
plt.tight_layout()
plt.show()
# OR (since kind='scatter' is the default value for the relplot() kind kwarg)
sns.relplot(data=df_titanic, x='age', y='fare', hue='who', size='who', )
plt.title("Dependency between age and fare split by type of person\nusing relplot() without kind='scatter' & with size='who'")
plt.tight_layout()
plt.show()


# Question 12e)
# ------------
# create the scatter plot
sns.scatterplot(data=df_titanic, x='age', y='fare', hue='who', style='who')
plt.title("Dependency between age and fare split by type of person\nusing scatterplot() with style='who'")
plt.show()
# OR
sns.relplot(data=df_titanic, x='age', y='fare', hue='who', style='who', kind='scatter')
plt.title("Dependency between age and fare split by type of person\nusing relplot() with kind='scatter' & style='who'")
plt.tight_layout()
plt.show()
# OR (since kind='scatter' is the default value for the relplot() kind kwarg)
sns.relplot(data=df_titanic, x='age', y='fare', hue='who', style='who', )
plt.title("Dependency between age and fare split by type of person\nusing relplot() without kind='scatter' & with style='who'")
plt.tight_layout()
plt.show()


# Question 12f)
# ------------
# create the scatter plot
sns.relplot(data=df_titanic, x='age', y='fare', hue='who', col='sex', kind='scatter')
plt.suptitle("Dependency between age and fare split by type of passenger for each facet of gender\nusing relplot() with kind='scatter'")
plt.tight_layout()
plt.show()
# OR (since kind='scatter' is the default value for the relplot() kind kwarg)
sns.relplot(data=df_titanic, x='age', y='fare', hue='who', col='sex')
plt.suptitle("Dependency between age and fare split by type of person\nusing relplot() without kind='scatter' & with style='who'")
plt.tight_layout()
plt.show()



# Question 13)
# ------------
'''
Using the 'titanic' Seaborn built-in dataset, create a joint plot
to combine a scatterplot(), showing the bivariate distribution
of passengers' age and fare, and two histplot(), showing marginal
distributions of ages on top and of fares on the right.
Add a linear regression fit to scatter plot (using regplot()) and
univariate KDE curves to hist plots. Drop missing values from the
data before plotting.
'''
# create the joint plot
sns.jointplot(data=df_titanic, x='age', y='fare', kind='reg', dropna = True)
plt.suptitle("Bivariate distribution of passengers' age and fare\nusing jointplot()")
plt.tight_layout()
plt.show()



# Question 14)
# ------------
'''
Using the 'titanic' Seaborn built-in dataset, change the scatter plot created
in task 10a by including the rugplot() to add ticks ('rugs') along the x and
y axes. The rugs on the bottom should illustrate the distribution of passengers'
age alone. The rugs on the left should illustrate the distribution of
passengers' fare alone.
'''
sns.relplot(data=df_titanic, x='age', y='fare')
sns.rugplot(data=df_titanic, x='age', y='fare')
plt.title("Dependency between age and fare\nusing relplot() and rugplot()")
plt.tight_layout()
plt.show()
