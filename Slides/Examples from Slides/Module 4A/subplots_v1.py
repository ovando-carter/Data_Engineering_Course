##########################
# Module 4A - Matplotlib #
##########################

import matplotlib.pyplot as plt
import numpy as np

# slides 25-28
# plot 1: number of male and female employees in a company, broken down by their age
no_age_groups = 6
male = np.array([235, 621, 823, 421, 120, 13])
female = np.array([435, 924, 532, 264, 125, 3]) 
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
index = np.arange(no_age_groups)
bar_width = 0.35   # bar width (0.35 units)
male_bars = ax[0].bar(index, male, bar_width, color='k', label='male')
female_bars = ax[0].bar(index + bar_width, female, bar_width, color='0.5', label='female')

ax[0].set_facecolor('orange') # sets the background colour of the plot 
ax[0].set_xlabel('Age group')
ax[0].set_ylabel('Number of employees')
ax[0].set_title('Number of employees by gender and age group')
ax[0].set_xticks(index + bar_width/2)
ax[0].set_xticklabels(('18-25', '26-34', '35-44', '45-54', '55-64', '65+'))
ax[0].bar_label(male_bars, padding=3)   # add values as labels to male bars
ax[0].bar_label(female_bars, padding=3) # add values as labels to female bars
ax[0].legend()

# plot 2: proportion of male and female employees
tot_male = np.sum(male)
tot_female = np.sum(female)
tot_employees = np.array([tot_male, tot_female])
pie_labels = "Male", "Female"
ax[1].set_title("Proportion of employees by gender")
ax[1].pie(tot_employees, explode=None, labels=None, autopct='%0.2f%%', shadow=True)
ax[1].axis('equal')  # equal aspect ratio ensures that pie is drawn as a circle.
ax[1].legend(pie_labels)

fig.tight_layout()
plt.savefig('subplots_v1.png')