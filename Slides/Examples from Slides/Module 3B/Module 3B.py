######################
# Module 3B - Pandas #
######################
import numpy as np
import pandas as pd

# display the currently installed Pandas version
print(pd.__version__)

# CREATING SERIES
# 1) from a list
# slide 11
names = ['John', 'Suzie', 'Paul', 'Leo', 'Ada', 'Evie']
names_series = pd.Series(names)
print(names_series)
print(type(names_series))  #<class 'pandas.core.series.Series'>

# 2) from a dictionary
# slide 12
calories = {"day1": 420, "day2": 380, "day3": 390, "day4": 390, "day5": 380}
calories_5_day_series = pd.Series(calories)
print(calories_5_day_series)

# 2) from an ndarray
# slide 13
week_days = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
week_days_series = pd.Series(week_days)
print(week_days_series)

# 2) from a scalar
# slide 14
scalar = 5
scalar_series = pd.Series(scalar, index=[0, 1, 2, 3])
print(scalar_series)

# slide 15 - accessing series' elements
# 1) Directly, iterating series' elements using loops
names = ['John', 'Suzie', 'Paul', 'Leo', 'Ada', 'Evie']
names_series = pd.Series(names)
for element in names_series:
    print(element)
    
# slide 16
# 2) Indirectly, iterating through series’ index, accessible with the subscript operator: [ ]
names = ['John', 'Suzie', 'Paul', 'Leo', 'Ada', 'Evie']
names_series = pd.Series(names)
print('names_series.index', names_series.index)
for index in names_series.index:
    print(names_series[index])
    
# slide 17
# 3) through slicing
print(names_series[1:3])
print(names_series[-2:])
print(names_series[:3])

# slide 18
# 4) Through a list of index label values
print(names_series[[2, 3, 4]])
print(names_series[[4, 0, 2]])
print(names_series[[1]])

# slide 19
# 5) Through Series' index and values attributes
print(names_series.index[0])  # returns index at position 0
print(names_series.values[0])  # returns the value in Series at index 0

calories = {"day1": 420, "day2": 380, "day3": 390, "day4": 390, "day5": 380}
calories_5_day_series = pd.Series(calories)
print(calories_5_day_series.index[3])  # day4
print(calories_5_day_series.values[3]) # 390

# slide 20 - Searchinig series
# where elements are unique:
target = 'Suzie'
for index in names_series.index:
    if names_series[index] == target:
        target_index = index
        break
print("target = %s, target_index = %d" % (target, target_index))

# slide 21
# find an element in Series with duplicate values – 1st method
genders = ['male', 'female', 'female', 'male', 'female']
gender_series = pd.Series(genders)
print(gender_series)
target = 'female'
target_indices = []
for index in gender_series.index:
         if gender_series[index] == target:
             target_indices.append(index)
print("target =", target, "; target_indices are", target_indices)

# slide 22
# Find an element in Series with duplicate values – 2nd method
genders = ['male', 'female', 'female', 'male', 'female']
gender_series = pd.Series(genders)
target = 'female'
target_indices = []
bool_target_indices = pd.Index(gender_series).get_loc(target)
print(bool_target_indices)
for index in range(len(bool_target_indices)):
    if bool_target_indices[index] == True:
        target_indices.append(index)
print("target =", target, "; target_indices are", target_indices)

# slide 23
# Find an element in Series with duplicate indices and duplicated values
indices = [1, 2, 2, 1, 2]
genders = ['male', 'female', 'female', 'male', 'female']
gender_series_with_dupl_indices = pd.Series(genders, index=indices)
print(gender_series_with_dupl_indices)
target = 'female'
index_range = gender_series_with_dupl_indices.index
target_indices = []
'''
for index in index_range:
   if gender_series_with_dupl_indices[index] == target: # throws ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
       target_indices.append(index)
'''
# slide 24
bool_target_indices = pd.Index(gender_series).get_loc(target)
print(bool_target_indices)
for index in range(len(bool_target_indices)):
    if bool_target_indices[index] == True:
       target_indices.append(index)
print("target =", target, "; target_indices are", target_indices)

# slide 25 - Applying string methods to Series
directions = pd.Series(['North', 'East', 'South', 'West'])
print(directions)
print(directions.str.len())
print(directions.str.upper())

# slide 26 - Accessing/Extracting sections from Series
directions_initials = directions.str[0]
print(directions_initials)
short_week_days_series = week_days_series.str[:3]
print(short_week_days_series)

# slide 27 - Naming Series
# at the point of creating Series:
named_week_days_series = pd.Series(week_days, name='week days')
print(named_week_days_series)

# slide 28
# after Series have been created:
# create the un-named series
scalar = 'string scalar'
scalar_series = pd.Series(scalar, index=[1, 2, 3])
print(scalar_series)
# name the series
scalar_series.name = 'scalar'
print(scalar_series)

# slide 29
print(named_week_days_series)
# rename series:
named_week_days_series.name = 'Mon-Fri'
print(named_week_days_series)

# slide 30 - Concatenating Series
se_pl_1 = pd.Series(['Python', 'Java', 'R'])
se_pl_2 = pd.Series(['C', 'C++', 'C#'])
# pass the two seriers to contact() function within a list:
concat_series = pd.concat([se_pl_1, se_pl_2])
print(concat_series)
print(type(concat_series))  # <class 'pandas.core.series.Series'>

# slide 31
# pd.concat([se_pl_1, se_pl_2]) is equivalent to:
# pd.concat([se_pl_1, se_pl_2], axis=0)
# passing axis=1, creates a DataFrame
df_concat_series_into_dataframe = pd.concat([se_pl_1, se_pl_2], axis=1)
print(df_concat_series_into_dataframe)
print(type(df_concat_series_into_dataframe)) # <class 'pandas.core.frame.DataFrame'>

