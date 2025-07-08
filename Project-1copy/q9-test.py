"""
  #####                                                 #####  
 #     # #    # ######  ####  ##### #  ####  #    #    #     # 
 #     # #    # #      #        #   # #    # ##   #    #     # 
 #     # #    # #####   ####    #   # #    # # #  #     #### #  
 #   # # #    # #           #   #   # #    # #  # #          # 
 #    #  #    # #      #    #   #   # #    # #   ##          # 
  #### #  ####  ######  ####    #   #  ####  #    #     #####  
                                                               
 #     #                   #######                             
 #     # #    # # #####       #    ######  ####  #####  ####   
 #     # ##   # #   #         #    #      #        #   #       
 #     # # #  # #   #         #    #####   ####    #    ####   
 #     # #  # # #   #         #    #           #   #        #  
 #     # #   ## #   #         #    #      #    #   #   #    #  
  #####  #    # #   #         #    ######  ####    #    ####   

"""

FILE = 'q9'       # Do NOT Include the .py
FUNCTION = 'summary_grades_2021_UK'

import os
import sys
import unittest
import warnings  # needed for setUpClass() class method
import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal

# Do not show the Traceback error
__unittest = True

# Check if the user has put their code in the correct file name
print('----------------------------------------------------------------------')
if not os.path.isfile(FILE+'.py'):
    print('The file "'+FILE+'.py" does not exist')
    print('\nFAILED (errors=1)')
    sys.exit(2)

# Check that there are no unreadable characters within the function
f = open(FILE+'.py', 'r')
try:
    text = f.read().replace(' ', '')
except:
    print("Error reading file "+FILE+'.py'+"\nMake sure there are no styled characters, such as single/double quotes or dash symbols.\nPython does not recognise such characters.")
    f.close()
    sys.exit(3)

# Check if the the function name is correct 
f = open(FILE+'.py', 'r')
text = f.read().replace(' ', '')
f.close()
if 'def'+FUNCTION+'(' not in text:
    print('The function "'+FUNCTION+'" does not exist in file: '+FILE+'.py')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(4)

# If the function exists but does not import then there are syntax errors
try:
    from q9 import summary_grades_2021_UK as test_function
