import matplotlib.pyplot as plt
import numpy as np

# Matplotlib Example: Line Plot
x = np.linspace(0,2,100)

y = x

plt.plot(x, y, label='linear')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title('simple plot')
plt.legend()

plt.show()
#plt.savefig('line_plot.png')

# Matplotlib Example: Quadratic & Cubic Plots
x = np.linspace(0,2,100)


plt.plot(x, x, label = 'linear')
plt.plot(x, x**2, label = 'quadratic')
plt.plot(x, x**3, label = 'cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('simple plot')
plt.legend()

plt.show()
#plt.savefig('multiple_line_plots.png')

# Matplotlib Example: Column Plot
# total covid vaccine doses per 100 people
x = np.array(['Israel', 'UAE', 'Chile', 'UK', \
              'Bahrain', 'US', 'Hungary', \
              'Qatar', 'Uruguay', 'Serbia']) 
y = np.array([121, 106, 76, 72, 72, 71, \
              60, 53, 51, 50])

plt.xlabel('Countries')
plt.ylabel('Doses')
plt.title('Total Covid vaccine doses per 100 people')

plt.bar(x,y, width = 0.1)
plt.show()
#plt.savefig('column_plot.png')

#Matplotlib Example: Scatterplot
# impact (in £k) of potential risks by % of their probability
x = np.array([60, 46, 66, 48, 48, \
              34, 41, 47, 45, 66])
y = np.array([456, 235, 478, 159, 248, \
              490, 697, 554, 387, 454]) 

plt.xlabel('Probability %')
plt.ylabel('Impact £k')
plt.title('Risks impact and their probability')
plt.scatter(x,y)
plt.show()
#plt.savefig('scatter_plot.png')

# Matplotlib Example: Grouped Bar Plot
no_age_groups = 6
male = np.array([235, 621, 823, 421, 120, 13])
female = np.array([435, 924, 532, 264, 125, 3])

fig, ax = plt.subplots()
index = np.arange(no_age_groups)
bar_width = 0.35

male_bars = ax.bar(index, male, bar_width, color = 'k', label='male')
female_bars = ax.bar(index + bar_width, female, bar_width, color='0.5', label='female')

ax.set_facecolor('orange') # sets the background colour of the plot 
ax.set_xlabel('Age group') # sets the x-axis label 
ax.set_ylabel('Number of employees') # sets the y-axis label 
ax.set_title('Number of employees by gender and age group') # sets the plot title

ax.set_xticks(index + bar_width/2) # places the ticks right between the male and female bars
ax.set_xticklabels(('18-25', '26-34', '35-44', '45-54', '55-64', '65+'))
ax.bar_label(male_bars, padding=3)   # add values as labels to male bars
ax.bar_label(female_bars, padding=3) # add values as labels to female bars
ax.legend()

fig.tight_layout()
plt.show()
#plt.savefig('grouped_bar_plot.png')

#Matplotlib Example: Pie Plot
male = np.array([235, 621, 823, 421, 120, 13])
female = np.array([435, 924, 532, 264, 125, 3])

tot_male = np.sum(male)
tot_female = np.sum(female)
tot_employees = np.array([tot_male, tot_female])
pie_labels = ["Male", "Female"]
plt.pie(tot_employees, labels=pie_labels, autopct='%.2f%%', shadow=True)
plt.legend(title="Employees:")
plt.savefig('pie_plot.png')
