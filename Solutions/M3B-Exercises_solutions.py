#find this here: /Users/apple/Documents/coding/companies/FDM/FDM_training/FDM_Python_2/Solutions

######################
# Module 3B - Pandas #
######################

import pandas as pd
import seaborn as sns

# Create the DataFrame from the 'planets.txt' file present 
# in the same folder (where data are separated with comma):
df_planets = pd.read_csv('planets.txt')
# force the editor to show all columns of a DataFrame
#pd.set_option('max_columns', None)



# Question 1
# ----------
'''
Think about correlations that might exists for the planets dataset.
a) For example do you think there might a correlation between the mass
of a planet and the force of its gravitational pull?
b) How about the mass of the planet and the number of moons orbiting that planet?
c) Or the mass of a planet and the distance of the planet from the sun?
Run the corr() function; do you always get expected correlations
or do some of the answers surprise you?
'''
# Question 1a)
# -----------
def Q1a():
    # Is there a correlation between the mass of a planet 
    # and the force of its gravitational pull?
    print(df_planets.corr())
    # The correlation between mass and gravity is 0.859830; this
    # is a strongly positive correlation.
    # To help clarifying the slight discrepancy between mass and gravity,
    # let's extract the data for relevant columns only
    # ('planet', 'mass', 'gravity') sorted in descending order by mass:
    print(df_planets[['planet', 'mass', 'gravity']].sort_values(by='mass', ascending=False))
    # Answer: generally, the mass is proportional to gravity: greater the mass,
    # greater its gravitational pull. Except from Saturn and Uranus, sorting is perfect, but
    # there is also the fact that Mars is twice greater than Mercury and yet has the same gravity.
    # Broadly speaking, the correlation between mass and gravity is as expected.

#Q1a()


# Question 1b)
# -----------
def Q1b():
    # Is there a correlation between the mass of the planet
    # and the number of moons orbiting that planet?
    print(df_planets.corr())
    # The correlation between mass and number of moons is 0.891003; this
    # is a strongly positive correlation.
    # To help clarifying the slight discrepancy between mass and gravity,
    # let's extract the data for relevant columns only
    # ('planet', 'mass', 'number_of_moons') sorted in descending order by mass:
    print(df_planets[['planet', 'mass', 'number_of_moons']].sort_values(by='mass', ascending=False))
    # Answer: again, sorting in general reveals positive correlation between mass
    # and the number of moons: greater the mass, greater the number of moons.
    # There are however some discrepancies: in case of Uranus, which would
    # have been expected to have less moons considering its mass. Mars and Pluto
    # on the other hand have too many moons considereing their mass.
    # Broadly speaking, the correlation between mass and number of moons is also as expected.

#Q1b()


# Question 1c)
# -----------
def Q1c():
    # Is there a correlation between the mass of a planet and the
    # distance of the planet from the sun?
    print(df_planets.corr())
    # The correlation between mass and distance from sun is -0.160660; this
    # is a slightly negative correlation. 0 would mean that there is no
    # specific relation between these two variables, and this is almost true.
    print(df_planets[['planet', 'mass', 'distance_from_sun']].sort_values(by='mass', ascending=False))
    # Answer: this time, sorting in general reveals no specific pattern (to the sorted
    # values of mass, the corresponding values of distance from sun are not sorted).
    # Broadly speaking, the correlation between mass and number of moons is somehow
    # unexpected. There seems to be no relation between these two variables
    # (the mass of a planet is almost unrelated to its distance from sun, and it
    # is slightly negative: greater the mass, less the distance from sun)

#Q1c()


# Question 2
# ----------
'''
Use Pandas to list the first 3 closest planets to the sun, sorted in ascending order (the closest first).
'''
def Q2v1():
    # using the head() function, passing the number of rows to retrieve - here 3
    print(df_planets[['planet', 'distance_from_sun']].sort_values(by='distance_from_sun', ascending=True).head(3))

#Q2v1()

def Q2v2():
    # using slicing: [index1:index2], [index1:], [:index2] (the row at index2 is never retrieved)
    print(df_planets[['planet', 'distance_from_sun']].sort_values(by='distance_from_sun', ascending=True)[0:3])

#Q2v2()

def Q2v3():
    # using the loc property with slicing
    # Note: slicing with loc property does NOT follow Pythons usual Inclusive:Exclusive convention - it instead 
    # retrieves rows following the Inclusive:Inclusive convention (hence to retrieve 3 rows the second index must be 2)
    print(df_planets[['planet', 'distance_from_sun']].sort_values(by='distance_from_sun', ascending=True).loc[0:2])
    # OR
    print(df_planets[['planet', 'distance_from_sun']].sort_values(by='distance_from_sun', ascending=True).loc[:2])

#Q2v3()


def Q2v4():
    # using the iloc property with slicing
    # Note: slicing with iloc property DOES follow Pythons usual Inclusive:Exclusive convention -
    # hence to retrieve 3 rows the second index must be 2)
    print(df_planets[['planet', 'distance_from_sun']].sort_values(by='distance_from_sun', ascending=True).iloc[0:3])
    # OR
    print(df_planets[['planet', 'distance_from_sun']].sort_values(by='distance_from_sun', ascending=True).iloc[:3])

#Q2v4()


def Q2v5():
    # using the loc property with the list of rows labels
    print(df_planets[['planet', 'distance_from_sun']].sort_values(by='distance_from_sun', ascending=True).loc[[0, 1, 2]])
    
#Q2v5()
    
def Q2v6():
    # using the iloc property with the list of rows indexes
    print(df_planets[['planet', 'distance_from_sun']].sort_values(by='distance_from_sun', ascending=True).iloc[[0, 1, 2]])
    
#Q2v6()


# Question 3
# ----------
'''
You are provided with a file called planet_colours.csv. Examine its contents, you will see that
the file contains a list of all the planets and their colours. Your job is to merge the initial
DataFrame provided with another DataFrame based on this new file and output
a list of planet name, mass, and the planets colours.
You will need the following code in your script to prevent data truncation:
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
'''
# https://re-thought.com/how-to-add-new-columns-in-a-dataframe-in-pandas/
def Q3():
    '''Common tasks for all 4 versions of solution to this question'''
    # create the first data frame, as a slice of the original df_planets DataFrame, listing planets with their mass:
    df_planet_mass = df_planets[['planet', 'mass']]

    # load the second data frame from file, listing planets with their colour:
    df_planet_colours = pd.read_csv('planet_colours.txt')
    
    # display the second data frame
    print(df_planet_colours)

    # return both data frames
    return df_planet_mass, df_planet_colours


def Q3v1_1():
    '''Version 1.1 - adding a new list as a column, and working on A COPY OF ORIGINAL DataFrame to avoid SettingWithCopyWarning.'''
    # call the function Q3() to create the two DataFrames
    df_planet_mass, df_planet_colours = Q3()
    # create a new dataframe (df_planet_mass_colour) as copy of the slice of the original DataFrame 
    # to avoid SettingWithCopyWarning: "A value is trying to be set on a copy of a slice from a DataFrame."
    # (the commented out instruction in line 192 would produce this warning).
    # This error is usually a result of creating a slice of the original dataframe before adding a new column to it.
    # The first way of avoiding this warning is to create a copy of the source DataFrame
    # so that methods called on the new DataFrame are not applied to the source DataFrame. This is shown here:
    df_planet_mass_colour = df_planet_mass.copy()

    # create the list of values from the 'colour' column of the second data frame:
    planet_colours_list = []
    for colour in df_planet_colours['colour']:
        planet_colours_list.append(colour)

    # Merge the two data frames: add a new column with different values
    # Method 1: By adding a new list as a column
    # df[new_column] = [value0, value1, ..., valueN] (N must correspond to the last index in the first dataframe)    
    # add the new column 'colour' with the list of colours
    #df_planet_mass['colour'] = planet_colours_list  # throws SettingWithCopyWarning as df_planet_mass is a slice of the original Dataframe
    df_planet_mass_colour['colour'] = planet_colours_list
    print(df_planet_mass_colour)
    
#Q3v1_1()

