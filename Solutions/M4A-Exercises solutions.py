##########################
# Module 4A - Matplotlib #
##########################

import matplotlib.pyplot as plt
import numpy as np


# Question 1
# ----------
"""
Write a Python program to display the popularity of programming languages worldwide using
a) column plot
b) bar plot
c) pie plot (adding 'other' to the sample data with the difference to make 100%).
   Make Python stand out by 'exploding' it slightly from the pie plot.

Sample data:
Programming languages: Python, Java,  JavaScript, C#,   C++,  PHP,  R
Popularity (%):        29.93,  17.78, 8.79,       6.73, 6.45, 5.76, 3.92
(Source: https://pypl.github.io/PYPL.html)
"""
# solution 1a
# initialising the headings and the data
languages = np.array(['Python', 'Java', 'JavaScript', 'C#', 'C++', 'PHP']) 
popularity = np.array([29.93, 17.78, 8.79, 6.73, 6.45, 5.76])
# adding the labels and the title
plt.xlabel('Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages\n' + 'Worldwide, Aug 2021')
# plotting the data and displaying the plot
plt.bar(languages,popularity)
plt.show()


# solution 1b
# initialising the headings and the data
languages = np.array(['Python', 'Java', 'JavaScript', 'C#', 'C++', 'PHP']) 
popularity = np.array([29.93, 17.78, 8.79, 6.73, 6.45, 5.76])
# adding the labels and the title
plt.xlabel('Popularity (%)')
plt.ylabel('Languages')
plt.title('Popularity of Programming Languages\n' + 'Worldwide, Aug 2021')
# plotting the data and displaying the plot
plt.barh(languages,popularity)
plt.tight_layout()
plt.show()


# solution 1c
# initialising the headings and the data
languages = np.array(['Python', 'Java', 'JavaScript', 'C#', 'C++', 'PHP']) 
popularity = np.array([29.93, 17.78, 8.79, 6.73, 6.45, 5.76])
# calculate the total percentage popularity
# of other programming languages, add it to
# the popularity array, and include the
# relevant label to the languages array
tot_popularity = sum(popularity)
tot_other = 100 - tot_popularity
popularity = np.append(popularity, tot_other)
languages = np.append(languages, 'other')
# exploding 'Python' a little away
explode = (0.1, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01)
# plotting the data and displaying the plot 
plt.pie(popularity, labels=languages, explode=explode, autopct='%.2f%%', shadow=True)
plt.title('Popularity of Programming Languages\n' + 'Worldwide, Aug 2021') 
plt.show()



# Question 2
# ----------
"""
The company "ABC Group" keeps daily records of its shares 
values (£).
The opening, high, low and closing values for 2nd August 2021
are given in the sample below:
Open,High,Low,Close
558.750000,570.559998,554.500000,569.065002
Write a Python program to draw line plot showing ABCs shares
values during 2nd August 2021.
"""
# solution 2
# initialising the headings and the data
points = np.array(['Open', 'High', 'Low', 'Close'])
day1 = np.array([558.750000,570.559998,554.500000,569.065002])
# plotting the data
plt.plot(points, day1)
# adding the labels, title and displaying the plot 
plt.xlabel("Points")
plt.ylabel("Value (£)")
plt.title("ABC Shares values\non 02-08-2021")
plt.show()



# Question 3
# ----------
"""
The company "ABC Group" also keeps weekly records of 
its shares values (£).
The opening, high, low and closing values for each 
day between 2nd and 6th August 2021 are given in 
the sample below:
Date,Open,High,Low,Close
02-08-2021,558.750000,570.559998,554.500000,569.065002
03-08-2021,556.835021,558.710022,552.890015,556.429993
04-08-2021,557.658439,578.070007,555.650024,556.469971
05-08-2021,559.213903,580.479980,555.039978,556.859985
06-08-2021,558.307553,559.659973,556.250000,557.034628
Write a Python program to draw line plot of ABCs shares
values during this period.
Tip: create a grouped line plot where each day will be
     represented with a separate line. Include the legend
     to list the dates.
"""
# solution 3
# initialising the headings and the data
points = np.array(['Open', 'High', 'Low', 'Close'])
day1 = np.array([558.750000,570.559998,554.500000,569.065002])
day2 = np.array([556.835021,558.710022,552.890015,556.429993])
day3 = np.array([557.658439,578.070007,555.650024,556.469971])
day4 = np.array([559.213903,580.479980,555.039978,556.859985])
day5 = np.array([558.307553,559.659973,556.250000,557.034628])
# plotting the data
fig, ax = plt.subplots()
# labelling each line plot will also include the label to the legend
day1_plot = ax.plot(points, day1, label='02-08-2021')
day2_plot = ax.plot(points, day2, label='03-08-2021')
day3_plot = ax.plot(points, day3, label='04-08-2021')
day4_plot = ax.plot(points, day4, label='05-08-2021')
day5_plot = ax.plot(points, day5, label='06-08-2021')
# adding the labels, title, legend and displaying the plot 
ax.set_xlabel("Points")
ax.set_ylabel("Value (£)")
ax.set_title("ABC Shares values by day\non w/c 02-08-2021")
ax.legend(title='Dates:', loc='upper right') 
plt.show()



# Question 4
# ----------
"""
Change the group line plot produced in question 3 so that each line
in the plot represents a point during the day (open, high, low, close).
The 5 weekdays should be displayed on the x-axis, and share values (£)
on the y-axis. Include the legend to list the points during the day
(day-points) for which shares values are given: open, high, low, close.
"""
# solution 4
# initialising the headings and the data
days = np.array(['02-08-2021', '03-08-2021','04-08-2021','05-08-2021','06-08-2021'])
open_values  = np.array([558.750000, 556.835021, 557.658439, 559.213903, 558.307553])
high_values  = np.array([570.559998, 558.710022, 578.070007, 580.479980, 559.659973])
low_values   = np.array([554.500000, 552.890015, 555.650024, 555.039978, 556.250000])
close_values = np.array([569.065002, 556.429993, 556.469971, 556.859985, 557.034628])
points = np.array(['Open', 'High', 'Low', 'Close'])
# plotting the data
fig, ax = plt.subplots()
# labelling each line will also include the label to the legend
open_plot  = ax.plot(days, open_values,  label='Open')
high_plot  = ax.plot(days, high_values,  label='High')
low_plot   = ax.plot(days, low_values,   label='Low')
close_plot = ax.plot(days, close_values, label='Close')
# adding the title, labels, legend and displaying the plot 
ax.set_title("ABC Shares values by point\non w/c 02-08-2021")
ax.set_xlabel("Dates")
ax.set_ylabel("Value (£)")
ax.legend(title='Points:', loc='upper left') 
plt.show()



# Question 5
# ----------
"""
Use the sample data from question 3 stored in the file abc_shares_data to
write a Python program to draw a column plot of ABCs shares 
values during this period.
Tip: create a grouped column plot where each day-point will be
     represented with a separate column (grouping the 4 columns together
     for each of the 5 days). Include the legend to list the day-points.
"""
# solution 5
import matplotlib.pyplot as plt
import numpy as np

