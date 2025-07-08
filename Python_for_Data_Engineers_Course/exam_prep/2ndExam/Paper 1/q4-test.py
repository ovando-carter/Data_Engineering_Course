"""
  #####                                                #       
 #     # #    # ######  ####  ##### #  ####  #    #    #    #  
 #     # #    # #      #        #   # #    # ##   #    #    #  
 #     # #    # #####   ####    #   # #    # # #  #    #    #  
 #   # # #    # #           #   #   # #    # #  # #    ####### 
 #    #  #    # #      #    #   #   # #    # #   ##         #  
  #### #  ####  ######  ####    #   #  ####  #    #         #  
                                                               
 #     #                   #######                             
 #     # #    # # #####       #    ######  ####  #####  ####   
 #     # ##   # #   #         #    #      #        #   #       
 #     # # #  # #   #         #    #####   ####    #    ####   
 #     # #  # # #   #         #    #           #   #        #  
 #     # #   ## #   #         #    #      #    #   #   #    #  
  #####  #    # #   #         #    ######  ####    #    ####   

"""

FILE = 'q4'
FUNCTION = 'fillCrosswordLine'

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
    from q4 import fillCrosswordLine as test_function
except:
    print('The function "'+FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(4)


class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False

    def explanation(self, word, line, string, result):
        message = FUNCTION+'("'+line+'", "'+word+'")'
        if string is None:
            message = message+'\n\nWord "'+word+'" does NOT fit in "'+line+'" - You returned "'+str(result)+'"'
        else:
            message = message+'\n\nWord "'+word+'" fits "'+line+'" as "'+string+'" - You returned "'+str(result)+'"'
        if not isinstance(result, str):
            message = message+'\n\nReturned value must be a string'
        return message

    def test_help_fits_into_4(self):
        line = '++----++++'
        word = 'help'
        string = '++help++++'
        result = test_function(line, word)
        message = self.explanation(word, line, string, result)
        self.assertEqual(string, result, msg=message)

    def test_help_doesnt_fit_into_6(self):
        line = '+------+++'
        word = 'help'
        string = None
        result = test_function(line, word)
        message = self.explanation(word, line, string, result)
        self.assertEqual(string, result, msg=message)

    def test_help_doesnt_fit_into_3(self):
        line = '++---+++++'
        word = 'help'
        string = None
        result = test_function(line, word)
        message = self.explanation(word, line, string, result)
        self.assertEqual(string, result, msg=message)

    def test_eclipse_fits_into_7(self):
        line = '+-------++'
        word = 'eclipse'
        string = '+eclipse++'
        result = test_function(line, word)
        message = self.explanation(word, line, string, result)
        self.assertEqual(string, result, msg=message)

    def test_eclipse_doesnt_fit_into_6(self):
        line = '++------++'
        word = 'eclipse'
        string = None
        result = test_function(line, word)
        message = self.explanation(word, line, string, result)
        self.assertEqual(string, result, msg=message)

    def test_eclipse_doesnt_fit_into_8(self):
        line = '+--------+'
        word = 'eclipse'
        string = None
        result = test_function(line, word)
        message = self.explanation(word, line, string, result)
        self.assertEqual(string, result, msg=message)

    def test_maximising_fits_into_10(self):
        line = '----------'
        word = 'maximising'
        string = 'maximising'
        result = test_function(line, word)
        message = self.explanation(word, line, string, result)
        self.assertEqual(string, result, msg=message)

    def test_maximising_doesnt_fit_into_9(self):
        line = '---------+'
        word = 'maximising'
        string = None
        result = test_function(line, word)
        message = self.explanation(word, line, string, result)
        self.assertEqual(string, result, msg=message)

    def test_11_letter_word_doesnt_fit_into_10(self):
        line = '----------'
        word = 'jeopardised'
        string = None
        result = test_function(line, word)
        message = self.explanation(word, line, string, result)
        self.assertEqual(string, result, msg=message)

    def test_4_dashes_fits_help(self):
        line = '----'
        word = 'help'
        string = 'help'
        result = test_function(line, word)
        message = self.explanation(word, line, string, result)
        self.assertEqual(string, result, msg=message)

    def test_5_dashes_returns_None(self):
        line = '-----'
        word = 'help'
        string = None
        result = test_function(line, word)
        message = self.explanation(word, line, string, result)
        self.assertEqual(string, result, msg=message)

    def test_10_dashes_returns_None(self):
        line = '----------'
        word = 'help'
        string = None
        result = test_function(line, word)
        message = self.explanation(word, line, string, result)
        self.assertEqual(string, result, msg=message)

    def test_plus_4_dashes_fits_help(self):
        line = '+----'
        word = 'help'
        string = '+help'
        result = test_function(line, word)
        message = self.explanation(word, line, string, result)
        self.assertEqual(string, result, msg=message)

    def test_4_dashes_plus_fits_help(self):
        line = '----+'
        word = 'help'
        string = 'help+'
        result = test_function(line, word)
        message = self.explanation(word, line, string, result)
        self.assertEqual(string, result, msg=message)


if __name__ == '__main__':
    unittest.main()