def Q3v1_2():
    '''Version 1.2 - adding a new list as a column TO THE ORIGINAL DataFrame to avoid SettingWithCopyWarning.'''
    # here we are working with the original DataFrame df_planets, created outside the function (hence the Q3() is not called)
    # load the second data frame from file, listing planets with their colour:
    df_planet_colours = pd.read_csv('planet_colours.txt')
    
    # display the second data frame
    print(df_planet_colours['colour'])
    
    # To avoid SettingWithCopyWarning: "A value is trying to be set on a copy of a slice from a DataFrame."
    # This error is usually a result of creating a slice of the original dataframe before declaring your new column
    # The first way of avoiding this warning is to create a copy of the source DataFrame
    # so that methods called on the new DataFrame are not applied to the source DataFrame (as shown in version Q3v1_1() above)
    # The second is to add the new column to the original dataframe and then create the slice. This is shown here:

    # create the list of values from the 'colour' column of the second data frame:
    planet_colours_list = []
    for colour in df_planet_colours['colour']:
        planet_colours_list.append(colour)
        
    # Merge the two data frames: add a new column with different values
    # Method 1: By declaring a new list as a column
    # df[new_column] = [value0, value1, ..., valueN] (N must correspond to the last index in the first dataframe)
    # add the new column 'colour'  with the list of colours TO THE ORIGINAL DataFrame
    df_planets['colour'] = planet_colours_list
    # THEN SLICE THE ORIGINAL DataFrame
    # create a slice of the original first DataFrame, listing planets with their mass and colour:
    df_planet_mass_colour = df_planets[['planet', 'mass', 'colour']]
    print(df_planet_mass_colour)

#Q3v1_2()

def Q3v2():
    '''Version 2 - adding a new list as a column using loc[] and working on A COPY OF ORIGINAL DataFrame to avoid SettingWithCopyWarning.'''
    # call the function Q3() to create the two DataFrames
    df_planet_mass, df_planet_colours = Q3()
    # create a new dataframe (df_planet_mass_colour) as copy of the slice of the original DataFrame 
    # to avoid SettingWithCopyWarning: "A value is trying to be set on a copy of a slice from a DataFrame."
    # This error is usually a result of creating a slice of the original dataframe before declaring your new column
    # The first way of avoiding this warning is to create a copy of the source DataFrame
    # so that methods called on the new DataFrame are not applied to the source DataFrame
    # The second if to add the new column to the original dataframe and then create the slice.
    df_planet_mass_colour = df_planet_mass.copy()
       
    # create the list of values from the 'colour' column of the second data frame:
    planet_colours_list = []
    for colour in df_planet_colours['colour']:
        planet_colours_list.append(colour)
    
    # Merge the two data frames: add a new column with different values
    # Method 2: using loc[]
    # df.loc[:, 'new_column'] = [value0, value1, ..., valueN] (N must correspond to the last index in the first dataframe)
    df_planet_mass_colour.loc[:, 'colour'] = planet_colours_list
    print(df_planet_mass_colour)

#Q3v2()


def Q3v3():
    '''Version 3 - adding a new list as a column using the assign() function.'''
    # call the function Q3() to create the two DataFrames
    df_planet_mass, df_planet_colours = Q3()
    # Note: here we can work on the slice of the original DataFrame, as assign() function
    # returns a new DataFrame (thus not modifying the original DataFrame), and chained indexing is not used

    # create the list of values from the 'colour' column of the second data frame:
    planet_colours_list = []
    for colour in df_planet_colours['colour']:
        planet_colours_list.append(colour)
    
    # Merge the two data frames: add a new column with different values
    # Method 3: using the assign() function
    # df = df.assign(new_column=[value0, value1, ..., valueN])
    df_planet_mass_colour = df_planet_mass.assign(colour=planet_colours_list)
    print(df_planet_mass)

#Q3v3()


def Q3v4():
    '''Version 4 - adding a new list as a column using the insert() function.'''
    # call the function Q3() to create the two DataFrames
    df_planet_mass, df_planet_colours = Q3()
    # Note: here we can work on the slice of the original DataFrame, as chained indexing is not used
    # (although the insert() function modifies the original DataFrame)
    
    # create the list of values from the 'colour' column of the second data frame:
    planet_colours_list = []
    for colour in df_planet_colours['colour']:
        planet_colours_list.append(colour)
    
    # Merge the two data frames: add a new column with different values
    # Method 4 Using the insert() function
    # df.insert(loc=1, column="New Column", value=[value0, value1, ..., valueN])
    # Note: loc is an integer which is the location of column where we want to 
    # insert new column. To insert a new column at the end of df, the integer
    # should be equal to n+1 (where n is the index of the last column in df).
    # If the integer is equal to the index of any existing column, this will
    # shift the existing column at that position (an all other columns
    # following it) to the right.
    df_planet_mass.insert(loc=2, column='colour', value=planet_colours_list)
    print(df_planet_mass)

#Q3v4()


def Q3v5():
    '''Version 5 - merge the two data frames using the join() function.'''
    # call the function Q3() to create the two DataFrames
    df_planet_mass, df_planet_colours = Q3()
    # Note: here we can work on the slice of the original DataFrame, as join() function
    # returns a new DataFrame (thus not modifying the original DataFrame), and chained indexing is not used
    
    # Merge the two data frames: 
    # Method 5 Using the join() function
    # df_1.join(df_2, on=None, how='left', lsuffix='', rsuffix='', sort=False)
    # here we need to join the two data frames using the common column 'planet',
    # hence we need to use the following syntax:
    # df_result = df_1.set_index(common_column).join(df_2.set_index(common_column))
    df_planet_mass_colour = df_planet_mass.set_index('planet').join(df_planet_colours.set_index('planet'))
    
    # set the options to display the whole DataFrame
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    
    # display the merged DataFrame    
    print(df_planet_mass_colour)

#Q3v5()


# Question 4
# ----------
'''
Print a list including the name of the planets, their mean temperature and distance from the sun.
'''
def Q4():
    # extract the data for relevant columns only ('planet', 'mean_temperature', 'distance_from_sun')
    df_planet_temp_dist = df_planets[['planet', 'mean_temperature', 'distance_from_sun']]
    print(df_planet_temp_dist)

#Q4()


# Question 5
# ----------
'''
Sort the previous query by the mean temperature in ascending order.
'''
def Q5():
    # extract the data for relevant columns only ('planet', 'mean_temperature',
    # 'distance_from_sun') sorted in ascending order by mean_temperature
    df_planet_temp_dist_asc = df_planets[['planet', 'mean_temperature', 'distance_from_sun']].sort_values(by='mean_temperature', ascending=True)
    print(df_planet_temp_dist_asc)
    
#Q5()


# Question 6
# ----------
'''
Print a list of planet names and the length of the day (this will be in hours)
'''
def Q6():
    # extract the data for relevant columns only ('planet', 'length_of_day')
    df_planet_day_length = df_planets[['planet', 'length_of_day']]
    print(df_planet_day_length)

#Q6()

# Question 7
# ----------
'''
Now add a new column that shows the length of the day in terms of days.
'''
def Q7v1():
    '''Version 1 - add a new column to the original DataFrame using apply() DataFrame method before slicing the Dataframe.'''
    # add the column obtained by converting the length_of_day in hours to length_of_day in days
    df_planets['length_of_day_in_days'] = df_planets['length_of_day'].apply(lambda ld: ld / 24)
    # now slice the original DataFrame
    print(df_planets[['length_of_day', 'length_of_day_in_days']])
    # Note: any of the following two lines would throw a warning, as a value is trying
    # to be set on a copy of a slice (df_planet_day_length) from a DataFrame (df_planets)
    # Warning is thrown due to performance issues, but more importantly as assigning
    # to the product of chained indexing has inherently unpredictable results.
    #df_planet_day_length['length_of_day_in_days'] = df_planet_day_length['length_of_day'].apply(lambda ld: ld / 24)
    #df_planet_day_length['length_of_day_in_days'] = df_planets['length_of_day'].apply(lambda ld: ld / 24)

#Q7v1()
    
def Q7v2():
    '''Version 2 - add a new column to a copy of the slice of the original DataFrame using apply() DataFrame method.'''
    df_planet_day_length = df_planets[['planet', 'length_of_day']]
    # the following line throws SettingWithCopyWarning;
    # to avoid this, the same two solutions as discussed in question 3 apply
    #df_planet_day_length['length_of_day_in_days'] = df_planet_day_length['length_of_day'].apply(lambda ld: ld / 24)
    # this version uses the copy of the original DataFrame
    df_planet_day_length_copy = df_planet_day_length.copy()
    df_planet_day_length_copy['length_of_day_in_days'] = df_planet_day_length_copy['length_of_day'].apply(lambda ld: ld / 24)
    print(df_planet_day_length_copy[['length_of_day', 'length_of_day_in_days']])

