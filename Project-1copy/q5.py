# ported from 4
from q4 import *

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print('avg_percentage_per_activity \n', avg_percentage_per_activity(file_name, course_code, attempt))
data_import = avg_percentage_per_activity(file_name, course_code, attempt)
data_q4 = data_import.sort_values(by='Average', ascending=True)

attempt = 1
# draw the plot
ax = sns.barplot(data=data_q4, x='Average', y='Activity Name')
# include numbers in the centre of the bars
ax.bar_label(ax.containers[0], fmt='%.2f', label_type='center')  # values for bars of each class
plt.title("Average percent for each activity in L-21-FOU-02 course")
plt.tight_layout()
plt.show()

