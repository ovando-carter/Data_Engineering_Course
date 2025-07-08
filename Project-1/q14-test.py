"""
  #####                                                  #   #  
 #     # #    # ######  ####  ##### #  ####  #    #     ##   #    #
 #     # #    # #      #        #   # #    # ##   #    # #   #    #
 #     # #    # #####   ####    #   # #    # # #  #      #   #    #
 #   # # #    # #           #   #   # #    # #  # #      #   #######
 #    #  #    # #      #    #   #   # #    # #   ##      #        #
  #### #  ####  ######  ####    #   #  ####  #    #    #####      #
                                                               
 #     #                   #######                             
 #     # #    # # #####       #    ######  ####  #####  ####   
 #     # ##   # #   #         #    #      #        #   #       
 #     # # #  # #   #         #    #####   ####    #    ####   
 #     # #  # # #   #         #    #           #   #        #  
 #     # #   ## #   #         #    #      #    #   #   #    #  
  #####  #    # #   #         #    ######  ####    #    ####   

"""

FILE = 'q14'       # Do NOT Include the .py
FUNCTION = 'summary_grades_per_activity'

import os
import sys
import unittest
import warnings  # needed for setUpClass() class method
import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal

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
    from q14 import summary_grades_per_activity as test_function
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

    def test_fdm_training_data_2021_L_21_FOU_02(self):
        input_file = 'fdm_training_data_2021.csv'
        course_code = 'L-21-FOU-02'
        output_list = [('L-21-FOU-02', 'Core - Business Fundamentals Exam', 1, 'unknown', 0),
                       ('L-21-FOU-02', 'Core - Business Fundamentals Exam', 1, 'F', 1),
                       ('L-21-FOU-02', 'Core - Business Fundamentals Exam', 1, 'P', 1),
                       ('L-21-FOU-02', 'Core - Business Fundamentals Exam', 1, 'M', 1),
                       ('L-21-FOU-02', 'Core - Business Fundamentals Exam', 1, 'D', 10),
                       ('L-21-FOU-02', 'Core - Business Fundamentals Exam', 2, 'unknown', 0),
                       ('L-21-FOU-02', 'Core - Business Fundamentals Exam', 2, 'F', 0),
                       ('L-21-FOU-02', 'Core - Business Fundamentals Exam', 2, 'P', 0),
                       ('L-21-FOU-02', 'Core - Business Fundamentals Exam', 2, 'M', 0),
                       ('L-21-FOU-02', 'Core - Business Fundamentals Exam', 2, 'D', 1),
                       
                       ('L-21-FOU-02', 'Core - Business Fundamentals Presentation', 1, 'unknown', 0),
                       ('L-21-FOU-02', 'Core - Business Fundamentals Presentation', 1, 'F', 0),
                       ('L-21-FOU-02', 'Core - Business Fundamentals Presentation', 1, 'P', 6),
                       ('L-21-FOU-02', 'Core - Business Fundamentals Presentation', 1, 'M', 2),
                       ('L-21-FOU-02', 'Core - Business Fundamentals Presentation', 1, 'D', 5),
                       ('L-21-FOU-02', 'Core - Business Fundamentals Presentation', 2, 'unknown', 0),
                       ('L-21-FOU-02', 'Core - Business Fundamentals Presentation', 2, 'F', 0),
                       ('L-21-FOU-02', 'Core - Business Fundamentals Presentation', 2, 'P', 0),
                       ('L-21-FOU-02', 'Core - Business Fundamentals Presentation', 2, 'M', 0),
                       ('L-21-FOU-02', 'Core - Business Fundamentals Presentation', 2, 'D', 0),
                       
                       ('L-21-FOU-02', 'EMEA Pro Skills I/V Assessment 2021', 1, 'unknown', 0),
                       ('L-21-FOU-02', 'EMEA Pro Skills I/V Assessment 2021', 1, 'F', 0),
                       ('L-21-FOU-02', 'EMEA Pro Skills I/V Assessment 2021', 1, 'P', 2),
                       ('L-21-FOU-02', 'EMEA Pro Skills I/V Assessment 2021', 1, 'M', 3),
                       ('L-21-FOU-02', 'EMEA Pro Skills I/V Assessment 2021', 1, 'D', 9),
                       ('L-21-FOU-02', 'EMEA Pro Skills I/V Assessment 2021', 2, 'unknown', 0),
                       ('L-21-FOU-02', 'EMEA Pro Skills I/V Assessment 2021', 2, 'F', 0),
                       ('L-21-FOU-02', 'EMEA Pro Skills I/V Assessment 2021', 2, 'P', 0),
                       ('L-21-FOU-02', 'EMEA Pro Skills I/V Assessment 2021', 2, 'M', 0),
                       ('L-21-FOU-02', 'EMEA Pro Skills I/V Assessment 2021', 2, 'D', 0),
                       
                       ('L-21-FOU-02', 'EMEA Pro Skills Presentation Assessment 2021', 1, 'unknown', 0),
                       ('L-21-FOU-02', 'EMEA Pro Skills Presentation Assessment 2021', 1, 'F', 0),
                       ('L-21-FOU-02', 'EMEA Pro Skills Presentation Assessment 2021', 1, 'P', 0),
                       ('L-21-FOU-02', 'EMEA Pro Skills Presentation Assessment 2021', 1, 'M', 4),
                       ('L-21-FOU-02', 'EMEA Pro Skills Presentation Assessment 2021', 1, 'D', 10),
                       ('L-21-FOU-02', 'EMEA Pro Skills Presentation Assessment 2021', 2, 'unknown', 0),
                       ('L-21-FOU-02', 'EMEA Pro Skills Presentation Assessment 2021', 2, 'F', 0),
                       ('L-21-FOU-02', 'EMEA Pro Skills Presentation Assessment 2021', 2, 'P', 0),
                       ('L-21-FOU-02', 'EMEA Pro Skills Presentation Assessment 2021', 2, 'M', 0),
                       ('L-21-FOU-02', 'EMEA Pro Skills Presentation Assessment 2021', 2, 'D', 0),
                       
                       
                       ('L-21-FOU-02', 'EMEA Pro Skills Written Assessment 2021', 1, 'unknown', 0),
                       ('L-21-FOU-02', 'EMEA Pro Skills Written Assessment 2021', 1, 'F', 0),
                       ('L-21-FOU-02', 'EMEA Pro Skills Written Assessment 2021', 1, 'P', 1),
                       ('L-21-FOU-02', 'EMEA Pro Skills Written Assessment 2021', 1, 'M', 3),
                       ('L-21-FOU-02', 'EMEA Pro Skills Written Assessment 2021', 1, 'D', 10),
                       ('L-21-FOU-02', 'EMEA Pro Skills Written Assessment 2021', 2, 'unknown', 0),
                       ('L-21-FOU-02', 'EMEA Pro Skills Written Assessment 2021', 2, 'F', 0),
                       ('L-21-FOU-02', 'EMEA Pro Skills Written Assessment 2021', 2, 'P', 0),
                       ('L-21-FOU-02', 'EMEA Pro Skills Written Assessment 2021', 2, 'M', 0),
                       ('L-21-FOU-02', 'EMEA Pro Skills Written Assessment 2021', 2, 'D', 0),
                       
                       ('L-21-FOU-02', 'EXCEL Exam - March 2017', 1, 'unknown', 0),
                       ('L-21-FOU-02', 'EXCEL Exam - March 2017', 1, 'F', 3),
                       ('L-21-FOU-02', 'EXCEL Exam - March 2017', 1, 'P', 1),
                       ('L-21-FOU-02', 'EXCEL Exam - March 2017', 1, 'M', 3),
                       ('L-21-FOU-02', 'EXCEL Exam - March 2017', 1, 'D', 7),
                       ('L-21-FOU-02', 'EXCEL Exam - March 2017', 2, 'unknown', 0),
                       ('L-21-FOU-02', 'EXCEL Exam - March 2017', 2, 'F', 0),
                       ('L-21-FOU-02', 'EXCEL Exam - March 2017', 2, 'P', 0),
                       ('L-21-FOU-02', 'EXCEL Exam - March 2017', 2, 'M', 1),
                       ('L-21-FOU-02', 'EXCEL Exam - March 2017', 2, 'D', 1),
                       
                       ('L-21-FOU-02', 'EXCEL Project - March 2017', 1, 'unknown', 0),
                       ('L-21-FOU-02', 'EXCEL Project - March 2017', 1, 'F', 2),
                       ('L-21-FOU-02', 'EXCEL Project - March 2017', 1, 'P', 4),
                       ('L-21-FOU-02', 'EXCEL Project - March 2017', 1, 'M', 6),
                       ('L-21-FOU-02', 'EXCEL Project - March 2017', 1, 'D', 2),
                       ('L-21-FOU-02', 'EXCEL Project - March 2017', 2, 'unknown', 0),
                       ('L-21-FOU-02', 'EXCEL Project - March 2017', 2, 'F', 0),
                       ('L-21-FOU-02', 'EXCEL Project - March 2017', 2, 'P', 1),
                       ('L-21-FOU-02', 'EXCEL Project - March 2017', 2, 'M', 0),
                       ('L-21-FOU-02', 'EXCEL Project - March 2017', 2, 'D', 0)]
        output_df = pd.DataFrame(output_list, columns=['Course Code', 'Activity Name', 'Attempt', 'Grade', 'Total'])
        output_df.Grade = pd.Categorical(output_df.Grade, categories=['unknown','F','P','M','D'])
        result = test_function(input_file, course_code)
        assert_frame_equal(output_df, result)

    def test_fdm_training_data_2021_H_20_OOD_06(self):
        input_file = 'fdm_training_data_2021.csv'
        course_code = 'H-20-OOD-06'
        output_list = [('H-20-OOD-06', 'OOD Marking Scheme', 1, 'unknown', 0),
                       ('H-20-OOD-06', 'OOD Marking Scheme', 1, 'F', 2),
                       ('H-20-OOD-06', 'OOD Marking Scheme', 1, 'P', 5),
                       ('H-20-OOD-06', 'OOD Marking Scheme', 1, 'M', 5),
                       ('H-20-OOD-06', 'OOD Marking Scheme', 1, 'D', 16),
                       ('H-20-OOD-06', 'OOD Marking Scheme', 2, 'unknown', 0),
                       ('H-20-OOD-06', 'OOD Marking Scheme', 2, 'F', 0),
                       ('H-20-OOD-06', 'OOD Marking Scheme', 2, 'P', 0),
                       ('H-20-OOD-06', 'OOD Marking Scheme', 2, 'M', 1),
                       ('H-20-OOD-06', 'OOD Marking Scheme', 2, 'D', 1)]
        output_df = pd.DataFrame(output_list, columns=['Course Code', 'Activity Name', 'Attempt', 'Grade', 'Total'])
        output_df.Grade = pd.Categorical(output_df.Grade, categories=['unknown','F','P','M','D'])
        result = test_function(input_file, course_code)
        assert_frame_equal(output_df, result)
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
