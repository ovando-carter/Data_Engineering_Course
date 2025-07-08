# ported from 4
from q4 import *

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# input data
file_name = 'fdm_training_data_2021.csv'
course_code = 'L-21-FOU-02'
attempt = 1


data_import = avg_percentage_per_activity(file_name, course_code, attempt)

print(data_import)
data_q4 = data_import.sort_values(by='Average', ascending=True)


# draw the plot
ax = sns.barplot(data=data_q4, x='Average', y='Activity Name')
# include numbers in the centre of the bars
ax.bar_label(ax.containers[0], fmt='%.2f', label_type='center')  # values for bars of each class
plt.title("Average percent for each activity in L-21-FOU-02 course")
plt.tight_layout()
plt.show()