days = np.array(['02-08-2021', '03-08-2021','04-08-2021','05-08-2021','06-08-2021'])
open_values = np.array([558.750000, 556.835021, 557.658439, 559.213903, 558.307553])
high_values = np.array([570.559998, 558.710022, 578.070007, 580.479980, 559.659973])
low_values = np.array([554.500000, 552.890015, 555.650024, 555.039978, 556.250000])
close_values = np.array([569.065002, 556.429993, 556.469971, 556.859985, 557.034628])
day_points = np.array(['Open', 'High', 'Low', 'Close'])
no_days = len(days)
index = np.arange(no_days)
# plotting the data
fig, ax = plt.subplots()
bar_width = 0.20   # bar width (0.20 units)
# bars start at position 0, 1, 2, 3, 4
# Note: position 0 is not where the intersection between x and y axis is.
# It is at the distance between the y-axis and the half of the width of the first bar
# (here the half of the width of the first bar is 0.1 because the bar width is set to 0.2).
# This is to leave some space between the y-axis and the left edge of the first bar.
# The distance between positions from that point on is constant (1 unit).
# The distance between the bars is calculated as 1 - n_bars * bar_width (here 1 - 4 * 0.20 = 0.20).
# Create five groups of four column bars: one bar for each day-point; one group for each of the 5 days
# (labelling each column plot will also include the label to the legend)
# the next day-point bar of the first day starts right after the previous day-point bar
# at positions 0.30, 0.50, 0.70, 0.90. The last day-point bar ends at 1.10, followed by 0.20
# (the distance between the bars). The first day-point bar of the second day starts at 1.30.
# The first day-point ('Open') starts at positions 0.30, 1.30, 2.30, 3.30 and 4.30.
# - the next day-point bar will be shifted bar_width (0.20) units from the previous day-point bar
open_bars  = ax.bar(index, open_values, bar_width, label=day_points[0])                  # label='Open'
high_bars  = ax.bar(index + 1 * bar_width, high_values, bar_width, label=day_points[1])  # label='Low'
low_bars   = ax.bar(index + 2 * bar_width, low_values, bar_width, label=day_points[2])   # label='High'
close_bars = ax.bar(index + 3 * bar_width, close_values, bar_width, label=day_points[3]) # label='Close'
# adding the title
ax.set_title("ABC Shares values by point\non w/c 02-08-2021")
# adding the labels
ax.set_xlabel("Dates")
ax.set_ylabel("Value (£)")
ax.legend(title='Points:', loc='upper left')
# add the x axis tick values, which are the locations
# along the x-axis where the tick marks appear:
# Note: if index was the argument to the set_xticks() function, the first tick (for the value 0)
# would be positioned half way between the width of the first bar; this is the default position of 0.
# Since our plot has four bars, we want to move the ticks so that they appear right between the
# 2nd and 3rd bar of each group - to achieve that we need to pass the value index + 1.5*bar_width
# to the set_xticks() function, setting the ticks to: 0.30, 1.30, 2.30, 3.30, 4.30.
ax.set_xticks(index + 1.5*bar_width)
# The limits on the y-axis can be changed using the set_ylim() function: ax.set_ylim([ymin,ymax])
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim
ax.set_ylim([550,590])
ax.set_xticklabels((days[0], days[1], days[2], days[3], days[4]))
# adjust the figure area and show the plot
fig.tight_layout()
plt.show()



# Question 6
# ----------
"""
Use the sample data from question 3 to write a Python
program to draw a column plot of ABCs stock's return
on each of the 5 days. 
The stock's return (or its performance in percentage terms)
is calculated as the difference between the stock's open and
close, divided by the open.
Note: question 6 requires data for two day-points only:
      'open' and 'close'.
"""
# solution 6:
days = np.array(['02-08-2021', '03-08-2021','04-08-2021','05-08-2021','06-08-2021'])
open_values = np.array([558.750000, 556.835021, 557.658439, 559.213903, 558.307553])
close_values = np.array([569.065002, 556.429993, 556.469971, 556.859985, 557.034628])
# calculate the stock's return values
stock_return_values = (open_values - close_values) / open_values
fig, ax = plt.subplots()
bar_width = 0.40   # bar width (0.40 units)
# create a column bar for each day
stock_return_bars = ax.bar(days, stock_return_values, bar_width)
# add the title
ax.set_title("ABC Stock's Return values\non w/c 02-08-2021")
# add the labels
ax.set_xlabel("Dates")
ax.set_ylabel("Stock's Return Value (£)")
# add values as labels to column bars
ax.bar_label(stock_return_bars, padding=3)
# adjust the figure area and show the plot
fig.tight_layout()
plt.show()
"""
Note:
stock_return_bars = ax.bar(days, stock_return_values, bar_width)
    is equivalent to:
no_days = len(days)
index = np.arange(no_days)
stock_return_bars = ax.bar(index, stock_return_values, bar_width)
ax.set_xticks(range(no_days))
ax.set_xticklabels((days[0], days[1], days[2], days[3], days[4]))
"""



# Question 7
# ----------
"""
Combine the two plots from questions 5 and 6 into one figure using
a) subplots() function
b) subplot() function
"""
# solution 7a - using subplots() function:
# ----------------------------------------
import matplotlib.pyplot as plt
import numpy as np

# 1st plot: ABC Shares values by point on w/c 02-08-2021
days = np.array(['02-08-2021', '03-08-2021','04-08-2021','05-08-2021','06-08-2021'])
open_values = np.array([558.750000, 556.835021, 557.658439, 559.213903, 558.307553])
high_values = np.array([570.559998, 558.710022, 578.070007, 580.479980, 559.659973])
low_values = np.array([554.500000, 552.890015, 555.650024, 555.039978, 556.250000])
close_values = np.array([569.065002, 556.429993, 556.469971, 556.859985, 557.034628])
day_points = np.array(['Open', 'High', 'Low', 'Close'])
no_days = len(days)
index = np.arange(no_days)
fig, ax = plt.subplots(1, 2, figsize=(15, 6))
bar_width = 0.20   # bar width (0.20 units)
# Create five groups of four column bars: one bar for each day-point; one group for each of the 5 days
# (labelling each column plot will also include the label to the legend)
# the next day-point bar of the first day starts right after the previous day-point bar
# at positions 0.30, 0.50, 0.70, 0.90. The last day-point bar ends at 1.10, followed by 0.20
# (the distance between the bars). The first day-point bar of the second day starts at 1.30.
# The first day-point ('Open') starts at positions 0.30, 1.30, 2.30, 3.30 and 4.30.
# - the next day-point bar will be shifted bar_width (0.20) units from the previous day-point bar
open_bars  = ax[0].bar(index, open_values, bar_width, label=day_points[0])                  # label='Open'
high_bars  = ax[0].bar(index + 1 * bar_width, high_values, bar_width, label=day_points[1])  # label='Low'
low_bars   = ax[0].bar(index + 2 * bar_width, low_values, bar_width, label=day_points[2])   # label='High'
close_bars = ax[0].bar(index + 3 * bar_width, close_values, bar_width, label=day_points[3]) # label='Close'
# adding the title
ax[0].set_title("ABC Shares values by point\non w/c 02-08-2021")
# adding the labels
ax[0].set_xlabel("Dates")
ax[0].set_ylabel("Value (£)")
ax[0].legend(title='Points:', loc='upper left')
# add the x axis tick values, which are the locations
# along the x-axis where the tick marks appear:
# Note: if index was the argument to the set_xticks() function, the first tick (for the value 0)
# would be positioned half way between the width of the first bar; this is the default position of 0.
# Since our plot has four bars, we want to move the ticks so that they appear right between the
# 2nd and 3rd bar of each group - to achieve that we need to pass the value index + 1.5*bar_width
# to the set_xticks() function, setting the ticks to: 0.30, 1.30, 2.30, 3.30, 4.30.
ax[0].set_xticks(index + 1.5*bar_width)
# The limits on the y-axis can be changed using the set_ylim() function: ax.set_ylim([ymin,ymax])
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim
ax[0].set_ylim([550,590])
ax[0].set_xticklabels((days[0], days[1], days[2], days[3], days[4]))

# 2nd plot: ABC Stock's Return values on w/c 02-08-2021
# calculate the stock's return values
stock_return_values = (open_values - close_values) / open_values
# create a column bar for each day
stock_return_bars = ax[1].bar(days, stock_return_values, bar_width)
# add the title
ax[1].set_title("ABC Stock's Return values\non w/c 02-08-2021")
# add the labels
ax[1].set_xlabel("Dates")
ax[1].set_ylabel("Stock's Return Value (£)")
# add values as labels to column bars
ax[1].bar_label(stock_return_bars, padding=3)

# adjust the figure area and show the plot
fig.tight_layout()
plt.show()