# DATA FRAMES

# Creating DataFrame
# slide 34
# 1. Creating a DataFrame from a list of tuples
# Each tuple represents a row; 
# column headers can be added when creating the DataFrame
students_list = [('Jack', 34, 'Sydney', 'Australia'),
                 ('Rita', 30, 'Delhi', 'India'),
                 ('Tom', 31, 'Mumbai', 'India'),
                 ('Neelu', 32, 'Bangalore', 'India'),
                 ('John', 16, 'New York', 'US'),
                 ('Mike', 17, 'Las Vegas', 'US')]
df_students_1 = pd.DataFrame(students_list, columns=['Name', 'Age', 'City', 'Country'])
print(df_students_1)

# slide 36
# 2. Creating a DataFrame from a dictionary of lists
# The dictionary keys are used as column headers and
# the values in each list as columns of the DataFrame
students_dict = {'Name':['Jack','Rita','Tom','Neelu','John','Mike'],
                       'Age':[34,30,31,32,16,17],
                       'City':['Sydney','Delhi','Mumbai','Bangalore','New York',
                               'Las Vegas'],
                       'Country':['Australia','India','India','India','US','US']}

df_students_2 = pd.DataFrame(students_dict)
print(type(df_students_2))  # <class 'pandas.core.frame.DataFrame'>
print('df_students_2:\n', df_students_2)

# slide 38
# 3. Creating a DataFrame from a NumPy ndarray
# The number of array elements at dimension 1 determines
# the number of rows of the DataFrame
# The number of array elements at dimension 2 determines
# the number of columns of the DataFrame
# Column headers can be added using the 'columns' kwarg
df_person_details = pd.DataFrame(np.array([['John', 23, 1.80, 72],
                                           ['Suzie', 40, 1.70, 60],
                                           ['Paul', 35, 1.86, 90]]),
                                 columns=['name', 'age', 'height', 'weight'])
df_person_details = pd.DataFrame(df_person_details)
print(type(df_person_details))
print('df_person_details:\n', df_person_details)

# slide 39
# By default, all values in NumPy array are of 'object'
# data type if at least one value is non-numerical
# (here 'name')
print("Data Types in df_person_details:\n", df_person_details.dtypes, sep='')

# slide 40
# To convert all values in one numeric column into numbers
# use to_numeric() Pandas function this way:
df_person_details['age'] = pd.to_numeric(df_person_details['age'])
print(df_person_details.dtypes)
# To convert data type of multiple numeric columns into
# numbers at once, use the apply() DataFrame function with
# to_numeric Pandas function (passing to_numeric without
# brackets):
df_person_details[['age', 'height', 'weight']] = df_person_details[['age', 'height', 'weight']].apply(pd.to_numeric)
print(df_person_details.dtypes)
# Note:
# Note: To convert values to date data type,
# use the Pandas function pd.to_datetime()

# slide 41
# If some values in DataFrame are non-numeric, include the
# errors='ignore' kwarg to the apply() function call
# (invalid parsing will return the original input)
df_person_details = pd.DataFrame(np.array([['John', 23, 1.80, 72],
                                           ['Suzie', 40, 1.70, True],
                                           ['Paul', 35, 'string', 90]]),
                                 columns=['name', 'age', 'height', 'weight'])
df_person_details = pd.DataFrame(df_person_details)
df_person_details[['age', 'height', 'weight']] = df_person_details[['age', 'height', 'weight']].apply(pd.to_numeric, errors='ignore')
print(df_person_details.dtypes)
# Note (see example from notes section on slide 39 as
# illustration) for the following points:
# - trying to convert the above array to a data frame
#   would throw an error, because of the value 'string'
# - Boolean values would not throw an error but would
#   prevent conversion
# - Empty values (None) will be displayed as NaN
#   (Not a Number), ignored and conversion will take place

# slide 42
# 4. Creating a DataFrame from a Series
# Each Series represents a column; column headers can be
# added when creating the DataFrame.
names = ['John', 'Suzie', 'Paul']
names_series = pd.Series(names)
df_names = pd.DataFrame(names_series, columns=['Name']) 
print('df_names:\n', df_names)
print(type(df_names))  #  <class 'pandas.core.frame.DataFrame'>

# slide 43
# 5. Creating a DataFrame from  a csv or txt file
# Values from each column in the file represent a column
# in a DataFrame.
# If headings are present in the first row if the file,
# they will be automatically used as column names
# If headings are not present in the first row if the file,
# the DataFrame will be created without column names
df_planets = pd.read_csv('planets.csv')
print('df_planets:\n ', df_planets)
# Note: 
# Use the following lines of code to display the
# untruncated DataFrame:
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
print('df_planets:\n ', df_planets)

# slide 45
# 1. Listing column names of a DataFrame
# There are 3 ways to display the column names of a DataFrame:
# 1) using the columns DataFrame attribute
print(df_planets.columns)
# 2) using the columns.values DataFrame attribute
print(df_planets.columns.values)
# 3) converting the output of the columns DataFrame attribute to list:
print(df_planets.columns.tolist())

# slide 48
# 2. Retrieving specific column name(s) from the DataFrame
# Applying the subscript operator to the columns attribute,
# specifying the index of the column (indexes starts from 0)
print(df_planets.columns[0])  # prints 'planet'
# Slicing can be used to retrieve a specific subset of columns
print(df_planets.columns[:3])  # Index(['planet', 'mass', 'diameter'], dtype='object')
print(df_planets.columns[-2:]) #  Index(['has_ring_system', 'has_global_magnetic_field'], dtype='object')

# slide 49
# 3. Re-naming indices and columns in a data frame
# Task: Rename the first column of df_students_1
# and the first three row indices
df_students_2_new = df_students_2.rename(columns={'Name': 'First Name'}, index={0: 'zero', 1: 'one', 2: 'two'})
print(df_students_2_new)