#Q7v2()

def Q7v3():
    '''Version 3 - using loc[] and apply() on the original DataFrame before slicing it.'''
    # The same note as above applies to any of the following two lines:
    #df_planet_day_length.loc[:, 'length_of_day_in_days'] = df_planets['length_of_day'].apply(lambda ld: ld / 24)
    #df_planet_day_length.loc[:, 'length_of_day_in_days'] = df_planet_day_length['length_of_day'].apply(lambda ld: ld / 24)
    # first add the new column to the original DataFrame
    # add the column obtained by converting the length_of_day in hours to length_of_day in days
    df_planets.loc[:, 'length_of_day_in_days'] = df_planets['length_of_day'].apply(lambda ld: ld / 24)
    # then slice the original DataFrame
    print(df_planets[['length_of_day', 'length_of_day_in_days']])

#Q7v3()


def Q7v4():
    '''Version 4 - using loc[] and apply() on a copy of sliced original DataFrame.'''
    df_planet_day_length = df_planets[['planet', 'length_of_day']]
    # make a copy of the original DataFrame
    df_planet_day_length_copy = df_planet_day_length.copy()
    # then use loc[] and apply() on the copy
    # add the column obtained by converting the length_of_day in hours to length_of_day in days
    df_planet_day_length_copy.loc[:, 'length_of_day_in_days'] = df_planet_day_length_copy['length_of_day'].apply(lambda ld: ld / 24)
    print(df_planet_day_length_copy)

#Q7v4()
   

def Q7v5():
    '''Version 5 - using the assign() DataFrame method. It returns a new DataFrame, hence no need to work on a copy.'''
    # add the column obtained by converting the length_of_day in hours to length_of_day in days
    df_planets_amended = df_planets.assign(length_of_day_in_days = df_planets['length_of_day'] / 24)
    print(df_planets_amended[['length_of_day', 'length_of_day_in_days']])

#Q7v5()

    
# Question 8
# ----------
'''
Write a python script that uses Pandas to print a list of planet names and their mass, densities and volumes.
Volume = Mass/Density. 
'''
def Q8():
    # Note: modifying the original DataFrame will always work
    # add a calculated column volume = mass/density to the existing data frame
    df_planets['volume'] = (df_planets['mass'] / df_planets['density'])
    print(df_planets[['planet', 'mass', 'density', 'volume']])

#Q8()


# Question 9
# ----------
'''
List the planets that have the mean temperature 
above the average mean temperature of all planets.
'''
def Q9():
    # find the average mean temperature of all planets
    average_mean_temp = df_planets['mean_temperature'].mean()  # returns -32.111111111111114
    # find planets with mean temperature above the average 
    df_planets.query('mean_temperature > @average_mean_temp')  # returns the rows for Mercury, Venus and Earth

#Q9()


# Question 10
# ----------
'''
List those planets which have more moons than Neptune. Sort the result by number of moons in descending order. 
'''
def Q10v1():
    # Version 1 (by working out the row index POSITION related to Neptune from the
    #             original DataFrame passing this index to ILOC property to find out
    #             Neptune's number of moons)
    
    # filter Neptune only data
    df_neptune_data = df_planets.query("planet == 'Neptune'")
    
    # get Neptune's number of moons (since the above query returns only one record, we can 
    # access it through iloc property, passing to it the index position of that record: 0)
    no_neptune_moons = df_neptune_data['number_of_moons'].iloc[0]
    
    # create a subset of the DataFrame listing the planets which have more moons
    # than Neptune and sort the result by number of moons in descending order
    df_planets_moon_gt_neptune = df_planets[['planet', 'number_of_moons']].query('number_of_moons > @no_neptune_moons').sort_values(by='number_of_moons', ascending=False)
    print(df_planets_moon_gt_neptune)

#Q10v1()


def Q10v2():
    # Version 2 (by working out the row index LABEL related to Neptune from the
    #             original DataFrame passing this index to LOC property to find out
    #             Neptune's number of moons)
    
    # filter Neptune only data
    df_neptune_data = df_planets.query("planet == 'Neptune'")
    
    # retrieve the index label of the row relevant to Neptune in the df_planets DataFrame
    index_range = df_planets.index
    for index in index_range:
        if df_planets['planet'].loc[index] == "Neptune":
            neptune_index = index
            break
        
    # get Neptune's number of moons (since the above query returns only record we can 
    # access it through loc property, passing to it the index label of that record: neptune_index)
    no_neptune_moons = df_neptune_data['number_of_moons'].loc[neptune_index]

    # create a subset of the DataFrame listing the planets which have more moons
    # than Neptune and sort the result by number of moons in descending order
    df_planets_moon_gt_neptune = df_planets[['planet', 'number_of_moons']].query('number_of_moons > @no_neptune_moons').sort_values(by='number_of_moons', ascending=False)
    print(df_planets_moon_gt_neptune)

#Q10v2()


def Q10v3():
    # Version 3 (by working out the row index LABEL related to Neptune from the
    #             original DATA FRAME and passing this index directly to the DataFrame
    #             through chain indexing to find out Neptune's number of moons)
    # create a subset of the DataFrame displaying the values from the planet and number_of_moons columns related to Neptune
    #df_no_neptune_moons = df_planets[['planet', 'number_of_moons']].query('planet=="Neptune"')
    #print("No of Neptune moons DataFrame:\n", df_no_neptune_moons)
    
    # retrieve the index label of the row relevant to Neptune in the df_planets DataFrame
    index_range = df_planets.index
    for index in index_range:
        if df_planets['planet'].loc[index] == "Neptune":
            neptune_index = index
            break

    # retrieve the number of Neptune's moons through chain indexing
    no_neptune_moons = df_planets['number_of_moons'][neptune_index]
    
    # create a subset of the DataFrame listing the planets which have more moons
    # than Neptune and sort the result by number of moons in descending order
    df_planets_moon_gt_neptune = df_planets[['planet', 'number_of_moons']].query('number_of_moons > @no_neptune_moons').sort_values(by='number_of_moons', ascending=False)
    print(df_planets_moon_gt_neptune)

#Q10v3()
    
    
def Q10v4():
    # Version 4 (by working out the row index LABEL related to Neptune from
    #             the SERIES and passing this index directly to the DataFrame
    #             to find outNeptune's number of moons)
    # selection the desired column ('number_of_moons')
    # (one column of a DataFrame is a series object)
    s_planets_names = df_planets['planet']

    # retrieve the index label of the row relevant to Neptune in the s_planets_names series
    index_range = s_planets_names.index
    for index in index_range:
        if s_planets_names[index] == 'Neptune':
            neptune_index = index
            break

    # retrieve the number of moons of Neptune through chain indexing
    no_neptune_moons = df_planets['number_of_moons'][neptune_index]
 
    # list planets which have more moons than Neptune and sort the result by number of moons in descending order
    df_planets_moon_gt_neptune = df_planets[['planet', 'number_of_moons']].query('number_of_moons > @no_neptune_moons').sort_values(by='number_of_moons', ascending=False)
    print(df_planets_moon_gt_neptune)

#Q10v4()


def Q10v5():
    # Version 5 (by working out the row index label related to Neptune
    #             from the condition Series to find out Neptune's number of moons)
    # Use pandas.DataFrame.index to access the index of pandas.DataFrame
    index_range = df_planets.index
    print('\nindex_range:\n', index_range)
    print(type(index_range))

    # subset the index by a condition to get only the index(es) of rows which satisfy the condition. 
    s_condition = df_planets["planet"] == "Neptune"
    print('\condition_series:\n', s_condition)
    print(type(s_condition))
    # create the list of row indices for Neptune
    neptune_indices = index_range[s_condition]
    '''
    # there is only one index for Neptune's row in the list, accessible through [0]
    print('\nNeptune_indices:\n', neptune_indices)
    print('\nNeptune_indices TYPE:\n',type(neptune_indices))
    neptune_index = neptune_indices[0]
    print('\nNeptune_index:\n', neptune_index)
    '''
    # call tolist() on this result to get a list of index(es).
    neptune_indices_list = neptune_indices.tolist()
    neptune_index = neptune_indices_list[0]
    print(neptune_index)
    print(type(neptune_index))
    
    # retrieve the number of moons of Neptune through chain indexing
    no_neptune_moons = df_planets['number_of_moons'][neptune_index]
    print('no_neptune_moons=', no_neptune_moons)

    # list planets which have more moons than Neptune and sort the result by number of moons in descending order
    df_planets_moon_gt_neptune = df_planets[['planet', 'number_of_moons']].query('number_of_moons > @no_neptune_moons').sort_values(by='number_of_moons', ascending=False)
    print(df_planets_moon_gt_neptune)
 