# solution 7b - using subplot() function:
# ---------------------------------------
# first make the figure
fig = plt.figure(figsize=(15, 6))
# now create each subplot individually
# 1st plot: ABC Shares values by point on w/c 02-08-2021
days = np.array(['02-08-2021', '03-08-2021','04-08-2021','05-08-2021','06-08-2021'])
open_values = np.array([558.750000, 556.835021, 557.658439, 559.213903, 558.307553])
high_values = np.array([570.559998, 558.710022, 578.070007, 580.479980, 559.659973])
low_values = np.array([554.500000, 552.890015, 555.650024, 555.039978, 556.250000])
close_values = np.array([569.065002, 556.429993, 556.469971, 556.859985, 557.034628])
day_points = np.array(['Open', 'High', 'Low', 'Close'])
no_days = len(days)
index = np.arange(no_days)
bar_width = 0.20   # bar width (0.20 units)
# create the first plot
ax1 = plt.subplot(1, 2, 1)
# Create five groups of four column bars: one bar for each day-point; one group for each of the 5 days
# (labelling each column plot will also include the label to the legend)
# the next day-point bar of the first day starts right after the previous day-point bar
# at positions 0.30, 0.50, 0.70, 0.90. The last day-point bar ends at 1.10, followed by 0.20
# (the distance between the bars). The first day-point bar of the second day starts at 1.30.
# The first day-point ('Open') starts at positions 0.30, 1.30, 2.30, 3.30 and 4.30.
# - the next day-point bar will be shifted bar_width (0.20) units from the previous day-point bar
open_bars  = ax1.bar(index, open_values, bar_width, label=day_points[0])                  # label='Open'
high_bars  = ax1.bar(index + 1 * bar_width, high_values, bar_width, label=day_points[1])  # label='Low'
low_bars   = ax1.bar(index + 2 * bar_width, low_values, bar_width, label=day_points[2])   # label='High'
close_bars = ax1.bar(index + 3 * bar_width, close_values, bar_width, label=day_points[3]) # label='Close'
# adding the title
ax1.set_title("ABC Shares values by point\non w/c 02-08-2021")
# adding the labels
ax1.set_xlabel("Dates")
ax1.set_ylabel("Value (£)")
ax1.legend(title='Points:', loc='upper left')
# add the x axis tick values, which are the locations
# along the x-axis where the tick marks appear:
# Note: if index was the argument to the set_xticks() function, the first tick (for the value 0)
# would be positioned half way between the width of the first bar; this is the default position of 0.
# Since our plot has four bars, we want to move the ticks so that they appear right between the
# 2nd and 3rd bar of each group - to achieve that we need to pass the value index + 1.5*bar_width
# to the set_xticks() function, setting the ticks to: 0.30, 1.30, 2.30, 3.30, 4.30.
ax1.set_xticks(index + 1.5*bar_width)
# The limits on the y-axis can be changed using the set_ylim() function: ax.set_ylim([ymin,ymax])
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim
ax1.set_ylim([550,590])
ax1.set_xticklabels((days[0], days[1], days[2], days[3], days[4]))

# 2nd plot: ABC Stock's Return values on w/c 02-08-2021
# calculate the stock's return values
stock_return_values = (open_values - close_values) / open_values
# create the first plot
ax2 = plt.subplot(1, 2, 2)
# create a column bar for each day
stock_return_bars = ax2.bar(days, stock_return_values, bar_width)
# add the title
ax2.set_title("ABC Stock's Return values\non w/c 02-08-2021")
# add the labels
ax2.set_xlabel("Dates")
ax2.set_ylabel("Stock's Return Value (£)")
# add values as labels to column bars
ax2.bar_label(stock_return_bars, padding=3)

# adjust the figure area and show the plot
fig.tight_layout()
plt.show()



# Question 8
# ----------
"""
ABC Group is looking at their domestic and international opportunities, comparing 
the revenue that can be generated to the probability of obtaining the revenue.
Write a Python program that loads data from the file abc_dom_int and draws a
grouped scatter plot, where the first plot compares revenue vs probability for
domestic opportunities, and the second plot compares revenue vs probability for
international opportunities. Add a label to each scatter point.
The program should be able to work with any number of opportunities (not just the
10 listed in the sample file abc_dom_int).
"""
# solution 8:
# -----------
# load data from the file abc_dom_int.txt into a NumPy array
import os
currentDirectoryPath = os.getcwd()
filePath = currentDirectoryPath + '\\abc_dom_int.txt'
abc_dom_int = np.loadtxt(filePath, delimiter=',', dtype=str)
# store the number of rows and the number of columns of the array
num_rows = abc_dom_int.shape[0]
num_cols = abc_dom_int.shape[1]
# extract opportunities (needed to label each scatter point)
# extract elements from the 1st column (with index 0) sliced from index 1 to index num_rows-1
opportunities = abc_dom_int[1:num_rows, 0]
# initialising the data
# extract domestic revenue, domestic probability,
# international revenue and international probability
# for each opportunity, convert them to int data type
# and store them in arrays
dom_rev_data  = np.array(abc_dom_int[1:num_rows, 1].astype(int))
dom_prob_data = np.array(abc_dom_int[1:num_rows, 2].astype(int))
int_rev_data  = np.array(abc_dom_int[1:num_rows, 3].astype(int))
int_prob_data = np.array(abc_dom_int[1:num_rows, 4].astype(int))
# plotting the data
fig, ax = plt.subplots()
# labelling each scatter plot will also include the label to the legend
dom_scatter = ax.scatter(dom_rev_data, dom_prob_data, label='Domestic')
int_scatter = ax.scatter(int_rev_data, int_prob_data, label='International')
# adding the title
ax.set_title("ABC Domestic & International Opportunities\nRevenue (£m) vs Probability (%)")
# adding the labels
ax.set_xlabel("Revenue (£m)")
ax.set_ylabel("Probability (%)")
ax.legend(loc='best')
# adding labels to domestic scatter plot points
for i, label in enumerate(opportunities):
    ax.text(dom_rev_data[i], dom_prob_data[i], label)
# adding labels to international scatter plot points
for i, label in enumerate(opportunities):
    ax.text(int_rev_data[i], int_prob_data[i], label)
# display the plot
plt.show()
"""
Notice the value 1e6 at the right end of the x-axis
(in the right bottom corner of the figure).
It indicates an overall scale factor for the x-axis.
That is, if there's a 2 on the x-axis and a 1e6 at its right end,
the value at 2 actually indicates 2*1e6 = 2e6 = 2 * 10^6 = 2,000,000.
"""



# Question 9
# ----------
"""
The sample file abc_training_costs provides data for ABC’s trainings and
related costs. Write a Python program that loads data from the file
abc_training_costs and draws a figure combining four column subplots
positioned in two rows:
• The first subplot, positioned in 1st row and 1st column, to show the total
  training costs incurred by each office (Finland, France, Germany, Ireland, Spain)
• The second subplot, positioned in 1st row and 2nd column, to show the total
  training costs by level (Management, Non management)
• The third subplot, positioned in 2nd row and 1st column, to show the total
  training costs by Course-type (Technical, Soft skills)
• The fourth subplot, positioned in 2nd row and 2nd column, to show the total
  training costs by Course-type (Technical, Soft skills).
Combine the four subplots using:
a) subplots() function
b) subplot() function
Tip: implement the SUMIF Excel function and use it to produce data for all four plots
"""
# Common tasks for both solutions: 9a & 9b:
def sumif(cond_range, cond, sum_range):
    total = 0
    for index in range(len(cond_range)):
        if cond_range[index] == cond:
            total += sum_range[index]
    return total

currentDirectoryPath = os.getcwd()
# import the whole data set as str data type
filePath = currentDirectoryPath + '\\abc_training_costs.txt'
abc_training_costs = np.loadtxt(filePath, delimiter='\t', dtype=str)

# solution 9a - using the subplots() function:
# --------------------------------------------
# create the figure for the multiplot
fig, ax = plt.subplots(2, 2, figsize=(15,10))

# 1st plot: total training cost by office (Finland, Germany, France, Ireland, Spain)
# calculate the totals
tot_finland = sumif(abc_training_costs[1:, 1], 'Finland', abc_training_costs[1:, 4].astype(int))    
tot_france = sumif(abc_training_costs[1:, 1], 'France', abc_training_costs[1:, 4].astype(int))    
tot_germany = sumif(abc_training_costs[1:, 1], 'Germany', abc_training_costs[1:, 4].astype(int))
tot_ireland = sumif(abc_training_costs[1:, 1], 'Ireland', abc_training_costs[1:, 4].astype(int))    
tot_spain = sumif(abc_training_costs[1:, 1], 'Spain', abc_training_costs[1:, 4].astype(int))
# initialising the headings and the data
offices = np.array(['Finland', 'France', 'Germany', 'Ireland', 'Spain']) 
tot_per_office = np.array([tot_finland, tot_france, tot_germany, tot_ireland, tot_spain])
# draw the first subplot with axis labels and title
tot_per_office_bars = ax[0, 0].bar(offices, tot_per_office)
ax[0, 0].set_xlabel('Offices')
ax[0, 0].set_ylabel('Total Cost (£)')
ax[0, 0].set_title("by office")
# add values as labels to column bars
ax[0, 0].bar_label(tot_per_office_bars)
# alternative way to add values as labels to column bars:
# using Matplotlib's text() function and
# passing the coordinates where the text shall be placed
# x-coordinate: i (ticks on the x-axis, defined by range(len(offices))
# y-coordinate: tot_per_office[i] the height of the bar at index i
# ha (horizontal alignment) to center text above the bars
#for i in range(len(offices)):
#    ax[0, 0].text(i, tot_per_office[i], tot_per_office[i], ha = 'center')

