"""
  #####                                                 #####  
 #     # #    # ######  ####  ##### #  ####  #    #    #     # 
 #     # #    # #      #        #   # #    # ##   #          # 
 #     # #    # #####   ####    #   # #    # # #  #     #####  
 #   # # #    # #           #   #   # #    # #  # #          # 
 #    #  #    # #      #    #   #   # #    # #   ##    #     # 
  #### #  ####  ######  ####    #   #  ####  #    #     #####  
                                                               
 #     #                   #######                             
 #     # #    # # #####       #    ######  ####  #####  ####   
 #     # ##   # #   #         #    #      #        #   #       
 #     # # #  # #   #         #    #####   ####    #    ####   
 #     # #  # # #   #         #    #           #   #        #  
 #     # #   ## #   #         #    #      #    #   #   #    #  
  #####  #    # #   #         #    ######  ####    #    ####   

"""
import numpy as np

FILE = 'q3'       # Do NOT Include the .py
FUNCTION = 'pad_arr_int_to_str'

import os
import sys
import unittest

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
    from q3 import pad_arr_int_to_str as test_function
except:
    print('The function "'+FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    sys.exit(5)


class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False

    def explanation(self, input_array, output_array, result):
        message = FUNCTION+'('+str(input_array).replace(' ','')+')'
        message = '\n\nFor input array '+str(input_array)+' the output aray is '+str(output_array)+' - You returned '+str(result)
        if not isinstance(result, np.ndarray):
            message = message+'\n\nReturned value must be a numpy array'
        return message

    def test_45_4832_123_987655(self):
        input_array = np.array([45, 4832, 123, 987655])
        output_array = np.array(['000045', '004832', '000123', '987655'])
        result = test_function(input_array)
        message = self.explanation(input_array, output_array, result)
        np.testing.assert_array_equal(output_array, result, err_msg=message)

    def test_529_0(self):
        input_array = np.array([529, 0])
        output_array = np.array(['529', '000'])
        result = test_function(input_array)
        message = self.explanation(input_array, output_array, result)
        np.testing.assert_array_equal(output_array, result, err_msg=message)

    def test_0_1_2_3_4_5_6_7_8_9(self):
        input_array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        output_array = np.array(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        result = test_function(input_array)
        message = self.explanation(input_array, output_array, result)
        np.testing.assert_array_equal(output_array, result, err_msg=message)

    def test_0(self):
        input_array = np.array([0])
        output_array = np.array(['0'])
        result = test_function(input_array)
        message = self.explanation(input_array, output_array, result)
        np.testing.assert_array_equal(output_array, result, err_msg=message)

    def test_empty_array(self):
        input_array = np.array([])
        output_array = np.array([])
        result = test_function(input_array)
        message = self.explanation(input_array, output_array, result)
        np.testing.assert_array_equal(output_array, result, err_msg=message)

    def test_1_12_123_1234_12345_123456_1234567(self):
        input_array = np.array([1, 12, 123, 1234, 12345, 123456, 1234567])
        output_array = np.array(['0000001', '0000012', '0000123', '0001234', '0012345', '0123456', '1234567'])
        result = test_function(input_array)
        message = self.explanation(input_array, output_array, result)
        np.testing.assert_array_equal(output_array, result, err_msg=message)

    def test_4444_22_333_55555_1(self):
        input_array = np.array([4444, 22, 333, 55555, 1])
        output_array = np.array(['04444', '00022', '00333', '55555', '00001'])
        result = test_function(input_array)
        message = self.explanation(input_array, output_array, result)
        np.testing.assert_array_equal(output_array, result, err_msg=message)

    def test_10_200_300_4000_5000_6000(self):
        input_array = np.array([10, 200, 300, 4000, 5000, 6000])
        output_array = np.array(['0010', '0200', '0300', '4000', '5000', '6000'])
        result = test_function(input_array)
        message = self.explanation(input_array, output_array, result)
        np.testing.assert_array_equal(output_array, result, err_msg=message)


if __name__ == '__main__':
    unittest.main(verbosity=2)
