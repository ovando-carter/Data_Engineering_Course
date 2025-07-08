import matplotlib.pyplot as plt
import numpy as np

# ported from 9
from q9 import *


# Matplotlib Example: Grouped Bar Plot
no_grades = 4

# convert dataframe into array 
#select rows called london, leeds and glasgow .iloc[,7]

xG = summary_grades_2021_UK(fileName, Academy).loc[3].to_numpy()
glasgow = xG[2:6]

xLe = summary_grades_2021_UK(fileName, Academy).loc[6].to_numpy()
leeds = xLe[2:6]

xLo = summary_grades_2021_UK(fileName, Academy).loc[7].to_numpy()
london = xLo[2:6]


'''
london = np.array([235, 621, 823, 421])
leeds = np.array([435, 924, 532, 264])
glasgow = np.array([435, 924, 532, 264])
'''

fig, ax = plt.subplots()
index = np.arange(no_grades)
bar_width = 0.35

london_bars = ax.bar(index, london, bar_width, color = 'blue', label='london')
leeds_bars = ax.bar(index + bar_width, leeds, bar_width, color='orange', label='leeds')
glasgow_bars = ax.bar(index + (2 * bar_width), glasgow, bar_width, color='green', label='glasgow')

ax.set_facecolor('white') # sets the background colour of the plot

ax.set_xlabel('Grade') # sets the x-axis label 
ax.set_ylabel('Number of exams') # sets the y-axis label 
ax.set_title('Number of exams by grades in UK Academies') # sets the plot title

ax.set_xticks(index + bar_width) # places the ticks right between the male and leeds bars
ax.set_xticklabels(('Distinction', 'Merit', 'Pass', 'Fail'))

ax.bar_label(london_bars, padding=3)   # add values as labels to london bars
ax.bar_label(leeds_bars, padding=3) # add values as labels to leeds bars
ax.bar_label(glasgow_bars, padding=3) # add values as labels to leeds bars

ax.legend()

fig.tight_layout()

plt.show()
#plt.savefig('grouped_bar_plot.png')