# 2nd plot: total training cost by level (management, non management)
# calculate the totals
tot_management = sumif(abc_training_costs[1:, 0], 'Management', abc_training_costs[1:, 4].astype(int))
tot_non_management = sumif(abc_training_costs[1:, 0], 'Non management', abc_training_costs[1:, 4].astype(int))
# initialising the headings and the data
levels = np.array(['Management', 'Non management']) 
tot_per_level = np.array([tot_management, tot_non_management])
# draw the second subplot with axis labels and title
tot_per_level_bars = ax[0, 1].bar(levels, tot_per_level)
ax[0, 1].set_xlabel('Levels')
ax[0, 1].set_ylabel('Total Cost (£)')
ax[0, 1].set_title("by level")
# add values as labels to column bars
ax[0, 1].bar_label(tot_per_level_bars)
# alternative way to add values as labels to column bars:
#for i in range(len(levels)):
#    ax[0, 1].text(i, tot_per_level[i], tot_per_level[i], ha = 'center')    

# 3rd plot: total training cost by Course type (Technical, Soft skills)
# calculate the totals
tot_technical = sumif(abc_training_costs[1:, 2], 'Technical', abc_training_costs[1:, 4].astype(int))
tot_soft_skills = sumif(abc_training_costs[1:, 2], 'Soft skills', abc_training_costs[1:, 4].astype(int))
# initialising the headings and the data
course_types = np.array(['Technical', 'Soft skills']) 
tot_per_course_type = np.array([tot_technical, tot_soft_skills])
# draw the third subplot with axis labels and title
tot_per_course_type_bars = ax[1, 0].bar(course_types, tot_per_course_type)
#ax[1, 0].bar(course_types, tot_per_course_type)
ax[1, 0].set_xlabel('Course types')
ax[1, 0].set_ylabel('Total Cost (£)')
ax[1, 0].set_title("by course type")
# add values as labels to column bars
ax[1, 0].bar_label(tot_per_course_type_bars)
# alternative way to add values as labels to column bars:
#for i in range(len(levels)):
#    ax[1, 0].text(i, tot_per_course_type[i], tot_per_course_type[i], ha = 'center')    

# 4th plot: total training cost by recommendation (Yes, No)
# calculate the totals
tot_recommendation = sumif(abc_training_costs[1:, 3], 'Yes', abc_training_costs[1:, 4].astype(int))
tot_not_recommended = sumif(abc_training_costs[1:, 3], 'No', abc_training_costs[1:, 4].astype(int))
# initialising the headings and the data
recommendation = np.array(['Yes', 'No']) 
tot_per_recommendation = np.array([tot_recommendation, tot_not_recommended])
# draw the fourth subplot with axis labels and title
tot_per_recommendation_bars = ax[1, 1].bar(recommendation, tot_per_recommendation)
ax[1, 1].set_xlabel('Recommendation')
ax[1, 1].set_ylabel('Total Cost (£)')
ax[1, 1].set_title("by recommendation")
# add values as labels to column bars
ax[1, 1].bar_label(tot_per_recommendation_bars)
# alternative way to add values as labels to column bars:
#for i in range(len(recommendation)):
#    ax[1, 1].text(i, tot_per_recommendation[i], tot_per_recommendation[i], ha = 'center')    

# set the title for the entire figure ('super title')
plt.suptitle("ABC's total training cost")
# display the plot
plt.show()


# solution 9b - using the subplot() function:
# -------------------------------------------
# first make the figure for the multiplot
fig = plt.figure(figsize=(15,10))

# 1st plot: total training cost by office (Finland, Germany, France, Ireland, Spain)
# calculate the totals
tot_finland = sumif(abc_training_costs[1:, 1], 'Finland', abc_training_costs[1:, 4].astype(int))    
tot_france = sumif(abc_training_costs[1:, 1], 'France', abc_training_costs[1:, 4].astype(int))    
tot_germany = sumif(abc_training_costs[1:, 1], 'Germany', abc_training_costs[1:, 4].astype(int))
tot_ireland = sumif(abc_training_costs[1:, 1], 'Ireland', abc_training_costs[1:, 4].astype(int))    
tot_spain = sumif(abc_training_costs[1:, 1], 'Spain', abc_training_costs[1:, 4].astype(int))
# initialising the headings and the data
offices = np.array(['Finland', 'France', 'Germany', 'Ireland', 'Spain']) 
tot_per_office = np.array([tot_finland, tot_france, tot_germany, tot_ireland, tot_spain])
# draw the first plot with axis labels and title
ax1 = plt.subplot(2, 2, 1)
tot_per_office_bars = ax1.bar(offices, tot_per_office)
ax1.set_xlabel('Offices')
ax1.set_ylabel('Total Cost (£)')
ax1.set_title("by office")
# add values as labels to column bars
ax1.bar_label(tot_per_office_bars)
# alternative way to add values as labels to column bars:
# using Matplotlib's text() function and
# passing the coordinates where the text shall be placed
# x-coordinate: i (ticks on the x-axis, defined by range(len(offices))
# y-coordinate: tot_per_office[i] the height of the bar at index i
# ha (horizontal alignment) to center text above the bars
#for i in range(len(offices)):
#    ax1.text(i, tot_per_office[i], tot_per_office[i], ha = 'center')

# 2nd plot: total training cost by level (management, non management)
# calculate the totals
tot_management = sumif(abc_training_costs[1:, 0], 'Management', abc_training_costs[1:, 4].astype(int))
tot_non_management = sumif(abc_training_costs[1:, 0], 'Non management', abc_training_costs[1:, 4].astype(int))
# initialising the headings and the data
levels = np.array(['Management', 'Non management']) 
tot_per_level = np.array([tot_management, tot_non_management])
# draw the second plot with axis labels and title
ax2 = plt.subplot(2, 2, 2)
tot_per_level_bars = ax2.bar(levels, tot_per_level)
ax2.set_xlabel('Levels')
ax2.set_ylabel('Total Cost (£)')
ax2.set_title("by level")
# add values as labels to column bars
ax2.bar_label(tot_per_level_bars)
# alternative way to add labels to column bars:
#for i in range(len(levels)):
#    ax2.text(i, tot_per_level[i], tot_per_level[i], ha = 'center')    

# 3rd plot: total training cost by Course type (Technical, Soft skills)
# calculate the totals
tot_technical = sumif(abc_training_costs[1:, 2], 'Technical', abc_training_costs[1:, 4].astype(int))
tot_soft_skills = sumif(abc_training_costs[1:, 2], 'Soft skills', abc_training_costs[1:, 4].astype(int))
# initialising the headings and the data
course_types = np.array(['Technical', 'Soft skills']) 
tot_per_course_type = np.array([tot_technical, tot_soft_skills])
# draw the third plot with axis labels and title
ax3 = plt.subplot(2, 2, 3)
tot_per_course_type_bars = ax3.bar(course_types, tot_per_course_type)
ax3.set_xlabel('Course types')
ax3.set_ylabel('Total Cost (£)')
ax3.set_title("by course type")
# add values as labels to column bars
ax3.bar_label(tot_per_course_type_bars)
# alternative way to add labels to column bars:
#for i in range(len(levels)):
#    ax3.text(i, tot_per_course_type[i], tot_per_course_type[i], ha = 'center')    

