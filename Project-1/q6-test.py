'''
  #####                                                 #####  
 #     # #    # ######  ####  ##### #  ####  #    #    #      
 #     # #    # #      #        #   # #    # ##   #    #      
 #     # #    # #####   ####    #   # #    # # #  #    # ####  
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
  
'''
import os
import sys
import unittest

FILE = 'q6'
FUNCTION = 'solution'

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

# Check if the function name is correct 
f = open(FILE+'.py', 'r')
text = f.read().replace(' ', '')
f.close()
if 'def'+FUNCTION+'(' not in text:
    print('The function "'+FUNCTION+'" does not exist in file: '+FILE+'.py')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(4)

# Check if the keyword 'lambda' appears in the file
if 'lambda' not in text:
    print('There is no lambda function in file: '+FILE+'.py')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(6)

# If the function exists but does not import then there are syntax errors
try:
    from q6 import solution as test_function
except:
    print('The function "'+FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(5)
    

class LambdaTest(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False
        
    def explanation(self, lst, char, position, output, result):
        message = FUNCTION+'('+str(lst)+',"'+char+'",'+str(position)+')'
        message = message+'\nFor input values:\n'+str(lst)+', "'+char+'", '+str(position)+'\nthe output is: '+str(output)+'\n- You returned '+str(result)
        if not isinstance(result, list):
            message = message+'\n\nReturned value must be a list'
        return message

    def test_date_and_time_10(self):
        input_list = ['12-11-2003-17:34:54', '12-11-2003-08:14:28', '28-02-2017-12:00:00', '01-05-2003-22:10:04', '04-10-1996-04:29:43', '10-04-1987-10:19:39']
        char = ' '
        position = 10
        output = ['12-11-2003 17:34:54', '12-11-2003 08:14:28', '28-02-2017 12:00:00', '01-05-2003 22:10:04', '04-10-1996 04:29:43', '10-04-1987 10:19:39']
        result = test_function(input_list, char, position)
        message = self.explanation(input_list, char, position, output, result)
        self.assertEqual(output, result, msg=message)

    def test_money_0(self):
        input_list = ['$153.25', '$100.50', '$199.99', '$300.00']
        char = '£'
        position = 0
        output = ['£153.25', '£100.50', '£199.99', '£300.00']
        result = test_function(input_list, char, position)
        message = self.explanation(input_list, char, position, output, result)
        self.assertEqual(output, result, msg=message)

    def test_various_2(self):
        input_list = ['toilet', 'sorrow', 'ANSI', 'offbone', 'tamra']
        char = ' '
        position = 2
        output = ['to let', 'so row', 'AN I', 'of bone', 'ta ra']
        result = test_function(input_list, char, position)
        message = self.explanation(input_list, char, position, output, result)
        self.assertEqual(output, result, msg=message)
       
    def test_empty_list_anything(self):
        input_list = []
        char = ' '
        position = 10
        output = []
        result = test_function(input_list, char, position)
        message = self.explanation(input_list, char, position, output, result)
        self.assertEqual(output, result, msg=message)


if __name__ == '__main__':
    unittest.main(verbosity=2)