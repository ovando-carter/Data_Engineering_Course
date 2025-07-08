#######################
# Module 4B - Seaborn #
#######################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn comes with a rich set of own data sets, to list them type
sns.get_dataset_names()

# CATEGORICAL PLOTS
# =================

# slides 19-21
# load the built-in 'iris' data set into a data frame
df_iris = sns.load_dataset("iris")

# To print all the column headers of a data frame (e.g. df_iris):
df_iris.columns

# construct the iris plot
sns.swarmplot(data=df_iris , x='species', y='petal_length')
plt.savefig('swarmplot.png')

# The same can be achieved through figure-level function catplot()
sns.catplot(data=df_iris , x='species', y='petal_length', kind='swarm')
plt.show()

# slide 22
# countplot() function can be used to show value counts for one or two categorical variables

# slide 24
# Show the number of passengers by gender (categorical variable 'sex')
# load the built-in 'titanic' data set into a data frame
df_titanic = sns.load_dataset("titanic")
# draw the plot and include the plot title (axes-level function)
sns.countplot(data=df_titanic, x="sex")
plt.title("Total number of passengers by gender")
plt.show()

# the same plot can be drawn using catplot() (figure-level) function:
sns.catplot(data=df_titanic, x='sex', kind='count')
plt.title("Total number of passengers by gender")
plt.tight_layout()
plt.show()

# slide 25
# countplot() applied to two categorical variables ('alive' & 'sex')
# Show the number of passengers by gender split by survival (categorical variables 'sex' and 'alive')
# using axes-level function countplot()
sns.countplot(data=df_titanic, x='alive', hue='sex')
plt.title("countplot() with 2 categorical variables")
plt.show()

# The same plot can be drawn using catplot() figure-level function:
sns.catplot(data=df_titanic, x='alive', hue='sex', kind='count', legend=False)
plt.legend(title="sex", loc="upper right")
plt.title("catplot() with 2 categorical variables")
plt.tight_layout()
plt.show()

# slide 26
# To group within three categorical variables, use the figure-level function catplot()
# Show the number of passengers by class (1st, 2nd, 3rd), split by passenger types (man, woman, child),
# for each facet (value) of survival (0, 1)
sns.catplot(data=df_titanic, x='class', hue='who', col='survived', kind='count')
plt.suptitle("catplot() with 3 categorical variables")

# display the plot
plt.tight_layout()
plt.show()

# slide 27
# The example below illustrates how catplot() can be used to draw subplots over multiple rows
# Example: Show the number of passengers by survival for each facet of deck.

# load the built-in 'titanic' data set into a data frame
df_titanic = sns.load_dataset("titanic")

# construct multiple plot in 4 columns showing the count of survivors by deck
sns.catplot(data=df_titanic, x='alive', col='deck', col_wrap=4, kind='count')

# display the plot
plt.tight_layout()
plt.show()

# slide 29
# To join multiple different axes-level plots into one figure use the subplots() matplotlib function

# Example: Show the number of passengers in relation to the
#  1) categorical variable 'alive'
#  2) categorical variable 'deck'
fig, ax = plt.subplots(1,2)
sns.countplot(data=df_titanic, x='alive', ax=ax[0])
sns.countplot(data=df_titanic, x='deck', ax=ax[1])
# suptitle() - supertitle, function is used to provide the overall title for the whole figure
plt.suptitle("countplot() - multiplot figure")
plt.show()

# slide 30 - barplot()
# barplot() function calculates a summary statistic for each category.
# By default, it calculates the mean.
# It is possible to change how sns.barplot summarizes the data by using the estimator parameter. 
# Note: with barplot() one of the x or y parameters must be set to a numeric variable
# (in order to work out the average value by default, or a different value according to the
# function set by the kwarg estimator); the other must be set to a categorical variable.
# The kwarg hue allows adding an additional categorical variable.