# 4th plot: total training cost by recommendation (Yes, No)
# calculate the totals
tot_recommendation = sumif(abc_training_costs[1:, 3], 'Yes', abc_training_costs[1:, 4].astype(int))
tot_not_recommended = sumif(abc_training_costs[1:, 3], 'No', abc_training_costs[1:, 4].astype(int))
# initialising the headings and the data
recommendation = np.array(['Yes', 'No']) 
tot_per_recommendation = np.array([tot_recommendation, tot_not_recommended])
# draw the fourth plot with axis labels and title
ax4 = plt.subplot(2, 2, 4)
tot_per_recommendation_bars = ax4.bar(recommendation, tot_per_recommendation)
ax4.set_xlabel('Recommendation')
ax4.set_ylabel('Total Cost (£)')
ax4.set_title("by recommendation")
# add values as labels to column bars
ax4.bar_label(tot_per_recommendation_bars)
# alternative way to add values as labels to column bars:
#for i in range(len(recommendation)):
#    ax4.text(i, tot_per_recommendation[i], tot_per_recommendation[i], ha = 'center')    

# set the title for the entire figure ('super title')
plt.suptitle("ABC's total training cost")
# display the plot
plt.show()



# Question 10
# -----------
"""
The sample data from questions 2 & 3 are stored in the file abc_shares_data.
a) perform the task in the same scenario as in question 2 by
   loading the data needed for the plot from the file abc_shares_data
   into a NumPy array
b) perform the task in the same scenario as in question 3 by
   loading the data needed for the plot from the file abc_shares_data
   into a NumPy array
c) perform the task in the same scenario as in question 4 by
   loading the data needed for the plot from the file abc_shares_data
   into a NumPy array
Note: the file abc_shares_data is just a sample. The solutions 
      must work for any number of rows and columns.
Tip: Questions 10b and 10c can be done in two ways:
     1. Using a list of arrays:
        In Question 10b extract data for each day, convert them to float data type
        and store them in a list of arrays 'days_data', so that
        index 0 corresponds to data array for day1,
        index 1 corresponds to data array for day2, ...
        index N-1 corresponds to data array for dayN (N=num_rows)
        In Question 10c extract data for each point during the day, convert them to float data type
        and store them in a list of arrays 'day_points_data', so that
        index 0 corresponds to data array for open,
        index 1 corresponds to data array for high, 
        index 2 corresponds to data array for low, 
        index 3 corresponds to data array for close (in general N, where N=num_cols)
     2. Find out how the exec() function works and use it in question
        10b to execute the statement to populate arrays for day1 - day5,
        and in question 10c to execute the statement to populate arrays
        for day_point1 data (open) to day_point4 data (close).
Implement the solution for questions 10b and 10c in both ways.
"""
# Common tasks for all 3 solutions: 10a, 10b, 10c & for solutions to questions 11 - 15:
# import data from the file 'abc_shares_data.txt' to numpy array 'abc_shares_data'
currentDirectoryPath = os.getcwd()
filePath = currentDirectoryPath + '\\abc_shares_data.txt'
abc_shares_data = np.loadtxt(filePath, delimiter=',', dtype=str)
# store the number of rows and the number of columns of the array
num_rows = abc_shares_data.shape[0]
num_cols = abc_shares_data.shape[1]

# solution 10a
# ------------
# initialising the headings
# extract elements from the 1st row (with index 0) sliced from index 1 to index num_cols-1
points = abc_shares_data[0, 1:num_cols]
# initialising the data
# from the second row (indexed 1)
# extract elements sliced from index 1 to index 4 (num_cols-1)
# compose the statement day1 = abc_shares_data[row_index, 1:num_cols]
day1 = abc_shares_data[1, 1:num_cols]
# convert values in array day1 from str to float
day1 = day1.astype(float)
# plotting the data
plt.plot(points, day1)
# adding the title
plt.title("ABC Shares values\non 02-08-2021")
# adding the labels
plt.xlabel("Points")
plt.ylabel("Value (£)")
plt.show()


# solution 10b - using the list of arrays
# ---------------------------------------
# initialising the headings
# extract elements from the 1st row (with index 0) sliced from index 1 to index 4
points = abc_shares_data[0, 1:num_rows]
# initialising the data
# from each of the remaining rows (indexed 1 to num_rows-1)
# extract elements sliced from index 1 to index num_cols-1
days_data = []
for row_index in range(1,num_rows):
    # extract data for each day, convert them to float data type
    # and store them in a list of arrays 'days_data', so that
    # index 0 corresponds to data array for day1,
    # index 1 corresponds to data array for day2, ...
    # index N-1 corresponds to data array for dayN (N=num_rows)
    days_data.append(abc_shares_data[row_index, 1:num_cols].astype(float))
# plotting the data
fig, ax = plt.subplots()
# extract the dates for the labels
# from the first column (indexed 0) extract elements
# sliced from index 1 to index num_rows-1
dates = abc_shares_data[1:num_rows, 0]
# create a plot for each day
# (labelling each line plot will also include the label to the legend)
for day_index in range(len(days_data)):
    day_plot = ax.plot(points, days_data[day_index], label=dates[day_index])
# adding the title
ax.set_title("ABC Shares values by day\non w/c 02-08-2021")
# adding the labels
ax.set_xlabel("Points")
ax.set_ylabel("Value (£)")
ax.legend(title='Dates:', loc='upper right') 
plt.show()


# solution 10c - using the list of arrays
# ---------------------------------------
# initialising the headings
# extract elements from the 1st column (with index 0) sliced from index 1 to index num_rows-1
days = abc_shares_data[1:num_rows, 0]
# initialising the data
# from each of the remaining columns (indexed 1 to num_cols-1)
# extract elements sliced from index 1 to index num_rows-1
day_points_data=[]
for col_index in range(1,num_cols):   
    # extract data for each point during the day, convert them to float data type
    # and store them in a list of arrays 'day_points_data', so that
    # index 0 corresponds to data array for open,
    # index 1 corresponds to data array for high, 
    # index 2 corresponds to data array for low, 
    # index 3 corresponds to data array for close (in general N, where N=num_cols)
    day_points_data.append(abc_shares_data[1:num_rows, col_index].astype(float))
# extract the points for the labels
# from the first row (indexed 0) extract elements
# sliced from index 1 to index num_cols-1
day_points = abc_shares_data[0, 1:num_cols]
# plotting the data
fig, ax = plt.subplots()
# create a plot for each day-point
# (labelling each line plot will also include the label to the legend)
for day_point_index in range(len(day_points_data)):
    day_point_plot = ax.plot(days, day_points_data[day_point_index], label=day_points[day_point_index])
# adding the title
ax.set_title("ABC Shares values by point\non w/c 02-08-2021")
# adding the labels
ax.set_xlabel("Dates")
ax.set_ylabel("Value (£)")
ax.legend(title='Points:', loc='upper left') 
plt.show()


# solution 10b - using the exec() function
# ----------------------------------------
# initialising the headings
# extract elements from the 1st row (with index 0) sliced from index 1 to index 4
points = abc_shares_data[0, 1:num_rows]
# initialising the data
# from each of the remaining rows (indexed 1 to num_rows-1)
# extract elements sliced from index 1 to index num_cols-1
for row_index in range(1,num_rows):
    # compose the statements to extract data for each day:
    # day1 = abc_shares_data[row_index, 1:num_cols] to
    # day5 = abc_shares_data[row_index, 1:num_cols]
    statement = 'day' + str(row_index) + ' = abc_shares_data[row_index, 1:num_cols]'
    exec(statement)
    # compose the statements day1 = day1.astype(float) to day5 = day5.astype(float)
    # to convert values in arrays day1 - day5 from str to float
    statement = 'day' + str(row_index) + ' = day' + str(row_index) + '.astype(float)'
    exec(statement)
# plotting the data
fig, ax = plt.subplots()
# extract the dates for the labels
# from the first column (indexed 0) extract elements
# sliced from index 1 to index num_rows-1
dates = abc_shares_data[1:num_rows, 0]
# labelling each line plot will also include the label to the legend
day1_plot = ax.plot(points, day1, label=dates[0])
day2_plot = ax.plot(points, day2, label=dates[1])
day3_plot = ax.plot(points, day3, label=dates[2])
day4_plot = ax.plot(points, day4, label=dates[3])
day5_plot = ax.plot(points, day5, label=dates[4])
# adding the title
ax.set_title("ABC Shares values by day\non w/c 02-08-2021")
# adding the labels
ax.set_xlabel("Points")
ax.set_ylabel("Value (£)")
ax.legend(title='Dates:', loc='upper right') 
plt.show()