# slide 50
# 4. Setting the index title of a data frame
df_students_2_new.index.name = "Index"
print(df_students_2_new)

# slide 51 - Vertical Slicing (selecting columns)
# To select one column, specify the column label
# within the subscript operator: [ ]
planets_names_series = df_planets['planet']
print(planets_names_series)
# Note: one column of a DataFrame is a Series object
print(print(type(planets_names_series)))  # <class 'pandas.core.series.Series'>

# slide 52
# To select two or more columns they must be provided as a list
planets_names_and_mass = df_planets[['planet', 'mass']]
print(planets_names_and_mass)

# slides 53-54 - Removing a column
# two ways:
# 1) using the del keyword
print(df_students_2)
del df_students_2['Country']  # removes the column named 'Country'
print(df_students_2)
# 2) using the pop() DataFrame method
city = df_students_2.pop('City') # removes the column named 'City' and returns it
print(df_students_2)
# city is series containing the removed cities from the
# data frame df_students_2
print(city)  

# slides 55-56 - Adding a column
# two ways
# 1) insert a column at the end of the DataFrame
df_students_2['City'] = city  # re-inserts the 'City' column
df_students_2['Country'] = ['Australia', 'India', 'India', 'India', 'US', 'US']  # re-inserts the 'Country' column
print(df_students_2)
# 2) insert a column at a specific location of the DataFrame
# insert surnames as 2nd column (with index 1)
df_students_2.insert(1, "Surname", ['Johnson', 'Patel', 'West', 'Patterson',  'Thompson', 'Ward'])
print(df_students_2)

# slides 57-64 - Horizontal Slicing (selecting rows)
# can be done in various ways:
# 1) through index label ("location") – using the loc attribute
#    (The provided index must exist in the DataFrame as a
#     label, otherwise KeyError is thrown)
print(df_students_2_new.loc['two']) # this works, as 'two' is the index label; returns the row with index label 'two'
print(df_students_2_new.loc['one']) # this works, as 'one' is the index label; returns the row with index label 'one'
print(df_students_2_new.loc[4])     # this works, as 4 is the actual index label; returns the row with index label 4
#df_students_2_new.loc[1] # throws KeyError, as loc expects the actual index label(s) (and there is no index labelled 1)
#df_students_2_new.loc[2] # throws KeyError, as loc expects index label(s)
# The returned row is a Series:
print(type(df_students_2_new.loc['two']))  # <class 'pandas.core.series.Series'>

# 2) through index position ("integer location") – using the
#    iloc attribute
#    (The provided index must exist in the DataFrame as a
#     position, otherwise KeyError is thrown)
print(df_students_2_new.iloc[1]) # this works, as 1 is the position of the index (index 'one' is at position 1); returns the row at position 1
print(df_students_2_new.iloc[4]) # this works, as 4 is the position of the index (index 4 is at position 4); returns the row at position 4
#df_students_2_new.iloc['one'] # throws TypeError, as loc expects an int representing the index position - starting from 0)
# The returned row is a Series:
print(type(df_students_2_new.iloc[1]))  #  <class 'pandas.core.series.Series'>

# 3) through slicing with loc or iloc attribute
# Slicing with loc property does NOT follow Pythons usual
# Inclusive:Exclusive convention
# It instead retrieves rows following the Inclusive:Inclusive
# convention (as here values are index labels)
print(df_students_2_new.loc['two':4]) # this works, as both provided values are actual index labels; retrieves rows with index labels 'two', 3, 4
print(df_students_2_new.loc['two':])  # this works, as the only provided value is the actual index label; rows from index label 'two' to the end
print(df_students_2_new.loc[:'two'])  # this works, as the only provided value is the actual index label; retrieves rows from the beginning to index label 'two' ('zero', 'one', 'two')
print(df_students_2_new.loc[:3])  # this works, as the only provided value is the actual index label; retrieves rows from the beginning to index label 3 ('zero', 'one', 'two', 3)
print(df_students_2_new.loc[4:])  # this works, as the only provided value is the actual index label; retrieves rows from index label 4 to the end (4, 5)
print(df_students_2_new.loc[:'zero'])  # this works, as the only provided value is the actual index label; retrieves rows from the beginning to index label 'zero' ('zero')
#df_students_2_new.loc[1:3] # throws TypeError, as loc expects the actual index label(s) and 1 is not an index label (3 is)
# The returned row is a DataFrame
# (even if it consists of one row only):
print(type(df_students_2_new.loc[:'zero']))  # <class 'pandas.core.frame.DataFrame'>
print(type(df_students_2_new.loc['zero']))   # <class 'pandas.core.series.Series'>
# Slicing with iloc property DOES follow Pythons usual
# Inclusive:Exclusive convention (as here values are index positions)
print(df_students_2_new.iloc[1:3]) # this works, as both values are positions of the indexes; retrieves rows with index positions 1 & 2 (with index labels 'one' & 'two')
print(df_students_2_new.iloc[1:2]) # this works, as both values are positions of the indexes; retrieves row with index position 1 (with index label 'one')
print(df_students_2_new.iloc[4:])  # this works, as the only provided value is position of an index; retrieves rows with index position 4 to the end (with index labels 4 & 5)
print(df_students_2_new.iloc[:4])  # this works, as the only provided value is position of an index; retrieves rows with index positions 0 to 3 (with index labels 'zero', 'one', 'two, & 3)
#df_students_2_new.iloc['two':4]  # throws TypeError, as 'two' is not numeric (not a position of an index)
#df_students_2_new.iloc['one':]   # throws TypeError, as 'one' is not numeric (not a position of an index)
#df_students_2_new.iloc[:'one']   # throws TypeError, as 'one' is not numeric (not a position of an index)
# The returned row is a DataFrame
# (even if it consists of one row only):
print(type(df_students_2_new.iloc[1:2])) # <class 'pandas.core.frame.DataFrame'>
print(type(df_students_2_new.iloc[1]))   # <class 'pandas.core.series.Series'>

