"""
  #####                                                  #    #####
 #     # #    # ######  ####  ##### #  ####  #    #     ##   #     #
 #     # #    # #      #        #   # #    # ##   #    # #         #
 #     # #    # #####   ####    #   # #    # # #  #      #    #####
 #   # # #    # #           #   #   # #    # #  # #      #   #
 #    #  #    # #      #    #   #   # #    # #   ##      #   #
  #### #  ####  ######  ####    #   #  ####  #    #    ##### #######
                                                               
 #     #                   #######                             
 #     # #    # # #####       #    ######  ####  #####  ####   
 #     # ##   # #   #         #    #      #        #   #       
 #     # # #  # #   #         #    #####   ####    #    ####   
 #     # #  # # #   #         #    #           #   #        #  
 #     # #   ## #   #         #    #      #    #   #   #    #  
  #####  #    # #   #         #    ######  ####    #    ####   

"""
FILE = 'q12'       # Do NOT Include the .py

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

# Check that there are no unreadable characters within the file
f = open(FILE+'.py', 'r')
try:
    text = f.read().replace(' ', '')
except:
    print("Error reading file "+FILE+'.py'+"\nMake sure there are no styled characters, such as single/double quotes or dash symbols.\nPython does not recognise such characters.")
    f.close()
    sys.exit(3)

# read the python script containing the three classes
f = open(FILE+'.py', 'r')
text = f.read().replace(' ', '')
f.close()

base_class = 'Employee'

# Check if the Trainee class name is correct 
CLASS = 'Trainee'
if 'class'+CLASS not in text:
    print('The class "'+CLASS+'" does not exist in file: '+FILE+'.py')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(4)
elif 'class'+CLASS+'('+base_class+'):' not in text:
    print('The class "'+CLASS+'" is not defined as subclass of class "'+base_class+'" in file: '+FILE+'.py')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(5)

# If the Trainee class exists but does not import then there are syntax errors
try:
    from q12 import Trainee as test_class_1
