#######################
# Module 4B - Seaborn #
#######################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# DISTRIBUTION PLOTS
# ==================

# slide 12 - KDE plot
# scores is a numpy array
scores = np.random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                          size=100,
                          p=[0.01, 0.02, 0.03, 0.04, 0.05,
                          0.12, 0.15, 0.25, 0.13, 0.12, 0.08])
print(scores)
print(type(scores)) # <class 'numpy.ndarray'>

sns.displot(data=scores, kind='kde')
plt.title("displot(), excl. x-axis label")
plt.tight_layout()
plt.show()
#plt.savefig('distribution_plot.py')
# Note: when displot() is based on an array, it does not include the x-axis label
# and the y-axis label is (the default) "Density"

# slide 13
scores_series = pd.Series(scores, name='Scores')
sns.displot(data=scores_series, kind='kde')
plt.title("displot(), incl. x-axis label")
plt.tight_layout()
plt.show()
# Note: when displot() is based on a Series, it does include the x-axis label, as the name of the Series
# and the y-axis label is (the default) "Density"

sns.kdeplot(data=scores_series)
plt.title("kdeplot(), incl. x-axis label")
plt.tight_layout()
plt.show()

# slide 14 - Histogram
sns.displot(data=scores_series, kind='hist')
#OR ('hist' is default value for kind kwarg)
#sns.displot(data=scores_series)
#OR (using equivalent axes-level plot)
#sns.histplot(data=scores_series)
plt.tight_layout()
plt.show()
# Note that ticks on teh x-axis are not correctly placed
# To place them in teh middle of the bars, use the discrete=True kwarg
sns.displot(data=scores_series, kind='hist', discrete=True)
#OR ('hist' is default value for kind kwarg)
#sns.displot(data=scores_series)
#OR (using equivalent axes-level plot)
#sns.histplot(data=scores_series)
plt.tight_layout()
plt.show()

# slide 15
# To display both kde and histogram, set the kde key word argument to True (kind='hist' by default):
sns.displot(data=scores_series, kde=True, discrete=True)
plt.tight_layout()
plt.show()

# slide 16 - ECDF plot
# using figure-level function displot()
sns.displot(data=scores_series, kind='ecdf')
plt.tight_layout()
plt.show()
# using axes-level function ecdflot()
sns.ecdfplot(data=scores_series)
plt.tight_layout()
plt.show()