# 4) through a list of rows supplied to loc or iloc attributes
print(df_students_2_new.loc[['zero','one',5]]) # returns rows with index labels 'zero','one' and 5
print(df_students_2_new.loc[[3,5]]) # returns rows with index labels 3 and 5
#df_students_2_new.loc[[2,4]] # throws KeyError, as 2 is not an index label
#df_students_2_new.loc[[0,1,5]] # throws KeyError, as 0 & 1 are not index labels
# The returned row is a DataFrame
# (even if it consists of one row only):
print(type(df_students_2_new.loc[['two']])) #  <class 'pandas.core.frame.DataFrame'>
print(type(df_students_2_new.loc['two']))   #  <class 'pandas.core.series.Series'>

print(df_students_2_new.iloc[[3,5]]) # returns rows with index position 3 and 5 (rows with index labels 3 and 5)
print(df_students_2_new.iloc[[0,1,5]]) # returns rows with index positions 0, 1 & 5 (index labels 'zero','one' and 5)
#df_students_2_new.iloc[[2,4]] # returns rows with index position 2 and 4 (rows with index labels 'two' and 4)
#df_students_2_new.iloc['one', 5] # throws ValueError, as 'one' is not a position
#df_students_2_new.iloc[['zero','one',5]] # throws ValueError, as 'zero' and 'one' are not index positions
# The returned row is a DataFrame
# (even if it consists of one row only):
print(type(df_students_2_new.iloc[[0]])) # <class 'pandas.core.frame.DataFrame'>
print(type(df_students_2_new.iloc[0])) # <class 'pandas.core.series.Series'>
# Note: loc and iloc are interchangeable when labels are 0-based integers
# df_students_2_new.loc[[3,5]]
# returns the same as
# df_students_2_new.iloc[[3,5]]
# because 3 and 5 are 0-based integer labels

# 5) through head() and tail() DataFrame methods
print(df_planets.head())  # lists first five rows
print(df_planets.head(3)) # lists first three rows
print(df_planets.tail())  # lists last five rows
print(df_planets.tail(2)) # lists last two rows
# Note:
# df.head(0) and df.tail(0) will list the DataFrame column
# labels
# If  n < 0 or n > number of rows, head(n) and tail(n) will
# list the whole DataFrame

# 6) through slicing [index1:index2], [index1:], [:index2]
#    (the row at index2 is never retrieved)
# This is not a recommended method for horizontal slicing, as
# there are rules to remember, e.g. both indices must both be
# either labels or index positions; if index exists as both
# position and a label, it will be regarded as position
# (not as index label), etc.
print(df_students_2_new['two':4]) # this works, as both provided values are actual index labels; retrieves rows with index labels 'two', 3 and 4
print(df_students_2_new['two':])  # this works, as the only provided value is the actual index label; retrieves rows from index label 'two' to the end
print(df_students_2_new[:'two'])  # this works, as the only provided value is the actual index label; retrieves rows from the beginning to index label 'two'
print(df_students_2_new[2:])  # retrieves rows from index position 2 to the end ('two', 3, 4, 5)
print(df_students_2_new[:2])  # retrieves rows from the beginning to index position 1 ('zero', 'one')
print(df_students_2_new[:3])  # retrieves rows from the beginning to index position 2 ('zero', 'one', 'two')
print(df_students_2_new[4:])  # retrieves rows from index position 4 to the end (4, 5)
print(df_students_2_new[3:5]) # retrieves rows from index position 3 and 4 (although they both exist as index labels as well)
#df_students_2_new['one':2] # throws TypeError as 'one' is index label and 2 is index position
#df_students_2_new[1:'two'] # throws TypeError as 1 is index position and 'two' is index label

# slide 65 - useful DataFrame attributes & methods
# shape is a DataFrame attribute (hence is not followed by brackets),
# that returns the number of rows and columns: (nrows, ncols)
print(df_planets.shape)  # returns (9, 21)
# list column data types by using the DataFrame dtypes attribute
# Note: string data type in DataFrames is listed as object
print(df_planets.dtypes)
# The DataFrame method info() provides technical information about a DataFrame
print(df_planets.info())
# The describe() method provides a quick overview of the numerical data in a DataFrame.
# All textual data columns are by default NOT taken into account by the describe() method.
print('Describe:\n', df_planets.describe())
print('Describe specified columns:\n', df_planets[['planet', 'mass', 'diameter']].describe())

# slide 67
# Applying functions to a column
# straightforward solution
print(df_planets['mass'] * 2.2)
# using lambda function
print(df_planets['mass'].apply(lambda w: w * 2.2))

# slide 68
# To store the calculated values in a separate column of the existing DataFrame:
df_planets['mass_pounds'] = df_planets['mass'] * 2.2
# OR
df_planets['mass_pounds'] = df_planets['mass'].apply(lambda w: w * 2.2)
print(df_planets[['mass', 'mass_pounds']])

# slide 69
# using the assign() method to assign new columns to a DataFrame
df_planets = df_planets.assign(mass_pounds = df_planets['mass'] * 2.2)
df_planets = df_planets.assign(mass_pounds = lambda w: w['mass'] * 2.2)
df_planets = df_planets.assign(mass_pounds = lambda w: w.mass * 2.2)

# slide 70
# Applying arithmetic operators directly between two column of numeric data type
df_planets['diff'] = df_planets['perihelion'] - df_planets['aphelion']
print(df_planets[['perihelion', 'aphelion', 'diff']])