except:
    print('The class "'+CLASS+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    sys.exit(6)

# Check if the Trainer class name is correct
CLASS = 'Trainer'
if 'class'+CLASS not in text:
    print('The class "'+CLASS+'" does not exist in file: '+FILE+'.py')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(7)
elif 'class'+CLASS+'('+base_class+'):' not in text:
    print('The class "'+CLASS+'" is not defined as subclass of class "'+base_class+'" in file: '+FILE+'.py')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(8)

# If the Trainer class exists but does not import then there are syntax errors
try:
    from q12 import Trainer as test_class_2
except:
    print('The class "'+CLASS+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    sys.exit(9)


# Check if the base_class class name is correct 
CLASS = base_class
if 'class'+CLASS not in text:
    print('The class "'+CLASS+'" does not exist in file: '+FILE+'.py')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(10)
elif 'class'+CLASS+'(ABC):' not in text:
    print('The class "'+CLASS+'" is not defined as abstract class in file: '+FILE+'.py')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(11)

# If the Employee class exists but does not import then there are syntax errors
try:
    from q12 import Employee as test_class_3
except:
    print('The class "'+CLASS+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    sys.exit(12)


class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False
        
    # explanation used for testing an object and displaying the object's instance attributes to which a value has been assigned
    def explanation_1(self, cl, input_values, output, result):
        message = cl+'('+input_values+')'
        message = message+'\nFor input values:\n'+input_values+'\nthe output is:\n'+str(output)+'\nYou returned '+str(result)
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
        message = message+'\nFor arguments: '+str(arguments)+'\nthe output is:\n'+str(output)+'\n- You returned:\n'+str(result)
        return message

    # explanation used for testing a specified object's instance method that sets a value of an attribute
    def explanation_5(self, obj, method, arguments, attr, output, result):
        message = 'object '+obj+'; method '+method+'():'
        message = message+'\nFor input value(s):\n'+str(arguments)+'\nthe value of attribute "'+str(attr)+'" is\n'+str(output)+'\n- You returned:\n'+str(result)
        return message

    def test_all_classes(self):
        
        #########################
        # testing Trainee class #
        #########################

        # test employing 1st trainee
        # --------------------------
        msg = "test employing 1st trainee:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        e_id = 25462
        f_n = 'Mark'
        l_n = 'Simpson'
        d_j = '15-03-2020'
        s = 'Data Engineering'
        w = 7
        output = {'trainee_id': 25462, '_first_name': 'Mark', '_last_name': 'Simpson', '_email': 'mark.simpson@fdmgroup.com', 'date_joined': '15-03-2020', '_date_left': None, 'stream': 'Data Engineering', 'weeks': 7, 'courses': {}}
        emp_25462 = test_class_1(e_id, f_n, l_n, d_j, s, w)
        message = self.explanation_1('Trainee', str(e_id)+', '+f_n+', '+l_n+', '+d_j+', '+s+', '+str(w), output, emp_25462.__dict__)
        self.assertEqual(output, emp_25462.__dict__, msg=message)

        # test count_trainees class attribute
        msg = "testing count_trainees class attribute:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 1
        result = test_class_1.count_trainees
        message = self.explanation_2(test_class_1, 'count_trainees', output, result)
        self.assertEqual(output, result, msg=message)        
        print("\033[0;31;48m ok\n")
        
        # testing Trainee's print_count() method
        msg = "testing Trainee's print_count() method - after 1st trainee joined:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_1.print_count()

        # test if Employee's class attributes were correctly populated
        # '_company': 'FDM Group'
        msg = "testing if Employee's class attributes were correctly populated"
        print()
        print("\033[1;32;40m" + msg + "\033[0m", end='')
        # 'company' : 'FDM Group'
        msg = "- company:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 'FDM Group'
        result = test_class_3._company
        message = self.explanation_2(test_class_3, '_company', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok")
        # 'count_employees' : 1
        msg = "- count_employees:"
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 1
        result = test_class_3.count_employees
        message = self.explanation_2(test_class_3, 'count_employees', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
         
        # test Employee's print_count() method
        msg = "testing Employee's print_count() method - after 1st trainee joined:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_3.print_count()
        
        # test assign_course() method
        msg = "testing assign_course() method:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_25462.assign_course('Java')
        emp_25462.assign_course('Python')
        emp_25462.assign_course('Advanced Python')
        emp_25462.assign_course('Hadoop & HDFS')
        emp_25462.assign_course('Hive + Architecture & Data')
        emp_25462.assign_course('Spark & PySpark')
        emp_25462.assign_course('APM')
        output = {'Java': 0, 'Python': 0, 'Advanced Python': 0, 'Hadoop & HDFS': 0, 'Hive + Architecture & Data': 0, 'Spark & PySpark': 0, 'APM': 0}
        message = self.explanation_5('emp_25462', 'assign_course', "'Java', 'Python', 'Advanced Python', 'Hadoop & HDFS', 'Hive + Architecture & Data', 'Spark & PySpark', 'APM'", 'courses', output, emp_25462.courses)
        self.assertEqual(output, emp_25462.courses, msg=message)
        print("\033[0;31;48m ok\n")
        
        # trying to assign more courses than the number of weeks produces a warning
        msg = "trying to assign more courses than the number of weeks:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_25462.assign_course('Project Week')
        output = {'Java': 0, 'Python': 0, 'Advanced Python': 0, 'Hadoop & HDFS': 0, 'Hive + Architecture & Data': 0, 'Spark & PySpark': 0, 'APM': 0}
        message = self.explanation_5('emp_25462', 'assign_course', "'Project Week'", 'courses', output, emp_25462.courses)
        self.assertEqual(output, emp_25462.courses, msg=message)

        # test assign_mark_for_course() method
        msg = "testing assign_mark_for_course() method:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_25462.assign_mark_for_course('Java', 82)
        emp_25462.assign_mark_for_course('Python', 100)
        emp_25462.assign_mark_for_course('Advanced Python', 91)
        emp_25462.assign_mark_for_course('Hadoop & HDFS', 92)
        emp_25462.assign_mark_for_course('Hive + Architecture & Data', 78)
        emp_25462.assign_mark_for_course('Spark & PySpark', 95)
        emp_25462.assign_mark_for_course('APM', 85)
        output = {'Java': 82, 'Python': 100, 'Advanced Python': 91, 'Hadoop & HDFS': 92, 'Hive + Architecture & Data': 78, 'Spark & PySpark': 95, 'APM': 85}
        message = self.explanation_5('emp_25462', 'assign_mark_for_course', "82, 100, 91, 92, 78, 95, 85", 'courses', output, emp_25462.courses)
        self.assertEqual(output, emp_25462.courses, msg=message)
        print("\033[0;31;48m ok\n")
        
        # test avg_mark() method
        msg = "testing avg_mark() method:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 89.0
        result = round(emp_25462.avg_mark(), 2)
        message = self.explanation_4('emp_25462', 'avg_mark', list(emp_25462.courses.values()), output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # test employing 2nd trainee
        # --------------------------
        msg = "test employing 2nd trainee:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        e_id = 25475
        f_n = 'Fatima'
        l_n = 'Farah'
        d_j = '16-03-2018'
        s = 'Data Engineering'
        w = 7
        output = {'trainee_id': 25475, '_first_name': 'Fatima', '_last_name': 'Farah', '_email': 'fatima.farah@fdmgroup.com', 'date_joined': '16-03-2018', '_date_left': None, 'stream': 'Data Engineering', 'weeks': 7, 'courses': {}}
        emp_25475 = test_class_1(e_id, f_n, l_n, d_j, s, w)
        message = self.explanation_1('Trainee', str(e_id)+', '+f_n+', '+l_n+', '+d_j+', '+s+', '+str(w), output, emp_25475.__dict__)
        self.assertEqual(output, emp_25475.__dict__, msg=message)
       
        # test count_trainees class attribute
        msg = "testing count_trainees class attribute:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 2
        result = test_class_1.count_trainees
        message = self.explanation_2(test_class_1, 'count_trainees', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")

        # testing Trainee's print_count() method
        msg = "testing Trainee's print_count() method - after 2nd trainee joined:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_1.print_count()

        # test if Employee's class attribute was correctly updated
        # 'count_employees' : 2
        msg = "testing if Employee's class attribute was correctly updated"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        msg = "- count_employees:"
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 2
        result = test_class_3.count_employees      
        message = self.explanation_2(test_class_3, 'count_employees', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # test Employee's print_count() method
        msg = "testing Employee's print_count() method - after 2nd trainee joined:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_3.print_count()
        
        # test assign_course() method
        msg = "testing assign_course() method:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_25475.assign_course('Java')
        emp_25475.assign_course('Python')
        emp_25475.assign_course('Advanced Python')
        emp_25475.assign_course('Hadoop & HDFS')
        emp_25475.assign_course('Hive + Architecture & Data')
        emp_25475.assign_course('Spark & PySpark')
        emp_25475.assign_course('APM')
        output = {'Java': 0, 'Python': 0, 'Advanced Python': 0, 'Hadoop & HDFS': 0, 'Hive + Architecture & Data': 0, 'Spark & PySpark': 0, 'APM': 0}
        message = self.explanation_5('emp_25462', 'assign_course', "'Java', 'Python', 'Advanced Python', 'Hadoop & HDFS', 'Hive + Architecture & Data', 'Spark & PySpark', 'APM'", 'courses', output, emp_25475.courses)
        self.assertEqual(output, emp_25475.courses, msg=message)
        print("\033[0;31;48m ok\n")
        
        # trying to assign more courses than the number of weeks produces a warning
        msg = "trying to assign more courses than the number of weeks:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_25475.assign_course('Project Week')
        output = {'Java': 0, 'Python': 0, 'Advanced Python': 0, 'Hadoop & HDFS': 0, 'Hive + Architecture & Data': 0, 'Spark & PySpark': 0, 'APM': 0}
        message = self.explanation_5('emp_25475', 'assign_course', "'Project Week'", 'courses', output, emp_25475.courses)
        self.assertEqual(output, emp_25475.courses, msg=message)
        
        # test assign_mark_for_course() method
        msg = "testing assign_mark_for_course() method:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_25475.assign_mark_for_course('Java', 78)
        emp_25475.assign_mark_for_course('Python', 90)
        emp_25475.assign_mark_for_course('Advanced Python', 91)
        emp_25475.assign_mark_for_course('Hadoop & HDFS', 81)
        emp_25475.assign_mark_for_course('Hive + Architecture & Data', 86)
        emp_25475.assign_mark_for_course('Spark & PySpark', 94)
        emp_25475.assign_mark_for_course('APM', 77)
        output = {'Java': 78, 'Python': 90, 'Advanced Python': 91, 'Hadoop & HDFS': 81, 'Hive + Architecture & Data': 86, 'Spark & PySpark': 94, 'APM': 77}
        message = self.explanation_5('emp_25475', 'assign_mark_for_course', "78, 90, 91, 81, 86, 94, 77", 'courses', output, emp_25475.courses)
        self.assertEqual(output, emp_25475.courses, msg=message)
        print("\033[0;31;48m ok\n")
        
        # test avg_mark() method
        msg = "testing avg_mark() method:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 85.29
        result = round(emp_25475.avg_mark(), 2)
        message = self.explanation_4('emp_25475', 'avg_mark', list(emp_25475.courses.values()), output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # test employing 3rd trainee
        # --------------------------
        msg = "test employing 3rd trainee:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        e_id = 25581
        f_n = 'Leta'
        l_n = 'Okeke'
        d_j = '23-06-2018'
        s = 'Data Engineering'
        w = 7
        output = {'trainee_id': 25581, '_first_name': 'Leta', '_last_name': 'Okeke', '_email': 'leta.okeke@fdmgroup.com', 'date_joined': '23-06-2018', '_date_left': None, 'stream': 'Data Engineering', 'weeks': 7, 'courses': {}}
        emp_25581 = test_class_1(e_id, f_n, l_n, d_j, s, w)
        message = self.explanation_1('Trainee', str(e_id)+', '+f_n+', '+l_n+', '+d_j+', '+s+', '+str(w), output, emp_25581.__dict__)
        self.assertEqual(output, emp_25581.__dict__, msg=message)
        
        # test count_trainees class attribute
        msg = "testing count_trainees class attribute:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 3
        result = test_class_1.count_trainees
        message = self.explanation_2(test_class_1, 'count_trainees', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # testing Trainee's print_count() method
        msg = "testing Trainee's print_count() method - after 3rd trainee joined:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_1.print_count()

        # test if Employee's class attribute was correctly updated
        # 'count_employees' : 3
        msg = "test if Employee's class attribute was correctly updated:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        msg = "- count_trainers:"
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 3
        result = test_class_3.count_employees      
        message = self.explanation_2(test_class_3, 'count_employees', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # test Employee's print_count() method
        msg = "testing Employee's print_count() method - after 3rd trainee joined:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_3.print_count()
        
        # test assign_course() method
        msg = "testing assign_course() method:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_25581.assign_course('Java')
        emp_25581.assign_course('Python')
        emp_25581.assign_course('Advanced Python')
        emp_25581.assign_course('Hadoop & HDFS')
        emp_25581.assign_course('Hive + Architecture & Data')
        emp_25581.assign_course('Spark & PySpark')
        emp_25581.assign_course('APM')
        output = {'Java': 0, 'Python': 0, 'Advanced Python': 0, 'Hadoop & HDFS': 0, 'Hive + Architecture & Data': 0, 'Spark & PySpark': 0, 'APM': 0}
        message = self.explanation_5('emp_25581', 'assign_course', "'Java', 'Python', 'Advanced Python', 'Hadoop & HDFS', 'Hive + Architecture & Data', 'Spark & PySpark', 'APM'", 'courses', output, emp_25581.courses)
        self.assertEqual(output, emp_25581.courses, msg=message)
        print("\033[0;31;48m ok\n")
        
        # trying to assign more courses than the number of weeks produces a warning
        msg = "trying to assign more courses than the number of weeks:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_25581.assign_course('Project Week')
        output = {'Java': 0, 'Python': 0, 'Advanced Python': 0, 'Hadoop & HDFS': 0, 'Hive + Architecture & Data': 0, 'Spark & PySpark': 0, 'APM': 0}
        message = self.explanation_5('emp_25581', 'assign_course', "'Project Week'", 'courses', output, emp_25581.courses)
        self.assertEqual(output, emp_25581.courses, msg=message)
        
        # test terminate_employment() method
        msg = "testing terminate_employment() method:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_25462.terminate_employment('12-07-2021')
        output = '12-07-2021'
        result = emp_25462.date_left
        message = self.explanation_5('emp_25462', 'terminate_employment', '12-07-2021', 'date_left', output, result)
        self.assertEqual(output, result, msg=message)
        
        # test count_trainees class attribute
        msg = "testing count_trainees class attribute:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 2
        result = test_class_1.count_trainees
        message = self.explanation_2(test_class_1, 'count_trainees', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # testing Trainee's print_count() method
        msg = "testing Trainee's print_count() method - after 1st trainee left:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_1.print_count()
        
        # test if Employee's class attribute was correctly updated        
        # 'count_employees' : 2
        msg = "testing if Employee's class attribute was correctly updated"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        msg = "- count_employees:"
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 2
        result = test_class_3.count_employees
        message = self.explanation_2(test_class_3, 'count_employees', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # test Employee's print_count() method
        msg = "testing Employee's print_count() method:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_3.print_count()
        
        # testing employee_id's getter
        msg = "testing employee_id's getter:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 25462
        result = emp_25462.employee_id
        message = self.explanation_3('emp_25462', 'employee_id', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # testing that employee_id is read only
        msg = "trying to change employee_id by the object:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_25475.employee_id = 32475
        output = 25475
        result = emp_25475.employee_id        
        message = self.explanation_3('emp_25475', 'employee_id', output, result)
        self.assertEqual(output, result, msg=message)        
        
        # testing that first & last name can be shanged
        # through the setter only (updating the email accordingly)
        # 1. change the first_name only
        msg = "testing that first & last name can be changed\n1) changing the first_name only:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_25462.first_name = 'Marcus'
        output = {'trainee_id': 25462, '_first_name': 'Marcus', '_last_name': 'Simpson', '_email': 'marcus.simpson@fdmgroup.com', 'date_joined': '15-03-2020', '_date_left': '12-07-2021', 'stream': 'Data Engineering', 'weeks': 7, 'courses': {'Java': 82, 'Python': 100, 'Advanced Python': 91, 'Hadoop & HDFS': 92, 'Hive + Architecture & Data': 78, 'Spark & PySpark': 95, 'APM': 85}}
        message = self.explanation_1('Employee', str(25462)+', '+'Marcus'+', '+'Simpson'+', '+'15-03-2020'+', '+'Data Engineering'+', '+str(7), output, emp_25462.__dict__)
        self.assertEqual(output, emp_25462.__dict__, msg=message)
        print("\033[0;31;48m ok")
        #print("\033[1;32;40m" + emp_25462.first_name, emp_25462.last_name, emp_25462.email + "\033[0m")
        
        # 2. change the last_name only
        msg = "2) changing the last_name only:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_25462.last_name = 'Sampson'
        output = {'trainee_id': 25462, '_first_name': 'Marcus', '_last_name': 'Sampson', '_email': 'marcus.sampson@fdmgroup.com', 'date_joined': '15-03-2020', '_date_left': '12-07-2021', 'stream': 'Data Engineering', 'weeks': 7, 'courses': {'Java': 82, 'Python': 100, 'Advanced Python': 91, 'Hadoop & HDFS': 92, 'Hive + Architecture & Data': 78, 'Spark & PySpark': 95, 'APM': 85}}
        message = self.explanation_1('Employee', str(25462)+', '+'Marcus'+', '+'Sampson'+', '+'15-03-2020'+', '+'Data Engineering'+', '+str(7), output, emp_25462.__dict__)
        self.assertEqual(output, emp_25462.__dict__, msg=message)
        print("\033[0;31;48m ok") 
        #print("\033[1;32;40m" + emp_25462.first_name, emp_25462.last_name, emp_25462.email + "\033[0m")
        
        # 3. change both first_name and last_name
        # 3a. changing the first_name before the last_name
        msg = "3) changing both first_name and last_name"
        msg = "3a) changing both but the first_name before the last_name:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_25462.first_name = 'Marc'
        emp_25462.last_name = 'Samson'
        output = {'trainee_id': 25462, '_first_name': 'Marc', '_last_name': 'Samson', '_email': 'marc.samson@fdmgroup.com', 'date_joined': '15-03-2020', '_date_left': '12-07-2021', 'stream': 'Data Engineering', 'weeks': 7, 'courses': {'Java': 82, 'Python': 100, 'Advanced Python': 91, 'Hadoop & HDFS': 92, 'Hive + Architecture & Data': 78, 'Spark & PySpark': 95, 'APM': 85}}
        message = self.explanation_1('Employee', str(25462)+', '+'Marc'+', '+'Samson'+', '+'15-03-2020'+', '+'Data Engineering'+', '+str(7), output, emp_25462.__dict__)
        self.assertEqual(output, emp_25462.__dict__, msg=message)
        print("\033[0;31;48m ok") 
        #print("\033[1;32;40m" + emp_25462.first_name, emp_25462.last_name, emp_25462.email + "\033[0m")

        # 3b. changing the last_name before the first_name
        msg = "3b) changing both but the last_name before the first_name:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_25462.last_name = 'Simson'
        emp_25462.first_name = 'Mark'
        output = {'trainee_id': 25462, '_first_name': 'Mark', '_last_name': 'Simson', '_email': 'mark.simson@fdmgroup.com', 'date_joined': '15-03-2020', '_date_left': '12-07-2021', 'stream': 'Data Engineering', 'weeks': 7, 'courses': {'Java': 82, 'Python': 100, 'Advanced Python': 91, 'Hadoop & HDFS': 92, 'Hive + Architecture & Data': 78, 'Spark & PySpark': 95, 'APM': 85}}
        message = self.explanation_1('Employee', str(25462)+', '+'Mark'+', '+'Simson'+', '+'15-03-2020'+', '+'Data Engineering'+', '+str(7), output, emp_25462.__dict__)
        self.assertEqual(output, emp_25462.__dict__, msg=message)
        print("\033[0;31;48m ok") 
        #print("\033[1;32;40m" + emp_25462.first_name, emp_25462.last_name, emp_25462.email + "\033[0m")
       
        # check that email is read only
        msg = "trying to change email by the object:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_25462.email = 'dummy.email@dummydomain.com'
        output = 'mark.simson@fdmgroup.com'
        result = emp_25462.email
        message = self.explanation_3('emp_25462', 'email', output, result)
        self.assertEqual(output, result, msg=message)
        
        # testing that date_left's getter works
        msg = "testing that date_left's getter works"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = '12-07-2021'
        result = emp_25462.date_left
        message = self.explanation_3('emp_25462', 'date_left', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # check that date_left is read only
        msg = "trying to change date_left by the object"
        print()
        print("\033[1;32;40m" + msg + "\033[0m", end='')
        # for a trainee that has left
        msg = "- for a trainee that has left:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_25462.date_left = '31-12-2030'
        output = '12-07-2021'
        result = emp_25462.date_left
        message = self.explanation_3('emp_25462', 'date_left', output, result)
        self.assertEqual(output, result, msg=message)
        # for a trainee that has not left
        msg = "- for a trainee that has not left:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_25581.date_left = '31-12-2030'
        output = None
        result = emp_25581.date_left
        message = self.explanation_3('emp_25581', 'date_left', output, result)
        self.assertEqual(output, result, msg=message)
        
        # test terminate_employment() method
        msg = "testing terminate_employment() method"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_25475.terminate_employment('31-01-2022')
        output = '31-01-2022'
        result = emp_25475.date_left
        message = self.explanation_5('emp_25475', 'terminate_employment', '31-01-2022', 'date_left', output, result)
        self.assertEqual(output, result, msg=message)
        
        # test count_trainees class attribute
        msg = "testing count_trainees class attribute"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 1
        result = test_class_1.count_trainees
        message = self.explanation_2(test_class_1, 'count_trainees', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # testing Trainee's print_count() method
        msg = "testing print_count() method - after 2nd trainee left:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_1.print_count()
                
        # test if Employee's class attribute was correctly updated
        # 'count_employees' : 1
        msg = "testing if Employee's class attribute was correctly updated"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        msg = "- count_employees:"
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 1
        result = test_class_3.count_employees
        message = self.explanation_2(test_class_3, 'count_employees', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # test Employee's print_count() method
        msg = "testing Employee's print_count() method - after 2nd trainee left:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_3.print_count()
        

        #########################
        # testing Trainer class #
        #########################
        
        # test creating 1st trainer
        # -------------------------
        msg = "test employing 1st trainer:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        e_id = 16384
        f_n = 'Evie'
        l_n = 'Klein'
        d_j = '24-11-2015'
        output = {'trainer_id': 16384, '_first_name': 'Evie', '_last_name': 'Klein', '_email': 'evie.klein@fdmgroup.com', 'date_joined': '24-11-2015', '_date_left': None, 'courses': [], 'trainings': {}}
        emp_16384 = test_class_2(e_id, f_n, l_n, d_j)
        message = self.explanation_1('Trainer', str(e_id)+', '+f_n+', '+l_n+', '+d_j, output, emp_16384.__dict__)
        self.assertEqual(output, emp_16384.__dict__, msg=message)
        
        # test count_trainers class attribute
        msg = "testing count_trainers class attribute"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        msg = "- count_trainers:"
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 1
        result = test_class_2.count_trainers
        message = self.explanation_2(test_class_2, 'count_trainers', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # testing Trainer's print_count() method
        msg = "testing Trainer's print_count() method - after 1st trainer joined:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_2.print_count()

        # test if Employee's class attribute was correctly updated
        # 'count_employees' : 2 (because count_trainees = 1)
        msg = "testing if Employee's class attribute was correctly updated"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        msg = "- count_employees:"
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 2
        result = test_class_3.count_employees      
        message = self.explanation_2(test_class_3, 'count_employees', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
                
        # test Employee's print_count() method
        msg = "testing Employee's print_count() method - after 1st trainer joined:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_3.print_count()
        
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
        message = self.explanation_5('emp_16384', 'assign_course', "'Excel', 'SQL', 'Unix', 'Python', 'Java'", 'courses', output, emp_16384.courses)
        self.assertEqual(output, emp_16384.courses, msg=message)
        print("\033[0;31;48m ok\n")

        # test assign_training() method
        msg = "testing assign_training() method: - asigning a course from courses list"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_16384.assign_training('16/05/2022', 'Excel')
        output = {'16/05/2022': 'Excel'}
        message = self.explanation_5('emp_16384', 'assign_training', "'16/05/2022', 'Excel'", 'trainings', output, emp_16384.trainings)
        self.assertEqual(output, emp_16384.trainings, msg=message)
        print("\033[0;31;48m ok\n")
                
        msg = "testing assign_training() method: - asigning another course from courses list with existing date"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_16384.assign_training('16/05/2022', 'Python1')
        output = {'16/05/2022': 'Python1'}
        message = self.explanation_5('emp_16384', 'assign_training', "'16/05/2022', 'Python1'", 'trainings', output, emp_16384.trainings)
        self.assertEqual(output, emp_16384.trainings, msg=message)
        print("\033[0;31;48m ok\n")
        
        msg = "testing assign_training() method: - asigning a course not in courses list"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_16384.assign_training('23/05/2022', 'Python2')
        output = {'16/05/2022': 'Python1'}
        message = self.explanation_5('emp_16384', 'assign_training', "'16/05/2022', 'Python1'", 'trainings', output, emp_16384.trainings)
        self.assertEqual(output, emp_16384.trainings, msg=message)
        
        msg = "testing assign_training() method: - asigning another course from courses list with inexisting date"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_16384.assign_training('23/05/2022', 'Unix')
        output = {'16/05/2022': 'Python1', '23/05/2022': 'Unix'}
        message = self.explanation_5('emp_16384', 'assign_training', "'23/05/2022': 'Unix'", 'trainings', output, emp_16384.trainings)
        self.assertEqual(output, emp_16384.trainings, msg=message)
        print("\033[0;31;48m ok\n")

        # test creating 2nd trainer
        # -------------------------
        msg = "test employing 2nd trainer:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        e_id = 17639
        f_n = 'Elena'
        l_n = 'Rostova'
        d_j = '04-05-2016'
        output = {'trainer_id': 17639, '_first_name': 'Elena', '_last_name': 'Rostova', '_email': 'elena.rostova@fdmgroup.com', 'date_joined': '04-05-2016', '_date_left': None, 'courses': [], 'trainings': {}}
        emp_17639 = test_class_2(e_id, f_n, l_n, d_j)
        message = self.explanation_1('Trainer', str(e_id)+', '+f_n+', '+l_n+', '+d_j, output, emp_17639.__dict__)
        self.assertEqual(output, emp_17639.__dict__, msg=message)
        
        # test count_trainers class attribute
        msg = "testing count_trainers() class attribute:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 2
        result = test_class_2.count_trainers
        message = self.explanation_2(test_class_2, 'count_trainers', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # testing Trainer's print_count() method
        msg = "testing Trainer's print_count() method - after 2nd trainer joined:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_2.print_count()
        
        # test if Employee's class attribute was correctly updated
        # 'count_employees' : 3
        msg = "testing if Employee's class attribute was correctly updated"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        msg = "- count_employees:"
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 3
        result = test_class_3.count_employees
        message = self.explanation_2(test_class_3, 'count_employees', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # test Employee's print_count() method
        msg = "testing Employee's print_count() method - after 2nd trainer joined:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_3.print_count()
        
        # test assign_course() method
        msg = "testing assign_course() method:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_17639.assign_course('Excel')
        emp_17639.assign_course('Hadoop & HDFS')
        emp_17639.assign_course('Hive + Architecture & Data')
        emp_17639.assign_course('Spark & PySpark')
        output = ['Excel', 'Hadoop & HDFS', 'Hive + Architecture & Data', 'Spark & PySpark']
        message = self.explanation_5('emp_17639', 'assign_course', "'Hadoop & HDFS', 'Hive + Architecture & Data', 'Spark & PySpark'", 'courses', output, emp_17639.courses)
        self.assertEqual(output, emp_17639.courses, msg=message)
        print("\033[0;31;48m ok\n")

        # test assign_training() method
        msg = "testing assign_training() method: - asigning a course from courses list"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_17639.assign_training('06/06/2022', 'Excel')
        output = {'06/06/2022': 'Excel'}
        message = self.explanation_5('emp_17639', 'assign_training', "'06/06/2022', 'Excel'", 'trainings', output, emp_17639.trainings)
        self.assertEqual(output, emp_17639.trainings, msg=message)
        print("\033[0;31;48m ok\n")
                
        msg = "testing assign_training() method: - asigning a course not in courses list"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_17639.assign_training('13/06/2022', 'SQL')
        output = {'06/06/2022': 'Excel'}
        message = self.explanation_5('emp_17639', 'assign_training', "'13/06/2022', 'SQL'", 'trainings', output, emp_16384.trainings)
        self.assertEqual(output, emp_17639.trainings, msg=message)
        
        msg = "testing assign_training() method: - asigning another course from courses list with inexisting date"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_17639.assign_training('13/06/2022', 'Hadoop & HDFS')
        output = {'06/06/2022': 'Excel', '13/06/2022': 'Hadoop & HDFS'}
        message = self.explanation_5('emp_17639', 'assign_training', "'13/06/2022', 'Hadoop & HDFS'", 'trainings', output, emp_17639.trainings)
        self.assertEqual(output, emp_17639.trainings, msg=message)
        print("\033[0;31;48m ok\n")
        
        msg = "testing assign_training() method: - asigning another course from courses list with existing date"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_17639.assign_training('13/06/2022', 'Spark & PySpark')
        output = {'06/06/2022': 'Excel', '13/06/2022': 'Spark & PySpark'}
        message = self.explanation_5('emp_17639', 'assign_training', "'13/06/2022', 'Spark & PySpark'", 'trainings', output, emp_17639.trainings)
        self.assertEqual(output, emp_17639.trainings, msg=message)
        print("\033[0;31;48m ok\n")

        # test terminate_employment() method
        msg = "testing terminate_employment() method:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_16384.terminate_employment('01-10-2021')
        output = '01-10-2021'
        result = emp_16384.date_left        
        message = self.explanation_5('emp_16384', 'terminate_employment', '01-10-2021', 'date_left', output, result)
        self.assertEqual(output, result, msg=message)
        
        # test count_trainers class attribute
        msg = "testing count_trainers class attribute"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        msg = "- count_trainers:"
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 1
        result = test_class_2.count_trainers
        message = self.explanation_2(test_class_2, 'count_trainers', output, result)
        self.assertEqual(output, result, msg=message)        
        print("\033[0;31;48m ok\n")
        
        # testing Trainer's print_count() method
        msg = "testing Trainer's print_count() method - after 1st trainer left:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_2.print_count()
        
        # test if Employee's class attribute was correctly updated
        # 'count_employees' : 2
        msg = "testing if Employee's class attribute was correctly updated"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        msg = "- count_employees:"
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 2
        result = test_class_3.count_employees
        message = self.explanation_2(test_class_3, 'count_employees', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # test Employee's print_count() method
        msg = "testing Employee's print_count() method - after 1st trainer left:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_3.print_count()

        # testing employee_id's getter
        msg = "testing employee_id's getter:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 16384
        result = emp_16384.employee_id
        message = self.explanation_3('emp_16384', 'employee_id', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # testing that employee_id is read only
        msg = "trying to change employee_id by the object::"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_16384.employee_id = 16666
        output = 16384
        result = emp_16384.employee_id        
        message = self.explanation_3('emp_16384', 'employee_id', output, result)
        self.assertEqual(output, result, msg=message)

        # testing that first & last name can be shanged
        # through the setter only (updating the email accordingly)
        # 1. change the first_name only
        msg = "testing that first & last name can be changed\n1) changing the first_name only:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_16384.first_name = 'Eva'
        output = {'trainer_id': 16384, '_first_name': 'Eva', '_last_name': 'Klein', '_email': 'eva.klein@fdmgroup.com', 'date_joined': '24-11-2015', '_date_left': '01-10-2021', 'courses': ['Excel', 'SQL', 'Unix', 'Python1', 'Java'], 'trainings': {'16/05/2022': 'Python1', '23/05/2022': 'Unix'}}
        message = self.explanation_1('Employee', str(16384)+', '+'Eva'+', '+'Klein'+', '+'24-11-2015', output, emp_16384.__dict__)
        self.assertEqual(output, emp_16384.__dict__, msg=message)
        print("\033[0;31;48m ok")       
        #print("\033[1;32;40m" + emp_16384.first_name, emp_16384.last_name, emp_16384.email + "\033[0m")
        
        # 2. change the last_name only
        msg = "2) changing the last_name only:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_16384.last_name = 'Clein'
        output = {'trainer_id': 16384, '_first_name': 'Eva', '_last_name': 'Clein', '_email': 'eva.clein@fdmgroup.com', 'date_joined': '24-11-2015', '_date_left': '01-10-2021', 'courses': ['Excel', 'SQL', 'Unix', 'Python1', 'Java'], 'trainings': {'16/05/2022': 'Python1', '23/05/2022': 'Unix'}}
        message = self.explanation_1('Employee', str(16384)+', '+'Eva'+', '+'Clein'+', '+'24-11-2015', output, emp_16384.__dict__)
        self.assertEqual(output, emp_16384.__dict__, msg=message)
        print("\033[0;31;48m ok") 
        #print("\033[1;32;40m" + emp_16384.first_name, emp_16384.last_name, emp_16384.email + "\033[0m")
        
        # 3. change both first_name and last_name
        # 3a. changing the first_name before the last_name
        msg = "3) changing both first_name and last_name"
        msg = "3a) changing both but the first_name before the last_name:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_16384.first_name = 'Eve'
        emp_16384.last_name = 'Clain'
        output = {'trainer_id': 16384, '_first_name': 'Eve', '_last_name': 'Clain', '_email': 'eve.clain@fdmgroup.com', 'date_joined': '24-11-2015', '_date_left': '01-10-2021', 'courses': ['Excel', 'SQL', 'Unix', 'Python1', 'Java'], 'trainings': {'16/05/2022': 'Python1', '23/05/2022': 'Unix'}}
        message = self.explanation_1('Employee', str(16384)+', '+'Eve'+', '+'Clain'+', '+'24-11-2015', output, emp_16384.__dict__)
        self.assertEqual(output, emp_16384.__dict__, msg=message)
        print("\033[0;31;48m ok")
        #print("\033[1;32;40m" + emp_16384.first_name, emp_16384.last_name, emp_16384.email + "\033[0m")

        # 3b. changing the last_name before the first_name
        msg = "3b) changing both but the last_name before the first_name:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_16384.first_name = 'Evie'
        emp_16384.last_name = 'Klein'
        output = {'trainer_id': 16384, '_first_name': 'Evie', '_last_name': 'Klein', '_email': 'evie.klein@fdmgroup.com', 'date_joined': '24-11-2015', '_date_left': '01-10-2021', 'courses': ['Excel', 'SQL', 'Unix', 'Python1', 'Java'], 'trainings': {'16/05/2022': 'Python1', '23/05/2022': 'Unix'}}
        message = self.explanation_1('Employee', str(16384)+', '+'Evie'+', '+'Klein'+', '+'24-11-2015', output, emp_16384.__dict__)
        self.assertEqual(output, emp_16384.__dict__, msg=message)
        print("\033[0;31;48m ok")
        #print("\033[1;32;40m" + emp_16384.first_name, emp_16384.last_name, emp_16384.email + "\033[0m")

        # check that email is read only
        msg = "trying to change email by the object:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_16384.email = 'dummy_email@dummydomain.com'
        output = 'evie.klein@fdmgroup.com'
        result = emp_16384.email
        message = self.explanation_3('emp_16384', 'email', output, result)
        self.assertEqual(output, result, msg=message)
                
        # testing that date_left's getter works
        msg = "testing that date_left's getter works"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = '01-10-2021'
        result = emp_16384.date_left
        message = self.explanation_3('emp_16384', 'date_left', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # check that date_left is read only
        msg = "trying to change date_left by the object:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m", end='')
        # for a trainer that has left
        msg = "- for a trainee that has left:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_16384.date_left = '31-12-2030'
        output = '01-10-2021'
        result = emp_16384.date_left
        message = self.explanation_3('emp_16384', 'date_left', output, result)
        self.assertEqual(output, result, msg=message) 
        # for a trainer that has not left
        msg = "- for a trainee that has not left:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_17639.date_left = '31-12-2030'
        output = None
        result = emp_17639.date_left
        message = self.explanation_3('emp_17639', 'date_left', output, result)
        self.assertEqual(output, result, msg=message)

        # test terminate_employment() method
        msg = "testing terminate_employment() method"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_17639.terminate_employment('15-01-2022')
        output = '15-01-2022'
        result = emp_17639.date_left
        message = self.explanation_5('emp_17639', 'terminate_employment', '15-01-2022', 'date_left', output, result)
        self.assertEqual(output, result, msg=message)
        
        # test count_trainers class attribute
        msg = "testing count_trainees class attribute"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 0
        result = test_class_2.count_trainers
        message = self.explanation_2(test_class_2, 'count_trainers', output, result)
        self.assertEqual(output, result, msg=message)        
        print("\033[0;31;48m ok\n")
        
        # testing Trainer's print_count() method
        msg = "testing Trainer's print_count() method - after 2nd trainer left:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_2.print_count()

        # test if Employee's class attribute was correctly updated
        # 'count_employees' : 1
        msg = "testing if Employee's class attribute was correctly updated"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        msg = "- count_employees:"
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 1
        result = test_class_3.count_employees
        message = self.explanation_2(test_class_3, 'count_employees', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # test Employee's print_count() method
        msg = "testing Employee's print_count() method - after 2nd trainer left:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_3.print_count()


        ########################################
        # removing the last employee (trainee) #
        ########################################
        
        # test terminate_employment() method
        msg = "testing terminate_employment() method:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_25581.terminate_employment('11-02-2022')
        output = '11-02-2022'
        result = emp_25581.date_left
        message = self.explanation_5('emp_25581', 'terminate_employment', '11-02-2022', 'date_left', output, result)
        self.assertEqual(output, result, msg=message)
        
        # test count_trainees class attribute
        msg = "testing count_trainees class attribute:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 0
        result = test_class_1.count_trainees
        message = self.explanation_2(test_class_1, 'count_trainees', output, result)
        self.assertEqual(output, result, msg=message)  
        print("\033[0;31;48m ok\n")
        
        # testing Trainee's print_count() method
        msg = "testing Trainee's print_count() method - after 3rd trainee left:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_1.print_count()
                
        # test if Employee's class attribute was correctly updated
        # 'count_employees' : 0
        msg = "testing if Employee's class attribute was correctly updated"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        msg = "- count_employees:"
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 0
        result = test_class_3.count_employees
        message = self.explanation_2(test_class_3, 'count_employees', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # test Employee's print_count() method
        msg = "testing Employee's print_count() method - after 3rd trainee left:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class_3.print_count()


if __name__ == '__main__':
    unittest.main(verbosity=2)
