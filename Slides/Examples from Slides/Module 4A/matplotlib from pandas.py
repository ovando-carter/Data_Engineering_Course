##########################
# Module 4A - Matplotlib #
##########################

# slides 33-35
# import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# obtain the data frame
# read all data stored as a csv file into a pandas DataFrame
df_sales = pd.read_csv('sales_by_customer_and_payment.csv')
print(df_sales)
# calculate total sales grouped by Customer Type & Payment Type
df_groupby = df_sales.groupby(['Customer Type', 'Payment Type']).sum()
print(df_groupby)
# split existing index into columns (Customer Type & Payment Type) and add default index
df_groupby_indexed = df_groupby.reset_index()
print(df_groupby_indexed)

# extract the necessary data for the plot
customer_types = df_groupby_indexed['Customer Type'].unique()
telephone_data = df_groupby_indexed.query("`Payment Type`=='Telephone'").iloc[:,2].to_numpy()
online_data = df_groupby_indexed.query("`Payment Type`=='Online'").iloc[:,2].to_numpy()
print(customer_types)
print(telephone_data)
print(online_data)

# draw the plot
no_customer_types = len(customer_types)
bar_width = 0.45
fig, ax = plt.subplots()
index = np.arange(no_customer_types)
telephone_bars = ax.bar(index, telephone_data, bar_width, label='telephone')
online_bars = ax.bar(index + bar_width, online_data, bar_width, label='online')

# label the plot
ax.set_xlabel('Customer Type')
ax.set_ylabel('Sale')
ax.set_title('Sale per customer type split by payment type')
# place the ticks between drink and food bars
ax.set_xticks(index + bar_width/2)
# set the tick labels (x-axis labels)
ax.set_xticklabels(customer_types)
# add values to telephone and online bars
ax.bar_label(telephone_bars, label_type='center')
ax.bar_label(online_bars, label_type='center')
# OR
#for container in ax.containers:
#    ax.bar_label(container, label_type='center')
# add the legend
ax.legend()

# display the plot
fig.tight_layout()
plt.show()