# slides 71-77
# Sorting data in a DataFrame - using sort_values() method
# in ascending order
df_planets[['planet', 'mass']].sort_values(by='mass', ascending=True)
# in descending order
df_planets[['planet', 'number_of_moons']].sort_values(by='number_of_moons', ascending=False)
# in custom order:
# - Version 1 – using the key keyword argument in sort_values() function
df_planets = pd.read_csv('planets.csv')
# Step 1: define the function that returns the category
# series in the required custom sorting order
# (the standard pandas Categorical constructor method is
# used to create a category object):
def custom_sorter(column):
    sort_order = ['Earth', 'Mars', 'Mercury', 'Venus', 'Neptune', 'Pluto', 'Jupiter', 'Uranus', 'Saturn']
    cat = pd.Categorical(column, categories=sort_order, ordered=True)
    cat_series = pd.Series(cat)
    return cat_series
# Step 2: apply the sort_values() function to the DataFrame,
# with parameters by and key, where by should be set to the
# column to be used for sorting and key should be set to the
# sorting function defined above:
df_planets = df_planets[['planet', 'diameter']].sort_values(by='planet', key=custom_sorter)
print(df_planets)
# - Version 2 – using CategoricalDtype – a data type for
# categorical data (with categories) and orderness
df_planets = pd.read_csv('planets.csv')
# Step 1: import CategoricalDtype:
from pandas.api.types import CategoricalDtype
# Step 2: define the custom sorting order through a list of values:
sort_order = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
# Step 3: Create a custom category type cat_order with the
# 1st argument set to sort_order list, and the 2nd argument
# ordered=True for this variable to be treated as an ordered categorical:
cat_order = pd.CategoricalDtype(sort_order, ordered=True)
# Step 4: call astype(cat_order) to cast the ordered data to
# the custom category type:
df_planets['planet'] = df_planets['planet'].astype(cat_order)
# At this stage, the 'planet' column has been casted to a
# category data type with the specified order:
print(df_planets['planet'])
# Step 5: call the sort_values() function passing the
# column name to be used for sorting:
df_planets_diameter = df_planets[['planet', 'diameter']].sort_values('planet')
print(df_planets_diameter)

# Example from notes section of slide 72:
# sorting by multiple columns (multi-level sorting)
# you can pass multiple columns as a list to the by 
# kwarg and the corresponding multiple sorting orders
# as a list to the ascending kwarg.
df_planets = pd.read_csv('planets.csv')
df_planets = df_planets[['planet', 'number_of_moons']].sort_values(by=['number_of_moons', 'planet'], ascending=[False, True])
print(df_planets)

df_planets = pd.read_csv('planets.csv')
# slides 78-89
# Filtering data in a DataFrame - using query() method
# Query based on a numerical value (of a numerical variable)
df_no_moons_gt_3 = df_planets.query('number_of_moons > 3')
print(df_no_moons_gt_3[['planet', 'number_of_moons']])
# Query based on a string value (of a categorical variable)
df_venus = df_planets.query("planet=='Venus'")
print(df_venus)
df_venus = df_planets.query('planet=="Venus"')
print(df_venus)
# Query based on a DataFrame index
df_first_3_rows = df_planets.query('index < 3')  # returns the first 3 rows
print(df_first_3_rows)
# Query that uses mathematical operations inside of the expression
df_odd_rows = df_planets.query('index % 2 == 1')  # returns odd rows
print(df_odd_rows)
# Query comparing two columns
df_compare_cols = df_planets.query('orbital_period < rotation_period')
print(df_compare_cols)
# Query applied to a DataFrame subset
# (When a DataFrame subset is obtained through selecting two
#  or more columns, they must be provided as a list)
# step 1: obtain the relevant subset of the DataFrame (through vertical slicing)
df_planets_and_moons = df_planets[['planet', 'number_of_moons']]
# step 2: apply the query() method to the DataFrame subset
df_planets_with_moons_gt_3 = df_planets_and_moons.query('number_of_moons > 3')
df_planets_and_moons
print(df_planets_with_moons_gt_3)
# Query with multiple conditions (using logical operators: and, or, not)
df_planets.query('mass > 100 and number_of_moons < 20')
df_planets.query('mass < 10 and number_of_moons >= 1')
df_planets.query('mass > 100 and number_of_moons < 20 or mass < 10 and number_of_moons >= 1')
df_planets.query('mass > 100 and (number_of_moons < 20 or number_of_moons > 70)')
# Query that uses a local variable
# refer to variables in the query string expression by prefixing them with the '@' character
# Task: list those planets that are warmer than Earth
# filter Earth only data
df_earth_data = df_planets.query("planet == 'Earth'")
# get Earth's mean temperature (since the above query returns one record only
# we can access it through iloc property, passing to it the index position: 0)
earth_mean_temp = df_earth_data['mean_temperature'].iloc[0]    # returns 15
# list warmer planets than Earth (showing only relevant columns – vertical slicing)
print(df_planets[['planet','mean_temperature']].query("mean_temperature > @earth_mean_temp"))
# filtering using "bracket notation" (for information only)
# (an alternative, but less user-friendly filtering method)
df_planets[df_planets['planet'] == 'Venus']
df_planets[df_planets['number_of_moons'] > 3]
df_planets[(df_planets['mass'] > 100) & (df_planets['number_of_moons'] < 20)]
df_planets[df_planets['mean_temperature'] > earth_mean_temp] [['planet','mean_temperature']]

# slide 90 - Aggregate functions
df_person_details = pd.DataFrame(np.array([['John', 23, 1.80, 72],
                                           ['Suzie', 40, 1.70, 60],
                                           ['Paul', 35, 1.86, 90]]),
                                 columns=['name', 'age', 'height', 'weight'])
