##########################
# Module 4A - Matplotlib #
##########################

import matplotlib.pyplot as plt
import numpy as np

# slides 29-31
# first make the figure
fig = plt.figure(figsize=(12,6))

# now create each subplot individually
# plot 1:
no_age_groups = 6
male = np.array([235, 621, 823, 421, 120, 13])
female = np.array([435, 924, 532, 264, 125, 3])
index = np.arange(no_age_groups)
bar_width = 0.35
# the figure consists of 2 plots: placed in two columns over 1 row and
# the current plot is the left one.
ax1 = plt.subplot(1, 2, 1)  
male_bars = ax1.bar(index, male, bar_width, color='k', label='male')
female_bars = ax1.bar(index + bar_width, female, bar_width, color='0.5', label='female')

ax1.set_facecolor('orange') # sets the background colour of the plot 
ax1.set_xlabel('Age group')
ax1.set_ylabel('Number of employees')
ax1.set_title('Number of employees by gender and age group')
ax1.set_xticks(index + bar_width/2)
ax1.set_xticklabels(('18-25', '26-34', '35-44', '45-54', '55-64', '65+'))
ax1.bar_label(male_bars, padding=3)   # add values as labels to male bars
ax1.bar_label(female_bars, padding=3) # add values as labels to female bars
ax1.legend()

# plot 2:
tot_male = np.sum(male)
tot_female = np.sum(female)
tot_employees = np.array([tot_male, tot_female])
pie_labels = "Male", "Female"
# the figure consists of 2 plots: placed in two columns over 1 row and
# the current plot is the right one.
ax2 = plt.subplot(1, 2, 2)
ax2.pie(tot_employees, explode=None, labels=None, autopct='%.2f%%', shadow=True)
ax2.axis('equal')  # equal aspect ratio (scaling) ensures that pie is drawn as a circle
ax2.set_title("Proportion of employees by gender")
ax2.legend(pie_labels)

fig.tight_layout()

#plt.show()
plt.savefig('subplot_v2.png')