# slide 32
# barplot() with one categorical and one numerical variable -
# Plot the dependency between categorical variable ‘sex’ and numerical variable ‘survived’
# (the survival rate by gender)
# load the built-in 'titanic' data set into  a data frame
df_titanic = sns.load_dataset("titanic")
# construct the plot (axes-level function) - if you put ci=none then it will remove the error bars
sns.barplot(data=df_titanic, x='sex', y='survived')
# display the plot
plt.show()

# slide 33
# (using the equivalent figure-level function)
# The same plot can be drawn using catplot() function, setting the kind kwarg to 'bar': 
# construct the plot
sns.catplot(data=df_titanic, x='sex', y='survived', kind='bar')

# display the plot
plt.tight_layout()
plt.show()

# slide 34 - barplot() with two categorical and one numerical variable
# Plot the dependency between categorical variable ‘sex’ and numerical variable ‘survived’
# against the categorical variable ‘class’(the survival rate by gender split by class)
sns.barplot(data=df_titanic, x='sex', y='survived', hue='class', order=['female', 'male'], ci=None)
# display the plot
plt.title("Survival rate by gender grouped by class")
plt.show()

# including (numerical) values to the bars
# ----------------------------------------

# slide 37
# For single-group axes-level plots (without 'hue'), pass the single bar container
# to the bar_label() method
# Example: show the rate between male & female survors
# store the matplotlib Axes object returned by axes-level function (e.g. barplot)
ax = sns.barplot(data=df_titanic, x='sex', y='survived', ci=None)
# include numbers on top of the bars, formatted with 3 decimal places
ax.bar_label(ax.containers[0], fmt='%.3f', label_type='edge')
# or just
ax.bar_label(ax.containers[0], fmt='%.3f')
# since 'edge' is the default value for label_type kwarg
# include numbers in the centre of the bars 
ax.bar_label(ax.containers[0], fmt='%.3f', label_type='center')
# set the title and display the plot
plt.title("Survival rate by gender\n(single-group axes-level plot with numbers on bars)")
plt.show()

# slide 38
# For multi-group axes-level plots (with 'hue'), iterate through multiple bar containers:
# store the matplotlib Axes object returned by axes-level function (e.g. countplot)
ax = sns.countplot(data=df_titanic, x='alive', hue='sex')
# iterate through containers (groups), identified by hue kwarg
for container in ax.containers:
    # include numbers on top of the bars
    ax.bar_label(container, label_type='edge')
    # include numbers in the centre of the bars
    ax.bar_label(container, label_type='center')
# set the title, adjust and display the plot
plt.title("Total number of dead & alive passengers split by gender\n (multi-group axes-level plot with numbers on bars)")
plt.tight_layout()
plt.show() 

# slide 40
# For single-plot figure-level plots (without 'col'), iterate through containers of the plot
# store the FaceGrid object returned by figure-level function (e.g. catplot)
fg = sns.catplot(data=df_titanic, x='sex', y='survived', kind='bar', ci=None)

# store the matplotlib Axes subplot objects returned by FacetGrid.facet_axis()
# here axis are present in row 0 and column 0 (since there are no subplots)
ax = fg.facet_axis(0, 0)

# iterate through containers, identified by hue kwarg
for container in ax.containers:
    # include numbers on top of the bars
    ax.bar_label(container, fmt='%.3f', label_type='edge')
    # include numbers in the centre of the bars
    ax.bar_label(container, fmt='%.3f', label_type='center')

plt.title("Survival rate by gender\n(single-plot figure-level plot with numbers on bars)")
plt.tight_layout()
plt.show()

# slide 42
# For multi-plot figure-level plots (with 'col'), iterate through multiple axes (subplots)
# and for each subplot  iterate through its containers
# store the FaceGrid object returned by figure-level function (e.g. catplot)
fg = sns.catplot(data=df_titanic, x='class', hue='who', col='survived', kind='count', height=6, aspect=.8, ci=None)

# iterate through axes (subplots), identified by col kwarg
for ax in fg.axes.ravel():
    # within each subplot iterate through its containers, identified by hue kwarg
    for container in ax.containers:
        # include numbers on top of the bars
        ax.bar_label(container, label_type='edge')
        # include numbers in the centre of the bars
        ax.bar_label(container, label_type='center')