#Q10v5()
    
    
# Question 11
# ----------
'''
Using the titanic built-in dataset, show the number of man, women and children in each passengers class
(the number of each passenger type split by class).
'''
def Q11v1():
    '''Version 1: slicing the original DataFrame to leave only the 3 required columns
       and counting the number of rows for each 'who', 'class' combination'''
    # load the titanic dataset
    df_titanic = sns.load_dataset('titanic')
    
    # slice the titanic DataFrame to include only 'survived', 'who' and 'class' columns
    df_tot_ptypes_per_class = df_titanic[['survived', 'who', 'class']]
    
    # calculate the number of passengers for each different ('who', 'class') combination - using groupby()
    # the calculated values will be placed in the 'survived' column of the resulting DataFrame
    df_tot_ptypes_per_class = df_tot_ptypes_per_class.groupby(['who', 'class']).count()
    
    # rename the 'survived' column to 'total'
    df_tot_ptypes_per_class = df_tot_ptypes_per_class.rename(columns={'survived': 'total'})
    
    # to include the index values and show values in all rows in the DataFrame use the reset_index() method:
    df_tot_ptypes_per_class = df_tot_ptypes_per_class.reset_index()
    
    # display the final DataFrame
    print(df_tot_ptypes_per_class)
    
#Q11v1()


def Q11v2():
    '''Version 2: using groupby() and counting the number of rows for each 'who', 'class' combination'''
    # load the titanic dataset
    df_titanic = sns.load_dataset('titanic')
    
    # calculate the total number of passengers of each passenger type split by class
    # Note: without applying the reset_index() method, the result would have been Series, not a DataFrame.
    df_tot_ptypes_per_class = df_titanic.groupby(['who', 'class'])['survived'].count()
    # the index of each calculated value in the Series (named 'survived')
    # consists of a different value of ('who', 'class') combination
    print("Without reset_index():\n", df_tot_ptypes_per_class)
    print("TYPE:\n", type(df_tot_ptypes_per_class))
    
    # to convert the Series to DataFrame, include the index values
    # and show values in all rows in the DataFrame use the reset_index() method
    df_tot_ptypes_per_class = df_tot_ptypes_per_class.reset_index()
    print("With reset_index():\n", df_tot_ptypes_per_class)
    print("TYPE:\n", type(df_tot_ptypes_per_class))

    # rename the 'survived' column to 'total'
    df_tot_ptypes_per_class = df_tot_ptypes_per_class.rename(columns={'survived': 'total'})
    
    # show the number of passengers of each type per class
    print(df_tot_ptypes_per_class)

#Q11v2()


# Question 12
# ----------
'''
Add and populate two new columns to the above DataFrame: 'survived' and 'died'
and place them to show the type of person, class, 'survived', 'died', 'total'.
'''
def Q12v1():
    '''Version 1: calculate all values using query() and add them to the DataFrame using lists, "pedestrian way"'''
    # load the titanic dataset
    df_titanic = sns.load_dataset('titanic')
    # calculate the total number of survived passengers for each passenger type split by class
    df_tot_ptypes_per_class = df_titanic.groupby(['who', 'class'])['survived'].count().reset_index()
    # rename the 'survived' column to 'total'
    df_tot_ptypes_per_class = df_tot_ptypes_per_class.rename(columns={'survived': 'total'})

    # calculate the total number of survived passengers for each ('who', pclass, 'survived') combination
    # (note that column 'class' cannot be used with queries as 'class' is a Python reserved word); 'pclass' column is used instead
    df_tot_man_1st_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="man" and pclass==1 and survived==1').count()[0]
    df_tot_man_1st_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="man" and pclass==1 and survived==0').count()[0]
    df_tot_man_2nd_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="man" and pclass==2 and survived==1').count()[0]
    df_tot_man_2nd_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="man" and pclass==2 and survived==0').count()[0]
    df_tot_man_3rd_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="man" and pclass==3 and survived==1').count()[0]
    df_tot_man_3rd_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="man" and pclass==3 and survived==0').count()[0]
    df_tot_woman_1st_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="woman" and pclass==1 and survived==1').count()[0]
    df_tot_woman_1st_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="woman" and pclass==1 and survived==0').count()[0]
    df_tot_woman_2nd_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="woman" and pclass==2 and survived==1').count()[0]
    df_tot_woman_2nd_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="woman" and pclass==2 and survived==0').count()[0]
    df_tot_woman_3rd_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="woman" and pclass==3 and survived==1').count()[0]
    df_tot_woman_3rd_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="woman" and pclass==3 and survived==0').count()[0]
    df_tot_child_1st_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="child" and pclass==1 and survived==1').count()[0]
    df_tot_child_1st_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="child" and pclass==1 and survived==0').count()[0]
    df_tot_child_2nd_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="child" and pclass==2 and survived==1').count()[0]
    df_tot_child_2nd_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="child" and pclass==2 and survived==0').count()[0]
    df_tot_child_3rd_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="child" and pclass==3 and survived==1').count()[0]
    df_tot_child_3rd_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="child" and pclass==3 and survived==0').count()[0]
    
    # create a list for survived from these values
    totals_survived =[df_tot_child_1st_1, df_tot_child_2nd_1, df_tot_child_3rd_1,
                      df_tot_man_1st_1, df_tot_man_2nd_1, df_tot_man_3rd_1,
                      df_tot_woman_1st_1, df_tot_woman_2nd_1, df_tot_woman_3rd_1]
    
    # create a list for died from these values
    totals_died = [df_tot_child_1st_0, df_tot_child_2nd_0, df_tot_child_3rd_0,
                   df_tot_man_1st_0, df_tot_man_2nd_0, df_tot_man_3rd_0,
                   df_tot_woman_1st_0, df_tot_woman_2nd_0, df_tot_woman_3rd_0]
    
    # insert the tot_survived column into the DataFrame after the 'class' column
    df_tot_ptypes_per_class.insert(2, "tot_survived", totals_survived)

    # insert the totals_died column into the DataFrame after the 'tot_survived' column
    df_tot_ptypes_per_class.insert(3, "tot_died", totals_died)
    
    # display the number of survived, died and total passengers of each type split by class
    print(df_tot_ptypes_per_class)

#Q12v1()