# solution 10c - using the exec() function
# ----------------------------------------
# initialising the headings
# extract elements from the 1st column (with index 0) sliced from index 1 to index num_rows-1
days = abc_shares_data[1:num_rows, 0]
# initialising the data
# from each of the remaining columns (indexed 1 to num_cols-1)
# extract elements sliced from index 1 to index num_rows-1
for col_index in range(1,num_cols):
    # compose the statements to extract data for points during the day:
    # data_day_point1 = abc_shares_data[1:num_rows, col_index] to
    # data_day_point4 = abc_shares_data[1:num_rows, col_index]
    # data_day_point1 for 'open'; data_day_point2 for 'high',
    # data_day_point3 for 'low'; data_day_point4 for 'close'
    statement = 'data_day_point' + str(col_index) + ' = abc_shares_data[1:num_rows, col_index]'
    exec(statement)
    # compose the statements to convert values in arrays
    # data_day_point1 - data_day_point4 from str to float:
    # data_day_point1 = data_day_point1.astype(float) to
    # day_point_data4 = day_point_data4.astype(float)
    statement = 'data_day_point' + str(col_index) + ' = data_day_point' + str(col_index) + '.astype(float)'
    exec(statement)
# extract the points for the labels
# from the first row (indexed 0) extract elements
# sliced from index 1 to index num_cols-1
day_points = abc_shares_data[0, 1:num_cols]
# plotting the data
fig, ax = plt.subplots()
# create a plot for each day-point
# (labelling each line plot will also include the label to the legend)
for col_index in range(1,num_cols):
    statement = "day_point_plot = ax.plot(days, data_day_point" + str(col_index) + ", label=day_points[col_index-1])"
    exec(statement)
# adding the title
ax.set_title("ABC Shares values by point\non w/c 02-08-2021")
# adding the labels
ax.set_xlabel("Dates")
ax.set_ylabel("Value (£)")
ax.legend(title='Points:', loc='upper left') 
plt.show()



# Question 11
# -----------
"""
Modify the Python program produced for question 5 to read
data from the file abc_shares_data into a NumPy array and to
generalise the solution to work for any number of rows and
columns, using the list of arrays, as done in question 10c.
"""
# solution 11:
# initialising the headings
# extract elements from the 1st column (with index 0) sliced from index 1 to index num_rows-1
days = abc_shares_data[1:num_rows, 0]
# initialising the data
# from each of the remaining columns (indexed 1 to num_cols-1)
# extract elements sliced from index 1 to index num_rows-1
day_points_data=[]
for col_index in range(1,num_cols):   
    # extract data for each point during the day, convert them to float data type
    # and store them in a list of arrays 'day_points_data', so that
    # index 0 corresponds to data array for open,
    # index 1 corresponds to data array for high, 
    # index 2 corresponds to data array for low, 
    # index 3 corresponds to data array for close (in general N, where N=num_cols)
    day_points_data.append(abc_shares_data[1:num_rows, col_index].astype(float))
# extract the points for the labels
# from the first row (indexed 0) extract elements
# sliced from index 1 to index num_cols-1
day_points = abc_shares_data[0, 1:num_cols]
no_days = len(days)
index = np.arange(no_days)
# plotting the data
fig, ax = plt.subplots()
bar_width = 0.20
# create a column bar for each day-point
# (labelling each column plot will also include the label to the legend)
for day_point_index in range(len(day_points_data)):
    bars_day_point = ax.bar(index + (day_point_index) * bar_width, day_points_data[day_point_index], bar_width, label=day_points[day_point_index])
# adding the title
ax.set_title("ABC Shares values by point\non w/c 02-08-2021")
# adding the labels
ax.set_xlabel("Dates")
ax.set_ylabel("Value (£)")
ax.legend(title='Points:', loc='upper left')
ax.set_xticks(index + 1.5*bar_width)
# The limits on the y-axis can be changed using the set_ylim() function: ax.set_ylim([ymin,ymax])
ax.set_ylim([550,590])
ax.set_xticklabels((days[0], days[1], days[2], days[3], days[4]))
# adjust the figure area and show the plot
fig.tight_layout()
plt.show()



# Question 12
# -----------
"""
Modify the Python program produced for question 5 to read
data from the file abc_shares_data into a NumPy array and
to generalise the solution to work for any number of rows
and columns, using the exec() function, as done in question 10c.
"""
# solution 12:
# initialising the headings
# extract elements from the 1st column (with index 0) sliced from index 1 to index num_rows-1
days = abc_shares_data[1:num_rows, 0]
# initialising the data
# from each of the remaining columns (indexed 1 to num_cols-1)
# extract elements sliced from index 1 to index num_rows-1
for col_index in range(1,num_cols):
    # compose the statements to extract data for points during the day:
    # data_day_point1 = abc_shares_data[1:num_rows, col_index] to
    # data_day_point4 = abc_shares_data[1:num_rows, col_index]
    # data_day_point1 for 'open'; data_day_point2 for 'high',
    # data_day_point3 for 'low'; data_day_point4 for 'close'
    statement = 'data_day_point' + str(col_index) + ' = abc_shares_data[1:num_rows, col_index]'
    exec(statement)
    # compose the statements to convert values in arrays
    # data_day_point1 - data_day_point4 from str to float:
    # data_day_point1 = data_day_point1.astype(float) to
    # day_point_data4 = day_point_data4.astype(float)
    statement = 'data_day_point' + str(col_index) + ' = data_day_point' + str(col_index) + '.astype(float)'
    exec(statement)
# extract the points for the labels
# from the first row (indexed 0) extract elements
# sliced from index 1 to index num_cols-1
day_points = abc_shares_data[0, 1:num_cols]
# plotting the data
fig, ax = plt.subplots()
no_days = len(days)
index = np.arange(no_days)
bar_width = 0.20
# create a column plot for each day-point
# (labelling each column plot will also
# include the label to the legend)
for col_index in range(1,num_cols):
    statement = "day_point_plot" + str(col_index) + " = ax.bar(index + (col_index-1) * bar_width, data_day_point" + str(col_index) + ", bar_width, label=day_points[" + str(col_index-1) + "])"
    exec(statement)
# adding the title
ax.set_title("ABC Shares values by point\non w/c 02-08-2021")
# adding the labels
ax.set_xlabel("Dates")
ax.set_ylabel("Value (£)")
ax.legend(title='Points:', loc='upper left')
# By default (without calling the set_xticks() function,
# or if the argument index is passed to the set_xticks() function),
# the first tick will be positioned at half of the width of the
# first ('open') bar - here 0.10 because the bar width is set to 0.20.
# The distance between ticks from that point on is the same as they are
# positioned at half of each ('open') bar's width. To move the ticks right
# between the 2nd (high) and 3rd (low) bars, the argument passed to set_xticks()
# function is: index + 1.5*bar_width
ax.set_xticks(index + 1.5*bar_width)
# The limits on the y-axis can be changed using the set_ylim() function: ax.set_ylim([ymin,ymax])
ax.set_ylim([550,590])
ax.set_xticklabels((days[0], days[1], days[2], days[3], days[4]))
fig.tight_layout()
plt.show()



# Question 13
# ----------
"""
Modify the Python program produced for question 6 to load data
from the file abc_shares_data into a NumPy array and to generalise
the solution to work for any number of rows and columns.
Assume that the file abc_shares_data lists dates in the 1st column,
open values in the 2nd column, and close values in the last column.
Note: Since question 13 (as question 6) requires data for two
      day-points only: 'open' and 'close', there is no need to 
      involve the exec() function or use the list of arrays to 
      store data for each day-point. Simply extract data from the
      1st and the last column of the array.
"""
# solution 13
# initialising the headings
# extract elements from the 1st column (with index 0) sliced from index 1 to index num_rows-1
days = abc_shares_data[1:num_rows, 0]
# just extract data from the 1st and the last column
open_values  = abc_shares_data[1:num_rows, 1].astype(float)
close_values = abc_shares_data[1:num_rows, num_cols-1].astype(float)
# calculate the stock's return values
stock_return_values = (open_values - close_values) / open_values
# plotting the data
fig, ax = plt.subplots()
bar_width = 0.40
# create a column bar for each day
stock_return_bars = ax.bar(days, stock_return_values, bar_width)
# add the title
ax.set_title("ABC Stock's Return values\non w/c 02-08-2021")
# add the labels
ax.set_xlabel("Dates")
ax.set_ylabel("Stock's Return Value (£)")
# add values as labels to column bars
ax.bar_label(stock_return_bars, padding=3)
# adjust the figure area and show the plot
fig.tight_layout()
plt.show()



