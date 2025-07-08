"""
  #####                                                  #    #####
 #     # #    # ######  ####  ##### #  ####  #    #     ##   #     #
 #     # #    # #      #        #   # #    # ##   #    # #         #
 #     # #    # #####   ####    #   # #    # # #  #      #    #####
 #   # # #    # #           #   #   # #    # #  # #      #         #
 #    #  #    # #      #    #   #   # #    # #   ##      #   #     #
  #### #  ####  ######  ####    #   #  ####  #    #    #####  #####
                                                               
 #     #                   #######                             
 #     # #    # # #####       #    ######  ####  #####  ####   
 #     # ##   # #   #         #    #      #        #   #       
 #     # # #  # #   #         #    #####   ####    #    ####   
 #     # #  # # #   #         #    #           #   #        #  
 #     # #   ## #   #         #    #      #    #   #   #    #  
  #####  #    # #   #         #    ######  ####    #    ####   

"""
import os
import sys
import numpy as np
import unittest

currentDirectoryPath = os.getcwd()

file_path = 'data_set_2.txt'
input_array = np.loadtxt(file_path, delimiter=';', dtype=str)


FILE = 'q13'       # Do NOT Include the .py
FUNCTION = 'total_yearly_loans'

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
    from q13 import total_yearly_loans as test_function
except:
    print('The function "'+FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    sys.exit(5)

# function to print text in red colour
def prRed(text):
    print("\033[91m {}\033[00m" .format(text))
    

class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False

    def explanation(self, input_array, output_array, result):
        message = FUNCTION+'('+str(input_array).replace(' ','')+')'
        message = '\n\nFor input array\n'+str(input_array)+'\nthe output aray is\n'+str(output_array)+'\n- You returned '+str(result)
        if not isinstance(result, np.ndarray):
            message = message+'\n\nReturned value must be a numpy array'
        return message

    def test_data_set_2(self):
        output_array = np.array([['Tot. Loans: Jan', 'Tot. Loans: Feb', 'Tot. Loans: Mar', 'Tot. Loans: Apr',
                                  'Tot. Loans: May', 'Tot. Loans: Jun', 'Tot. Loans: Jul', 'Tot. Loans: Aug',
                                  'Tot. Loans: Sep', 'Tot. Loans: Oct', 'Tot. Loans: Nov', 'Tot. Loans: Dec'],
                                 ['181', '164', '139', '138', '172', '137', '156', '128', '100', '104', '80', '119']])
        result = test_function(input_array)
        message = self.explanation(input_array, output_array, result)
        np.testing.assert_array_equal(output_array, result, err_msg=message)

    def test_output_file_data_set_2(self):
        output_array = np.array([['Tot. Loans: Jan', 'Tot. Loans: Feb', 'Tot. Loans: Mar', 'Tot. Loans: Apr',
                                  'Tot. Loans: May', 'Tot. Loans: Jun', 'Tot. Loans: Jul', 'Tot. Loans: Aug',
                                  'Tot. Loans: Sep', 'Tot. Loans: Oct', 'Tot. Loans: Nov', 'Tot. Loans: Dec'],
                                 ['181', '164', '139', '138', '172', '137', '156', '128', '100', '104', '80', '119']])
        result = test_function(input_array)
        # check if the test_data_set_2() produced the output file
        output_file = "tot_yearly_loans.txt"
        if os.path.exists(output_file):
            # check if the file content is correct
            
            file_path =  output_file
            result = np.loadtxt(file_path, delimiter=';', dtype=str)   
            message = self.explanation(input_array, output_array, result)
            np.testing.assert_array_equal(output_array, result, err_msg=message)
            
        else:
            prRed('\nThe output array has not been saved to the text file "' + output_file + '".')
            sys.exit(6)


if __name__ == '__main__':
    unittest.main(verbosity=2)
