# find this here: /Users/apple/Documents/coding/companies/FDM/FDM_training/FDM_Python_2/exercise_answers_ovando
import subprocess
import pandas as pd
try: 
    import seaborn as sns
except: 
    # Install numpy if they do not have it installed already
    import pip 
    pip.main(['install', 'seaborn'])
    import seaborn as sns


# pandas
#ex3B
# importing .txt file? as csv? 
# Create the DataFrame from the 'planets.txt' file present 
df_planets = pd.read_csv('/Users/apple/Documents/coding/companies/FDM/FDM_training/FDM_Python_2/Exercises/planets.txt')

'''
# display all the column headers of the data frame
print(df_planets.columns.values)


#1 Think about correlations that might exists for the planets dataset.

#1a Is there a correlation between the mass of a planet 
def Q1a(df_planets):
    print(df_planets.corr())

    print(df_planets[['planet', 'mass', 'gravity']].sort_values(by='mass', ascending=False))

Q1a(df_planets)

#1b How about the mass of the planet and the number of moons orbiting that planet?
def Q1b(df_planets):
    print(df_planets.corr())

    print(df_planets[['planet', 'mass', 'number_of_moons']].sort_values(by='mass', ascending=False))

Q1b(df_planets)

#1c. Or the mass of a planet and the distance of the planet from the sun?
def Q1b(df_planets):
    print(df_planets.corr())

    print(df_planets[['planet', 'mass', 'distance_from_sun']].sort_values(by='mass', ascending=False))

Q1b(df_planets)


#2 Use Pandas to list the first 3 closest planets to the sun, sorted in ascending order (the closest first).

def Q2(df_planets):
    # using the head() function, passing the number of rows to retrieve - here 3
    print(df_planets[['planet', 'distance_from_sun']].sort_values(by='distance_from_sun', ascending=True).head(3))

Q2(df_planets)
'''

#3 You are provided with a file called planet_colours.csv.Examineitscontents, you will see that the file contains a list of 
# all the planets and their colours. Your job is to merge the initial DataFrame provided with another DataFrame based 
# on this new file and output a list of planet name, mass, and the planets colours.



def Q3(df_planets):
    '''Common tasks for all 4 versions of solution to this question'''
    # create the first data frame, as a slice of the original df_planets DataFrame, listing planets with their mass:
    df_planet_mass = df_planets[['planet', 'mass']]

    # load the second data frame from file, listing planets with their colour:
    df_planet_colours = pd.read_csv('/Users/apple/Documents/coding/companies/FDM/FDM_training/FDM_Python_2/Exercises/planet_colours.csv')

    print(df_planet_colours)

    # return both data frames
    return df_planet_mass, df_planet_colours

print(Q3(df_planets))