# convert data in 'age' column to int
df_person_details['age'] = pd.to_numeric(df_person_details['age'])
# now we can apply sum() and mean() aggregate functions to 'age' column
# (max(), min() and mode() could be applied to object data type as well)
total_age = df_person_details['age'].sum()    # returns 98
average_age = df_person_details['age'].mean() # returns 32.666667
max_age = df_person_details['age'].max()      # returns 40
min_age = df_person_details['age'].min()      # returns 23
mode_no_moons = df_planets['number_of_moons'].mode()  # returns 0 (0 is the most frequent number of moons, as it appears twice; all other frequencies are 1)

# slides 91-94 - Combining aggregation with query
# Task: find the number of people younger than 40 from the df_person_details DataFrame
# Age must be of numeric type so that we can compare it with 40
# (by default all values in in NumPy array are of 'object' data type if at least one value is non-numerical - here 'name')
# To convert data type of MULTIPLE numeric columns into numbers
# at once, use the apply() function with to_numeric Pandas function
# (passing to_numeric without brackets), 
df_person_details[['age', 'height', 'weight']] = df_person_details[['age', 'height', 'weight']].apply(pd.to_numeric)
# To convert all values in ONE numeric column into numbers
# use to_numeric() Pandas function:
# df['numeric_column'] = pd.to_numeric(df['numeric_column'])
print(df_person_details.dtypes)
# We need to apply the aggregate function to the age column
# only, but if we extract the age column, we obtain a Series,
# which does not have the query() method
print(type(df_person_details['age'])) #  <class 'pandas.core.series.Series'>
# the following line throws  AttributeError: 'Series' object has no attribute 'query'
#print(df_person_details['age'].query('age < 40').count()
# Therefore, we need to apply the aggregate function to the DataFrame:
print(df_person_details.query('age < 40').count())
# The aggregate function count() applied to all columns of the DataFrame, and the resulting object is Series, with column names as index labels:
print(type(df_person_details.query('age < 40').count())) # <class 'pandas.core.series.Series'>
# To return the actual value only (the result of applying
# aggregate function to the query), use subscript operator
# (in a number of ways):
# directly from the Series, using subscript operator with the row index
print(df_person_details.query('age < 40').count()[1]) # prints 2
# using loc attribute and passing the index label to its subscript operator
print(df_person_details.query('age < 40').count().loc['age']) # prints 2
# using iloc attribute and passing the index position to its subscript operator
print(df_person_details.query('age < 40').count().iloc[1]) # prints 2

# slides 95-100 - Combining aggregation with groupby
# Aggregation with groupby is performed by passing a list of
# column(s) to the groupby() method, and chain the desired
# aggregate function call to it.
# 1. Combining aggregation with groupby – on single column
# Example 1: calculate the number of planets for all different values of
# the 'has_global_magnetic_field' column: (Yes, No, Unknown)
# step 1: slice DataFrame to show only the relevant columns
# (here 'has_global_magnetic_field' and 'planet')
df_planets_magn_field = df_planets[['planet', 'has_global_magnetic_field']]
print(df_planets_magn_field)
# step 2: pass the column for which to apply count() to
# groupby() & apply count()
df_planets_magn_field = df_planets_magn_field.groupby(['has_global_magnetic_field']).count()
print(df_planets_magn_field)
# step 3: rename the 'planet' column to 'total'
df_planets_magn_field = df_planets_magn_field.rename(columns={'planet': 'total'})
# 2. Combining aggregation with groupby – on multiple columns
# Example 2: calculate the number of planets for all different
# values' combinations of the ('has_ring_system', 'has_global_magnetic_field')
# columns: (Yes, No) and (Yes, No, Unknown)
# step 1: slice DataFrame to show only the relevant columns
df_planets_ring_magn_field = df_planets[['planet', 'has_ring_system', 'has_global_magnetic_field']]
print(df_planets_ring_magn_field)
# step 2: pass the columns for which to apply count() to
# groupby() & apply count()
df_planets_ring_magn_field = df_planets_ring_magn_field.groupby(['has_ring_system', 'has_global_magnetic_field']).count()
print(df_planets_ring_magn_field)
# step 3:
# rename the 'planet' column to 'total'
df_planets_ring_magn_field = df_planets_ring_magn_field.rename(columns={'planet': 'total'})
# 3. Combining aggregation with groupby – adding an index to the resulting DataFrame
# By default groupby() result doesn't include row Index;
# you can add the index using reset_index() method
# To include the index chain the reset_index() method call
# to the DataFarme.gropuby().agg_func() statement
# pass the column for which to apply count() to groupby()
# & apply count() and include the index
df_groupby_indexed = df_planets_ring_magn_field.reset_index()
print(df_groupby_indexed)

# slides 101-106 - Combining two DataFrames into one
# DataFrames can be combined together using pandas.concat(),
# pandas.merge() and DataFrame.join() functions
# 1. using concat() pandas function
# Example 1:
df_users_1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Melinda', 'Kevin', 'Karolina', 'Sherella'],
    'hobbies': ['electronics', 'programming', 'diy', 'travel']
})
df_users_2 = pd.DataFrame({
    'id': [5,6],
    'name': ['Jennifer', 'Angela'],
    'hobbies': ['electronics', 'programming']
})
df_result = pd.concat([df_users_1, df_users_2])
print(df_result)
# Note: concat() by default appends one DataFrame at the end
# of the other DataFrame across rows using outer join
# (<=> full outer join in SQL), useful if both data frames
# have the same column names, as in the above example
# Notice in the above example, it just added the row index
# as-is from two DataFrame: indices 0, 1, 2, 3 from the first
# and indices 0, 1 from the second DataFrame.
# Sometimes you may want to reset the index. You can do so by
# using the ignore_index=True kwarg:
df_result = pd.concat([df_users_1, df_users_2], ignore_index=True)
print(df_result)
# 2. using merge() pandas function
# Example 2: merging data frames with different index values
df_users = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Melinda', 'Kevin', 'Karolina', 'Sherella'],
    'hobbies': ['electronics', 'programming', 'diy', 'travel'],
})
df_info = pd.DataFrame({
    'id': [2, 3, 4, 5],
    'age': [31, 20, 40, 70],
    'gender': ['M', 'F' , 'M', 'F']
})
df_result = pd.merge(df_users, df_info)
# OR
df_result = df_users.merge(df_info)
print(df_result)
# In practice, merge() is the first choice method to join
# DataFrames on columns - because by default merge() joins
# DataFrames on common columns (using inner join).
# Inner join keeps the common rows and discards the ones
# that don't match from both DataFrames
# To include all columns from both data frames, set the 'how'
# kwarg to 'outer' (<=> to full outer join in SQL).
# All values for the kwarg how are 'left', 'right', 'outer', 'inner', 'cross’.
print("Merge Example 2a:\n", pd.merge(df_users, df_info, how='outer'))
# OR
print("Merge Example 2b:\n", df_users.merge(df_info, how='outer'))
# Example 3: merging data frames with same index values
df_users = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Melinda', 'Kevin', 'Karolina', 'Sherella'],
    'hobbies': ['electronics', 'programming', 'diy', 'travel'],
})
df_info = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'age': [31, 20, 40, 70],
    'gender': ['M', 'F' , 'M', 'F']
})