def Q12v2():
    '''Version 2: create two Series - the first for survived and the second for died passengers of each
    type and class and add them to the DataFrame using merge(), also "pedestrian way"'''
    # load the titanic dataset
    df_titanic = sns.load_dataset('titanic')
    # calculate the total number of survived passengers for each passenger type split by class
    df_tot_ptypes_per_class = df_titanic.groupby(['who', 'class'])['survived'].count().reset_index()
    # rename the 'survived' column to 'total'
    df_tot_ptypes_per_class = df_tot_ptypes_per_class.rename(columns={'survived': 'total'})

    # calculate the total number of survived passengers for each passenger type split by class
    df_tot_man_1st_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="man" and pclass==1 and survived==1').count()[0]
    df_tot_man_1st_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="man" and pclass==1 and survived==0').count()[0]
    df_tot_man_2nd_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="man" and pclass==2 and survived==1').count()[0]
    df_tot_man_2nd_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="man" and pclass==2 and survived==0').count()[0]
    df_tot_man_3rd_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="man" and pclass==3 and survived==1').count()[0]
    df_tot_man_3rd_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="man" and pclass==3 and survived==0').count()[0]
    df_tot_woman_1st_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="woman" and pclass==1 and survived==1').count()[0]
    df_tot_woman_1st_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="woman" and pclass==1 and survived==0').count()[0]
    df_tot_woman_2nd_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="woman" and pclass==2 and survived==1').count()[0]
    df_tot_woman_2nd_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="woman" and pclass==2 and survived==0').count()[0]
    df_tot_woman_3rd_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="woman" and pclass==3 and survived==1').count()[0]
    df_tot_woman_3rd_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="woman" and pclass==3 and survived==0').count()[0]
    df_tot_child_1st_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="child" and pclass==1 and survived==1').count()[0]
    df_tot_child_1st_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="child" and pclass==1 and survived==0').count()[0]
    df_tot_child_2nd_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="child" and pclass==2 and survived==1').count()[0]
    df_tot_child_2nd_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="child" and pclass==2 and survived==0').count()[0]
    df_tot_child_3rd_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="child" and pclass==3 and survived==1').count()[0]
    df_tot_child_3rd_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="child" and pclass==3 and survived==0').count()[0]

    # create a Series for survivors from these values
    s_totals_survived = pd.Series([df_tot_child_1st_1, df_tot_child_2nd_1, df_tot_child_3rd_1,
                                   df_tot_man_1st_1, df_tot_man_2nd_1, df_tot_man_3rd_1,
                                   df_tot_woman_1st_1, df_tot_woman_2nd_1, df_tot_woman_3rd_1],
                                   name='tot_survived')
    
    # create a DataFrame for died from these values
    s_totals_died = pd.Series([df_tot_child_1st_0, df_tot_child_2nd_0, df_tot_child_3rd_0,
                               df_tot_man_1st_0, df_tot_man_2nd_0, df_tot_man_3rd_0,
                               df_tot_woman_1st_0, df_tot_woman_2nd_0, df_tot_woman_3rd_0],
                               name='tot_died')
    
    # add each of these series to the existing DataFrame - using merge()
    # using the indexes from left object (DataFrame) and right object Series as the join key(s) - since they are the same
    df_tot_ptypes_per_class_per_surv = df_tot_ptypes_per_class.merge(s_totals_survived, left_index=True, right_index=True)
    df_tot_ptypes_per_class_per_surv = df_tot_ptypes_per_class_per_surv.merge(s_totals_died, left_index=True, right_index=True)

    # display the number of survived, died and total passengers of each type split by class
    print(df_tot_ptypes_per_class_per_surv)
    # Note: as it is, the DataFrame lists columns in this order: 'who', 'class', 'total', 'tot_survived', 'tot_died'
    # to move the 'total' column in a Pandas dataframe remove the column 
    # from its current place and insert it in the desired position
    total_column = df_tot_ptypes_per_class_per_surv.pop('total')
    # insert the column at the end of the DataFrame
    df_tot_ptypes_per_class_per_surv['total'] = total_column
    # or insert the column in the desired position using insert()
    #df_tot_ptypes_per_class_per_surv.insert(4, 'total', total_column)
    
    # display the final DataFrame
    print(df_tot_ptypes_per_class_per_surv)

#Q12v2()
    
def Q12v3():
    '''Version 3: create two DataFrames - the first for survived and the second for died passengers of each
     type and class and add them to the existing DataFrame using merge(), also "pedestrian way"'''
    # load the titanic dataset
    df_titanic = sns.load_dataset('titanic')
    # calculate the total number of survived passengers for each passenger type split by class
    df_tot_ptypes_per_class = df_titanic.groupby(['who', 'class'])['survived'].count().reset_index()
    # rename the 'survived' column to 'total'
    df_tot_ptypes_per_class = df_tot_ptypes_per_class.rename(columns={'survived': 'total'})

    # calculate the total number of survived passengers for each passenger type split by class
    df_tot_man_1st_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="man" and pclass==1 and survived==1').count()[0]
    df_tot_man_1st_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="man" and pclass==1 and survived==0').count()[0]
    df_tot_man_2nd_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="man" and pclass==2 and survived==1').count()[0]
    df_tot_man_2nd_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="man" and pclass==2 and survived==0').count()[0]
    df_tot_man_3rd_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="man" and pclass==3 and survived==1').count()[0]
    df_tot_man_3rd_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="man" and pclass==3 and survived==0').count()[0]
    df_tot_woman_1st_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="woman" and pclass==1 and survived==1').count()[0]
    df_tot_woman_1st_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="woman" and pclass==1 and survived==0').count()[0]
    df_tot_woman_2nd_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="woman" and pclass==2 and survived==1').count()[0]
    df_tot_woman_2nd_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="woman" and pclass==2 and survived==0').count()[0]
    df_tot_woman_3rd_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="woman" and pclass==3 and survived==1').count()[0]
    df_tot_woman_3rd_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="woman" and pclass==3 and survived==0').count()[0]
    df_tot_child_1st_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="child" and pclass==1 and survived==1').count()[0]
    df_tot_child_1st_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="child" and pclass==1 and survived==0').count()[0]
    df_tot_child_2nd_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="child" and pclass==2 and survived==1').count()[0]
    df_tot_child_2nd_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="child" and pclass==2 and survived==0').count()[0]
    df_tot_child_3rd_1 = df_titanic[['survived', 'who', 'pclass']].query('who=="child" and pclass==3 and survived==1').count()[0]
    df_tot_child_3rd_0 = df_titanic[['survived', 'who', 'pclass']].query('who=="child" and pclass==3 and survived==0').count()[0]

    # create a DataFrame for survivors from these values
    df_totals_survived = pd.DataFrame({'who': ['child', 'child', 'child', 
                                               'man', 'man', 'man',
                                               'woman', 'woman', 'woman',],
                                       'class': ['First', 'Second', 'Third',
                                                 'First', 'Second', 'Third',
                                                 'First', 'Second', 'Third'],
                                       'tot_survived': [df_tot_child_1st_1, df_tot_child_2nd_1, df_tot_child_3rd_1,
                                                        df_tot_man_1st_1, df_tot_man_2nd_1, df_tot_man_3rd_1,
                                                        df_tot_woman_1st_1, df_tot_woman_2nd_1, df_tot_woman_3rd_1]
    })

    # create a DataFrame for died from these values
    df_totals_died = pd.DataFrame({'who': ['child', 'child', 'child', 
                                           'man', 'man', 'man',
                                           'woman', 'woman', 'woman',],
                                   'class': ['First', 'Second', 'Third',
                                             'First', 'Second', 'Third',
                                             'First', 'Second', 'Third'],
                                   'tot_died': [df_tot_child_1st_0, df_tot_child_2nd_0, df_tot_child_3rd_0,
                                                df_tot_man_1st_0, df_tot_man_2nd_0, df_tot_man_3rd_0,
                                                df_tot_woman_1st_0, df_tot_woman_2nd_0, df_tot_woman_3rd_0]
    })
    
    # merge each of these data frames with the existing DataFrame - using merge()
    # using the indexes from left object (DataFrame) and right object DataFrame as the join key(s) - since they are the same
    df_tot_ptypes_per_class_per_surv = df_tot_ptypes_per_class.merge(df_totals_survived)
    df_tot_ptypes_per_class_per_surv = df_tot_ptypes_per_class_per_surv.merge(df_totals_died)

    # move the 'total' column at the end: remove the column 
    # from its current place and insert it in the desired position
    total_column = df_tot_ptypes_per_class_per_surv.pop('total')
    # insert the column at the end of the DataFrame
    df_tot_ptypes_per_class_per_surv['total'] = total_column
    # or insert the column in the desired position using insert()
    #df_tot_ptypes_per_class_per_surv.insert(4, 'total', total_column)
    
    # display the number of survived, died and total passengers of each type split by class
    print(df_tot_ptypes_per_class_per_surv)
    
#Q12v3()


def Q12v4():
    '''Version 4: using groupby()'''
    # load the titanic dataset
    df_titanic = sns.load_dataset('titanic')
    #print(df_titanic.columns)
    # calculate the total number of passengers of each passenger type split by class
    df_tot_ptypes_per_class_per_surv = df_titanic.groupby(['who', 'class', 'survived']).count().reset_index()
    # the resulting DataFrame shows correctly calculated values in all columns except for the three grouped by columns
    # all the required information is there, but displayed in one column;
    # we need to move it to different columns - using horizontal slicing
    # rename the 'pclass' column to 'total'
    df_tot_ptypes_per_class_per_surv = df_tot_ptypes_per_class_per_surv.rename(columns={'pclass': 'total'})
    # slice the resulting DataFrame to show only 'who', 'class', 'survived' and the renamed 'pclass' column
    df_tot_ptypes_per_class_per_surv = df_tot_ptypes_per_class_per_surv[['who', 'class', 'survived', 'total']]
    # show the number of passengers of each type per class
    #print(df_tot_ptypes_per_class_per_surv)
    # slice the data frame horizontally (extract rows for survivors and non-survivors)
    df_tot_ptypes_per_class_per_1 = df_tot_ptypes_per_class_per_surv.query('survived==1')
    df_tot_ptypes_per_class_per_0 = df_tot_ptypes_per_class_per_surv.query('survived==0')
    
    # merge the two data frames into one through the common columns ('who', 'class')
    df_totals = df_tot_ptypes_per_class_per_1.set_index(['who', 'class']).join(df_tot_ptypes_per_class_per_0.set_index(['who', 'class']), lsuffix='_survived', rsuffix='_died')
 
    # insert the new 'totals' column obtained by adding up the values from 'total_survived' and 'total_died' columns
    df_totals['total'] = df_totals['total_survived'] + df_totals ['total_died']
 
    # the survived columns are not needed any more - remove them
    df_totals.pop('survived_survived')
    df_totals.pop('survived_died')

    print(df_totals)
    