# Question 14
# -----------
"""
Modify the Python programs produced for questions 7a and 7b
to load data from the file abc_shares_data into a NumPy
array and to generalise the solution to work for any number
of rows and columns, using the exec()  function for the
first plot, as done in question 11. For the second plot
extract data from the 1st and the last column of the array
as done in question 13.
"""
# solution 14a - using the subplots() function:
# ---------------------------------------------
# 1st plot: ABC Shares values by point on w/c 02-08-2021
# initialising the data
# from each of the remaining columns (indexed 1 to num_cols-1)
# extract elements sliced from index 1 to index num_rows-1
day_points_data=[]
for col_index in range(1,num_cols):   
    # extract data for each point during the day, convert them to float data type
    # and store them in a list of arrays 'day_points_data', so that
    # index 0 corresponds to data array for open,
    # index 1 corresponds to data array for high, 
    # index 2 corresponds to data array for low, 
    # index 3 corresponds to data array for close (in general N, where N=num_cols)
    day_points_data.append(abc_shares_data[1:num_rows, col_index].astype(float))
# extract the points for the labels
# from the first row (indexed 0) extract elements
# sliced from index 1 to index num_cols-1
day_points = abc_shares_data[0, 1:num_cols]
no_days = len(days)
index = np.arange(no_days)
# plotting the data
fig, ax = plt.subplots(1, 2, figsize=(15, 6))
bar_width = 0.20
# create a column bar for each day-point
# (labelling each column plot will also include the label to the legend)
for day_point_index in range(len(day_points_data)):
    bars_day_point = ax[0].bar(index + (day_point_index) * bar_width, day_points_data[day_point_index], bar_width, label=day_points[day_point_index])
# adding the title
ax[0].set_title("ABC Shares values by point\non w/c 02-08-2021")
# adding the labels
ax[0].set_xlabel("Dates")
ax[0].set_ylabel("Value (£)")
ax[0].legend(title='Points:', loc='upper left')
ax[0].set_xticks(index + 1.5*bar_width)
# The limits on the y-axis can be changed using the set_ylim() function: ax.set_ylim([ymin,ymax])
ax[0].set_ylim([550,590])
ax[0].set_xticklabels((days[0], days[1], days[2], days[3], days[4]))

# 2nd plot: ABC Stock's Return values on w/c 02-08-2021
# initialising the data
# extract days - elements from the 1st column (with index 0)
# sliced from index 1 to index num_rows-1
days = abc_shares_data[1:num_rows, 0]
# just extract data from the 1st and the last column
open_values  = abc_shares_data[1:num_rows, 1].astype(float)
close_values = abc_shares_data[1:num_rows, num_cols-1].astype(float)
# calculate the stock's return values
stock_return_values = (open_values - close_values) / open_values
# create a column bar for each day
stock_return_bars = ax[1].bar(days, stock_return_values, bar_width)
# add the title
ax[1].set_title("ABC Stock's Return values\non w/c 02-08-2021")
# add the labels
ax[1].set_xlabel("Dates")
ax[1].set_ylabel("Stock's Return Value (£)")
# add values as labels to column bars
ax[1].bar_label(stock_return_bars, padding=3)

# adjust the figure area and show the plot
fig.tight_layout()
plt.show()


# solution 14b - using the subplot() function:
# ---------------------------------------------
# first make the figure
fig = plt.figure(figsize=(15, 6))
# now create each subplot individually
# 1st plot: ABC Shares values by point on w/c 02-08-2021
# initialising the data
# from each of the remaining columns (indexed 1 to num_cols-1)
# extract elements sliced from index 1 to index num_rows-1
day_points_data=[]
for col_index in range(1,num_cols):   
    # extract data for each point during the day, convert them to float data type
    # and store them in a list of arrays 'day_points_data', so that
    # index 0 corresponds to data array for open,
    # index 1 corresponds to data array for high, 
    # index 2 corresponds to data array for low, 
    # index 3 corresponds to data array for close (in general N, where N=num_cols)
    day_points_data.append(abc_shares_data[1:num_rows, col_index].astype(float))
# extract the points for the labels
# from the first row (indexed 0) extract elements
# sliced from index 1 to index num_cols-1
day_points = abc_shares_data[0, 1:num_cols]
no_days = len(days)
index = np.arange(no_days)
bar_width = 0.20
# create the first plot
ax1 = plt.subplot(1, 2, 1)
# create a column bar for each day-point
# (labelling each column plot will also include the label to the legend)
for day_point_index in range(len(day_points_data)):
    bars_day_point = ax1.bar(index + (day_point_index) * bar_width, day_points_data[day_point_index], bar_width, label=day_points[day_point_index])
    # This is equivalent to:
    #open_bars  = ax1.bar(index + 0 * bar_width, bars_day_point1, bar_width, label=day_points[0])
    #high_bars  = ax1.bar(index + 1 * bar_width, bars_day_point2, bar_width, label=day_points[1])
    #low_bars   = ax1.bar(index + 2 * bar_width, bars_day_point3, bar_width, label=day_points[2])
    #close_bars = ax1.bar(index + 3 * bar_width, bars_day_point4, bar_width, label=day_points[3])
    # but will work for as many day-points there may be.
# adding the title
ax1.set_title("ABC Shares values by point\non w/c 02-08-2021")
# adding the labels
ax1.set_xlabel("Dates")
ax1.set_ylabel("Value (£)")
ax1.legend(title='Points:', loc='upper left')
# add the x axis tick values, which are the locations
# along the x-axis where the tick marks appear:
# Note: if index was the argument to the set_xticks() function, the first tick (for the value 0)
# would be positioned half way between the width of the first bar; this is the default position of 0.
# Since our plot has four bars, we want to move the ticks so that they appear right between the
# 2nd and 3rd bar of each group - to achieve that we need to pass the value index + 1.5*bar_width
# to the set_xticks() function, setting the ticks to: 0.30, 1.30, 2.30, 3.30, 4.30.
ax1.set_xticks(index + 1.5*bar_width)
# The limits on the y-axis can be changed using the set_ylim() function: ax.set_ylim([ymin,ymax])
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim
ax1.set_ylim([550,590])
ax1.set_xticklabels((days[0], days[1], days[2], days[3], days[4]))

# 2nd plot: ABC Stock's Return values on w/c 02-08-2021
# initialising the data
# extract days - elements from the 1st column (with index 0)
# sliced from index 1 to index num_rows-1
days = abc_shares_data[1:num_rows, 0]
# just extract data from the 1st and the last column
open_values  = abc_shares_data[1:num_rows, 1].astype(float)
close_values = abc_shares_data[1:num_rows, num_cols-1].astype(float)
# calculate the stock's return values
stock_return_values = (open_values - close_values) / open_values
# create the second plot
ax2 = plt.subplot(1, 2, 2)
# create a column bar for each day
stock_return_bars = ax2.bar(days, stock_return_values, bar_width)
# add the title
ax2.set_title("ABC Stock's Return values\non w/c 02-08-2021")
# add the labels
ax2.set_xlabel("Dates")
ax2.set_ylabel("Stock's Return Value (£)")
# add values as labels to column bars
ax2.bar_label(stock_return_bars, padding=3)
# adjust the figure area and show the plot
fig.tight_layout()
plt.show()



