"""
  #####                                                 #####  
 #     # #    # ######  ####  ##### #  ####  #    #    #     # 
 #     # #    # #      #        #   # #    # ##   #          # 
 #     # #    # #####   ####    #   # #    # # #  #     #####  
 #   # # #    # #           #   #   # #    # #  # #    #       
 #    #  #    # #      #    #   #   # #    # #   ##    #       
  #### #  ####  ######  ####    #   #  ####  #    #    ####### 
                                                               
 #     #                   #######                             
 #     # #    # # #####       #    ######  ####  #####  ####   
 #     # ##   # #   #         #    #      #        #   #       
 #     # # #  # #   #         #    #####   ####    #    ####   
 #     # #  # # #   #         #    #           #   #        #  
 #     # #   ## #   #         #    #      #    #   #   #    #  
  #####  #    # #   #         #    ######  ####    #    ####   

"""

FILE = 'q2'
FUNCTION = 'numberOfOccurrencesInString'

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
    from q2 import numberOfOccurrencesInString as test_function
except:
    print('The function "'+FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(4)


class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False

    def explanation(self, string, occurrences, result):
        s = '' if occurrences == 1 else 's'
        message = FUNCTION+'("'+string+'")'
        message = message+'\n\nIn the string "'+string+'" a number occurs '+str(occurrences)+' time'+s+' - You returned '+str(result)
        if not isinstance(result, int):
            message = message+'\n\nReturned value must be an integer'
        return message

    def test_500_numbers_returns_50(self):
        string = ''
        for i in range(50):
            string = string + 'abc0123456789'
        occurrences = 500
        result = test_function(string)
        message = self.explanation(string, occurrences, result)
        self.assertEqual(occurrences, result, msg=message)

    def test_empty_string_returns_0(self):
        string = ''
        occurrences = 0
        result = test_function(string)
        message = self.explanation(string, occurrences, result)
        self.assertEqual(occurrences, result, msg=message)

    def test_abc_returns_0(self):
        string = 'abc'
        occurrences = 0
        result = test_function(string)
        message = self.explanation(string, occurrences, result)
        self.assertEqual(occurrences, result, msg=message)

    def test_1234_returns_4(self):
        string = '1234'
        occurrences = 4
        result = test_function(string)
        message = self.explanation(string, occurrences, result)
        self.assertEqual(occurrences, result, msg=message)

    def test_abc1234_returns_4(self):
        string = 'abc1234'
        occurrences = 4
        result = test_function(string)
        message = self.explanation(string, occurrences, result)
        self.assertEqual(occurrences, result, msg=message)

    def test_12345_abc_12345_special_returns_10(self):
        string = '12345 abc 12345 !"£$%^&*()_+\/"'
        occurrences = 10
        result = test_function(string)
        message = self.explanation(string, occurrences, result)
        self.assertEqual(occurrences, result, msg=message)

    def test_Commodore_64_returns_2(self):
        string = 'Commodore 64'
        occurrences = 2
        result = test_function(string)
        message = self.explanation(string, occurrences, result)
        self.assertEqual(occurrences, result, msg=message)

    def test_Texas_Instruments_TI99_4A_returns_3(self):
        string = 'Texas Instruments TI-99/4A'
        occurrences = 3
        result = test_function(string)
        message = self.explanation(string, occurrences, result)
        self.assertEqual(occurrences, result, msg=message)

    def test_Tandy_TRS80_returns_2(self):
        string = 'Tandy TRS-80'
        occurrences = 2
        result = test_function(string)
        message = self.explanation(string, occurrences, result)
        self.assertEqual(occurrences, result, msg=message)

    def test_Apple_IIe_returns_0(self):
        string = 'Apple IIe'
        occurrences = 0
        result = test_function(string)
        message = self.explanation(string, occurrences, result)
        self.assertEqual(occurrences, result, msg=message)

    def test_Timex_Sinclair_1000_returns_4(self):
        string = 'Timex Sinclair 1000'
        occurrences = 4
        result = test_function(string)
        message = self.explanation(string, occurrences, result)
        self.assertEqual(occurrences, result, msg=message)

    def test_IBM_PCjr_returns_0(self):
        string = 'IBM_PCjr'
        occurrences = 0
        result = test_function(string)
        message = self.explanation(string, occurrences, result)
        self.assertEqual(occurrences, result, msg=message)

    def test_Coleco_Adam_returns_0(self):
        string = 'Coleco Adam'
        occurrences = 0
        result = test_function(string)
        message = self.explanation(string, occurrences, result)
        self.assertEqual(occurrences, result, msg=message)

    def test_Commodore_Amiga_1000_returns_4(self):
        string = 'Commodore Amiga (1000)'
        occurrences = 4
        result = test_function(string)
        message = self.explanation(string, occurrences, result)
        self.assertEqual(occurrences, result, msg=message)

    def test_Osborne_1_returns_1(self):
        string = 'Osborne 1'
        occurrences = 1
        result = test_function(string)
        message = self.explanation(string, occurrences, result)
        self.assertEqual(occurrences, result, msg=message)

    def test_IBM_PC_5150_returns_4(self):
        string = 'IBM PC 5150'
        occurrences = 4
        result = test_function(string)
        message = self.explanation(string, occurrences, result)
        self.assertEqual(occurrences, result, msg=message)


if __name__ == '__main__':
    unittest.main()