except:
    print('The function "'+FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    sys.exit(5)


class UnitTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore")
    
    # Only show custom message
    def setUp(self):
        self.longMessage = False

    # error message related only to opening the input file for reading
    def explanation(self, input_file, output, result):
        message = FUNCTION+'('+input_file.replace(' ','')+')'
        message = '\n\nFor the input file '+input_file+' the output is '+output+' - You returned '+str(result)
        if not isinstance(result, str):
            message = message+'\n\nReturned value must be a string'
        return message
    
    def test_fdm_training_data_2021_UK(self):
        input_file = 'fdm_training_data_2021.csv'
        academies = ['London', 'Leeds', 'Glasgow']
        output_list = [('London', 6802, 2991, 2172, 970, 669),
                       ('Leeds', 3249, 1184, 1199, 622, 244),
                       ('Glasgow', 3241, 1399, 1190, 400, 252)]
        output_df = pd.DataFrame(output_list, columns=['Academy', 'Total No. Exams', 'Distinction', 'Merit', 'Pass', 'Fail'])
        result = test_function(input_file, academies)
        assert_frame_equal(output_df, result)

    def test_fdm_training_data_2021_EU(self):
        input_file = 'fdm_training_data_2021.csv'
        academies = ['Frankfurt', 'Poland', 'Luxembourg']
        output_list = [('Frankfurt', 1081, 613, 298, 116, 54),
                       ('Poland', 227, 135, 71, 20, 1),
                       ('Luxembourg', 166, 61, 86, 17, 2)]
        output_df = pd.DataFrame(output_list, columns=['Academy', 'Total No. Exams', 'Distinction', 'Merit', 'Pass', 'Fail'])
        result = test_function(input_file, academies)
        assert_frame_equal(output_df, result)

    def test_fdm_training_data_2021_North_America(self):
        input_file = 'fdm_training_data_2021.csv'
        academies = ['Arlington', 'Austin', 'New York', 'Toronto']
        output_list = [('Arlington', 469, 253, 148, 38, 30),
                       ('Austin', 151, 81, 44, 15, 11),
                       ('New York', 2815, 1297, 884, 369, 265),
                       ('Toronto', 4454, 1990, 1476, 637, 351)]
        output_df = pd.DataFrame(output_list, columns=['Academy', 'Total No. Exams', 'Distinction', 'Merit', 'Pass', 'Fail'])
        result = test_function(input_file, academies)
        assert_frame_equal(output_df, result)

    def test_fdm_training_data_2021_Asia(self):
        input_file = 'fdm_training_data_2021.csv'
        academies = ['Hong Kong', 'Singapore']
        output_list = [('Hong Kong', 2477, 1141, 824, 365, 147),
                       ('Singapore', 1566, 894, 428, 170, 74)]
        output_df = pd.DataFrame(output_list, columns=['Academy', 'Total No. Exams', 'Distinction', 'Merit', 'Pass', 'Fail'])
        result = test_function(input_file, academies)
        assert_frame_equal(output_df, result)

    def test_fdm_training_data_2021_Johannesburg(self):
        input_file = 'fdm_training_data_2021.csv'
        academies = ['Johannesburg']
        output_list = [('Johannesburg', 190, 58, 76, 39, 17)]
        output_df = pd.DataFrame(output_list, columns=['Academy', 'Total No. Exams', 'Distinction', 'Merit', 'Pass', 'Fail'])
        result = test_function(input_file, academies)
        assert_frame_equal(output_df, result)
        
    def test_fdm_training_data_2021_Sydney(self):
        input_file = 'fdm_training_data_2021.csv'
        academies = ['Sydney']
        output_list = [('Sydney', 2901, 1376, 1037, 312, 176)]
        output_df = pd.DataFrame(output_list, columns=['Academy', 'Total No. Exams', 'Distinction', 'Merit', 'Pass', 'Fail'])
        result = test_function(input_file, academies)
        assert_frame_equal(output_df, result)

    def test_fdm_training_data_2021_None(self):
        input_file = 'fdm_training_data_2021.csv'
        academies = []
        output_list = []
        output_df = pd.DataFrame(output_list, columns=['Academy', 'Total No. Exams', 'Distinction', 'Merit', 'Pass', 'Fail'])
        output_df = pd.DataFrame(output_list, index=np.arange(0, 0, 1), columns=['Academy', 'Total No. Exams', 'Distinction', 'Merit', 'Pass', 'Fail'])
        output_df = output_df.astype({'Academy':'object', 'Total No. Exams':'int64', 'Distinction':'int64', 'Merit':'int64', 'Pass':'int64', 'Fail':'int64'})
        result = test_function(input_file, academies)
        result = result.astype({'Academy':'object', 'Total No. Exams':'int64', 'Distinction':'int64', 'Merit':'int64', 'Pass':'int64', 'Fail':'int64'})
        assert_frame_equal(output_df, result)

    def test_inexistent_file(self):
        input_file = 'inexistent_file'
        academies = ['London', 'Leeds', 'Glasgow']
        output = 'The file "' + input_file + '" does not exist'
        result = test_function(input_file, academies)
        message = self.explanation(input_file, output, result)
        self.assertEqual(output, result, msg=message)

    def test_unreadable_file(self):
        input_file = 'existing_unreadable_file'
        academies = ['London', 'Leeds', 'Glasgow']
        output = 'Error reading file "' + input_file + '"'
        result = test_function(input_file, academies)
        message = self.explanation(input_file, output, result)
        self.assertEqual(output, result, msg=message)


if __name__ == '__main__':
    unittest.main(verbosity=2)