df_result = pd.merge(df_users, df_info)
# OR
df_result = df_users.merge(df_info)
print(df_result)
# If the data frames have the same index values in the
# common columns, by default merge() will keep all rows from
# each of the merging data frames, as the inner join won't
# discard any rows. This is useful when data sets have
# different column names that relate to the same entity
# instance (identified by the row value).

# 2. using join() DataFrame method
# join() joins columns with another DataFrame either on index or on a key column. 
# Example 1: – joining DataFrames on common index (using left join by default)
df_users = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Melinda', 'Kevin', 'Karolina', 'Sherella']
}, index = ['K1','K2', 'K3', 'K4'])
df_info = pd.DataFrame({
    'id': [4, 5, 6, 7],
    'age': [31, 20, 40, 70],
    'gender': ['M', 'F' , 'M', 'F'],
    'hobbies': ['electronics', 'programming', 'diy', 'travel'],
}, index = ['K1','K2', 'K3', 'K4'])
df_result = df_users.join(df_info, lsuffix='_users', rsuffix='_info')
print("Join Example 1:\n", df_result)
# In practice, join() is the first choice method to join
# DataFrames on rows - because by default join() joins
# DataFrames on rows (using left join), through row indexes.

# If the values of the common column ('id') are the same, the common column can be used as index to join the two DataFrames with the same outcome - indexes of the resulting DataFrame will have default values 0, 1, 2, 3
# Example 2: – joining DataFrames on common column ('id')
df_users = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Melinda', 'Kevin', 'Karolina', 'Sherella'],
})
df_info = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'age': [31, 20, 40, 70],
    'gender': ['M', 'F' , 'M', 'F'],
    'hobbies': ['electronics', 'programming', 'diy', 'travel']
})
df_result = df_users.join(df_info, lsuffix='_users', rsuffix='_info')
print("Join Example 2:\n", df_result)

# If columns overlap, at least one of lsufix or rsufix must
# be set, or alternatively, set_index() method can be used to
# specify the common column in both DataFrames containing the
# values to be used as indexes:
df_users = pd.DataFrame({'id': [1, 2, 3, 4],
                         'name': ['Melinda', 'Kevin', 'Karolina', 'Sherella']
                        })
df_info = pd.DataFrame({'id': [1, 2, 3, 4],
                        'age': [31, 20, 40, 70],
                        'sex': ['F', 'M', 'F', 'F'],
                        'hobbies': ['electronics', 'programming', 'diy', 'travel']
                       })
df_result = df_users.set_index('id').join(df_info.set_index('id'))
print("Join Example 3:\n", df_result)

# set_index() method can be used to specify any common column
# (does not need to be the id)
df_users = pd.DataFrame({'name': ['Melinda', 'Kevin', 'Karolina', 'Sherella']
                        })
df_info = pd.DataFrame({'name': ['Melinda', 'Kevin', 'Karolina', 'Sherella'],
                        'age': [31, 20, 40, 70],
                        'sex': ['F', 'M', 'F', 'F'],
                        'hobbies': ['electronics', 'programming', 'diy', 'travel']
                       })
df_users.set_index('name').join(df_info.set_index('name'))
print("Join Example 4:\n", df_result)

# slides 107-111: Data Cleaning
'''
Data cleaning means fixing bad data in your data set.
Bad data could be:
- Empty cells
- Data in wrong format
- Wrong data
- Duplicates
'''
# 1. Removing rows where data is missing
# To remove any rows where a column value is not provided
# use the dropna() method
# Note: dropna returns a DataFrame object with the modifications.
# If you need the original DataFrame to change use inplace = True
# Example 1: remove any rows where a column value is not provided:
students_list = [('Jack', 34, 'Sydney', 'Australia'),
                 ('Rita', 30, 'Delhi', 'India'),
                 ('Tom', 31, 'Mumbai', 'India'),
                 ('Neelu', 32, ),                     # City and Country values missing
                 ('John', 16, 'New York'),            # Country value missing
                 ('Mike', 17, 'Las Vegas', 'US')]
df_students_1 = pd.DataFrame(students_list, columns=['Name', 'Age', 'City', 'Country'])
df_students_1_clean = df_students_1.dropna()
# Example 2: remove rows where data is not provided for a particular column:
students_list = [('Jack', 34, 'Sydney', 'Australia'),
                 ('Rita', 30, 'Delhi', 'India'),
                 ('Tom', 31, 'Mumbai', 'India'),
                 ('Neelu', 32, ),                     # City and Country values missing
                 ('John', 16, 'New York'),            # Country value missing
                 ('Mike', 17, 'Las Vegas', 'US')]
