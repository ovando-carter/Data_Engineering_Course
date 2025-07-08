##########################
# Module 4A - Matplotlib #
##########################

import numpy as np
import matplotlib.pyplot as plt

# slide 21 - 23
no_age_groups = 6
male = np.array([235, 621, 823, 421, 120, 13])
female = np.array([435, 924, 532, 264, 125, 3])

fig, ax = plt.subplots()
index = np.arange(no_age_groups)
bar_width = 0.35
male_bars = ax.bar(index, male, bar_width, color='k', label='male')
female_bars = ax.bar(index + bar_width, female, bar_width, color='0.5', label='female')
ax.set_facecolor('orange') # sets the background colour of the plot 
ax.set_xlabel('Age group') # sets the x-axis label 
ax.set_ylabel('Number of employees') # sets the y-axis label 
ax.set_title('Number of employees by gender and age group') # sets the plot title

ax.set_xticks(index + bar_width/2) # places the ticks right between the male and female bars
ax.set_xticklabels(('18-25', '26-34', '35-44', '45-54', '55-64', '65+'))
ax.bar_label(male_bars, padding=3)   # add values as labels to male bars
ax.bar_label(female_bars, padding=3) # add values as labels to female bars
ax.legend()

fig.tight_layout()
plt.savefig('grouped_bar_plot.png')
