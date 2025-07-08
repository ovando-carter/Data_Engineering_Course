#######################
# Module 4B - Seaborn #
#######################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# RELATIONAL PLOTS
# =================
# slide 59

# get the data set from csv file 
data_set = pd.read_csv("employees.csv")

# create a scatter plot
# plot the dependency between 'age_ranges' and 'no_employees'
# data variables against the data variable 'gender' of the dataset
sns.scatterplot(data=data_set, x='age_ranges', y='no_employees', hue='gender')

# save the plot into a file
plt.savefig('scatter_plot_axes_level.png')

# The same plot can be drawn using the figure-level function relplot() and setting its
# kind kwarg to ‘scatter’:
sns.relplot(data=data_set, x='age_ranges', y='no_employees', hue='gender', kind='scatter')
plt.savefig('scatter_plot_figure_level.png')

# slide 65 (preferred way to the one demonstrated on slide 63)
sns.relplot(data=data_set, x='age_ranges', y='no_employees', hue='gender',  col='gender', kind='scatter')
plt.show()
#plt.savefig('multiple_scatter_plot_figure_level.png')