df_students_1 = pd.DataFrame(students_list, columns=['Name', 'Age', 'City', 'Country'])
df_students_1_clean_city = df_students_1.dropna(subset=['City'])
'''
To identify missing data use the isna() method.
isna() identifies:
NaN in numeric arrays, 
None or NaN in object arrays, 
NaT in datetimelike. 
'''
print(df_students_1.isna())
ds = pd.Series( ['john', 'paul', None, 'ringo', 'george', None])
print(ds.isna())

# 2. Replacing missing values
# If the tuples have different lengths, missing values will
# be automatically filled in with the value None:
students_list = [('Jack', 34, 'Sydney', 'Australia'),
                 ('Rita', 30, 'Delhi', 'India'),
                 ('Tom', 31, 'Mumbai', 'India'),
                 ('Neelu', 32, ),                     # City and Country values missing
                 ('John', 16, 'New York'),            # Country value missing
                 ('Mike', 17, 'Las Vegas', 'US')]
df_students_1 = pd.DataFrame(students_list, columns=['Name', 'Age', 'City', 'Country'])
# To replace missing values in a data structure, use the
# fillna() method:
# To replace missing values with 0:
# >>> new_df = df.fillna(0)
df_students_1_filled = df_students_1.fillna(0)
print(df_students_1_filled)
# You can also use the fillna() method to replace empty
# values for a particular column:
students_list = [('Jack', 34, 'Sydney', 'Australia'),
                 ('Rita', 30, 'Delhi', 'India'),
                 ('Tom', 31, 'Mumbai', 'India'),
                 ('Neelu', 32, ),                     # City and Country values missing
                 ('John', 16, 'New York'),            # Country value missing
                 ('Mike', 17, 'Las Vegas', 'US')]
df_students_1 = pd.DataFrame(students_list, columns=['Name', 'Age', 'City', 'Country'])
# To replace missing values from the 'Country' column with 0:
df_students_1_country_filled = df_students_1['Country'].fillna(0)
print(df_students_1)

# 3. Data of wrong format
# Cells with data of wrong format can make it difficult,
# or even impossible, to analyse data.
# To fix it, you have two options: remove the rows, or
# convert all cells in the columns into the same format.
# To remove the rows, use the dropna() method, as illustrated before 
# To convert all values in a date column into dates use
# to_datetime() method:
# >>> df['date_column'] = pd.to_datetime(df['date_column'])
# To convert all values in a numeric column into numbers use
# to_numeric() method:
# >>> df['numeric_column'] = pd.to_numeric(df['numeric_column'])
# To convert data type of multiple numeric columns into
# numbers at once, use the apply() function with to_numeric
# pandas function (passing to_numeric without brackets):
df_person_details[['age', 'height', 'weight']] = df_person_details[['age', 'height', 'weight']].apply(pd.to_numeric)

# 4. Fixing wrong values
# For small data sets you might be able to replace the wrong
# data one by one, for example:
# replaces wrong City value in row with index label 3
df_students_1.loc[3,'City'] = 'Bangalore'
print(df_students_1)
# For larger data sets you can create some rules, e.g. set some boundaries for valid values, and replace any values that are outside of the boundaries, for example:
# >>> for i in df_sales.index: # replaces all negative values in Price column with 0
#         if df_sales.loc[i, "Price"] < 0:
#             df_sales.loc[i, "Price"] = 0

# 5. Removing rows with wrong values
# Another way of handling wrong values is to remove the rows
# that contains wrong values. This is an option if there is a
# good chance you do not need them to do your analyses.
# To remove the rows, use the drop() method, as illustrated
# below: 
# >>> for i in df_sales.index: # removes rows with negative values in Price column             
#         if df_sales.loc[i, "Price"] < 0:
#            df_sales.drop(i, inplace=True)

# Print statistical information to help you identify
# possible correlations between column data
print(df_planets.corr())

# 6. Removing duplicates
# If the tuples have different lengths, missing values will
# be automatically filled in with the value None:
students_list = [('Jack', 34, 'Sydney', 'Australia'),
                 ('Rita', 30, 'Delhi', 'India'),
                 ('Tom', 31, 'Mumbai', 'India'),
                 ('Tom', 31, 'Mumbai', 'India'), # duplicated row
                 ('John', 16, 'New York'),
                 ('Mike', 17, 'Las Vegas', 'US')]
df_students_1 = pd.DataFrame(students_list, columns=['Name', 'Age', 'City', 'Country'])
# To discover duplicates, use the duplicated() method, which returns a Booelan value for each duplicate row:
# replaces wrong City value in row with index label 3
print(df_students_1.duplicated())
# To remove duplicates, use the drop_duplicates() method:
df_students_1.drop_duplicates(inplace=True)
print(df_students_1)
# 7. Print statistical information to help you identify
# possible correlations between column data
print(df_planets.corr() )

# slide 112: line plot
import matplotlib.pyplot as plt

df = pd.read_csv('planets.csv')
df = df[['planet', 'number_of_moons']]
# construct the plot
df.plot()
# display the plot
plt.show()

# slide 113: line plot with labels
df = pd.read_csv('planets.csv')
df = df[['planet', 'number_of_moons']]
# construct the plot
df.plot()
# display the plot
plt.show()

# slide 114: scatter plot
df = pd.read_csv('planets.csv')
df = df[['planet', 'number_of_moons']]
# construct the plot
df.plot(x='planet', y='number_of_moons', kind='scatter')
# display the plot
plt.show()

# slide 115: bar plot
df = pd.read_csv('planets.csv')
df = df[['planet', 'number_of_moons']]
df.plot(x='planet', y='number_of_moons', kind='bar')
# include the title
plt.title("planets' number of moons")
# prevent truncating axis labels
plt.tight_layout()
plt.show()


