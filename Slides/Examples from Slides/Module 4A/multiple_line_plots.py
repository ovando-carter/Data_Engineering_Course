##########################
# Module 4A - Matplotlib #
##########################

import numpy as np
import matplotlib.pyplot as plt

# slide 17
x = np.linspace(0,2,100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')


plt.xlabel('x label')
plt.ylabel('y label')
plt.title('simple plot')
plt.legend()

#plt.show()
plt.savefig('multiple_line_plots.png')