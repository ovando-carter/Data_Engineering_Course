"""
  #####                                                  #   
 #     # #    # ######  ####  ##### #  ####  #    #     ##   
 #     # #    # #      #        #   # #    # ##   #    # #   
 #     # #    # #####   ####    #   # #    # # #  #      #   
 #   # # #    # #           #   #   # #    # #  # #      #   
 #    #  #    # #      #    #   #   # #    # #   ##      #   
  #### #  ####  ######  ####    #   #  ####  #    #    ##### 

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
import unittest

FILE = 'q1'
LAMBDA_FUNCTION = 'replace_ch_in_pos'

# Do not show the Traceback error
__unittest = True

# Check if the user has put their code in the correct file name
print('----------------------------------------------------------------------')
if not os.path.isfile(FILE+'.py'):
    print('The file "'+FILE+'.py" does not exist')
    print('\nFAILED (errors=1)')
    sys.exit(2)

# Check that there are no unreadable characters within the file
f = open(FILE+'.py', 'r')
try:
    text = f.read().replace(' ', '')
except:
    print("Error reading file "+FILE+'.py'+"\nMake sure there are no styled characters, such as single/double quotes or dash symbols.\nPython does not recognise such characters.")
    f.close()
    sys.exit(3)

# Check if the lambda function name is correct 
f = open(FILE+'.py', 'r')
text = f.read().replace(' ', '')
f.close()
if LAMBDA_FUNCTION+'=' not in text:
    print('The lambda function "'+LAMBDA_FUNCTION+'" does not exist in file: '+FILE+'.py')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(4)

# Check if the keyword 'lambda' appears in the file
if 'lambda' not in text:
    print('There is no lambda function in file: '+FILE+'.py')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(6)

# If the lambda function exists but does not import then there are syntax errors
try:
    from q1 import replace_ch_in_pos as test_function
except:
    print('The lambda function "'+LAMBDA_FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(5)


class LambdaTest(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False
        
    def explanation(self, char, position, string, output, result):
        message = LAMBDA_FUNCTION
        message = message+'\nFor input values: "'+char+'", '+str(position)+', "'+string+'" the output is: '+str(output)+' - You returned '+str(result)
        if not isinstance(result, str):
            message = message+'\n\nReturned value must be a string'
        return message

    def test_space_date_and_time_10(self):
        input_char = ' '
        position = 10
        input_string = '12-11-2003-17:34:54'
        output = '12-11-2003 17:34:54'
        result = test_function(input_string, input_char, position)
        message = self.explanation(input_char, position, input_string, output, result)
        self.assertEqual(output, result, msg=message)

    def test_hash_ABCDE_3(self):
        input_char = '#'
        position = 3
        input_string = 'ABCDE'
        output = 'ABC#E'
        result = test_function(input_string, input_char, position)
        message = self.explanation(input_char, position, input_string, output, result)
        self.assertEqual(output, result, msg=message)

    def test_d_Advances_7(self):
        input_char = 'd'
        position = 7
        input_string = 'Advances'
        output = 'Advanced'
        result = test_function(input_string, input_char, position)
        message = self.explanation(input_char, position, input_string, output, result)
        self.assertEqual(output, result, msg=message)

    def test_e_Trainer_6(self):
        input_char = 'e'
        position = 6
        input_string = 'Trainer'
        output = 'Trainee'
        result = test_function(input_string, input_char, position)
        message = self.explanation(input_char, position, input_string, output, result)
        self.assertEqual(output, result, msg=message)

    def test_P_python_0(self):
        input_char = 'P'
        position = 0
        input_string = 'python'
        output = 'Python'
        result = test_function(input_string, input_char, position)
        message = self.explanation(input_char, position, input_string, output, result)
        self.assertEqual(output, result, msg=message)

    def test_c_stutter_1(self):
        input_char = 'c'
        position = 1
        input_string = 'stutter'
        output = 'scutter'
        result = test_function(input_string, input_char, position)
        message = self.explanation(input_char, position, input_string, output, result)
        self.assertEqual(output, result, msg=message)
        
    def test_0_12345_4(self):
        input_char = '0'
        position = 4
        input_string = '12345'
        output = '12340'
        result = test_function(input_string, input_char, position)
        message = self.explanation(input_char, position, input_string, output, result)
        self.assertEqual(output, result, msg=message)

    def test_pound_P_0(self):
        input_char = '£'
        position = 0
        input_string = 'P'
        output = '£'
        result = test_function(input_string, input_char, position)
        message = self.explanation(input_char, position, input_string, output, result)
        self.assertEqual(output, result, msg=message)


if __name__ == '__main__':
    unittest.main(verbosity=2)