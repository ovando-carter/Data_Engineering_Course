##########################
# Module 4A - Matplotlib #
##########################

# slide 24
import matplotlib.pyplot as plt
import numpy as np

male = np.array([235, 621, 823, 421, 120, 13])
female = np.array([435, 924, 532, 264, 125, 3])

tot_male = np.sum(male)
tot_female = np.sum(female)
tot_employees = np.array([tot_male, tot_female])
pie_labels = ["Male", "Female"]
plt.pie(tot_employees, labels=pie_labels, autopct='%.2f%%', shadow=True)
plt.legend(title="Employees:")
plt.savefig('pie_plot.png')