#Q12v4()

    
# Question 13
# -----------
"""
Using the 'titanic' Seaborn built-in dataset, calculate the number of passengers 
by class, for each value of survival (0, 1), split by each age group, following
the sinking of the titanic
a) creating a new data frame using queries, consisting of the following columns:
   class, age_range, survived and a column listing the number of passengers for
   each (class, survived, age_range) combination
b) creating and populating a new column within the existing data frame
   step 1: define a function set_age_range() that will populate the new column
           'age_range' with the different age ranges, as defined below 
   step 2: create a new column in the titanic data frame  and populate it passing
           the custom-made set_age_range() function to the apply() method
c) creating and populating a new column within the existing data frame, but using
   the built-in Pandas function cut() instead of applying the custom-made function
   to populate the column. Use the where() NumPy function to replace NaN values
   with 'unknown' in the age_range column.
Categorise the age ranges using the following categories:
0-18
18-25
26-34
35-44
45-54
55-64
65+
unknown
"""
# There are three ways of working out the age range for each age:
#    a) creating a new data frame using queries, 'pedestrian way'. The new data frame will
#       consist of just the columns that we need: class, survived, age_range and a column
#       listing the number of passengers for each (class, survived, age_range) combination.
#    b) creating and populating a new column within the existing data frame to show the age
#       range for each age in df_titanic - using the apply() Pandas method and passing to it the
#       custom-made function that determines the age range for an age passed to it as parameter
#    c) creating and populating a new column within the existing data frame, but using the
#       built-in Pandas function cut() instead of applying the custom-made function to 
#       populate the column. Use the where() NumPy function to replace NaN values with 
#       'unknown' in the age_range column.
# Solutions 13a_v1, 13a_v2 and 13a_v3 follow the 1st way; solution 13b follows the 2nd way;
# solution 13c follows the 3rd way

# Question 13a - 1st version: creating a new data frame using queries, extremely 'pedestrian' way
# --------------------------
# create data series, storing the total number of survivors
# calculate the number of survived passengers from each age group by class
# Note: the variable 'class' cannot be used as it is a Python keyword - there are
# 2 possibilities to resolve this problem:
# 1) use the column pclass instead of class (it has values 1, 2, 3 instead of 'First', 'Second', 'Third')
# 2) rename the class column and use the renamed column
# The solutions Q13a_v1, Q13a_v2 & Q13b follow the 1st idea; the 2nd idea is implemented in the solution Q13a_v3.
# Note also that instead of the 'survived' column we could use the 'alive' column,
# which has values 'No' and 'Yes' instead of the less user-friendly values 0 and 1
# (this is also implemented in the solution Q13a_v3)
# calculating values for every age group of the survived passengers from the 1st class
def Q13a_v1():
    # load the titanic dataset
    df_titanic = sns.load_dataset('titanic')

    # calculating values for every age group of the survived passengers from the 1st class
    survived_1st_unknown = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==1 and age.isnull()').count()
    survived_1st_lt18 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==1 and age<18').count()
    survived_1st_18to25 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==1 and age>=18 and age<=25').count()
    survived_1st_26to34 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==1 and age>=26 and age<=34').count()
    survived_1st_35to44 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==1 and age>=35 and age<=44').count()
    survived_1st_45to54 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==1 and age>=45 and age<=54').count()
    survived_1st_55to64 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==1 and age>=55 and age<=64').count()
    survived_1st_gte65 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==1 and age>=65').count()
    # calculating values for every age group of the survived passengers from the 2nd class
    survived_2nd_unknown = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==2 and age.isnull()').count()
    survived_2nd_lt18 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==2 and age<18').count()
    survived_2nd_18to25 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==2 and age>=18 and age<=25').count()
    survived_2nd_26to34 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==2 and age>=26 and age<=34').count()
    survived_2nd_35to44 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==2 and age>=35 and age<=44').count()
    survived_2nd_45to54 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==2 and age>=45 and age<=54').count()
    survived_2nd_55to64 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==2 and age>=55 and age<=64').count()
    survived_2nd_gte65 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==2 and age>=65').count()
    # calculating values for every age group of the survived passengers from the 3rd class
    survived_3rd_unknown = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==3 and age.isnull()').count()
    survived_3rd_lt18 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==3 and age<18').count()
    survived_3rd_18to25 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==3 and age>=18 and age<=25').count()
    survived_3rd_26to34 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==3 and age>=26 and age<=34').count()
    survived_3rd_35to44 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==3 and age>=35 and age<=44').count()
    survived_3rd_45to54 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==3 and age>=45 and age<=54').count()
    survived_3rd_55to64 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==3 and age>=55 and age<=64').count()
    survived_3rd_gte65 = df_titanic[['survived', 'pclass', 'age']].query('survived==1 and pclass==3 and age>=65').count()
    # calculating values for every age group of the non-survived passengers from the 1st class
    not_survived_1st_unknown = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==1 and age.isnull()').count()
    not_survived_1st_lt18 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==1 and age<18').count()
    not_survived_1st_18to25 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==1 and age>=18 and age<26').count()
    not_survived_1st_26to34 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==1 and age>=26 and age<35').count()
    not_survived_1st_35to44 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==1 and age>=35 and age<45').count()
    not_survived_1st_45to54 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==1 and age>=45 and age<55').count()
    not_survived_1st_55to64 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==1 and age>=55 and age<65').count()
    not_survived_1st_gte65 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==1 and age>=65').count()
    # calculating values for every age group of the non-survived passengers from the 2nd class
    not_survived_2nd_unknown = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==2 and age.isnull()').count()
    not_survived_2nd_lt18 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==2 and age<18').count()
    not_survived_2nd_18to25 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==2 and age>=18 and age<26').count()
    not_survived_2nd_26to34 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==2 and age>=26 and age<35').count()
    not_survived_2nd_35to44 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==2 and age>=35 and age<45').count()
    not_survived_2nd_45to54 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==2 and age>=45 and age<55').count()
    not_survived_2nd_55to64 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==2 and age>=55 and age<65').count()
    not_survived_2nd_gte65 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==2 and age>=65').count()
    # calculating values for every age group of the non-survived passengers from the 3rd class
    not_survived_3rd_unknown = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==3 and age.isnull()').count()
    not_survived_3rd_lt18 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==3 and age<18').count()
    not_survived_3rd_18to25 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==3 and age>=18 and age<26').count()
    not_survived_3rd_26to34 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==3 and age>=26 and age<35').count()
    not_survived_3rd_35to44 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==3 and age>=35 and age<45').count()
    not_survived_3rd_45to54 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==3 and age>=45 and age<55').count()
    not_survived_3rd_55to64 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==3 and age>=55 and age<65').count()
    not_survived_3rd_gte65 = df_titanic[['survived', 'pclass', 'age']].query('survived==0 and pclass==3 and age>=65').count()

    # create the data frame with these calculated values
    df_totals = pd.DataFrame({
       'p_survived': [1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 1,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0],
       'p_class': ['First', 'First', 'First', 'First', 'First', 'First', 'First', 'First',
                   'Second', 'Second', 'Second', 'Second', 'Second', 'Second', 'Second', 'Second',
                   'Third', 'Third', 'Third', 'Third', 'Third', 'Third', 'Third', 'Third',
                   'First', 'First', 'First', 'First', 'First', 'First', 'First', 'First',
                   'Second', 'Second', 'Second', 'Second', 'Second', 'Second', 'Second', 'Second',
                   'Third', 'Third', 'Third', 'Third', 'Third', 'Third', 'Third', 'Third'],
       'p_age_range': ['unknown', '0-18', '18-25', '26-34', '35-44', '45-54', '55-64', '>=65',
                       'unknown', '0-18', '18-25', '26-34', '35-44', '45-54', '55-64', '>=65',
                       'unknown', '0-18', '18-25', '26-34', '35-44', '45-54', '55-64', '>=65',
                       'unknown', '0-18', '18-25', '26-34', '35-44', '45-54', '55-64', '>=65',
                       'unknown', '0-18', '18-25', '26-34', '35-44', '45-54', '55-64', '>=65',
                       'unknown', '0-18', '18-25', '26-34', '35-44', '45-54', '55-64', '>=65'],
        # Note: the counts obtained above are series;
        # to return the actual percentages only use subscript operator:
       'p_count': [survived_1st_unknown[0], survived_1st_lt18[0], survived_1st_18to25[0], survived_1st_26to34[0], 
                   survived_1st_35to44[0], survived_1st_45to54[0], survived_1st_55to64[0], survived_1st_gte65[0],
                   survived_2nd_unknown[0], survived_2nd_lt18[0], survived_2nd_18to25[0], survived_2nd_26to34[0], 
                   survived_2nd_35to44[0], survived_2nd_45to54[0], survived_2nd_55to64[0], survived_2nd_gte65[0],
                   survived_3rd_unknown[0], survived_3rd_lt18[0], survived_3rd_18to25[0], survived_3rd_26to34[0], 
                   survived_3rd_35to44[0], survived_3rd_45to54[0], survived_3rd_55to64[0], survived_3rd_gte65[0],
                   not_survived_1st_unknown[0], not_survived_1st_lt18[0], not_survived_1st_18to25[0], not_survived_1st_26to34[0], 
                   not_survived_1st_35to44[0], not_survived_1st_45to54[0], not_survived_1st_55to64[0], not_survived_1st_gte65[0],
                   not_survived_2nd_unknown[0], not_survived_2nd_lt18[0], not_survived_2nd_18to25[0], not_survived_2nd_26to34[0], 
                   not_survived_2nd_35to44[0], not_survived_2nd_45to54[0], not_survived_2nd_55to64[0], not_survived_2nd_gte65[0],             
                   not_survived_3rd_unknown[0], not_survived_3rd_lt18[0], not_survived_3rd_18to25[0], not_survived_3rd_26to34[0], 
                   not_survived_3rd_35to44[0], not_survived_3rd_45to54[0], not_survived_3rd_55to64[0], not_survived_3rd_gte65[0]             
                  ]
    })
    
    # display the final DataFrame
    print(df_totals)

