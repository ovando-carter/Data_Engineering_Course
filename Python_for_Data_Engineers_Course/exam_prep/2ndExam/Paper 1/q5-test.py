"""
  #####                                                ####### 
 #     # #    # ######  ####  ##### #  ####  #    #    #       
 #     # #    # #      #        #   # #    # ##   #    #       
 #     # #    # #####   ####    #   # #    # # #  #    ######  
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

FILE = 'q5'
FUNCTION = 'longestPalindrome'

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
    from q5 import longestPalindrome as test_function
except:
    print('The function "'+FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(4)


class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False

    def explanation(self, letters, longest, result):
        message = FUNCTION+'("'+letters+'")'
        message = message+'\n\nLongest palindrome in "'+letters+'" is '+str(longest)+' - You returned '+str(result)
        if not isinstance(result, int):
            message = message+'\n\nReturned value must be an integer'
        return message

    def test_case_insensitive(self):
        letters = 'MOM mom'
        palindrome = 'MOM mom'
        longest = len(palindrome)
        result = test_function(letters)
        message = self.explanation(letters, longest, result)
        if isinstance(result, int) and result == 3:
            message = message+'\n\nNote: You need to ignore the case of the input' 
        if isinstance(result, int) and result > longest:
            message = message+'\n\nNote: The longest palindrome is "'+palindrome+'"'
        self.assertEqual(longest, result, msg=message)

    def test_empty_string_returns_0(self):
        letters = ''
        longest = 0
        result = test_function(letters)
        message = self.explanation(letters, longest, result)
        self.assertEqual(longest, result, msg=message)

    def test_string_with_dot_returns_0(self):
        letters = '.'
        longest = 0
        result = test_function(letters)
        message = self.explanation(letters, longest, result)
        if isinstance(result, int) and result == 1:
            message = message+'\n\nNote: A palindrome cannot be a single letter.' 
        self.assertEqual(longest, result, msg=message)

    def test_string_with_single_quote_returns_0(self):
        letters = "'"
        longest = 0
        result = test_function(letters)
        message = self.explanation(letters, longest, result)
        if isinstance(result, int) and result == 1:
            message = message+'\n\nNote: A palindrome cannot be a single letter.' 
        self.assertEqual(longest, result, msg=message)

    def test_single_letter_returns_0(self):
        letters = 'a'
        longest = 0
        result = test_function(letters)
        message = self.explanation(letters, longest, result)
        if isinstance(result, int) and result == 1:
            message = message+'\n\nNote: A palindrome cannot be a single letter.' 
        self.assertEqual(longest, result, msg=message)

    def test_palindrome_returns_1(self):
        letters = 'palindrome'
        longest = 0
        result = test_function(letters)
        message = self.explanation(letters, longest, result)
        if isinstance(result, int) and result == 1:
            message = message+'\n\nNote: A palindrome cannot be a single letter.' 
        self.assertEqual(longest, result, msg=message)

    def test_annahasaracecar_returns_7(self):
        letters = 'annahasaracecar'
        palindrome = 'racecar'
        longest = len(palindrome)
        result = test_function(letters)
        message = self.explanation(letters, longest, result)
        if isinstance(result, int) and result != longest:
            message = message+'\n\nNote: The longest palindrome is "'+palindrome+'"'
        self.assertEqual(longest, result, msg=message)

    def test_aracecarannahas_returns_9(self):
        letters = 'aracecarannahas'
        palindrome = 'aracecara'
        longest = len(palindrome)
        result = test_function(letters)
        message = self.explanation(letters, longest, result)
        if isinstance(result, int) and result > longest:
            message = message+'\n\nNote: The longest palindrome is "'+palindrome+'"'
        self.assertEqual(longest, result, msg=message)

    def test_detartratedannahasaRACECAR_returns_11(self):
        letters = 'detartratedannahasaRACECAR'
        longest = 11
        result = test_function(letters)
        message = self.explanation(letters, longest, result)
        self.assertEqual(longest, result, msg=message)

    def test_annahasadetartratedracecar_returns_11(self):
        letters = 'annahasadetartratedracecar'
        longest = 11
        result = test_function(letters)
        message = self.explanation(letters, longest, result)
        self.assertEqual(longest, result, msg=message)

    def test_annahasaracecardetartrated_returns_11(self):
        letters = 'annahasaracecardetartrated'
        longest = 11
        result = test_function(letters)
        message = self.explanation(letters, longest, result)
        self.assertEqual(longest, result, msg=message)

    def test_mumanddad_returns_3(self):
        letters = 'mumanddad'
        palindrome = 'mum'
        longest = len(palindrome)
        result = test_function(letters)
        message = self.explanation(letters, longest, result)
        if isinstance(result, int) and result > longest:
            message = message+'\n\nNote: The longest palindrome is "'+palindrome+'"'
        self.assertEqual(longest, result, msg=message)

    def test_madam_and_eve_returns_5(self):
        letters = 'madam and eve'
        palindrome = 'madam'
        longest = len(palindrome)
        result = test_function(letters)
        message = self.explanation(letters, longest, result)
        if isinstance(result, int) and result != longest:
            message = message+'\n\nNote: The longest palindrome is "'+palindrome+'"'
        self.assertEqual(longest, result, msg=message)

    def test_nurses_run_returns_0(self):
        letters = 'nurses run'
        palindrome = 'ses'
        longest = len(palindrome)
        result = test_function(letters)
        message = self.explanation(letters, longest, result)
        if isinstance(result, int) and result != longest:
            message = message+'\n\nNote: The longest palindrome is "'+palindrome+'"'
        self.assertEqual(longest, result, msg=message)

    def test_tattarrattat_returns_0(self):
        letters = 'tattarrattat'
        palindrome = 'tattarrattat'
        longest = len(palindrome)
        result = test_function(letters)
        message = self.explanation(letters, longest, result)
        if isinstance(result, int) and result > longest:
            message = message+'\n\nNote: The longest palindrome is "'+palindrome+'"'
        self.assertEqual(longest, result, msg=message)

    def test_Rotavator_returns_0(self):
        letters = 'Rotavator'
        palindrome = 'Rotavator'
        longest = len(palindrome)
        result = test_function(letters)
        message = self.explanation(letters, longest, result)
        if isinstance(result, int) and result == 7:
            message = message+'\n\nNote: You need to ignore the case of the input' 
        if isinstance(result, int) and result > longest:
            message = message+'\n\nNote: The longest palindrome is "'+palindrome+'"'
        self.assertEqual(longest, result, msg=message)


if __name__ == '__main__':
    unittest.main()
