#######################
# Module 4B - Seaborn #
#######################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# JOINT PLOTS
# ===========

# slides 66-68 
# The following script creates a joint plot to combine a scatterplot(),
# showing the bivariate distribution of petal’s width and length, and a
# histplot(), showing marginal distributions, using the ‘iris’ seaborn built-in data set
# load the built-in 'iris' data set into a data frame
df_iris = sns.load_dataset("iris")
print(df_iris)

# construct the iris plot
sns.jointplot(data=df_iris, x='petal_width', y='petal_length')

# plot acording to plant species, and distribution
sns.jointplot(data=df_iris, x="sepal_length", y="petal_length", hue="species", palette="magma",)


# save the plot into a file
plt.savefig('joint_plot.png')


# slide 69
# remember that the default value for kind kwarg of relplot() is 'scatter'
sns.relplot(data=df_iris, x='petal_width', y='petal_length')
sns.rugplot(data=df_iris, x='petal_width', y='petal_length')
# save the plot into a file
#plt.savefig('relplot_ with_rugplot.png')
plt.show()
