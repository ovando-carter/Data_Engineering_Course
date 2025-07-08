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

FILE = 'q1'
FUNCTION = 'minimumWage'

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
    from q1 import minimumWage as test_function
except:
    print('The function "'+FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(4)


class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False

    def explanation(self, age, wage, result):
        message = FUNCTION+'('+str(age)+')'
        message = message+'\n\nThe minimum wage for age '+str(age)+' should be '+str(wage)+' - You returned '+str(result)
        if not isinstance(result, float):
            message = message+'\n\nReturned value must be a float'
        return message

    def test_negative_wage_None(self):
        age = -10
        wage = None
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_0_wage_None(self):
        age = 0
        wage = None
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_10_wage_None(self):
        age = 10
        wage = None
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_11_wage_None(self):
        age = 11
        wage = None
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_12_wage_435(self):
        age = 12
        wage = 4.35
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_13_wage_435(self):
        age = 13
        wage = 4.35
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_17_wage_435(self):
        age = 17
        wage = 4.35
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_18_wage_615(self):
        age = 18
        wage = 6.15
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_19_wage_615(self):
        age = 19
        wage = 6.15
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_20_wage_615(self):
        age = 20
        wage = 6.15
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_21_wage_770(self):
        age = 21
        wage = 7.70
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_22_wage_770(self):
        age = 22
        wage = 7.70
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_23_wage_770(self):
        age = 23
        wage = 7.70
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_24_wage_770(self):
        age = 24
        wage = 7.70
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_25_wage_821(self):
        age = 25
        wage = 8.21
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_26_wage_821(self):
        age = 26
        wage = 8.21
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_30_wage_821(self):
        age = 30
        wage = 8.21
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_70_wage_821(self):
        age = 70
        wage = 8.21
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_80_wage_821(self):
        age = 80
        wage = 8.21
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_81_wage_None(self):
        age = 81
        wage = None
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)

    def test_age_100_wage_None(self):
        age = 100
        wage = None
        result = test_function(age)
        message = self.explanation(age, wage, result)
        self.assertEqual(wage, result, msg=message)


if __name__ == '__main__':
    unittest.main()
