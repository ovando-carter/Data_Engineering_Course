##########################
# Module 4A - Matplotlib #
##########################

import numpy as np
import matplotlib.pyplot as plt

# slides 10 - 16
x = np.linspace(0,2,100)

plt.plot(x, x, label='linear')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title('simple plot')
plt.legend()

#plt.show()
plt.savefig('line_plot.png')

