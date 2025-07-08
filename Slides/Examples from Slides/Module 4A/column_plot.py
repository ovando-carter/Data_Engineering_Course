##########################
# Module 4A - Matplotlib #
##########################

import numpy as np
import matplotlib.pyplot as plt

# slide 18
# total covid vaccine doses per 100 people
x = np.array(['Israel', 'UAE', 'Chile', 'UK', \
              'Bahrain', 'US', 'Hungary', \
              'Qatar', 'Uruguay', 'Serbia']) 
y = np.array([121, 106, 76, 72, 72, 71, \
              60, 53, 51, 50])

plt.xlabel('Countries')
plt.ylabel('Doses')
plt.title('Total Covid vaccine doses per 100 people')

plt.bar(x,y)
plt.savefig('column_plot.png')