Q13a_v1()


# Question 13a - 2nd version: creating a new data frame using queries, slightly less 'pedestrian' way
# --------------------------
# Same idea as in 13a_v1, but using loops to populate the dictionary with values of pclass and 
# survived columns. unique() function is used to find unique values in pclass and survived columns.
def Q13a_v2():
    # load the titanic dataset
    df_titanic = sns.load_dataset('titanic')

    # find the different values from the 'survived' and 'p_class' columns
    # (sorting ensures that values appear in DataFrame in the desired order;
    # in order to apply sort() method values need to be converted from NumPy
    # array to list - using tolist() function)
    # Note: different values from the 'class' column are needed to populate the dictionary
    # and the DataFrame with values 'First', 'Second' and 'Third' instead of 1, 2, 3
    arr_survived = df_titanic['survived'].unique().tolist()
    arr_survived.sort()
    arr_pclass = df_titanic['pclass'].unique().tolist()
    arr_pclass.sort()
    arr_class = df_titanic['class'].unique().tolist()
    arr_class.sort()
    
    # initialise the dictionary of lists
    totals_dict = {'class':[],
                   'survived':[],
                   'age_range':[],
                   'count':[]}

    # loop through the different values of p_survived and p_class columns
    for value_pclass in arr_pclass:
        for value_survived in arr_survived:
            # calculating values for every age group of every different value of p_survived survived and p_class columns 
            age_lt18    = df_titanic[['survived', 'pclass', 'age']].query("survived==@value_survived and pclass==@value_pclass and age<18").count()
            age_18to25  = df_titanic[['survived', 'pclass', 'age']].query("survived==@value_survived and pclass==@value_pclass and age>=18 and age<=25").count()
            age_26to34  = df_titanic[['survived', 'pclass', 'age']].query("survived==@value_survived and pclass==@value_pclass and age>=26 and age<=34").count()
            age_35to44  = df_titanic[['survived', 'pclass', 'age']].query("survived==@value_survived and pclass==@value_pclass and age>=35 and age<=44").count()
            age_45to54  = df_titanic[['survived', 'pclass', 'age']].query("survived==@value_survived and pclass==@value_pclass and age>=45 and age<=54").count()
            age_55to64  = df_titanic[['survived', 'pclass', 'age']].query("survived==@value_survived and pclass==@value_pclass and age>=55 and age<=64").count()
            age_gte65   = df_titanic[['survived', 'pclass', 'age']].query("survived==@value_survived and pclass==@value_pclass and age>=65").count()
            age_unknown = df_titanic[['survived', 'pclass', 'age']].query("survived==@value_survived and pclass==@value_pclass and age.isnull()").count()
            
            # prepare data for the DataSet (populate the dictionary of lists)
            for index in range(8):  # there are 8 age ranges
                # assign the class value for the corresponding pclass value
                # (i.e. 'First' for 1, 'Second' for 2, 'Third' for 3)
                totals_dict['class'].append(arr_class[arr_pclass.index(value_pclass)])
                totals_dict['survived'].append(value_survived)
            totals_dict['age_range'].append('0-18')
            totals_dict['age_range'].append('18-25')
            totals_dict['age_range'].append('26-34')
            totals_dict['age_range'].append('35-44')
            totals_dict['age_range'].append('45-54')
            totals_dict['age_range'].append('55-64')
            totals_dict['age_range'].append('>=65')
            totals_dict['age_range'].append('unknown')
            # Note: the counts obtained above are series;
            # to return the actual percentages only use subscript operator:
            totals_dict['count'].append(age_lt18[0])
            totals_dict['count'].append(age_18to25[0])
            totals_dict['count'].append(age_26to34[0])
            totals_dict['count'].append(age_35to44[0])
            totals_dict['count'].append(age_45to54[0])
            totals_dict['count'].append(age_55to64[0])
            totals_dict['count'].append(age_gte65[0])
            totals_dict['count'].append(age_unknown[0])

    # create the DataFrame from the dictionary
    df_totals = pd.DataFrame(totals_dict)
    # provide the customised order in which age_range values ought to appear within
    # the dataframe: '0-18','18-25','26-34','35-44','45-54','55-64','65+','unknown'
    df_totals.age_range = pd.Categorical(df_totals.age_range, categories=['0-18','18-25','26-34','35-44','45-54','55-64','>=65','unknown'])
    
    # settings necessary to display the untruncated DataFrame
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    # display the final DataFrame
    print(df_totals)

Q13a_v2()


