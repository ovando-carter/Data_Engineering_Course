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

FILE = 'q3'
FUNCTION = 'percentageUnderTenPounds'

import os
import sys
import unittest

# Do not show the Traceback error
__unittest = True

# See if the user has put their code in the correct file name
print('----------------------------------------------------------------------')
if not os.path.isfile(FILE+'.py'):
    print('The file "'+FILE+'.py" does not exist')
    print('\nFAILED (errors=1)')
    sys.exit(2)

# See if they use the correct function name
f = open(FILE+'.py', 'r')
text = f.read().replace(' ', '')
f.close()
if 'def'+FUNCTION+'(' not in text:
    print('The function "'+FUNCTION+'" does not exist in file: '+FILE+'.py')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(3)

# If the function exists but does not import then there are syntax errors
try:
    from q3 import percentageUnderTenPounds as test_function
except:
    print('The function "'+FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(4)


class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False

    def explanation(self, prices, percentage, result):
        message = FUNCTION+'('+str(prices).replace(' ','')+')'
        message = message+'\n\nFor price list '+str(prices).replace(' ','')+' the percentage is '+str(percentage)+'\n\nYou returned '+str(result)
        if not isinstance(result, float):
            message = message+'\n\nReturned value must be a float'
        elif round(percentage,2) == round((result*100),2):
            message = message+' **\n\n** Returned value may need to be multiplied by 100'
        return message

    def test_exactly_10pounds(self):
        prices = [10.00]
        percentage = 0.0
        result = test_function(prices)
        message = self.explanation(prices, percentage, result)
        self.assertAlmostEqual(percentage, result, places=2, msg=message)

    def test_0_out_of_1(self):
        prices = [99.00]
        percentage = 0.0
        result = test_function(prices)
        message = self.explanation(prices, percentage, result)
        self.assertAlmostEqual(percentage, result, places=2, msg=message)

    def test_1_out_of_1(self):
        prices = [9.00]
        percentage = 100.0
        result = test_function(prices)
        message = self.explanation(prices, percentage, result)
        self.assertAlmostEqual(percentage, result, places=2, msg=message)

    def test_1_out_of_3_integers(self):
        prices = [9, 10, 11]
        percentage = 33.333
        result = test_function(prices)
        message = self.explanation(prices, percentage, result)
        if isinstance(result, float) and int(result) == int(percentage):
            message = message+'\n\nNote: You do not need to round the return value' 
        self.assertAlmostEqual(percentage, result, places=2, msg=message)

    def test_1_out_of_6(self):
        prices = [5.99, 15.49, 25.00, 10.25, 15.50, 19.99]
        percentage = 16.666
        result = test_function(prices)
        message = self.explanation(prices, percentage, result)
        if isinstance(result, float) and int(result) == int(percentage):
            message = message+'\n\nNote: You do not need to round the return value' 
        self.assertAlmostEqual(percentage, result, places=2, msg=message)

    def test_2_out_of_4(self):
        prices = [2.50, 75.99, 39.50, 7.99]
        percentage = 50.0
        result = test_function(prices)
        message = self.explanation(prices, percentage, result)
        self.assertAlmostEqual(percentage, result, places=2, msg=message)

    def test_2_out_of_7(self):
        prices = [1, 2, 3, 4, 5, 16, 17]
        percentage = 71.429
        result = test_function(prices)
        message = self.explanation(prices, percentage, result)
        if isinstance(result, float) and int(result) == int(percentage):
            message = message+'\n\nNote: You do not need to round the return value' 
        self.assertAlmostEqual(percentage, result, places=2, msg=message)

    def test_3_out_of_7(self):
        prices = [1.0, 2.0, 3.0, 44.0, 55.0, 66.0, 77.0]
        percentage = 42.857
        result = test_function(prices)
        message = self.explanation(prices, percentage, result)
        if isinstance(result, float) and int(result) == int(percentage):
            message = message+'\n\nNote: You do not need to round the return value' 
        self.assertAlmostEqual(percentage, result, places=2, msg=message)

    def test_7_out_of_8(self):
        prices = [2.50, 1.99, 9.50, 7.99, 48.99, 5.50, 7.50, 1.50]
        percentage = 87.5
        result = test_function(prices)
        message = self.explanation(prices, percentage, result)
        if isinstance(result, float) and int(result) == int(percentage):
            message = message+'\n\nNote: You do not need to round the return value' 
        self.assertAlmostEqual(percentage, result, places=2, msg=message)

    def test_10_out_of_18(self):
        prices = [2.50, 1.99, 9.50, 7.99, 48.99, 5.50, 7.50, 1.50, 2.50, 75.99,
                  39.50, 7.99, 5.99, 15.49, 25.00, 10.25, 15.50, 19.99]
        percentage = 55.555
        result = test_function(prices)
        message = self.explanation(prices, percentage, result)
        if isinstance(result, float) and int(result) == int(percentage):
            message = message+'\n\nNote: You do not need to round the return value' 
        self.assertAlmostEqual(percentage, result, places=2, msg=message)


if __name__ == '__main__':
    unittest.main()