# Question 15
# -----------
"""
Modify the Python programs produced for questions 7a and 7b
to load data from the file abc_shares_data into a NumPy
array and to generalise the solution to work for any number
of rows and columns, using the exec() function for the
first plot, as done in question 12. For the second plot
extract data from the 1st and the last column of the array
as done in question 13.
"""
# solution 15a - using the subplots() function:
# ---------------------------------------------
# 1st plot: ABC Shares values by point on w/c 02-08-2021
# initialising the data
# from each of the remaining columns (indexed 1 to num_cols-1)
# extract elements sliced from index 1 to index num_rows-1
for col_index in range(1,num_cols):
    # compose the statements to extract data for points during the day:
    # data_day_point1 = abc_shares_data[1:num_rows, col_index] to
    # data_day_point4 = abc_shares_data[1:num_rows, col_index]
    # data_day_point1 for 'open'; data_day_point2 for 'high',
    # data_day_point3 for 'low'; data_day_point4 for 'close'
    statement = 'data_day_point' + str(col_index) + ' = abc_shares_data[1:num_rows, col_index]'
    exec(statement)
    # compose the statements to convert values in arrays
    # data_day_point1 - data_day_point4 from str to float:
    # data_day_point1 = data_day_point1.astype(float) to
    # day_point_data4 = day_point_data4.astype(float)
    statement = 'data_day_point' + str(col_index) + ' = data_day_point' + str(col_index) + '.astype(float)'
    exec(statement)
# extract the points for the labels
# from the first row (indexed 0) extract elements
# sliced from index 1 to index num_cols-1
day_points = abc_shares_data[0, 1:num_cols]
no_days = len(days)
index = np.arange(no_days)
# plotting the data
fig, ax = plt.subplots(1, 2, figsize=(15, 6))
bar_width = 0.20
# create a column bar for each day point
# (labelling each column plot will also
# include the label to the legend)
for col_index in range(1,num_cols):
    statement = "bars_day_point" + str(col_index) + " = ax[0].bar(index + (col_index-1) * bar_width, data_day_point" + str(col_index) + ", bar_width, label=day_points[" + str(col_index-1) + "])"
    exec(statement)
    # This is equivalent to:
    #open_bars  = ax[0].bar(index + 0 * bar_width, bars_day_point1, bar_width, label=day_points[0])
    #high_bars  = ax[0].bar(index + 1 * bar_width, bars_day_point2, bar_width, label=day_points[1])
    #low_bars   = ax[0].bar(index + 2 * bar_width, bars_day_point3, bar_width, label=day_points[2])
    #close_bars = ax[0].bar(index + 3 * bar_width, bars_day_point4, bar_width, label=day_points[3])
    # but will work for as many day points there may be.
# adding the title
ax[0].set_title("ABC Shares values by point\non w/c 02-08-2021")
# adding the labels
ax[0].set_xlabel("Dates")
ax[0].set_ylabel("Value (£)")
ax[0].legend(title='Points:', loc='upper left')
ax[0].set_xticks(index + 1.5*bar_width)
# The limits on the y-axis can be changed using the set_ylim() function: ax.set_ylim([ymin,ymax])
ax[0].set_ylim([550,590])
ax[0].set_xticklabels((days[0], days[1], days[2], days[3], days[4]))

# 2nd plot: ABC Stock's Return values on w/c 02-08-2021
# initialising the data
# extract days - elements from the 1st column (with index 0)
# sliced from index 1 to index num_rows-1
days = abc_shares_data[1:num_rows, 0]
# just extract data from the 1st and the last column
open_values  = abc_shares_data[1:num_rows, 1].astype(float)
close_values = abc_shares_data[1:num_rows, num_cols-1].astype(float)
# calculate the stock's return values
stock_return_values = (open_values - close_values) / open_values
# create the second plot
ax2 = plt.subplot(1, 2, 2)
# create a column bar for each day
stock_return_bars = ax2.bar(days, stock_return_values, bar_width)
# add the title
ax2.set_title("ABC Stock's Return values\non w/c 02-08-2021")
# add the labels
ax2.set_xlabel("Dates")
ax2.set_ylabel("Stock's Return Value (£)")
# add values as labels to column bars
ax2.bar_label(stock_return_bars, padding=3)
# adjust the figure area and show the plot
fig.tight_layout()
plt.show()


# solution 15b - using the subplot() function:
# ---------------------------------------------
# first make the figure
fig = plt.figure(figsize=(15, 6))
# now create each subplot individually
# 1st plot: ABC Shares values by point on w/c 02-08-2021
# initialising the data
# from each of the remaining columns (indexed 1 to num_cols-1)
# extract elements sliced from index 1 to index num_rows-1
for col_index in range(1,num_cols):
    # compose the statements to extract data for points during the day:
    # data_day_point1 = abc_shares_data[1:num_rows, col_index] to
    # data_day_point4 = abc_shares_data[1:num_rows, col_index]
    # data_day_point1 for 'open'; data_day_point2 for 'high',
    # data_day_point3 for 'low'; data_day_point4 for 'close'
    statement = 'data_day_point' + str(col_index) + ' = abc_shares_data[1:num_rows, col_index]'
    exec(statement)
    # compose the statements to convert values in arrays
    # data_day_point1 - data_day_point4 from str to float:
    # data_day_point1 = data_day_point1.astype(float) to
    # day_point_data4 = day_point_data4.astype(float)
    statement = 'data_day_point' + str(col_index) + ' = data_day_point' + str(col_index) + '.astype(float)'
    exec(statement)
# extract the points for the labels
# from the first row (indexed 0) extract elements
# sliced from index 1 to index num_cols-1
day_points = abc_shares_data[0, 1:num_cols]
no_days = len(days)
index = np.arange(no_days)
bar_width = 0.20
# create the first plot
ax1 = plt.subplot(1, 2, 1)
# create a column bar for each day point
# (labelling each column plot will also
# include the label to the legend)
for col_index in range(1,num_cols):
    statement = "bars_day_point" + str(col_index) + " = ax1.bar(index + (col_index-1) * bar_width, data_day_point" + str(col_index) + ", bar_width, label=day_points[" + str(col_index-1) + "])"
    exec(statement)
    # This is equivalent to:
    #open_bars  = ax1.bar(index + 0 * bar_width, bars_day_point1, bar_width, label=day_points[0])
    #high_bars  = ax1.bar(index + 1 * bar_width, bars_day_point2, bar_width, label=day_points[1])
    #low_bars   = ax1.bar(index + 2 * bar_width, bars_day_point3, bar_width, label=day_points[2])
    #close_bars = ax1.bar(index + 3 * bar_width, bars_day_point4, bar_width, label=day_points[3])
    # but will work for as many day points there may be.
# adding the title
ax1.set_title("ABC Shares values by point\non w/c 02-08-2021")
# adding the labels
ax1.set_xlabel("Dates")
ax1.set_ylabel("Value (£)")
ax1.legend(title='Points:', loc='upper left')
# add the x axis tick values, which are the locations
# along the x-axis where the tick marks appear:
# Note: if index was the argument to the set_xticks() function, the first tick (for the value 0)
# would be positioned half way between the width of the first bar; this is the default position of 0.
# Since our plot has four bars, we want to move the ticks so that they appear right between the
# 2nd and 3rd bar of each group - to achieve that we need to pass the value index + 1.5*bar_width
# to the set_xticks() function, setting the ticks to: 0.30, 1.30, 2.30, 3.30, 4.30.
ax1.set_xticks(index + 1.5*bar_width)
# The limits on the y-axis can be changed using the set_ylim() function: ax.set_ylim([ymin,ymax])
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim
ax1.set_ylim([550,590])
ax1.set_xticklabels((days[0], days[1], days[2], days[3], days[4]))

# 2nd plot: ABC Stock's Return values on w/c 02-08-2021
# initialising the data
# extract days - elements from the 1st column (with index 0)
# sliced from index 1 to index num_rows-1
days = abc_shares_data[1:num_rows, 0]
# just extract data from the 1st and the last column
open_values  = abc_shares_data[1:num_rows, 1].astype(float)
close_values = abc_shares_data[1:num_rows, num_cols-1].astype(float)
# calculate the stock's return values
stock_return_values = (open_values - close_values) / open_values
# create the second plot
ax2 = plt.subplot(1, 2, 2)
# create a column bar for each day
stock_return_bars = ax2.bar(days, stock_return_values, bar_width)
# add the title
ax2.set_title("ABC Stock's Return values\non w/c 02-08-2021")
# add the labels
ax2.set_xlabel("Dates")
ax2.set_ylabel("Stock's Return Value (£)")
# add values as labels to column bars
ax2.bar_label(stock_return_bars, padding=3)
# adjust the figure area and show the plot
fig.tight_layout()
plt.show()