plt.suptitle("Number of passengers by class, split by passenger types (man, woman, child) for each facet of survival (0, 1)\n(multi-group multi-plot figure-level plot with numbers on bars)")
plt.tight_layout()
plt.show()

# from Notes section on slide 42:
# The above code runs for any single/multi group, single/multi-plot figure-level:
fg = sns.catplot(data=df_titanic, x='sex', y='survived', kind='bar', height=6, aspect=1.1, ci=None)
#fg = sns.catplot(data=df_titanic, x="class", hue="who", col="survived", kind="count", height=4, aspect=.7, ci=None)
# iterate through axes (subplots)
for ax in fg.axes.ravel():
    # iterate through containers
    for container in ax.containers:
        # include numbers on top of the bars
        ax.bar_label(container, fmt='%.3f', label_type='edge')
        # include numbers in the centre of the bars
        ax.bar_label(container, fmt='%.3f', label_type='center')
plt.suptitle("Number of dead & alive passenger by gender\n(single/multi-group single/multi-plot figure-level plot with numbers on bars)")
plt.tight_layout()
plt.show()

# slide 45
# axes-level plot created with barplot() 
sns.barplot(data=df_titanic, x='sex', y='survived', hue='class', ci=None)
plt.show()

# equivalent figure-level plot using catplot()
sns.catplot(data=df_titanic, x='sex', y='survived', hue='class', kind='bar', ci=None)
plt.show()

# slide 46
# the effect of despine() applied to the plot created with barplot() 
ax = sns.barplot(data=df_titanic, x='sex', y='survived', hue='class', ci=None)
for container in ax.containers:
    ax.bar_label(container, label_type='edge')
sns.despine()
plt.show()

# the effect of calling the tight_layout() function just before displaying the plot created with catplot() 
fg = sns.catplot(data=df_titanic, x='sex', y='survived', hue='class', kind='bar', ci=None)
for container in fg.ax.containers:
    fg.ax.bar_label(container, label_type='edge')
plt.tight_layout()
plt.show()

# from Notes section on slide 46: the final figure-level plot created with catplot()
fg = sns.catplot(data=df_titanic, x='sex', y='survived', hue='class', kind='bar', legend=False, ci=None)
for container in fg.ax.containers:
    fg.ax.bar_label(container, label_type='edge')
plt.legend(title='sex', loc="upper left")
plt.tight_layout()
plt.show()

# slides 47-49 - example of using Pandas query() function with barplot()
# Task: show the number of dead & alive passengers split by gender
# (categorical variables: 'alive' and 'sex') 
import pandas as pd
# calculate the number of alive female passengers
alive_f_count =  df_titanic[['sex', 'alive']].query('sex=="female" and alive=="yes"').count()
# calculate the number of alive male passengers
alive_m_count =  df_titanic[['sex', 'alive']].query('sex=="male" and alive=="yes"').count()
# calculate the number of dead female passengers
dead_f_count =  df_titanic[['sex', 'alive']].query('sex=="female" and alive=="no"').count()
# calculate the number of dead male passengers
dead_m_count =  df_titanic[['sex', 'alive']].query('sex=="male" and alive=="no"').count()

print("The number of alive female passengers:", alive_f_count[0])
print("The number of alive male passengers:", alive_m_count[0])
print("The number of dead female passengers:", dead_f_count[0])
print("The number of dead male passengers:", dead_m_count[0])

df_totals = pd.DataFrame({'gender': ['male', 'female', 'male', 'female'],
                          'alive': ['no', 'no', 'yes', 'yes'],
                          'count': [dead_m_count[0], dead_f_count[0], alive_m_count[0], alive_f_count[0]]
})

# Note: inverting the order of 'gender' values inverts the order of related bars:
# female bars will be listed before male bars
'''
df_totals = pd.DataFrame({'gender': ['female', 'male', 'female', 'male'],
                          'alive': ['no', 'no', 'yes', 'yes'],
                          'count': [dead_f_count[0], dead_m_count[0], alive_f_count[0], alive_m_count[0]]
})
'''
print(df_totals)

