##########################
# Module 4A - Matplotlib #
##########################

import numpy as np
import matplotlib.pyplot as plt

# slide 20
# impact (in £k) of potential risks by % of their probability
x = np.array([60, 46, 66, 48, 48, \
              34, 41, 47, 45, 66])
y = np.array([456, 235, 478, 159, 248, \
              490, 697, 554, 387, 454]) 

plt.xlabel('Probability %')
plt.ylabel('Impact £k')
plt.title('Risks impact and their probability')
plt.scatter(x,y)
plt.savefig('scatter_plot.png')
