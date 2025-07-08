"""
  #####                                                 #####  
 #     # #    # ######  ####  ##### #  ####  #    #    #     # 
 #     # #    # #      #        #   # #    # ##   #    #     # 
 #     # #    # #####   ####    #   # #    # # #  #     #####  
 #   # # #    # #           #   #   # #    # #  # #    #     # 
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
import os

file_path = 'data_set_1.txt'
input_array = np.loadtxt(file_path, usecols=(1,2,3,4,5,6,7,8,9,10,11), delimiter='\t', dtype=str)
file_path_2 = 'data_set_1_bis.txt'
input_array_2 = np.loadtxt(file_path_2, usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22), delimiter='\t', dtype=str)

FILE = 'q8'       # Do NOT Include the .py
FUNCTION = 'hlookup'

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
    from q8 import hlookup as test_function
except:
    print('The function "'+FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    sys.exit(5)


class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False

    def explanation(self, input_array, lookup_val, row_num, output, result):
        message = FUNCTION+'(\n'+str(input_array)+',\n'+str(lookup_val)+',\n'+str(row_num)+')'
        if result == None:
            message = message+'\n\nThe returned value is not a string. - You returned the value None instead of the string "None"'
        elif result == 'None':
            message = message+'\n\nThe index '+str(row_num)+' does not exist within data set - You returned "'+str(result)+'"'
        elif result == '-1':
            message = message+'\n\nThe lookup value "'+lookup_val+'" is not found within the first row of the data set - You returned "'+str(result)+'"'
        else:
            message = message+'\n\nThe matching value for the lookup value "'+lookup_val+'" is found in row '+str(row_num)+' within the data set as "'+output+'" - You returned "'+str(result)+'"'
        if not isinstance(result, str):
            message = message+'\n\nReturned value must be a string'
        return message

    def test_WX534_5(self):
        lookup_val = 'WX-534'
        row_num = 5
        output = '539'
        result = test_function(input_array, lookup_val, row_num)
        message = self.explanation(input_array, lookup_val, row_num, output, result)
        self.assertEqual(output, result, msg=message)
    
    def test_UW698_8(self):
        lookup_val = 'UW-698'
        row_num = 8
        output = '2053'
        result = test_function(input_array, lookup_val, row_num)
        message = self.explanation(input_array, lookup_val, row_num, output, result)
        self.assertEqual(output, result, msg=message)
    
    def test_UW698_9(self):
        lookup_val = 'UW-698'
        row_num = 9
        output = 'None'
        result = test_function(input_array, lookup_val, row_num)
        message = self.explanation(input_array, lookup_val, row_num, output, result)
        self.assertEqual(output, result, msg=message)

    def test_XY_123_5(self):
        lookup_val = 'XY-123'
        row_num = 5
        output = '-1'
        result = test_function(input_array, lookup_val, row_num)
        message = self.explanation(input_array, lookup_val, row_num, output, result)
        self.assertEqual(output, result, msg=message)

    def test_LJ_328_2(self):
        lookup_val = 'LJ-328'
        row_num = 2
        output = '388924'
        result = test_function(input_array, lookup_val, row_num)
        message = self.explanation(input_array, lookup_val, row_num, output, result)
        self.assertEqual(output, result, msg=message)

    def test_LJ_328_1(self):
        lookup_val = 'LJ-328'
        row_num = 1
        output = 'LJ-328'
        result = test_function(input_array, lookup_val, row_num)
        message = self.explanation(input_array, lookup_val, row_num, output, result)
        self.assertEqual(output, result, msg=message)
        
    def test_KE738_10_bis(self):
        lookup_val = 'KE-738'
        row_num = 10
        output = '410'
        result = test_function(input_array_2, lookup_val, row_num)
        message = self.explanation(input_array_2, lookup_val, row_num, output, result)
        self.assertEqual(output, result, msg=message)

    def test_DG101_8_bis(self):
        lookup_val = 'DG-101'
        row_num = 8
        output = '651'
        result = test_function(input_array_2, lookup_val, row_num)
        message = self.explanation(input_array_2, lookup_val, row_num, output, result)
        self.assertEqual(output, result, msg=message)

    def test_DG101_12_bis(self):
        lookup_val = 'DG-101'
        row_num = 12
        output = 'None'
        result = test_function(input_array_2, lookup_val, row_num)
        message = self.explanation(input_array_2, lookup_val, row_num, output, result)
        self.assertEqual(output, result, msg=message)

    def test_XY_123_5_bis(self):
        lookup_val = 'XY-123'
        row_num = 5
        output = '-1'
        result = test_function(input_array_2, lookup_val, row_num)
        message = self.explanation(input_array_2, lookup_val, row_num, output, result)
        self.assertEqual(output, result, msg=message)

    def test_LJ_328_7_bis(self):
        lookup_val = 'LJ-328'
        row_num = 7
        output = '422'
        result = test_function(input_array_2, lookup_val, row_num)
        message = self.explanation(input_array_2, lookup_val, row_num, output, result)
        self.assertEqual(output, result, msg=message)

    def test_PF_220_11_bis(self):
        lookup_val = 'PF-220'
        row_num = 11
        output = '757'
        result = test_function(input_array_2, lookup_val, row_num)
        message = self.explanation(input_array_2, lookup_val, row_num, output, result)
        self.assertEqual(output, result, msg=message)

if __name__ == '__main__':
    unittest.main(verbosity=2)
