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
FILE = 'q2'       # Do NOT Include the .py
CLASS = 'Trainer'

import os
import sys
import unittest
import types

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

# Check if the class name is correct 
f = open(FILE+'.py', 'r')
text = f.read().replace(' ', '')
f.close()
if 'class'+CLASS not in text:
    print('The class "'+CLASS+'" does not exist in file: '+FILE+'.py')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(4)

# If the class exists but does not import then there are syntax errors
try:
    from q2 import Trainer as test_class
except:
    print('The class "'+CLASS+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    sys.exit(5)


class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False
    
    # explanation used for testing objects and displaying the object's instance attributes to which a value has been assigned
    def explanation_1(self, e_id, f_n, l_n, d_j, output, result):
        message = CLASS+'('+str(e_id)+', '+f_n+', '+l_n+', '+d_j+')'
        message = message+'\nFor input value(s):\n'+str(e_id)+', '+f_n+', '+l_n+', '+d_j+'\nthe output is:\n'+str(output)+'\n- You returned '+str(result)
        return message

    # explanation used for testing a specified class attribute and displaying its value
    def explanation_2(self, cl, attr, output, result):
        message = 'class '+str(cl)+':'
        message = message+'\nFor attribute "'+attr+'" the output is '+str(output)+' - You returned '+str(result)
        return message
    
    # explanation used for testing a specified object's instance attribute and displaying its value
    def explanation_3(self, obj, attr, output, result):
        message = 'object '+obj + ':'
        message = message+'\nFor attribute "'+attr+'" the output is '+str(output)+' - You returned '+str(result)
        return message

    # explanation used for testing a specified object's instance method that returns a value
    def explanation_4(self, obj, method, arguments, output, result):
        message = 'object '+obj+'; method '+method+'():'
        message = message+'\nFor input value(s): '+str(arguments)+'\nthe output is:\n'+str(output)+'\n- You returned:\n'+str(result)
        return message

    # explanation used for testing a specified object's instance method that sets a value of an attribute
    def explanation_5(self, obj, method, arguments, attr, output, result):
        message = 'object '+obj+'; method '+method+'():'
        message = message+'\nFor input value(s):\n'+str(arguments)+'\nthe value of attribute "'+str(attr)+'" is\n'+str(output)+'\n- You returned:\n'+str(result)
        return message
    
    def test_trainer_class(self):
        # test employing 1st trainer
        # --------------------------
        msg = "test employing 1st trainer:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        e_id = 16384
        f_n = 'Evie'
        l_n = 'Klein'
        d_j = '24-11-2015'
        output = {'trainer_id': 16384, 'first_name': 'Evie', 'last_name': 'Klein', 'email': 'evie.klein@fdmgroup.com', 'date_joined': '24-11-2015', 'date_left': None, 'courses': [], 'trainings': {}}
        emp_16384 = test_class(e_id, f_n, l_n, d_j)
        message = self.explanation_1(e_id, f_n, l_n, d_j, output, emp_16384.__dict__)
        self.assertEqual(output, emp_16384.__dict__, msg=message)
        print("\033[0;31;48m ok\n")
        
        # test count_trainers class attribute
        msg = "testing count_trainers class attribute"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 1
        result = test_class.count_trainers
        message = self.explanation_2(test_class, 'count_trainers', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # test count_trainers class attribute
        msg = "testing count_trainers class attribute:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 1
        result = test_class.count_trainers
        message = self.explanation_2(test_class, 'count_trainers', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # testing print_count() method
        msg = "testing print_count() method - after 1st trainer joined:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class.print_count()

        # test assign_course() method
        msg = "testing assign_course() method:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_16384.assign_course('Excel')
        emp_16384.assign_course('SQL')
        emp_16384.assign_course('Unix')
        emp_16384.assign_course('Python1')
        emp_16384.assign_course('Java')
        output = ['Excel', 'SQL', 'Unix', 'Python1', 'Java']
        message = self.explanation_5('emp_16384', 'assign_course', "'Excel', 'SQL', 'Unix', 'Python1', 'Java'", 'courses', output, emp_16384.courses)
        self.assertEqual(output, emp_16384.courses, msg=message)
        print("\033[0;31;48m ok\n")

        # test assign_training() method
        msg = "testing assign_training() method: - asigning a course from courses list"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_16384.assign_training('16/05/2022', 'Excel', 'L-22-RRC-06')
        output = {'16/05/2022': ('Excel', 'L-22-RRC-06')}
        message = self.explanation_5('emp_16384', 'assign_training', "'16/05/2022', 'Excel', 'L-22-RRC-06'", 'trainings', output, emp_16384.trainings)
        self.assertEqual(output, emp_16384.trainings, msg=message)
        print("\033[0;31;48m ok\n")
                
        msg = "testing assign_training() method: - asigning another course from courses list with existing date"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_16384.assign_training('16/05/2022', 'Python1', 'P-21-FOU-01')
        output = {'16/05/2022': ('Python1', 'P-21-FOU-01')}
        message = self.explanation_5('emp_16384', 'assign_training', "'16/05/2022', 'Python1', 'P-21-FOU-01'", 'trainings', output, emp_16384.trainings)
        self.assertEqual(output, emp_16384.trainings, msg=message)
        print("\033[0;31;48m ok\n")
        
        msg = "testing assign_training() method: - asigning a course not in courses list"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_16384.assign_training('23/05/2022', 'Python2', 'L-22-DET-02')
        output = {'16/05/2022': ('Python1', 'P-21-FOU-01')}
        message = self.explanation_5('emp_16384', 'assign_training', "'23/05/2022', 'Python2', 'L-22-DET-02'", 'trainings', output, emp_16384.trainings)
        self.assertEqual(output, emp_16384.trainings, msg=message)
        
        msg = "testing assign_training() method: - asigning another course from courses list with inexisting date"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_16384.assign_training('23/05/2022', 'Unix', 'L-22-FOU-10')
        output = {'16/05/2022': ('Python1', 'P-21-FOU-01'), '23/05/2022': ('Unix', 'L-22-FOU-10')}
        message = self.explanation_5('emp_16384', 'assign_training', "'23/05/2022': 'Unix', 'L-22-FOU-10'", 'trainings', output, emp_16384.trainings)
        self.assertEqual(output, emp_16384.trainings, msg=message)
        print("\033[0;31;48m ok\n")

        # test employing 2nd trainer
        # --------------------------
        msg = "test employing 2nd trainer:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        e_id = 17639
        f_n = 'Elena'
        l_n = 'Rostova'
        d_j = '04-05-2016'
        output = {'trainer_id': 17639, 'first_name': 'Elena', 'last_name': 'Rostova', 'email': 'elena.rostova@fdmgroup.com', 'date_joined': '04-05-2016', 'date_left': None, 'courses': [], 'trainings': {}}
        emp_17639 = test_class(e_id, f_n, l_n, d_j)
        message = self.explanation_1(e_id, f_n, l_n, d_j, output, emp_17639.__dict__)
        self.assertEqual(output, emp_17639.__dict__, msg=message)
        print("\033[0;31;48m ok\n")
        
        # test count_trainers class attribute
        msg = "testing count_trainers class attribute:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 2
        result = test_class.count_trainers
        message = self.explanation_2(test_class, 'count_trainers', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # testing print_count() method
        msg = "testing print_count() method - after 2nd trainer joined:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class.print_count()
      
        # test assign_course() method
        msg = "testing assign_course() method:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_17639.assign_course('Excel')
        emp_17639.assign_course('Hadoop & HDFS')
        emp_17639.assign_course('Hive + Architecture & Data')
        emp_17639.assign_course('Spark & PySpark')
        output = ['Excel', 'Hadoop & HDFS', 'Hive + Architecture & Data', 'Spark & PySpark']
        message = self.explanation_5('emp_17639', 'assign_course', "'Excel', 'Hadoop & HDFS', 'Hive + Architecture & Data', 'Spark & PySpark', 'Java'", 'courses', output, emp_17639.courses)
        self.assertEqual(output, emp_17639.courses, msg=message)
        print("\033[0;31;48m ok\n")
               
        # test assign_training() method
        msg = "testing assign_training() method: - asigning a course from courses list"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_17639.assign_training('06/06/2022', 'Excel', 'G-21-GB2B-09')
        output = {'06/06/2022': ('Excel', 'G-21-GB2B-09')}
        message = self.explanation_5('emp_17639', 'assign_training', "'06/06/2022', 'Excel', 'G-21-GB2B-09'", 'trainings', output, emp_17639.trainings)
        self.assertEqual(output, emp_17639.trainings, msg=message)
        print("\033[0;31;48m ok\n")
                
        msg = "testing assign_training() method: - asigning a course not in courses list"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_17639.assign_training('13/06/2022', 'SQL', 'L-21-FOU-36')
        output = {'06/06/2022': ('Excel', 'G-21-GB2B-09')}
        message = self.explanation_5('emp_17639', 'assign_training', "'13/06/2022', 'SQL', 'L-21-FOU-36'", 'trainings', output, emp_16384.trainings)
        self.assertEqual(output, emp_17639.trainings, msg=message)
        
        msg = "testing assign_training() method: - asigning another course from courses list with inexisting date"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_17639.assign_training('13/06/2022', 'Hadoop & HDFS', 'L-22-DET-02')
        output = {'06/06/2022': ('Excel', 'G-21-GB2B-09'), '13/06/2022': ('Hadoop & HDFS', 'L-22-DET-02')}
        message = self.explanation_5('emp_17639', 'assign_training', "'13/06/2022', 'Hadoop & HDFS', 'L-22-DET-02'", 'trainings', output, emp_17639.trainings)
        self.assertEqual(output, emp_17639.trainings, msg=message)
        print("\033[0;31;48m ok\n")
        
        msg = "testing assign_training() method: - asigning another course from courses list with existing date"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_17639.assign_training('13/06/2022', 'Spark & PySpark', 'L-22-FOU-10')
        output = {'06/06/2022': ('Excel', 'G-21-GB2B-09'), '13/06/2022': ('Spark & PySpark', 'L-22-FOU-10')}
        message = self.explanation_5('emp_17639', 'assign_training', "'13/06/2022', 'Spark & PySpark', 'L-22-FOU-10'", 'trainings', output, emp_17639.trainings)
        self.assertEqual(output, emp_17639.trainings, msg=message)
        print("\033[0;31;48m ok\n")

        # test terminate_employment() method
        msg = "testing terminate_employment() method:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_17639.terminate_employment('01-10-2021')
        output = '01-10-2021'
        result = emp_17639.date_left
        message = self.explanation_5('emp_17639', 'terminate_employment', '01-10-2021', 'date_left', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
   
        # test count_trainers class attribute
        msg = "testing count_trainers class attribute:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 1
        result = test_class.count_trainers
        message = self.explanation_2(test_class, 'count_trainers', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # testing print_count() method
        msg = "testing print_count() method - after 1st trainer left:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class.print_count()
        
        # test terminate_employment() method
        emp_16384.terminate_employment('15-01-2022')
        output = '15-01-2022'
        result = emp_16384.date_left
        message = self.explanation_5('emp_17639', 'terminate_employment', '15-01-2022', 'date_left', output, result)
        self.assertEqual(output, result, msg=message)
        
        # test count_trainers class attribute
        msg = "testing count_trainers class attribute:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 0
        result = test_class.count_trainers
        message = self.explanation_2(test_class, 'count_trainers', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")

        # testing print_count() method
        msg = "testing print_count() method - after 2nd trainer left:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class.print_count()


if __name__ == '__main__':
    unittest.main(verbosity=2)