# draw the plot
ax = sns.barplot(data=df_totals, x='alive', y ='count', hue='gender')

# include numbers in the centre of the bars
ax.bar_label(ax.containers[0], label_type='center')  # values for 'male' bars
ax.bar_label(ax.containers[1], label_type='center')  # values for 'female' bars
plt.title("Total number of dead & alive passengers split by gender\n- using query()")
plt.tight_layout()
plt.show()

# the same plot can be produced by using groupby()
# slides 50-51 - example of using Pandas groupby() function with barplot()
# Show the number of dead & alive passengers by gender
# (categorical variables: 'alive' and 'sex') 
# calculate the number of alive/dead female/male passengers
df_totals = df_titanic.groupby(['sex','alive'])['survived'].count().reset_index()
print(df_totals)
# draw the plot
ax = sns.barplot(data=df_totals, x='alive', y ='survived', hue='sex')
# include numbers in the centre of the bars
ax.bar_label(ax.containers[0], label_type='center')  # values for 'female' bars
ax.bar_label(ax.containers[1], label_type='center')  # values for 'male' bars
plt.title("Total number of dead & alive passengers split by gender\n- using groupby()")
plt.tight_layout()
plt.show()

# slide 52: sorting column values in ascending/descending order 
df_totals = df_titanic.groupby(['sex','alive'])['survived'].count().reset_index().sort_values('sex', ascending=False)
print(df_totals)
# draw the plot
ax = sns.barplot(data=df_totals, x='alive', y ='survived', hue='sex')
# include numbers in the centre of the bars
ax.bar_label(ax.containers[0], label_type='center')  # values for 'male' bars
ax.bar_label(ax.containers[1], label_type='center')  # values for 'female' bars
plt.title("Total number of dead & alive passengers split by gender\n- using groupby() and sort_values()")
plt.tight_layout()
plt.show()

# slides 53-54: sorting column values in custom order
df_totals = df_titanic.groupby(['sex', 'alive'])['survived'].count().reset_index()
print(df_totals)
# compose the list with sex values sorted in the desired order
sorted_sex = ['male', 'female']
# change the order of the sex values according to the order given in the list
# supplied to the kwarg categories (Categorical function is used to convert/typecast
# integer or character column to categorical in Pandas Python)
df_totals.sex = pd.Categorical(df_totals.sex, categories=sorted_sex)
# readjust the index to a new sequential index that will correspond to the sex values
# sorted according to the  new given order (in the sorted_sex list)
df_totals = df_totals.groupby(['sex', 'alive'])['survived'].sum().reset_index()
print(df_totals)
# draw the plot
ax = sns.barplot(data=df_totals, x='alive', y ='survived', hue='sex')
# include numbers in the centre of the bars
ax.bar_label(ax.containers[0], label_type='center') # values for 'male' bars
ax.bar_label(ax.containers[1], label_type='center') # values for 'female' bars
plt.title("Total number of dead & alive passengers split by gender\n- using groupby() and custom sorting using Categorical()")
plt.tight_layout()
plt.show()

# slide 55: improved sorting column values in custom order
# running the Categorical function directly against the sex column
# of the df_titanic DataFrame
df_titanic.sex = pd.Categorical(df_titanic.sex, categories=['male', 'female'])
print(df_titanic)
# create a new DataFrame with calculated number of alive/dead female/male passengers
df_totals = df_titanic.groupby(['sex','alive'])['survived'].count().reset_index()
# draw the plot
print(df_totals)
ax = sns.barplot(data=df_totals, x='alive', y ='survived', hue='sex')
# include numbers in the centre of the bars
ax.bar_label(ax.containers[0], label_type='center')  # values for 'male' bars
ax.bar_label(ax.containers[1], label_type='center')  # values for 'female' bars
plt.title("Total number of dead & alive passengers by gender")
plt.tight_layout()
plt.show()







