# Question 13a - 3rd version: creating a new data frame using queries, slightly less 'pedestrian' way
# --------------------------
# The only difference between this solution and solution Q13a_v2
# is that this solution renames column 'class' to 'p_class', as the
# variable name 'class' cannot ne used, being a Python keyword.
# To make the output more user friendly, instead of the 'survived'
# column, the 'alive' column is used, which has values 'No' and
# 'Yes' instead of the less user-friendly values 0 and 1
def Q13a_v3():
    # load the titanic dataset
    df_titanic = sns.load_dataset('titanic')
    #print(df_titanic.columns.tolist())
    
    # rename the class column ('class' cannot be used as it is Python keyword)
    df_titanic = df_titanic.rename(columns={'class': 'p_class'})
    #print(df_titanic.columns.tolist())
    # find and sort the different values from the alive and p_class columns
    # (sorting ensures that values appear in DataFrame in the desired order;
    # in order to apply sort() method values need to be converted from NumPy
    # array to list - using tolist() function)
    arr_alive = df_titanic['alive'].unique().tolist()
    arr_alive.sort()
    arr_p_class = df_titanic['p_class'].unique().tolist()
    arr_p_class.sort()
    
    # initialise the dictionary of lists
    totals_dict = {'class':[],
                   'alive':[],
                   'age_range':[],
                   'count':[]}

    # loop through the different values of alive and p_class columns
    for value_p_class in arr_p_class:
        for value_alive in arr_alive:
            # calculating values for every age group of every different value of p_alive alive and p_class columns 
            age_lt18    = df_titanic[['alive', 'p_class', 'age']].query("alive==@value_alive and p_class==@value_p_class and age<18").count()
            age_18to25  = df_titanic[['alive', 'p_class', 'age']].query("alive==@value_alive and p_class==@value_p_class and age>=18 and age<=25").count()
            age_26to34  = df_titanic[['alive', 'p_class', 'age']].query("alive==@value_alive and p_class==@value_p_class and age>=26 and age<=34").count()
            age_35to44  = df_titanic[['alive', 'p_class', 'age']].query("alive==@value_alive and p_class==@value_p_class and age>=35 and age<=44").count()
            age_45to54  = df_titanic[['alive', 'p_class', 'age']].query("alive==@value_alive and p_class==@value_p_class and age>=45 and age<=54").count()
            age_55to64  = df_titanic[['alive', 'p_class', 'age']].query("alive==@value_alive and p_class==@value_p_class and age>=55 and age<=64").count()
            age_gte65   = df_titanic[['alive', 'p_class', 'age']].query("alive==@value_alive and p_class==@value_p_class and age>=65").count()
            age_unknown = df_titanic[['alive', 'p_class', 'age']].query("alive==@value_alive and p_class==@value_p_class and age.isnull()").count()
            
            # prepare data for the DataSet (populate the dictionary of lists)
            for index in range(8):  # there are 8 age ranges
                totals_dict['class'].append(value_p_class)
                totals_dict['alive'].append(value_alive)
            totals_dict['age_range'].append('0-18')
            totals_dict['age_range'].append('18-25')
            totals_dict['age_range'].append('26-34')
            totals_dict['age_range'].append('35-44')
            totals_dict['age_range'].append('45-54')
            totals_dict['age_range'].append('55-64')
            totals_dict['age_range'].append('>=65')
            totals_dict['age_range'].append('unknown')
            # Note: the counts obtained above are series;
            # to return the actual percentages only use subscript operator:
            totals_dict['count'].append(age_lt18[0])
            totals_dict['count'].append(age_18to25[0])
            totals_dict['count'].append(age_26to34[0])
            totals_dict['count'].append(age_35to44[0])
            totals_dict['count'].append(age_45to54[0])
            totals_dict['count'].append(age_55to64[0])
            totals_dict['count'].append(age_gte65[0])
            totals_dict['count'].append(age_unknown[0])

    # create the DataFrame from the dictionary
    df_totals = pd.DataFrame(totals_dict)
    
    # provide the customised order in which age_range values ought to appear within
    # the dataframe: '0-18','18-25','26-34','35-44','45-54','55-64','65+','unknown'
    df_totals.age_range = pd.Categorical(df_totals.age_range, categories=['0-18','18-25','26-34','35-44','45-54','55-64','>=65','unknown'])
    
    # display the final DataFrame
    print(df_totals)

Q13a_v3()

# Question 13b: creating and populating a new column within the existing data frame
# ------------
# step 1: define a function that will populate the new column 'age_range'
def set_age_range(age):
    if age >= 65:
        return '65+'
    elif age >=55:
        return '55-64'
    elif age >=45:
        return '45-54'
    elif age >= 35:
        return '35-44'
    elif age >= 26:
        return '26-34'
    elif age >= 18:
        return '18-25'
    elif age >= 0:
        return '0-18'
    else:
        # NaN value
        return 'unknown'

# step 2: create a new column in the df_titanic data frame
# and populate it passing the custom made set_age_range() function
# to the apply() method. Then use the Categorical() function to
# sort values in age_range column in a custom order, and calculate
# the number of rows for each (class, survived, age_range) combination
# using groupby().
def Q13b():
    # show all column and row names (avoid truncation)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    
    # load the titanic dataset
    df_titanic = sns.load_dataset('titanic')
    #print(df_titanic.dtypes)

    # use the custom-made set_age_range function to create and
    # populate the 'age_range' column with different age ranges
    df_titanic['age_range'] = df_titanic['age'].apply(set_age_range)
   
    # create a dataframe with age_range values sorted in custom order:
    # 'unknown','0-18','18-25','26-34','35-44','45-54','55-64','65+'
    df_titanic.age_range = pd.Categorical(df_titanic.age_range, categories=['0-18','18-25','26-34','35-44','45-54','55-64','65+','unknown'])
    
    # calculate the number of survived and non-survived passengers of each class split by each age range
    df_titanic = df_titanic.groupby(['class', 'survived', 'age_range']).count()
    # the resulting DataFrame consists of one index composed of different values
    # of the grouped by columns ('class','survived','age_range') and most of the
    # remaining columns with calculated values in place of their original values
    # note however that not all columns have the same value for 'unknown': 'age',
    # and 'deck' columns have different values...
    # rename any of the columns with correct calculated values to 'Total',
    # (any except from 'age' and 'deck', e.g. 'pclass' column)
    df_titanic = df_titanic.rename(columns={'pclass': 'total'})
  
    # reset the index and split the index into columns,
    # to obtain the DataFrame consisting of all (4) required columns
    # including the newly calculated 'total' column
    df_titanic = df_titanic.reset_index()
    
    # slice the fdm DataFrame to include only required columns
    df_titanic = df_titanic[['class', 'survived', 'age_range', 'total']]
    
    # show the number of passengers of each type per class
    print(df_titanic)

Q13b()

# Note: a 'cleaner' and more efficient solution, avoiding the situation
# where not all columns have the same value for 'unknown', and loading
# only required columns from the titanic dataset, would be the following:
def Q13b_improved():  
    # load only required columns from the titanic dataset
    df_titanic = sns.load_dataset('titanic')[['class', 'survived', 'age']]

    # use the custom-made set_age_range function to create and
    # populate the 'age_range' column with different age ranges
    df_titanic['age_range'] = df_titanic['age'].apply(set_age_range)
   
    # create a dataframe with age_range values sorted in custom order:
    # '0-18','18-25','26-34','35-44','45-54','55-64','65+','unknown'
    df_titanic.age_range = pd.Categorical(df_titanic.age_range, categories=['0-18','18-25','26-34','35-44','45-54','55-64','65+','unknown'])
    
    # remove the 'age'column, as it is not needed any more
    del df_titanic['age']

    # add the new column 'total', to be populated with the totals
    # for each ('class','survived','age_range') combination
    df_titanic['total'] = 0
    
    # calculate the number of survived and non-survived passengers of each class for each age range
    df_titanic = df_titanic.groupby(['class', 'survived', 'age_range']).count()
  
    # reset the index and split the index into columns,
    # to obtain the DataFrame consisting of all (4) required columns
    # including the newly calculated 'total' column
    df_titanic = df_titanic.reset_index()
       
    # show the number of passengers of each type per class
    print(df_titanic)

Q13b_improved()

# Question 13c: using Pandas cut() and NumPy's where() function
# ------------
import numpy as np
def Q13c():
    # load only required columns from the titanic dataset
    df_titanic = sns.load_dataset('titanic')[['class', 'survived', 'age']]
    
    # create the new column (series): age_range_data containing categories for each range
    age_range_data = pd.cut(df_titanic['age'], bins=[0, 18, 26, 35, 45, 55, 65, 120],
                            right=False, include_lowest=True, labels=['0-18', '18-25', '26-34', '35-44', '45-54', '55-64', '65+'])
    
    # replace NaN values with 'unknown'; leave the remaining values unchanged
    # Note: Series is a 1-D array, hence NumPy functions can be applied to Series
    age_range_data = np.where(age_range_data.isna(), 'unknown', age_range_data)  # note: isnull() can be used instead of isna()
    
    # assign the new column 'age_range' to existing DataFrame with values 
    # stored in a 1D NumPy array age_range_data to the existing DataFrame
    df_titanic = df_titanic.assign(age_range=age_range_data)

    # remove the 'age'column, as it is not needed any more
    del df_titanic['age']

    # add the new column 'total', to be populated with the totals
    # for each ('class','survived','age_range') combination
    df_titanic['total'] = 0
    
    # calculate the number of survived and non-survived passengers of each class for each age range
    df_titanic = df_titanic.groupby(['class', 'survived', 'age_range']).count()

    # the resulting DataFrame consists of one index composed of different values
    # of the grouped by columns ('class','survived','age_range') and one column
    # named 'age' containing the totals for each ('class','survived','age_range')
    # combination - rename the 'age' column to 'total'
    df_titanic = df_titanic.rename(columns={'age': 'total'})
    
    # reset the index and split the index into columns,
    # to obtain the DataFrame consisting of all (4) required columns
    # including the newly calculated 'total' column
    df_titanic = df_titanic.reset_index()
    
    # display the final DataFrame
    print(df_titanic)
    
Q13c()