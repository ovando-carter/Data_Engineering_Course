"""
  #####                                                #       
 #     # #    # ######  ####  ##### #  ####  #    #    #    #  
 #     # #    # #      #        #   # #    # ##   #    #    #  
 #     # #    # #####   ####    #   # #    # # #  #    #    #  
 #   # # #    # #           #   #   # #    # #  # #    ####### 
 #    #  #    # #      #    #   #   # #    # #   ##         #  
  #### #  ####  ######  ####    #   #  ####  #    #         #  
                                                               
 #     #                   #######                             
 #     # #    # # #####       #    ######  ####  #####  ####   
 #     # ##   # #   #         #    #      #        #   #       
 #     # # #  # #   #         #    #####   ####    #    ####   
 #     # #  # # #   #         #    #           #   #        #  
 #     # #   ## #   #         #    #      #    #   #   #    #  
  #####  #    # #   #         #    ######  ####    #    ####   

"""

FILE = 'q4'       # Do NOT Include the .py
FUNCTION = 'avg_percentage_per_activity'

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
    from q4 import avg_percentage_per_activity as test_function
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
        message = '\n\nFor the input file "'+input_file+'" the output is '+output+' - You returned '+str(result)
        if not isinstance(result, str):
            message = message+'\n\nReturned value must be a string'
        return message
    
    def test_fdm_training_data_2021_L_21_FOU_02_1(self):
        input_file = 'fdm_training_data_2021.csv'
        course_code = 'L-21-FOU-02'
        attempt = 1
        output_list = [('L-21-FOU-02', 'Core - Business Fundamentals Exam', 1, 0.884615),
                       ('L-21-FOU-02', 'Core - Business Fundamentals Presentation', 1, 0.839231),
                       ('L-21-FOU-02', 'EMEA Pro Skills I/V Assessment 2021', 1, 0.901793),
                       ('L-21-FOU-02', 'EMEA Pro Skills Presentation Assessment 2021', 1, 0.929757),
                       ('L-21-FOU-02', 'EMEA Pro Skills Written Assessment 2021', 1, 0.926186),
                       ('L-21-FOU-02', 'EXCEL Exam - March 2017', 1, 0.822143),
                       ('L-21-FOU-02', 'EXCEL Project - March 2017', 1, 0.787857)]
        output_df = pd.DataFrame(output_list, columns=['Course Code', 'Activity Name', 'Attempt', 'Average'])
        result = test_function(input_file, course_code, attempt)
        assert_frame_equal(output_df, result)
        
    def test_fdm_training_data_2021_L_21_FOU_02_2(self):
        input_file = 'fdm_training_data_2021.csv'
        course_code = 'L-21-FOU-02'
        attempt = 2
        output_list = [('L-21-FOU-02', 'Core - Business Fundamentals Exam', 2, 0.95),
                       ('L-21-FOU-02', 'EXCEL Exam - March 2017', 2, 0.88),
                       ('L-21-FOU-02', 'EXCEL Project - March 2017', 2, 0.78)]
        output_df = pd.DataFrame(output_list, columns=['Course Code', 'Activity Name', 'Attempt', 'Average'])
        result = test_function(input_file, course_code, attempt)
        assert_frame_equal(output_df, result)

    def test_fdm_training_data_2021_L_21_FOU_02_3(self):
        input_file = 'fdm_training_data_2021.csv'
        course_code = 'L-21-FOU-02'
        attempt = 3
        output_list = []
        output_df = pd.DataFrame(output_list, index=np.arange(0, 0, 1), columns=['Course Code', 'Activity Name', 'Attempt', 'Average'])
        output_df.Attempt = output_df.Attempt.astype('int64')
        output_df.Average = output_df.Average.astype('float64')
        result = test_function(input_file, course_code, attempt)
        assert_frame_equal(output_df, result)

    def test_fdm_training_data_2021_G_21_PSO_05_1(self):
        input_file = 'fdm_training_data_2021.csv'
        course_code = 'G-21-PSO-05'
        attempt = 1
        output_list = [('G-21-PSO-05', 'Financial Awareness Course Exam', 1, 0.832143),
                       ('G-21-PSO-05', 'General Marking Scheme', 1, 0.829286),
                       ('G-21-PSO-05', 'PMO Sign Off Exam', 1, 0.821443),
                       ('G-21-PSO-05', 'PSO Exam Aug 2013', 1, 0.817857),
                       ('G-21-PSO-05', 'PSO Internal BA Exam', 1, 0.912143)]
        output_df = pd.DataFrame(output_list, columns=['Course Code', 'Activity Name', 'Attempt', 'Average'])
        result = test_function(input_file, course_code, attempt)
        assert_frame_equal(output_df, result)

    def test_fdm_training_data_2021_G_21_PSO_05_2(self):
        input_file = 'fdm_training_data_2021.csv'
        course_code = 'G-21-PSO-05'
        attempt = 2
        output_list = [('G-21-PSO-05', 'PMO Sign Off Exam', 2, 0.8542),
                       ('G-21-PSO-05', 'PSO Exam Aug 2013', 2, 0.8150)]
        output_df = pd.DataFrame(output_list, columns=['Course Code', 'Activity Name', 'Attempt', 'Average'])
        result = test_function(input_file, course_code, attempt)
        assert_frame_equal(output_df, result)

    def test_fdm_training_data_2021_G_21_PSO_05_3(self):
        input_file = 'fdm_training_data_2021.csv'
        course_code = 'G-21-PSO-05'
        attempt = 3
        output_list = [('G-21-PSO-05', 'PSO Exam Aug 2013', 3, 0.93)]
        output_df = pd.DataFrame(output_list, columns=['Course Code', 'Activity Name', 'Attempt', 'Average'])
        result = test_function(input_file, course_code, attempt)
        assert_frame_equal(output_df, result)

    def test_inexistent_file(self):
        input_file = 'inexistent_file'
        course_code = 'G-21-PSO-05'
        attempt = 3
        output = 'The file "' + input_file + '" does not exist'
        result = test_function(input_file, course_code, attempt)
        message = self.explanation(input_file, output, result)
        self.assertEqual(output, result, msg=message)

    def test_unreadable_file(self):
        input_file = 'existing_unreadable_file'
        course_code = 'G-21-PSO-05'
        attempt = 3
        output = 'Error reading file "' + input_file + '"'
        result = test_function(input_file, course_code, attempt)
        message = self.explanation(input_file, output, result)
        self.assertEqual(output, result, msg=message)
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
